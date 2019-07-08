# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 21:02

# 列表并不是唯一标识序列值的数据类型

# 字符串按照索引取值,和列表一样的取值方法

params = "James"

print(params[0]) # print J

# 判断字符串中是否含有某个字符

print("J" in params) # 返回 True

print("J" not in params) # 返回 False

# 循环输出字符串中的字符

for i in params:

    print("***** "+i+" *****")



