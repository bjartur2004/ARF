#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import AF_INET,SOCK_STREAM,socket

# AF_INET => TCP
# SOCK_STREAM => IPv4

sobj = socket(AF_INET,SOCK_STREAM)
sobj.bind(('127.0.0.1',32032))
sobj.listen(1)

client , addr = sobj.accept()
print("the ip is connected to server ",addr)

while(True):
    
    message = input()
    if(message == "exit"):
        client.close()
        break
    else:
        client.send(message.encode())

