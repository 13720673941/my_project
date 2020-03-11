#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/27 16:15

import random
from config.pathConfig import *
"""
    随机生成手机号码和注册用户名
"""
def create_phoneNum():
    '''随机生成手机号'''

    # 电话本保存文档
    PhoneBook = regPhonePath
    # 11位手机号 1开头，后面十位随机产生，系统注册没有过多要求
    # 初始化手机号为1开头的电话号
    PhoneNum='1'
    # 无限循环直到生成没有重复的手机号
    while True:
        # 循环随机生成10个数字
        for i in range(10):
            # 随机0-9数字
            randomNum = random.randint(0,9)
            PhoneNum = PhoneNum+str(randomNum)
        # 读取电话本
        NewList=[]
        with open(PhoneBook,'r',encoding='UTF-8') as f:
            # 逐行读取
            for line in f.readlines():
                # 使用strip函数去除 换行
                NewList.append(line.strip('\n'))
        # 遍历电话本列表,如果生成的话号不再列表中停止循环
        if PhoneNum not in NewList:
            # 生成的电话写入txt文档
            with open(PhoneBook,'a') as f:
                # 一行一行写入便于读取
                f.write(PhoneNum+'\n')
            break
        else:
            # 如果在列表中及继续循还生成号码
            continue
    # print('* Create phone number: {0}.'.format(PhoneNum))
    return PhoneNum

def create_username():
    '''随机生成用户名'''

    # 获取用户名的txt文档
    UserNameData = regUserPath
    # 用户名默认设置为固定五个汉字,五个字母和8个数字组合
    # 生成26个字母列表
    LetterList=list(map(chr,range(ord('a'),ord('z')+1)))
    while True:
        # 初始化字母名字
        UserName1 = ''
        for i in range(5):
            randomNum = random.randint(0,25)
            randomLetter = LetterList[randomNum]
            UserName1 = UserName1+randomLetter
        # 初始化数字名字
        UserName2 = ''
        for i in range(5):
            # 随机0-9数字
            randomNum = random.randint(0,9)
            UserName2 = UserName2+str(randomNum)
        # 正确的用户名
        UserName = '自动化注册' + UserName1 + UserName2
        # 读取用户名文档判断不能重复
        UserNameList=[]
        with open(UserNameData,'r',encoding='gbk') as f:
            for line in f.readlines():
                # 去掉换行符
                line.strip('\n')
                UserNameList.append(line)
        # 判断是否重复
        if UserName not in UserNameList:
            # 写入txt文档
            with open(UserNameData,'a') as f:
                f.write(UserName+'\n')
            break
        else:
            continue
    # print('* Create user name: {0}.'.format(UserName))
    return UserName



 #
 # print(CreateUserName())
 # print(CreatePhoneNum())


