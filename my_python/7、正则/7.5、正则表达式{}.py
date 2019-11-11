# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 18:05

"""
正则表达式中 {} 表示匹配特定次数
"""

import re

text1 = "hahaha"

text2 = "hahahahaha"


regex = re.compile(r"(ha){3,5}")

print(regex.search(text1).group())

print(regex.search(text2).group())


"""
贪心与非贪心匹配
"""

# ? 表示匹配出的字段的最短字段信息

regex1 = re.compile(r"(ha){3,5}?")

print(regex1.search(text2).group())

