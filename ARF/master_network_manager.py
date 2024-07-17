#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import AF_INET,SOCK_STREAM,socket

BUFFER_SIZE = 1024

def checkStatus(ip):
    client.send("checkstatus".encode())
    responce = client.recv(BUFFER_SIZE)
    print(responce)


# AF_INET => TCP
# SOCK_STREAM => IPv4


if __name__ == '__main__':
    sobj = socket(AF_INET,SOCK_STREAM)
    sobj.bind(('127.0.0.1',32032))
    sobj.listen(1)

    client , addr = sobj.accept()
    print("the ip is connected to server ",addr)

