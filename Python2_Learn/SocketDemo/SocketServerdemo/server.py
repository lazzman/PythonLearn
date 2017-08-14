#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月17日

SocketServer内部使用 IO多路复用 以及 “多线程”，从而实现并发处理多个客户端请求的Socket服务端。
即：每个客户端请求连接到服务器时，Socket服务端都会在服务器是创建一个“线程”或者“进 程” 专门负责处理当前客户端的所有请求。

@author: NodCat 
'''
import SocketServer

class MyRequestHandle(SocketServer.BaseRequestHandler):
    '''
    处理请求的类
    '''
    
    def setup(self):
        pass

    def handle(self):
        # print self.request, self.client_address, self.server
        conn = self.request
        address = self.client_address
        conn.send('hello! you address is {0}'.format(address))
        flag = True
        while flag:
            data = conn.recv(1024)  # recv也是阻塞方法
            print '{0}:{1}'.format(address, data)
            if data == 'exit':
                flag = False
            conn.send('你说啥？')
        conn.close()
        

    def finish(self):
        pass


if __name__ == '__main__':
    # 创建一个socketserver对象
    socketserver = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyRequestHandle) 
    '''
    SocketServer.ThreadingTCPServer的__init__方法就是封装了TCP socket的创建过程，其实就是创建了一个socket对象
        ...
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family, self.socket_type)
        ...
    '''
    
    # 每个请求会开一个线程
    socketserver.serve_forever() 
