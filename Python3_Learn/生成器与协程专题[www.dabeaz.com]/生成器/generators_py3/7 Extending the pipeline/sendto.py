# sendto.py
# 结合生成器以及序列化将序列化内容发送到远程机器上（监视追加的日志内容并序列化发送到远程机器）
# Send items to a remote machine

import socket
from genpickle import *


def sendto(source, addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    for pitem in gen_pickle(source):
        s.sendall(pitem)
    s.close()


# Example use.   This requires you to run receivefrom.py
# in a different process/window

if __name__ == '__main__':
    from apachelog import *
    from follow import *

    lines = follow(open("access-log"))
    log = apache_log(lines)
    sendto(log, ("127.0.0.1", 15000))
