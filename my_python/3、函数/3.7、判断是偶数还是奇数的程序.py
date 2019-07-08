# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 15:30


# 数字小游戏 判断用户输入的数字是 偶数 还是 奇数

def collatz():

    while True:

        try:

            print("input qiut to exit.")

            input_number = int(input("please input a number: "))

            # 判断用户输入的是奇数 还是 偶数

            # 如果输入的数字除以 2 余 0 那么就是偶数 反则为 奇数
            if input_number % 2 == 0:

                print("your number is a even number.")

            else:

                print("your number is a odd number.")

        except ValueError:

            print("you must input a int type of number.")


collatz()