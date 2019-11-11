# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 19:06

import re


text1 = "These are my fruits: \t\n 10 苹果,20 apple,90 banana,12 lemon"

# \D 除 0-9 以外的任意字符
regex1 = re.compile(r"\D+")

print(regex1.findall(text1))

# \w 任何字母、数字和下划线,即匹配单词

regex2 = re.compile(r"\w+")

print(regex2.findall(text1))

# \W 除字母、数字和下划线任何字符

print(re.compile(r"\W").findall(text1))

# \s 空格、制表符和换行符

print(re.compile(r"\s").findall(text1))

# \S 除空格、制表符和换行符

print(re.compile(r"\S+").findall(text1))

# 混合使用查找所有水果列表 + 表示至少出现一次否则返回None

fruits = re.compile(r"\d+\s+\D+")

print(fruits.findall(text1))







