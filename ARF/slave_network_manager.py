#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import AF_INET,SOCK_STREAM,socket

sobj = socket(AF_INET,SOCK_STREAM)
sobj.connect(('127.0.0.1',32032))
while True:
    message = sobj.recv(2048)
    if(message == "exit"):
        sobj.close()
        break
    elif(message.decode() == ''):
        pass
    else:
        print(message.decode())