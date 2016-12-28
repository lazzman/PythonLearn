'''
函数的学习
注意：
1.编码必须为utf-8
2.python中默认使用换行符作为结束符
3.语句块的结束全看空格缩进,不要使s用tab
4.python中大约有70+BIF，想要查看所有的BIF只需要在SHELL或IDLE中输入：dir(__builtins__)，所有的小写单词都是BIF，可以使用help(BIF)查看具体用法
5.在交互式解释器中，第一次输入import this可以查看python圣经
6.Python3中默认最大递归深度不大于100
'''
# 定义一个元素为列表的列表
games = [["魔兽","暴雪"],["征途","巨人"],["屁股","暴雪"],["梦幻西游","网易"],["GTA5","RStar"]];
# 我们要输出列表中的每一个元素，如果元素是列表，则迭代该元素，将内部的元素打印出来
for item in games:
  '''
  Help on built-in function isinstance in module builtins:
  isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.
  '''
  if(isinstance(item,list)):
    for item2 in item:
      print(item2)
  else:
    print(item)

# 分隔符
print("================================================================================================")

# 上面的方式并不灵活，如果元素是多重列表嵌套呢？因此这里使用函数+递归方式便肯容易解决这个问题
def print_list(lists):
  for item in lists:
    if(isinstance(item,list)):
      print_list(item);
    else:
      print(item);
# 调用函数输出list
print_list(games);
