# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 21:10

# **列表和字符串在一个重要的地方是不同的，字符串不能对字符进行添加、删除、修改

# **改变一个字符串的方式只能是；使用切片 和 连接，构造一个新的字符串

params = "my name is deng."

# 使用切片和索引取字符串中的字符进行重新构造一个变量

new_name = params[0:10] +" zhang"+params[-1]

print(new_name)