# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 0:02

# for 循环 + range() 函数

# i 取值 0 1 2 3 4

for i in range(5):
    print(i)


# for 循环打印字符串

for i in range(5):
    print('hello')

# for 循环和 if 语句

for i in range(5):
    if i == 4:
        print('is four.')

# range() 函数不包括最后一个数字

for i in range(1,5):

    # 输出的 i 的值 只有 1 2 3 4

    print(i)