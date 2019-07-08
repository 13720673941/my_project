# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/7 16:23

# 定义一个列表 统计你的所有爱好

hobby_list = []

while True:

    hobby_name = input("please your hobby of "+str(len(hobby_list))+": ")

    # 如果输入的值为空退出程序

    if hobby_name == '':

        break

    # 把输入的爱好加入道列表中 也可以使用 append()

    hobby_list = hobby_list+[hobby_name]

print("your all hobby are: ")

# 遍历列表循环打印所有爱好

for hobby in hobby_list:

    print(" "+"hobby: "+hobby)