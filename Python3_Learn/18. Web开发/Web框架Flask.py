#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 测试flask默认使用的
import time

from flask import Flask
from flask import request

# 创建Flask实例
app = Flask(__name__)


# 配置url映射方法
@app.route('/', methods=['GET', 'POST'])
def home():
    # flask默认使用的server同样是单线程单进程阻塞的
    time.sleep(5)
    return '<h1>Home</h1>'


# 配置url映射方法
@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


# 配置url映射方法
@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()
