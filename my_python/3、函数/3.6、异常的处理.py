# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 15:17

# try 尝试运行，expect 接受一个错误

try:

    print(2/0)

except ZeroDivisionError:

    # 接受这个错误并打印 下面句子
    print("error: invalid argument.")




