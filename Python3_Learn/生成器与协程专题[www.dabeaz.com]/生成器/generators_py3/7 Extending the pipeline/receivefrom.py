# receivefrom.py
# 使用生成器实现SocketServer
# A generator that yields connections to a TCP 15. 网络编程

import socket
from genpickle import *


def receive_connections(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    while True:
        client = s.accept()
        yield client


# Example use
if __name__ == '__main__':
    for c, a in receive_connections(("", 15000)):
        print("Got connection from %s Details: %s " % (a, c))
        for item in gen_unpickle(c.recv(20480)):
            print("ReciveMsg： %s" % (item))
        c.send(b"Hello World\n")
        c.close()
