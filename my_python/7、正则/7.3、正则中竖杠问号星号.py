# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 15:34

"""
正则表达式匹配多个字段
"""

# 在正则表达式中 | 表示或的意思，如果匹配的原始字符中有 | 符号需要使用 \| 转义

names = "邓鹏飞、邓鹏、邓飞、张三、李四"

import re

# 或的关系如果匹配到第一个直接返回结果不会再去匹配第二个
regex = re.compile(r"邓鹏飞|张三")

mo = regex.search(names)

print(mo.group())

# 使用 findall() 返回全部的字段 该方法返回的是一个列表

print(regex.findall(names))

"""
匹配字符中以 邓 开头的字段
group方法中传入数字匹配括号里面的，不传入数字表示返回全部的mo对象
"""
regex1 = re.compile(r"邓(鹏飞|鹏|飞)")

mo1 = regex1.search(names)

print(mo1.group(1))

"""
正则表达式匹配可有可无的字段信息
"""

names1 = "邓飞 邓鹏飞"

# ()? 表示括号里面的匹配项可以有也可以没有

regex2 = re.compile(r"邓(鹏)?飞")

mo2 = regex2.search(names1)

print(mo2.group())

"""
* 匹配零次或者多次，意思是 括号内匹配的字段可以没有可以出现一次也可以出现多次
"""

names2 = "邓鹏鹏鹏鹏飞"

names3 = "邓鹏飞"

names4 = "邓飞"

regex3 = re.compile(r"邓(鹏)*飞")

print(regex3.search(names2).group())

print(regex3.search(names3).group())

print(regex3.search(names4).group())


