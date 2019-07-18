# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 23:22


dict_data = {
    "name":"james",
    "age":"19",
    "sex":"man",
    "city":"xian"
}

# * get() 方法:: 如果要获取一个字典中的值，如果不存在返回一个备用的值

# 下示：该字典中不存在 love 的值，返回一个 your

get_value = dict_data.get("love","your")

print(get_value)

# 下示：该字典中存在 name 的值，就返回的是 james

get_value1 = dict_data.get("name","dpf")

print(get_value1)