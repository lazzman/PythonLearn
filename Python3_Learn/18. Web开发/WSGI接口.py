#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
from wsgiref.simple_server import make_server


# 定义实现WSGI接口规范的函数
def application(environ, start_response):
    print('远程IP：%s 请求方式：%s 请求URI:%s 服务器处理线程ID：%s ' % (
        environ['REMOTE_ADDR'],
        environ['REQUEST_METHOD'], environ['PATH_INFO'], threading.current_thread().getName()))
    start_response('200 OK', [('Content-Type', 'text/html; charset=UTF-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or '18. Web开发')
    if environ['PATH_INFO'] == '/sleep':
        # 阻塞5s 其他请求此时无法进入application，单线程并且单进程导致
        time.sleep(5)
    return [body.encode('utf-8')]


# WSGI仅仅将全部请求处理传递给application函数，如果application函数中发生阻塞，那么后面的请求也将无法处理
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
