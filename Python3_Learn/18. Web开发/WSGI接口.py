#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from wsgiref.simple_server import make_server


# 定义实现WSGI接口规范的函数
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=UTF-8')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or '18. Web开发')
    if environ['PATH_INFO'] == '/sleep':
        time.sleep(20)
    return [body.encode('utf-8')]


# WSGI仅仅将全部请求处理传递给application函数，如果application函数中发生阻塞，那么后面的请求也将无法处理
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
