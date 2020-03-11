# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/3 10:42

"""
enumerate()是python的内置函数、适用于python2.x和python3.x
enumerate在字典上是枚举、列举的意思
enumerate参数为可遍历/可迭代的对象(如列表、字符串)
enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用enumerate
enumerate()返回的是一个enumerate对象
"""

data = [1,1,1,1,2,2,2,2,3,3,3,3,]

b = []

c = []

for index,nums in enumerate(data):
    if nums == 1:
        b.append(index)
        c.append(nums)

print("索引：%s"%b)
print("参数：%s"%c)