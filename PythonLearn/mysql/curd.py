#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Created on 2017年4月16日

mysql数据库的增删改查操作
MySQLdb模块需要到https://sourceforge.net/projects/mysql-python/?source=typ_redirect下载

@author: NodCat
'''

import MySQLdb

# 获取Connect连接对象
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='python', port=3306)

# 获取数据库游标Cursor
cur = conn.cursor()


def select():
    
    print '=================查询=================='
    
    # 执行sql语句,execute返回值代表SQL语句影响行数
    ret = cur.execute('select * from user')
    
    # 获取返回数据
    data = cur.fetchall()
    
    print ret
    print data

def insert():
    
    print '=================添加=================='
    
    # sql的参数占位符不论参数是什么类型都是用%s占位
    sql = 'insert into user(name,age) values(%s,%s)'
    param = ['nodcat', 19]
    
    # 执行sql语句
    ret = cur.execute(sql, param)
    
    # 提交事务
    conn.commit()

    print ret

def update():

    print '=================修改=================='
    
    # sql的参数占位符不论参数是什么类型都是用%s占位
    sql = "update user set age = %s where name = %s"
    param = [20, 'nodcat']
    
    # 执行sql语句
    ret = cur.execute(sql, param)
    
    # 提交事务
    conn.commit()
    
    print ret


def delete():
    
    print '=================删除=================='
    
    # sql的参数占位符不论参数是什么类型都是用%s占位
    sql = "delete from user where name = %s"
    param = ['nodcat', ]
    
    # 执行sql语句
    ret = cur.execute(sql, param)
    
    # 提交事务
    conn.commit()
    
    # 回滚事务
#   conn.rollback()
    
    print ret

def batchinsert():
    
    print '=================批量添加=================='
    
    # sql的参数占位符不论参数是什么类型都是用%s占位
    sql = 'insert into user(name,age) values(%s,%s)'
    param = [
        ['nodcat', 19],
        ['elfier', 20],
        ['tom', 30],
        ['lucio', 25],
    ]
    
    # 执行sql语句
    ret = cur.executemany(sql, param)
    
    # 提交事务
    conn.commit()

    print ret
    
def selectdict():
    
    print '=================查询字典类型的结果=================='
    
    # 指定结果以字典类型返回
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    # 执行sql语句,execute返回值代表SQL语句影响行数
    ret = cur.execute('select * from user')
    
    # 获取返回数据
    data = cur.fetchall()
    
    print ret
    print data
    
def selectfetchone():
    
    print '=================查询单条结果=================='
    
    # 指定结果以字典类型返回
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    
    # 执行sql语句,execute返回值代表SQL语句影响行数
    ret = cur.execute('select * from user')
    
    print ret
    
    # 获取一条数据 fetchone类似yield，就是数据库中的游标，每次调用，获取一条数据，游标索引+1
    data = cur.fetchone()
    print data
    
    # 获取一条数据
    data = cur.fetchone()
    print data
    
    # 改变游标索引
#     cur.scroll(0, mode='absolute')  # 以绝对路径方式将游标索引重新指向0
    cur.scroll(-1, mode='relative')  # 以相对路径方式将游标索引-1，即指向上一次的位置
    
    # 获取一条数据
    data = cur.fetchone()
    print data
    
    
def insertGetIncrementID():
    
    print '=================插入数据时获取自增ID=================='
    
    # sql的参数占位符不论参数是什么类型都是用%s占位
    sql = 'insert into user(name,age) values(%s,%s)'
    param = ['nodcat', 19]
    
    # 执行sql语句
    ret = cur.execute(sql, param)
    
    # 提交事务
    conn.commit()
    
    # 提交事务后再获取自增ID
    incrementid = cur.lastrowid

    print ret
    print incrementid
    
    
    
    
    

# 调用CURD
# select()
# insert()
# update()
# delete()
# batchinsert()
# selectdict()
# selectfetchone()
insertGetIncrementID()

# 关闭游标和连接
cur.close()
conn.close()

