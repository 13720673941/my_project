# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 21:24

# 列表转换成元组 tuple() 函数

list_params = ["deng","peng","fei"]

print(tuple(list_params))

# 元组转换成列表 list() 函数

tuple_params = ("deng","peng","fei")

print(list(tuple_params))

# 传递引用列表

def name(language):

    language.append("python")

name_list = ["deng","peng"]

name(language=name_list)

print(name_list)