# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 23:18


dict_data = {
    "name":"james",
    "age":"19",
    "sex":"man",
    "city":"xian"
}

# 检查字典中是否存在键:: 判断 name 是否存在字典的 键 中 返回 True/False

have_key = "name" in dict_data.keys()

print(have_key)

# 检查字典中是否存在值:: 判断 xian 是否存在字典的 值 中 返回 True/False

have_vlaue = "xian" in dict_data.values()

print(have_vlaue)