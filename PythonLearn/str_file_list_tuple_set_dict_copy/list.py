#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
列表操作
'''

if __name__ == '__main__':
    # range函数快速生成一个列表
    a_list = range(2, 20)
    print('range:' + str(a_list))
    
    a_list = [x*2 for x in range(5)]
    print('a_list:' + str(a_list))
    
    b_list = list(['a', 'e', 'a', 'b', 'c', 'd'])
    # 追加元素append
    b_list.append(a_list)
    print('append:' + str(b_list))
    
    # 插入元素insert
    b_list.insert(0, (1, 2, 3))
    print('insert:' + str(b_list))
    
    # 从原列表中删除指定索引的元素,并返回删除的元素（空参则默认删除最后一个元素）pop
    delete_meta = b_list.pop()
    print('pop:' + str(b_list) + ' delete_meta:' + str(delete_meta))
    delete_meta = b_list.pop(0)
    print('pop:' + str(b_list) + ' delete_meta:' + str(delete_meta))
    
    # 删除列表中匹配的第一个元素
    b_list.remove('a')
    print('remove:' + str(b_list))
    
    # 统计元素在列表中出现的次数
    print('count:' + str(b_list.count('d')))
    
    # 返回指定元素的索引，没有找到元素则抛异常
    print('index:' + str(b_list.index('d')))
    
    # 将一个list合并到当前list中 
    b_list.extend(a_list)
    print('extend:' + str(b_list))
    
    # 排序
    b_list.sort(cmp=None, key=None, reverse=False)
    print('sort:' + str(b_list))
    
    # 倒序
    b_list.reverse()
    print('reverse:' + str(b_list))
    
    # 列表截取（同字符串的截取）
    print('原列表:' + str(b_list) + ' 截取列表:' + str(b_list[9:]))

    # 列表拼接（同extend）
    b_list = b_list + ['111', '222', '333']
    print('listA+listB:' + str(b_list))
    
    # 列表的不常用的其他方法
    c_list = [2,2]
    c_list = c_list * 3
    print('listA*n:' + str(c_list))
    
    # 删除指定下标的元素
    d_list = [0,1,2,3,4,5]
    del(d_list[3])
    print('del(list[index]):' + str(d_list))
    
    # 删除指定下标范围的元素
    d_list = [0,1,2,3,4,5]
    del(d_list[2:4])
    print('del(list[start:end]):' + str(d_list))
    
    # 列表的复制
    d_list = [0,1,2,3,4,5]
    e_list = d_list[:]
    print('list[:] :' + str(e_list))
    
    
    
    
    
    
    
    
    
