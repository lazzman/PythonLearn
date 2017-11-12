#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'字典推导式'

country_code_list = [
    (86, 'china'),
    (91, 'India'),
    (7, 'Russia'),
    (81, 'Japan')
]

# 利用字典推导式生成字典
country_code_dict = {country: code for code, country in country_code_list}
print(country_code_dict)
