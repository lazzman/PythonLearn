#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple ORM using metaclass '


# 基类
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 字符串型字段
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


# 整型字段
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 定义元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # 如果类的名称为Model，直接返回
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        # 如果类的名称不为Model，打印类名
        print('Found model: %s' % name)
        # 创建一个字典，存储所有Field类型的属性
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 从类中删除Field类型的属性
        for k in mappings.keys():
            attrs.pop(k)
        # 在类中使用__mappings__属性保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        # 在类中使用__table__属性保存表名，假设表名和类名一致
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 定义一个继承dict的Model类
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        # 继承了dict，可以直接存储到当前对象字典中
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
