# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/28 14:58


# strip() rstrip() lstrip() 删除字符串 左边 右边 或者两边 多余的字符/空白

spam = "myHellomy"

# 删除左边的 my

print(spam.lstrip("my"))

# 删除右边的 my

print(spam.rstrip("my"))

# 删除两边的 my 传入的字符串顺序不重要

print(spam.strip("ym"))