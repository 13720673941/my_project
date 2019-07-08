# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 21:37

# 调用python中的copy模块

import copy

params = ["1","2","3"]

# 调用 copy 模块中的 copy 函数进行复制

new_params = copy.copy(params)

# 对复制的列表 0 索引进行重新赋值

new_params[0] = "my"

print(params)

print(new_params)

# ** 如果要赋值列表中的列表就得使用 deepcopy

deep_list = ["1","2",["3","4"],"5"]

copy_list = copy.deepcopy(deep_list)

print(deep_list)

print(copy_list)
