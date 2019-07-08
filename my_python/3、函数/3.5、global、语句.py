# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 14:55

# 如果需要在一个函数内修改全局变量，就可以使用 global

num = 1
def fun():

     num = 123
     print(num)

fun()
print(num)

# 上面所示 num = 1 为全局变量，num = 123 为局部变量

# 使用 global 把 123 变成全局变量

number = 1

def fnc():

    # 开始全局变量为 1 使用 global 把全局变量 变成 123
    global number

    number = 123

    print(number)

fnc()
print(number)
