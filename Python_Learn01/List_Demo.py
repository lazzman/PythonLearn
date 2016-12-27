'''
列表的学习
（注意：编码必须为utf-8）
python中默认使用换行符作为结束符
'''
# python中没有数组，列表就是数组，列表功能更强大，比如动态增加，减小
games = ["魔兽","征途","屁股"];
# 打印某个列表元素
print(games[1]);
# 打印列表的长度
print(len(games));
# 列表某位追加数据
games.append("剑灵");
# 删除数据(POP方式)
popData = games.pop();
print('pop的数据项为：'+popData);
# 追加另一个列表
games.extend(["梦幻西游","剑网3"]);
# 查找并删除特定的数据项
games.remove("梦幻西游");
# 在指定位置插入数据
games.insert(0,"GTA5");
# 直接打印列表对象
print(games);

# 分隔符
print("=========================================================================================");

# 重新定义列表中的数据（列表中的元素可以是各种类型，类似js）
games = [["魔兽","暴雪"],["征途","巨人"],["屁股","暴雪"],["梦幻西游","网易"],["GTA5","RStar"]];
# 显示第一个列表中的第一个元素
print("第一个列表中的第一个元素："+games[0][0]);
# for-each迭代输出列表中每项的值
for item in games:
  # "".join(列表) 将列表对象转为字符串对象
  print("for-each迭代："+"".join(item));
# while迭代列表项
count = 0;
while count < len(games):
  print("while迭代："+"".join(games[count]));
  # count++这种写法在python中不支持哦
  count+=1;

# 直接打印列表对象
print(games);