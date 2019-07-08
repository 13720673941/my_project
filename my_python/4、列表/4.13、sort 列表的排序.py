# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 20:41

# 定义一个列表

params = ["cat","dog","Rat","elephant"]

# sort() 列表的排序

# ** 不能对即有字母还有数字的列表进行排序，因为python不知道如何比较他们

# ** 在对字母进行排序的时候，默认按照 ASCII 字符的顺序排，大写排在小写前面，按字母顺序排列

params.sort()

print(params)

# 如果要列表按照字母的顺序排列可以给 sort 内传递一个参数 key=str.lower *不会影响原来列表中的值的变化

params.sort(key=str.lower)

print(params)