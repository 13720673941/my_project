# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/6 23:34

# if 语句为真就执行 if 下面的语句，为假就跳过 if 下面的语句

params = 'hello'

if params == 'hello':
    print('is true.')

# elif 和 if 用法一样

age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")

# else 不符合上述所有条件执行 else

name = 'james'

if name == 'kobe':
    print('hello kobe.')
else:
    print('who are you.')
