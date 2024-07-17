#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import AF_INET,SOCK_STREAM,socket

BUFFER_SIZE = 1024

if __name__ == '__main__':
    sobj = socket(AF_INET,SOCK_STREAM)
    sobj.connect(('127.0.0.1',32032))
    while True:
        message = sobj.recv(BUFFER_SIZE).decode()
        if(message == "checkstatus"):
            sobj.send()

