#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月11日
使用反射模拟web的路由实现
代码没有优化，明白大意即可
@author: nodcat
'''

if __name__ == '__main__':
    # 定义路由映射
    router_mapping = {"index":"indexController"}
    
    # 用户输入访问地址
    account = raw_input("请输入账号: ")
    pwd = raw_input("请输入密码: ")
    url = raw_input("请输入访问的url: ")
    # 拆分controllerKey与actionKey
    split = url.split('/')
    controllerkey = split[0]
    actionkey = split[1]
    # 获取对应的Controller，如果找不到则返回404
    ctlr = router_mapping.get(controllerkey, "errorController")
    
    if ctlr == "errorController":
        modle = __import__("errorController")
        # 创建对象
        obj = modle.Error()
        # 检查成员
        ret = hasattr(obj, 'error404')  # 因为有error404方法所以返回True
        if ret:
            obj.error404()  # 调用error404方法
    else:
        modle = __import__(ctlr)
        # 创建对象
        obj = modle.Index(account, pwd)
        # 检查成员
        ret = hasattr(obj, actionkey)  # 因为有error404方法所以返回True
        if ret:
            # 获取成员
            func = getattr(obj, actionkey)  # 获取的是个对象
            func()  # 调用login方法
        else:  # 如果访问的action错误则返回404
            modle = __import__("errorController")
            # 创建对象
            obj = modle.Error()
            # 检查成员
            ret = hasattr(obj, 'error404')  # 因为有error404方法所以返回True
            if ret:
                obj.error404()  # 调用error404方法
    
    
