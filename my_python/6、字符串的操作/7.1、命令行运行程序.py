#! python3
# test.py - An insecure password locker program

"""
1、创建该 bat 程序文本 加入环境变量
"""

password = {"email":"908066950@qq.com",
            "blog":"ashdkjhakjdhk2kakhdkahs9329",
            "luggage":"123456"}

import sys,pyperclip

if len(sys.argv) > 2:

    print("Usage: [account] - copy account password")

    sys.exit()

# sys.argv 生成一个列表 0 索引为 文件路径，1 索引为 命令行传入的第一个参数

account = sys.argv[1]

# 判断传入的参数的值是否在字典中sw

if account in password:

    pyperclip.copy(password[account])

    print("password for " + account + " copied to clipboard.")

else:

    print("There is no account named " + account)
