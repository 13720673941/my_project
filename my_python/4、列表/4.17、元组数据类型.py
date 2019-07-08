# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 21:16

# 元组数据类型用括号表示 :: 元组中的值不能进行 修改 添加 删除

# 定义一个元组

name = ("deng","peng","fei")

# 计算元组长度

len_name = len(name)

print(len_name)

# 按照索引取值，和列表一样

index_name= name[0]

print(index_name)

# type 函数查看数据类型

list_type = type(["list"])          # 列表

tuple_type = type(("tuple",))       # 元组

str_type = type("str")              # 字符串

dic_type = type({"name":"deng"})    # 字典

print(list_type)

print(tuple_type)

print(str_type)

print(dic_type)