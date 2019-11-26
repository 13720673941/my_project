# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/17 16:10

"""

有时候（\d、\w、\s）等太过于广泛，你可以使用 [] 定义自己的字符分类

"""

import re

# ** 字符分类[]里面的将匹配所有元音字符 无论大小写

regex = re.compile(r"[aeiouAEIOU]")

mo = regex.findall("My name is Deng Peng Fei")

print(mo)


# 也可以使用 - 来表示字符或者数字的范围,使用 [] 时就不需要再里面加上斜杠转义

regex1 = re.compile(r"[a-zA-Z0-9]")

mo1 = regex1.findall("I am 25 years old.")

print(mo1)

# 使用 ^ 符号得到非字符类

regex2 = re.compile(r"[^0-9]")

print(regex2.findall("I am 25 years old."))




