# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 16:42

# 列表中判断是否存在那个值 可以使用 in 或者 not in :: 返回的是布尔类型

# 定义一个列表

params = ["cat","dog","rat","elephant"]

# 判断列表中是否存在 cat 返回 True 反则返回 False

print("cat" in params)

print("bee" in params)

# 判断列表中不存在那个值

print("cat" not in params)

print("bee" not in params)
