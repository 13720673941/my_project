# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 2:08

import sys

# sys.exit() 提前结束程序,需要导入 sys 模块

# 该程序中 while 无限循环，当输入的字符等于 exit 时，调用 sys 模块中的 exit() 函数 终止程序

while True:
    params = input('please input exit to exit.')
    if params == 'exit':
        sys.exit()
