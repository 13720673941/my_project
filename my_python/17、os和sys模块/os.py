# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 15:22

"""
    python 中 os 库的使用
"""

import os

# os.getcwd:得到当前工作目录，即当前python脚本工作的目录路径。
print(os.getcwd())

# os.curdir:返回当前目录
print(os.curdir)

# os.pardir:获取当前目录的父目录字符串名：('..')
print(os.pardir)

# os.listdir():返回指定目录下的所有文件和目录名
print(os.listdir(os.getcwd()))

# os.pardir
# os.makedirs():创建文件夹
# os.makedirs(os.getcwd()+"\\test01")

# 函数用来运行shell命令
os.system("dir")

# 运行shell命令，生成对象，可赋给变量，再用read读取
a = os.popen("bash command")
out = a.read()
print(out)

# 获取当前目录
print(os.path.dirname(__file__))

# 获取当前上级目录
print(os.path.dirname(os.path.dirname(__file__)))

# os.path.exists():判断文件是否存在返回 true/false
print(os.path.exists(os.getcwd()))

# os.path.isfile(path)                如果path是一个存在的文件，返回True。
# os.path.isdir(path)                 如果path是一个存在的目录，则返回True
# os.path.isabs(path)                 如果path是绝对路径，返回True
# os.path.isdir(path)                 如果path是一个存在的目录，则返回True
# os.path.join(path1[, path2[, ...]]) 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join(os.getcwd(),'test',"test1","__init__.py"))
# os.path.getatime(path)              返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)              返回path所指向的文件或者目录的最后修改时间
# os.path.getctime(path)              返回path所指向的文件或者目录的最后修改时间
print(os.path.getctime(os.getcwd()))

print(os.path.abspath(__file__))