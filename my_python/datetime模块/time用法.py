# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/26 17:41

import calendar,time,datetime

print("当前时间戳：",time.time())

print("本地时间：",time.localtime(time.time()))

print("格式化时间：",time.asctime(time.localtime(time.time())))

print("格式化日期：",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

print("格式化成Sat Mar 28 22:24:24 2016形式：",time.strftime("%a %b %d %H:%M:%S",time.localtime()))

print("转化时间戳：",time.mktime(time.strptime("2020-05-26 17:48:13","%Y-%m-%d %H:%M:%S")))

print("以下输出2016年1月份的日历:")
print(calendar.month(2018,2))

while True:
    nowDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\r",nowDateTime,end="")