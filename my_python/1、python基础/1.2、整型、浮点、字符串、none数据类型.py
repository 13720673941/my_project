# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/6 22:46

# python 中数据类型： 整型 int 浮点： float 字符串： str None: 是 NoneType 数据类型的唯一值

# 整型： -2 -1 0 1 2 3 4

# 浮点型： 0.1 0.22 -1.23 0.0 1.0

# 字符串： 'a' 'aaa' '123' 'hello' '1@hello'

# 字符串的拼接

str1 = 'Hello'
str2 = ' Mr.deng'

# 输出 == Hello Mr.deng
print(str1 + str2)

# 字符串的复制 后面复制的次数必须是 整型

str3 = ' hello'

# 输出 == hello hello hello hello hello
print(str3*5)

# None 数据类型 意思是 空   其他变成语言可能是（null undefined nil）

params = None

print(params)