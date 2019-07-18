# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 23:11

dict_data = {
    "name":"james",
    "age":"19",
    "sex":"man",
    "city":"xian"
}

# keys():: 方法

for key in dict_data:
    print(key)

# 或者下方法

for k in dict_data.keys():
    print(k)

# values()

for value in dict_data:
    print(value)

# 或者下方法

for v in dict_data.values():
    print(v)

# items():: 方法

for key,value in dict_data.items():

    print(key)
    print(value)

# :::::: 生成的是一个个元组类型结构

for i in dict_data.items():
    print(i)