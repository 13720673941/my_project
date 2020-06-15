# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 11:38

"""
    .txt 文件的读写操作
    “r” 只读模式，不能编辑和删除文件内容。
    “w” 写入模式，会先将文件之前的内容清空，然后再写入。
    “a” 追加模式，会将数据添加的之前内容的后面。
"""

# txt 文件路径
filePath = "txttest"

# 写入文本字符串
with open(filePath,"w",encoding="utf-8") as f:
    f.write("python 是世界最好的编程语言！"+"\n")

# 写入列表
with open(filePath,"a",encoding="utf-8") as f:
    f.writelines(["python","java","php","javascript"])

# 读取全部
with open(filePath,"r",encoding="utf-8") as f:
    print(f.read())

# 逐行读取
with open(filePath,"r",encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())

# # 读取所有行返回列表
# with open(filePath,"r",encoding="utf-8") as f:
#     print(f.readlines())

