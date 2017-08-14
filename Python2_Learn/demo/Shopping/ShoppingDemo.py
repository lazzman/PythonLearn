#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

'''
函数练习
'''
# 商品列表
__dic = {
    1:'apple 500',
    2:'iphone 5000',
    3:'zuk 5',
    0:'商品结算（退出程序）'
}

# 初始化消费预算金额
__money = int(input('请输入您的消费预算：'))

# 存储已购买的商品信息 __dict
__bag = dict()


def __init():
    '''初始化打印内容'''

    content_start = '''
-------------------------------------
购物列表清单：

'''

    content_end = '''
-------------------------------------
请选择您要购买的商品：
'''

    for k,v in __dic.items():
        content_start += str(k)+':'+v+'\r\n'

    content_start += content_end
    return content_start

def __choise(content):
    '''处理用户选择'''

    # 引用全局变量
    global __money
    global __bag

    try:
        num = int(input(content))
        if num == 0:  # 如果输入0则直接结算
            __jiesuan()

        item = __dic[num]
        item_list = item.split(" ") # 分割字符串
        thing = item_list[0]    # 购买的商品
        jiage = int(item_list[1])    # 商品价格
        __money -= jiage;
        if __money < 0:
            print('【购买' + thing + '失败，您的余额不足】')
            __money += jiage
            __jiesuan()

        if __bag.has_key(thing):
            num = __bag[thing]
            __bag[thing] = num + 1
        else:
            __bag[thing] = 1

        print('【购买'+thing+'成功】')
    except Exception, e:
        print(e)
        print('选择错误！请重新选择！')

    __choise(content) # 递归调用

def __jiesuan():
    '''结算并退出程序'''

    global __money

    tip_start = '''
你购买了以下商品：
==================================
商品名称\t数量
'''
    tip_end ='=================================='


    for i in __bag:
        tip_start += (i+"\t\t\t"+str(__bag[i])+"\r\n")

    tip = tip_start + tip_end
    print(tip)
    print("剩余金额：" + str(__money))
    print("感谢您的使用，88~")
    os._exit(0)

def __main():
    '''程序主函数'''

    # 初始化商品列表
    content = __init()

    # 处理用户选择
    __choise(content)


if __name__ == '__main__':
    pass
    __main()
else:
    print("呵呵哒")





