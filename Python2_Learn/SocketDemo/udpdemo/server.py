#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

与client一起演示

@author: NodCat
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
    15. 网络编程.SOCK_STREAM 流式socket，for TCP协议(默认)
    15. 网络编程.SOCK_DGRAM 数据报式socket，for UDP协议
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
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    ip_port = ('127.0.0.1', 9999)
    sk.bind(ip_port)
    
    while True:
        data = sk.recv(1024)  # recv也是阻塞方法
        print data
    

if __name__ == '__main__':
    main()
