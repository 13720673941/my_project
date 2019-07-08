# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 16:10

# 定义一个列表

params = ["cat","dog","rat","elephant"]

# 删除列表中的某一个值 del :: 删除后的值不能再次使用

del params[2]

print(params)

# 删除列表中的某一个值 pop :: 会返回删除的值，可以再次使用

# 先定义一个空列表 用来储存删除的值

new_list = []

# pop() 括号内传递的是列表索引

params_remove = params.pop(0)

new_list.append(params_remove)

print(new_list)


# 删除列表中的某一个值 remove :: 删除后不能使用 如果该值在列表中多次出现，只删除第一个

params.remove("dog")

print(params)