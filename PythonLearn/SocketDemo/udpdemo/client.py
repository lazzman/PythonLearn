#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

与server一起演示

@author: NodCat
'''

import socket

client_sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

ip_port = ('127.0.0.1', 9999)

while True:
    inp = raw_input('client:').strip()
    client_sk.sendto(inp, ip_port)
    if(inp == 'exit'):
        break
