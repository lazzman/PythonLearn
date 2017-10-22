# genmessages.py
# 使用生成器接收UDP套接字的接收内容
# A generator that yields messages on a UDP 15. 网络编程

import socket


def receive_messages(addr, maxsize):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(addr)
    while True:
        msg = s.recvfrom(maxsize)
        yield msg


# Example use
if __name__ == '__main__':
    for msg, addr in receive_messages(("", 10000), 1024):
        print(msg, "from", addr)

