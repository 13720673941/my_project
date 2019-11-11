# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 17:51

"""

正则表达式中 + 表示括号里面的字段至少出现一次或者多次，否则返回None

"""

name1 = "邓飞"

name2 = "邓鹏鹏鹏飞"

import re

regex = re.compile(r"邓(鹏)+飞")

print(regex.search(name1))

print(regex.search(name2).group())