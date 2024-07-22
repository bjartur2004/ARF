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

def client_listen(client_socket, client_address, message_callback):
    #print(f"New connection from {client_address}")

    with clients_locked:
        clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(BUFFER_SIZE).decode()
            #print("nm",message)
            if not message:
                break
            #print(f"Received from {client_address}: {message}")
            message_callback(client_socket, client_address, message)
    except Exception as e:
        print(f"Error with client: {e}")
        pass
    finally:
        with clients_locked:
            clients.remove(client_socket)
        client_socket.close()
        #print(f"Connection with {client_address} closed")

def accept_connections(server_socket, message_callback):
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = Thread(target=client_listen, args=(client_socket, client_address, message_callback))
        client_thread.daemon = True  # This ensures the thread will exit when the main program exits
        client_thread.start()

def send_file_to_client(client_socket, file_path):
    try:
        with open(file_path, 'rb') as f:
            client_socket.sendall("send_file".encode())

            while chunk := f.read(BUFFER_SIZE):
                client_socket.sendall(chunk)
    except Exception as e:
        print(f"Error sending file to client: {e}")

def send_file_to_all_clients(file_path):
    # todo: add a way to select what clients are included
    with clients_locked:
        for client_socket in clients:
            send_thread = Thread(target=send_file_to_client, args=(client_socket, file_path))
            send_thread.daemon = True
            send_thread.start()

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

