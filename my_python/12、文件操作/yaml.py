# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/10 9:21

"""
yaml是一个专门用来写配置文件的语言。

1. yaml文件规则
区分大小写；
使用缩进表示层级关系；
使用空格键缩进，而非Tab键缩进
缩进的空格数目不固定，只需要相同层级的元素左侧对齐；
文件中的字符串不需要使用引号标注，但若字符串包含有特殊字符则需用引号标注；
注释标识为#
2. yaml文件数据结构
对象：键值对的集合（简称 "映射或字典"）
键值对用冒号 “:” 结构表示，冒号与值之间需用空格分隔
数组：一组按序排列的值（简称 "序列或列表"）
数组前加有 “-” 符号，符号与值之间需用空格分隔
纯量(scalars)：单个的、不可再分的值（如：字符串、bool值、整数、浮点数、时间、日期、null等）
None值可用null可 ~ 表示
"""

from ruamel import yaml

desired_caps = {
    "模块":"登录功能测试用例",
    "测试数据":[
        {"用例名称":"验证正确的用户名密码可以成功登录","用户名":"13700000001","密码":"111111"},
        {"用例名称":"验证正确的用户名密码可以成功登录","用户名":'13700000001',"密码":"111111"},
    ]
}

# with open("test.yaml","w") as f:
#     yaml.dump(desired_caps,f,encoding="utf-8",allow_unicode=True,Dumper=yaml.RoundTripDumper)

with open("test.yaml","r") as f:
    data=yaml.load(f,Loader=yaml.Loader)
    print(data)
