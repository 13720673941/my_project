# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 1:14

"""
[1]: 创建正则表达式对象
"""

# 导入python正则表达式模块

import re

# *** r 表示原始字符串，防止 \ 符号误认为是转义符号

# \d 是一个正则表达式可以匹配 0-9 之内的任意数字

# 向 compile() 中传递一个字符串，表示正则表达式，返回一个 regex 模式对象

phone_number_1 = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# 正则表达式中 {} 中的数字表示匹配这个模式几次，1、2是一个表达意思

phone_number_2 = re.compile(r"\d{3}-\d{3}-\d{4}")

"""
[2]: 匹配 regex 对象
"""

# regex 对象的search函数传入查找的字符串，查找所有正则表达式的匹配，如果没有找到返回 None

# 如果search查找到了返回一个match对象，match中有一个group()函数，返回所要查找格式的字段

text = phone_number_2.search("my phone is: 666-999-8989")

print("number is: %s"%text)

print("number is: %s"%text.group())


## 练习

"""
在个人信息中查找身份证号
"""

my_info = "姓名：邓鹏飞，性别：男，手机号：13720673941，身份证：610528199312110312"

# 创建一个 regex 对象

mo = re.compile(r"\d{18}")

# 字符串中匹配正则表达式

my_number = mo.search(my_info)

print(my_number.group())

"""
利用 group() 方法把身份证中的出生时间分离出来
"""

mo_2 = re.compile(r"(\d{6})(\d{8})(\d{4})")

my = mo_2.search(my_info)

# 提取日期

# * group() 方法中传入数字表示第几个字段

birthday_date = my.group(2)

print(birthday_date)

# 获取分离的多个字段用 groups() 方法返回一个元祖

print(my.groups())

"""
如果匹配的字符串中有括号小需要进行转义
"""

# 正则表达式中 () 用 \(\) 表示 字符串中的括号注意中英文


WeiNan_phone_number = "渭南市的座机电话：(0913)-8236632"

# 使用正则提取电话号

mo_3 = re.compile(r"\(\d{4}\)-\d{7}")

phone_number_3 = mo_3.search(WeiNan_phone_number)

print(phone_number_3.group())