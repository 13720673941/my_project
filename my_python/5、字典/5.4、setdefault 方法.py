# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/13 23:28

dict_data = {
    "name": "james",
    "age": "19",
    "sex": "man",
    "city": "xian"
}

# * setdefault() 方法:: 传递给该方法的第一个参数为要检查的键，
# * 第二个参数，如果该键不存在时要设置的值，如果存在就返回键的值

# 字典中不存在该键时，返回的字段

new_value = dict_data.setdefault("sex","your")

print(new_value)

# ** 该方法会把设置的键值对添加的字典中去

print(dict_data)


# 计算一个字符串中每个字符出现的次数

message = 'it was a bright cold day in april , and the clocks were striking thirteen.'

count = {}

for i in message:

    # 遍历字符串添加到字典count中初始化为0
    count.setdefault(i,0)

    # 每次加 1 ，字符串内有该字符 +1 没有的重新创建 +1
    count[i] = count[i] + 1

print(count)

# pprint() 模块使用:: 漂亮的打印，按键的顺序排列

import pprint

pprint.pprint(count)

# 如果字典中不存在一个值，就把这个值写入字典中

spam = {}

if "color" not in spam:

    spam["color"] = "black"

print(spam)

# 上面的简洁程序可以用 setdefault() 方法代替上面的操作代码

spam.setdefault("color","black")

print(spam)

