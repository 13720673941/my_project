# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 20:56

import random

# 定义一个列表我的爱好

my_hobby = [
    "I like play basketball.",
    "I like to eat delicious food.",
    "I like driver car.",
    "I like python."
]

# 列表中的索引最大是 3 ，获取列表最大长度后是 4 所以要 -1

random_select = my_hobby[random.randint(0,len(my_hobby)-1)]

print(random_select)