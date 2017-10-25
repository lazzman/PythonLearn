#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'异步非阻塞服务器'

from socket import *
from scheduler import *


def handle_client(client, addr):
    print('Connection from', addr)
    while True:
        yield ReadWait(client)
        data = client.recv(65536)
        if not data:
            break
        yield WriteWait(client)
        client.send(data)
    client.close()
    print('Client Closed')
    yield


def server(port):
    print('Server Starting')
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        yield ReadWait(sock)
        client, addr = sock.accept()
        yield NewTask(handle_client(client, addr))


def alive():
    while True:
        print('i m alive')
        yield


sched = Scheduler()
sched.new(alive())
sched.new(server(45000))
sched.mainloop()
