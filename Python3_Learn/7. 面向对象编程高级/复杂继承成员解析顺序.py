#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'由于Python是多继承，那么很容易想到一个问题，继承顺序是如何？'

'''
mro是method resolution order的缩写，表示了类继承体系中的成员解析顺序。

注意：python2与python3的mro策略有所不同，这里我们只看Python3的mro策略

在python中，每个类都有一个mro的类方法。
---------------------------------------------
class Base(object):
	def __init__(self):
		print “Base init”
class Medium1(Base):
	def __init__(self):
		super(Medium1, self).__init__()
		print “Medium1 init”
class Medium2(Base):
	def __init__(self):
		super(Medium2, self).__init__()
		print “Medium2 init”
class Leaf(Medium1, Medium2):
	def __init__(self):
		super(Leaf, self).__init__()
		print “Leaf init”
>>> Leaf.mro()
[<class '__main__.Leaf'>, <class '__main__.Medium1'>, <class '__main__.Medium2'>, <class '__main__.Base'>, <class 'object'>]
---------------------------------------------

mro方法返回的是一个祖先类的列表。Leaf的每个祖先都在其中出现一次，这也是super在父类中查找成员的顺序。

通过mro，python巧妙地将多继承的图结构，转变为list的顺序结构。super在继承体系中向上的查找过程，变成了在mro中向右的线性查找过程，任何类都只会被处理一次。

通过这个方法，python解决了多继承中的2大难题：

1. 查找顺序问题。从Leaf的mro顺序可以看出，如果Leaf类通过super来访问父类成员，那么Medium1的成员会在Medium2之前被首先访问到。如果Medium1和Medium2都没有找到，最后再到Base中查找。

2. 钻石继承的多次初始化问题。在mro的list中，Base类只出现了一次。事实上任何类都只会在mro list中出现一次。这就确保了super向上调用的过程中，任何祖先类的方法都只会被执行一次。

至于mro的生成算法，可以参考这篇wiki：https://en.wikipedia.org/wiki/C3_linearization

小结：
mro()返回的父类列表：
1. 查找顺序，列表元素从左向右查找
2. 初始化顺序，列表元素从右向左依次初始化
'''


class D(object):
    def run(self):
        print('d')

    def sing(self):
        print('d')


class E(object):
    def run(self):
        print('e')

    def sing(self):
        print('e')

    def look(self):
        print('e')


class F(object):
    def run(self):
        print('f')

    def sing(self):
        print('f')


class C(D, F):
    def run(self):
        print('c')

    def sing(self):
        print('c')

    def look(self):
        print('c')


class B(E, D):
    pass


class A(B, C):
    pass


# 按照继承顺序，查找run()方法时顺序是：B->E->C->D->F
print(A.mro())
a = A()
a.run()

# 按照继承顺序，查找run()方法时顺序是：B->E->C->D->F
a.look()

# 按照继承顺序,查找sing()方法的顺序是：B->E->D
print(B.mro())
b = B()
b.sing()

print('---------------------------------------------------')


class Base(object):
    def __init__(self):
        print("Base init")

    def hi(self):
        print("Base hi")


class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()
        print("Medium1 init")


class Medium2(Base):
    def __init__(self):
        super(Medium2, self).__init__()
        print("Medium2 init")

    def hi(self):
        print("Medium2 hi")


class Leaf(Medium1, Medium2):
    def __init__(self):
        super(Leaf, self).__init__()
        print("Leaf init")


print(Leaf.mro())
leaf = Leaf()
