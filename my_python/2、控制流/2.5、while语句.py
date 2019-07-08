# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/6 23:48

# while 不满足条件可以无限循环

number = 0

while number < 10:
    print('number is < 10.')
    number = number + 1

# while 无限循环 只有当 name == quit 的时候才会退出

# break 停止循环

while True:
    name = input('please enter your name:')
    if name == 'quit':
        break

# continue 继续循环

while True:
    params = input('please enter a word:')
    if params != 'james':
        continue
    print('hello james, please input your password:')
    pwd = input('password:')
    if pwd == '111111':
        break
print('login success.')