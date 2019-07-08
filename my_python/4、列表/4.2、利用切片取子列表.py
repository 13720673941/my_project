# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 15:54

# 定义一个列表

params = ["cat","dog","rat","elephant"]

# 取列表 params 中的 dog rat 生成另外一个列表

# 切片取值，第一个整数是开始的索引，第二个是结束的索引，**但是不包括随后索引在列表的值

print(params[1:3])

# 如果开始的索引为 0 可以忽略不写, 开始为 0 的意思就是从第一个值开始取值

print(params[:3])

# 同理最后一个也可以为 0 取的是从 索引 2 开始到最后一个

print(params[2:])

# 列表的复制 从开始取到结束

print(params[:])