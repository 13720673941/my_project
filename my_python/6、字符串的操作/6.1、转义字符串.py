# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/14 20:53

# 转义字符:: \' 单引号 \" 双引号 \t 制表符 \n 换行符 \\ 倒斜符

# \' :: 表示单引号

print("I\'m fine.")

# \" :: 表示双引号

print("my name is \"DengPengFei\".")

# \t :: 表示缩进，制表符

print("What\'s your name?")
print("\tMy name is DengPengFei.")

# \n :: 表示换行

print("my\nname\nis\nDengPengFei.")

# \\ :: 表示倒斜符,一般用于文件夹的路径

print("D:\\my_test_script\\my_python")

# r 原始字符串 :: 加上 r 所有的转义符号都没有作用

print(r"my\'s name is \"dpf\"")


# 三重引号的多行字符串 :: 可以多行输出 还可以表示多行注释

# 多行输出

print("""
Hello!
What is your name?
My name is DengPengFei.
""")

# 多行注释

"""
this is comments.
"""