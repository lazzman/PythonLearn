# blaster.py
# 测试我们实现的高并发服务器-与服务器建立大量套接字并随机发送大量信息
# Open up a large number of socket connections with a server and then
# just start randomly blasting it with messages.

# 一个非常简单的脚本，打开与回显服务器的300个套接字连接，并随机将其与1024字节消息一起发送。
# 程序runblaster.py将在不同的子进程中运行该程序的多个副本以增加负载。
# 注意：这些脚本与我在过去描述的Twisted vs. Coroutines上做了基本的基准测试一样。
# 此类的主要目标尚未进行性能测量，因此您可能希望使用脚本来改变连接数量，进程数量，消息大小等不同的设置。
# 为了允许大量的套接字连接，您可能需要解决系统设置。
# 例如，在我的Mac上，我首先必须在shell中使用'ulimit -n 1024'来更改服务器上的文件描述符数量（否则只能处理256个连接）。

from socket import *
import select
import random

NCONNECTIONS = 300  # Number of connections to make
MSGSIZE = 1024  # Message size
SERVER = ('localhost', 45000)  # Server address
MSG = "x" * MSGSIZE  # The message

# Open up connections
connections = []
for i in range(NCONNECTIONS):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(SERVER)
    connections.append(s)


# Send a message on a socket and get a response
def send_message(dest):
    bytes_sent = 0
    bytes_recv = 0
    while bytes_recv < MSGSIZE:
        r, w, e = select.select([dest], [dest], [])
        # Receive response data
        for s in r:
            bytes_recv += len(s.recv(65536))
        if bytes_sent < MSGSIZE:
            for s in w:
                bytes_sent += s.send(MSG[:MSGSIZE - bytes_sent])


# Send a bunch of random messages
def send_random(count):
    for x in range(count):
        dest = random.choice(connections)
        if x % 10000 == 0:
            print(x)
        send_message(dest)


# Run it
send_random(100000)
