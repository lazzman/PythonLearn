#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

与server一起演示

@author: NodCat
'''

import socket

client = socket.socket()

ip_port = ('127.0.0.1', 9999)

client.connect(ip_port)

while True:
    data = client.recv(1024)  # recv也是阻塞方法
    print data
    inp = raw_input('client:')
    client.send(inp)
    if(inp == 'exit'):
        break
