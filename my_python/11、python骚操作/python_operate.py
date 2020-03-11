# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/12 11:06

# 1 列表转化字符串

list_a = ["name","age","tall"]

print(" ".join(list_a))

# 2 查找列表出现最多次数的字符串

list_b = [1,2,3,4,2,2,2,1,2,3,4,5,6,6]

print(max(set(list_b),key=list_b.count))

# 3 列表倒转

list_c = [1,2,3,4]

print(list_c[::-1])

# 4 转置二维数组

list_d = [[1,2],[3,4],[5,6]]

print(list(zip(*list_d)))

# 5 链式函数调用, 链式判断

a = 1
b = 2

print("a>b"if a>b else "a<b")

def add(c,d):

    return c+d

def subtract(c,d):

    return d-c

start=False

print((add if start else subtract)(5,1))

# 6 字典 get 方法

dict_1 = {"a":2,"b":1}

print(dict_1.get("b"))

# 7 通过「键」排序字典元素
print(sorted(dict_1.items(),key=lambda x:x[1]))
print(sorted(dict_1,key=dict_1.get))


# 8 For Else

list_e = [1,2,3,4,5,6,6]

for i in list_e:

    if i == 6:

        print("溜溜溜")
# 9 没有在循环下所以这里else只执行一次
else:
    print("垃圾")


# 10 转换列表为逗号分割符格式

list_f = ["ff","ch","ie","op"]

print(",".join(list_f))


# 11 合并字典

dict_2 = {"a":1}
dict_3 = {"b":2}

# python3.5 以上
print({**dict_2,**dict_3})

print(dict(dict_2.items()|dict_3.items()))

# --
dict_2.update(dict_3)
print(dict_2)

# 12 移除列表中的重复元素

list_g = [1,1,2,3,4,4,4,4,]

print(list(set(list_g)))

# 13 列出当前目录下的所有文件和目录名
import os

print([d for d in os.listdir('.')])

# 14 把一个list中所有的字符串变成小写

list_aa = ["A","C"]

