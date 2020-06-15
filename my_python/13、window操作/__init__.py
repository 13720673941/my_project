# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/15 12:22

import requests
import json
import hashlib
import datetime模块

url = "http://apitest/supervise/manage/searchInfo"

headers = {"Content-Type": "application/json", "User_Agent": "sec_test"}
now_time = datetime模块.datetime.now().strftime('%Y-%m-%d')  # 获取当前日期

data = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYnJhbmNoMDQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiLnvZHngrnllYbnu4QiLCJuYmYiOjE1ODI2MTQ5ODYsImV4cCI6MTU4MzgyNDU4NiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo1MDAwIn0.tsj9zJ0ZAjmYyYFduDckARM14zXIl1GdWnqhgQAcQTg", # 认证后的授权token
    "timestamp": now_time,
    "param":"UseSparePartLog(BranchPkId='76bd5ee6-4469-4bdf-a843-e4502cc45cbb',TradeId='undefined'):{UseSparePartLogId[desc],SparePartId,Num,SparePartName,TreeCode,SparePartModel,SparePartType,SparePartBrand,TotalMoney,IsCharge}"
}

keys = []
for key in data:
    keys.append(key)

keys = sorted(keys)  # 参数首字母Ascii升序
aa = []
for key in keys:
    if isinstance(data[key], int):
        data[key] = str(data[key])
    aa.append(key + '=' + data[key])

# print(" ASCII", ord('a'),ord('k'),ord('p'),ord('c'),ord('s'))
str = ''
index = 0
for s in aa:
    index = index + 1
    if index == len(aa):
        str = str + s
    else:
        str = str + s + '&'

signature = hashlib.md5(str.encode("utf-8")).hexdigest()  # 对参数拼接后进行md5
print(signature)
