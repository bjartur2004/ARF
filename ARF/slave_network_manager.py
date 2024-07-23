#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, AF_INET,SOCK_STREAM,SHUT_RDWR
from threading import Thread, Lock
from time import sleep
import uuid

BUFFER_SIZE = 1024
RETRY_DELAY = 5

soc = None

def connectSocket():
    #soc.connect(('192.168.0.101',32032))
    soc.connect(('127.0.0.1',32032))

def closeSocket():
    soc.shutdown(SHUT_RDWR)
    soc.close()

def onConnectionFailiure(error=None):
    global soc

    if error:
        print(f"Connection failed: {error}. Retrying in {RETRY_DELAY} seconds...\r")
    else:
        print(f"Connection failed. Retrying in {RETRY_DELAY} seconds...\r")
        closeSocket() # if the error was not passed the socket had been connected. this is not a good test..
        soc = socket(AF_INET,SOCK_STREAM)

    sleep(RETRY_DELAY)

def sendStatus(statusId):
    print("sendstatus")
    soc.sendall(f"/SetStatus={statusId}".encode())

def sendMac():
    macAd = uuid.getnode()
    soc.sendall(f"/SetMacAddr={macAd}".encode())

def receive_file(filesize):
    try:
        filesize = int(filesize)
        received_size = 0
        with open("blend.blend", 'wb') as f:
            while received_size < filesize:
                data = soc.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
                received_size += len(data)

        print(f"File received successfully and saved as blend.blend")
    except Exception as e:
        print(f"Error receiving file: {e}")


def connectToMaster(message_callback):
    while True:
        try:
            connectSocket()

            sendMac()
            sendStatus(3)
            #start listening
            listening_thread = Thread(target=listen_to_master, args=(message_callback,))
            listening_thread.daemon = True  # This ensures the thread will exit when the main program exits
            listening_thread.start()

            listening_thread.join()
            onConnectionFailiure()

        except Exception as e:
            onConnectionFailiure(e)


def listen_to_master(message_callback):
    try:
        while True:
            message = soc.recv(BUFFER_SIZE).decode()
            messages = message.split("/")
            for mes in messages:
                if not mes or len(mes) <= 1:
                    continue

                messageType,messageVar = mes.split("=")
                
                if messageType == 'send_file':
                    receive_file(messageVar)  
                else:
                    message_callback(soc, message)
    except Exception as e:
        print(f"error occured with connection to master: {e}")
        pass


def startNetworkManager(message_callback):
    global soc
    soc = socket(AF_INET,SOCK_STREAM)
    
    connecting_thread = Thread(target=connectToMaster, args=(message_callback,))
    connecting_thread.daemon = True  # This ensures the thread will exit when the main program exits
    connecting_thread.start()

