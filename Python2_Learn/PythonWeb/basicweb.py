#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

Python的Web体系包含两部分：Web服务器，Web应用
Python对于Web体系也有一套规范叫做WSGI（Web Server Gateway Interface），规定了Web服务器与Web应用交互的接口规范（类似JavaWeb），实现了Web Server与Web App的解耦和

层次关系图：
    Web应用(处理框架分发的请求；并将结果返回给框架)[程序员根据框架来开发Web应用]
     ↑↓
    Web框架(路由分发请求，调用Web应用对应的处理方法；处理应用返回的结果，再返回给Web服务器)[django、Flask、18. Web开发.py、Bottle、Quixote...]
     ↑↓ 
    Web服务器 (监听请求，将客户端请求传递给框架；将结果返回给客户端)[python内置的wsgiref.simple_server、Tornado...]        

Python本身提供了Web服务器，基本上就是对之前使用的ServerSocket的封装与重构
Python中Web框架集成了Web服务器，例如Django，我们可以在一个框架下开发多个app，这不同于javaweb，可以说Python的Web开发是在框架'下'开发，而java的Web开发是在框架'上'开发

'''

from wsgiref.simple_server import make_server

def MyApp(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello,18. Web开发!</h1>'

if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8000, MyApp)
    print 'Serving HTTP on port 8000...'
    httpd.serve_forever()

