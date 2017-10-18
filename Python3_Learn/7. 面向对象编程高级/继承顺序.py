#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'由于Python是多继承，那么很容易想到一个问题，继承顺序是如何？'


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


class B(E, D):
    pass


class A(B, C):
    pass


# 按照继承顺序，查找run()方法时顺序是：B->E->C->D->F
a = A()
a.run()

# 按照继承顺序,查找sing()方法的顺序是：E->D
b = B()
b.sing()
