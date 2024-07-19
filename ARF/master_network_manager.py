#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import AF_INET,SOCK_STREAM,socket
from threading import Thread, Lock

BUFFER_SIZE = 1024

clients = []
clients_locked = Lock()


def checkStatus(ip):
    #client.send("checkstatus".encode())
    #responce = client.recv(BUFFER_SIZE)
    #print(responce)
    pass

def handle_client(client_socket, client_address, message_callback):
    print(f"New connection from {client_address}")

    with clients_locked:
        clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(BUFFER_SIZE).decode()
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            if message == "checkstatus":
                client_socket.send(b'3')
            message_callback(client_socket, message)
    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        with clients_locked:
            clients.remove(client_socket)
        client_socket.close()
        print(f"Connection with {client_address} closed")

def accept_connections(server_socket, message_callback):
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = Thread(target=handle_client, args=(client_socket, client_address, message_callback))
        client_thread.daemon = True  # This ensures the thread will exit when the main program exits
        client_thread.start()


def openSlavePort(message_callback):
    global client

    serverSocket = socket(AF_INET,SOCK_STREAM)
    #serverSocket.bind(('192.168.0.101',32032))
    serverSocket.bind(('127.0.0.1',32032))
    serverSocket.listen(25)
    
    accept_thread = Thread(target=accept_connections, args=(serverSocket,message_callback))
    accept_thread.daemon = True  # This ensures the thread will exit when the main program exits
    accept_thread.start()

    return serverSocket



