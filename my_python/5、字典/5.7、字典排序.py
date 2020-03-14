# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/11 16:40

dict_data = {
    "name":"james",
    "age":"19",
    "sex":"man",
    "city":"xian"
}

# 0 表示 key ; 1 表示 value

a = sorted(dict_data.items(),key=lambda x:x[0])

new_dict = {}
for su in a:
    new_dict[su[0]] = su[1]

print(new_dict)