# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 2:48

# return 函数返回一个值，后面可以赋值给某个变量

def hello(name):

    return "hello " + name

# 调用这个函数，会返回一个值 hello name 给 params 这个变量

params = hello(name="james")

print(params)