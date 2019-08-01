# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/28 14:50


# rjust() 字符串开始空  ljust() 字符串末尾空 center() 文本居中

# rjust() * hello 为 5 个字符，传入 10 前面传入的字符串站 5 个字符 左对齐 居中 同理

spam = "Hello"

# 右对齐

print(spam)
print(spam.rjust(10,"="))

# ljust()

# 左对齐

print(spam)
print(spam.ljust(10,"="))

# 居中

print(spam)
print(spam.center(20,"-"))