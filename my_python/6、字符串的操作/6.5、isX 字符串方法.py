# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/21 22:01

"""
isalpha() 返回 True 如果字符串只包含字母且非空
isalnum() 返回 True 如果字符串只包含字母和数字且非空
isdecimal() 返回 True 如果字符串只包含数字字符且非空
isspace() 返回 True 如果字符串只包含空格、制表符和换行，且非空
istitle() 返回 True 如果字符串仅包含以大写字母开头、后面都是小写字母的单词
"""

# isalpha()

print("hello".isalpha())

# isalnum()

print("hello123".isalnum())

# isdecimal()

print("132".isdecimal())

# isspace()

print(" ".isspace())

# istitle()

print("Hello".istitle())

# 请输入你个年龄必须是数字否则就继续循环

while True:

    age_number = input("Please input your age: ")

    if age_number.isdecimal():

        break

    print("Please input a number for your age.")

# ** 该类型的函数可以用来判断输入的字符的类型

# 判断注册输入的用户名只包含数字和字母

while True:

    register_username = input("Please input your account username: ")

    if register_username.isalnum():

        break

    print("Please input your username only contains letters and numbers.")

