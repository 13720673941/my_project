# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 14:46

# 局部变量不能在全局中使用

def spam():
    eggs = 9523

# 下面错误展示，eggs 只是作用于 spam 函数内，不能在全局调用

# print(eggs)

def name():

    # name 函数内的局部变量只能在name 中使用
    name = "james"

    print(name)

name()

