# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 16:36

# 定义一个列表 params

params = ["cat","dog","rat","elephant"]

# for 循环遍历列表中的所有值

for i in range(4):

    print("list index "+str(i)+": "+params[i])

# 当不知道循环多少次数时候可以获取列表长度

for j in range(len(params)):

    print(params[j])

