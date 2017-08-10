#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

浏览器可访问的服务端demo

常见的阻塞操作  (阻塞操作发生的原因多是由于应用层和内核层的交互，需要等待内核层处理完才会返回结果给应用层，因此应用层线程被阻塞)：
1.等待客户端连接
2.等待控制台输入
3.从网络中读取数据到程序内存中
4.将数据通过网络发送

socket阻塞和非阻塞的区别 简单点说: 
阻塞就是干不完不准回来， 非组赛就是你先干，我现看看有其他事没有，完了告诉我一声

我们拿最常用的send和recv两个函数来说吧... 比如你调用send函数发送一定的Byte,在系统内部send做的工作其实只是把数据传输(Copy)到TCP/IP协议栈的输出缓冲区,
它执行成功并不代表数据已经成功的发送出去了,如果TCP/IP协议栈没有足够的可用缓冲区来保存你Copy过来的数据的话...这时候就体现出阻塞和非阻塞的不同之处了:
对于阻塞模式的socket send函数将不返回直到系统缓冲区有足够的空间把你要发送的数据Copy过去以后才返回,
而对于非阻塞的socket来说send会立即返回WSAEWOULDDBLOCK告诉调用者说:"发送操作被阻塞了!!!你想办法处理吧..." 
对于recv函数,同样道理,该函数的内部工作机制其实是在等待TCP/IP协议栈的接收缓冲区通知它说:嗨,你的数据来了.
对于阻塞模式的socket来说如果TCP/IP协议栈的接收缓冲区没有通知一个结果给它它就一直不返回:耗费着系统资源....
对于非阻塞模式的socket该函数会马上返回,然后告诉你:WSAEWOULDDBLOCK---"现在没有数据,回头在来看看"

@author: NodCat
'''

import socket
import time

def main():
    sk = socket.socket()
    ip_port = ('127.0.0.1', 80)
    # 绑定监听的的端口
    sk.bind(ip_port)
    # 最大连接数
    sk.listen(5) 

    while True:
        # 阻塞方法，直到有客户端连接才会继续向下执行
        conn, address = sk.accept()  # 获取到客户端socket对象和客户端address(ip port)
        
        raw_input("模拟阻塞:")
        
        handleRquest(conn, address)
        
def handleRquest(client, address):
    buf = client.recv(1024)
    
    print buf
    
    client.send("HTTP/1.1 200 OK\r\n\r\n")
   
    client.send('hello! your ip is {0}  time is {1}'.format(address, time.strftime('%Y-%m-%d %H:%M:%S')))
    client.close()
    
if __name__ == '__main__':
    main()
