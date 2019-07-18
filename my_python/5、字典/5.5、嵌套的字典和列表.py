# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/14 13:39


# 定义一个字典 包含字典、列表

my = {
    "my_info":{"name":"dpf","age":26,"tall":175,"sex":"man"},
    "my_hobby":["basketball","singing","python"]
}

# 遍历我的信息

my_info = my["my_info"]

# 循环遍历我的信息字典

print("this is my info: "+"\n")

for key,value in my_info.items():

    print("\t" + key + " : " + str(value))

# 循环输出我的爱好


