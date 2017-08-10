#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月17日

文件上传服务端

@author: NodCat
'''

import SocketServer
import os

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'G:/temp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            # 获取请求方法、文件名、文件大小
            cmd, file_name, file_size = pre_data.split('|')
            # 已经接收文件的大小
            recv_size = 0
            # 上传文件路径拼接
            file_dir = os.path.join(base_path, file_name)
            f = file(file_dir, 'wb')
            Flag = True
            while Flag:
                # 未上传完毕，
                if int(file_size) > recv_size:
                    # 最多接收1024，可能接收的小于1024
                    data = conn.recv(1024) 
                    recv_size += len(data)
                    # 写入文件
                    f.write(data)
                # 上传完毕，则退出循环
                else:
                    recv_size = 0
                    Flag = False
               
            print 'upload successed.'
            f.close()
    
instance = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
instance.serve_forever()
