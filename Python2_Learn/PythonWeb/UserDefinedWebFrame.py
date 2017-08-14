#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

自己实现一个Web框架
基本功能：路由

'''

from wsgiref.simple_server import make_server

import conf

def MyApp(environ, start_response):
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    
    # 1、获取用户输入的URL 
    userUrl = environ['PATH_INFO']
#     if userUrl == '/index':
#         return '<h1>index</h1>'
#     elif userUrl == '/login':
#         return '<h1>login</h1>'
#     elif userUrl == '/logout':
#         return '<h1>logout</h1>'
#     else:
#         return '<h1>404 no found</h1>'
    
    result = None
    for item in conf.url: # 从路由表中找到对应的处理方法
        if item[0] == userUrl:
            result = item[1]()  # 调用对应的处理方法
    
    if result == None: # 如果路由表中没有映射，就返回错误404
        result = '<h1>404 not found</h1>'
    
    return result

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, MyApp)
    print 'Serving HTTP on port 8000...'
    httpd.serve_forever()
