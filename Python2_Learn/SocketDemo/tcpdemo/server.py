#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

与client一起演示

@author: NodCat
'''

'''
socket常用方法

sk.bind(address)
s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。
在AF_INET下，以元组（host,port）的形式表示地址。
 
sk.listen(backlog)
开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的
连接个数最大为5,这个值不能无限大，因为要在内核中维护连接队列
 
sk.setblocking(bool)
是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
 
sk.accept()
接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收
和发送数据。address是连接客户端的地址。接收TCP 客户的连接（阻塞式）等待连接的到来
 
sk.connect(address)
连接到address处的套接字。一般，address的格式为元组（hostname,port）,
如果连接出错，返回socket.error错误。
 
sk.connect_ex(address)
同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
 
sk.close()
关闭套接字
 
sk.recv(bufsize[,flag])
接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。
flag提供有关消息的其他信息，通常可以忽略。
 
sk.recvfrom(bufsize[.flag])
与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，
address是发送数据的套接字地址。
 
sk.send(string[,flag])
将string中的数据发送到连接的套接字。返回值是要发送的字节数量，
该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
 
sk.sendall(string[,flag])
将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。
成功返回None，失败则抛出异常。
内部通过递归调用send，将所有内容发送出去。
 
sk.sendto(string[,flag],address)
将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。
返回值是发送的字节数。该函数主要用于UDP协议。
 
sk.settimeout(timeout)
设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作
（如 client 连接最多等待5s ）
 
sk.getpeername()
返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
 
sk.getsockname()
返回套接字自己的地址。通常是一个元组(ipaddr,port)
 
sk.fileno()
套接字的文件描述符
'''

import socket


def main():
    '''
    15. 网络编程.15. 网络编程()默认使用的是tcp协议，ipv4地址簇
    方法签名：
    15. 网络编程.15. 网络编程(15. 网络编程.AF_INET,15. 网络编程.SOCK_STREAM,0)
    参数一：地址簇
    15. 网络编程.AF_INET IPV4(默认)
    15. 网络编程.AF_INET6 IPV6
    15. 网络编程.AF_UNIX 只能用于单一的unix系统进程间的通信
    参数二：类型
    15. 网络编程.SOCK_STREAM 流式socket，TCP协议(默认)
    15. 网络编程.SOCK_DGRAM 数据报式socket,UDP协议
    15. 网络编程.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPV4报文；
                 此外，利用原始套接字，可以通过IP_HRDINCL套接字选项由用户构造IP头
    15. 网络编程.SOCK_DRW 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_DRW用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。
      SOCK_DRW通常仅限于高级用户或管理员运行的程序使用。
    15. 网络编程.SOCK_SEQPACKET 可靠的连续数据包服务
    参数三：协议
    0 (默认)与特定的地址家族相关的协议，如果是0，则系统会根据地址格式和套接类别，自动选择一个合适的协议
    返回值：
    socket对象
    
    '''
    sk = socket.socket()
    ip_port = ('127.0.0.1', 9999)
    sk.bind(ip_port)
    sk.listen(15)
    
    while True:
        conn, address = sk.accept()
        conn.send('hello! you address is {0}'.format(address))
        flag = True
        while flag:
            data = conn.recv(1024)  # recv也是阻塞方法
            print '{0}:{1}'.format(address, data)
            if data == 'exit':
                flag = False
            conn.send('你说啥？')
        conn.close()
    

if __name__ == '__main__':
    main()
