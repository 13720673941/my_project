# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/21 21:55


"""
字符串的小写转化：lower()
字符串的大写转化：upper()
判断字符串是否全部小写：islower()
判断字符串是否全部大写：isupper()
"""

spam = "hEllO"

# 全部转化为小写

lower_spam= spam.lower()

print(lower_spam)

# 全部转化为大写

upper_spam = spam.upper()

print(upper_spam)

# 判断全部小写/大写返回，True/False

print(spam.islower())

print(spam.isupper())