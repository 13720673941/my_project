# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 18:55

"""

findall() 表示匹配字符串中所有符合条件的字符

如果正则表达式没分组则返回的是一个列表，否则返回一个元祖列表

"""

# 返回一个列表

names = "zhangsan,lisi,wangwu,zhangsan"

import re

regex1 = re.compile(r"zhangsan")

# 查找所有符合类型的字符返回一个列表

print(regex1.findall(names))

regex2 = re.compile(r"(zhang)(san)")

# 返回的是包含两个分组的列表

print(regex2.findall(names))



