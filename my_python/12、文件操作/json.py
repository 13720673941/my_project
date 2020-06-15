# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/28 11:11

import json

# 1.json.dumps()函数是将字典转化为字符串
dict1 = {"age": "12"}
json_info = json.dumps(dict1)

# 2.json.loads()函数是将字符串转化为字典
json_info1 = '{"age": "12"}'
dict1 = json.loads(json_info1)

# 3.json.dump()函数的使用，将json信息写进文件
json_msg = {"in": {"install_date": "2018/09/26","install_result": "success"}}
file = open('1.json', 'w')
json.dump(json_msg, file)

# 4.json.load()函数的使用，将读取json信息
file = open('1.json','r',encoding='utf-8')
info = json.load(file)
with open('1.json', 'r') as f:
    data = json.load(f)