#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from wsgiref.simple_server import make_server

from hello import application

# WSGI仅仅将请求处理传递给application函数，如果application函数中发生阻塞，那么后面的请求也将无法处理
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
