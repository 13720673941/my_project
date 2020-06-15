# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/26 17:17

import datetime

# 获取当前时间带毫秒
print(datetime.datetime.now())

# 获取当前日期
print(datetime.datetime.now().date())

# 获取当前时间tuple
print(datetime.datetime.now().timetuple())
print(datetime.datetime.now().timetuple().tm_hour)

# 时间移动（几天、几小时前后...） 1 加一天 ，-1 减一天  参数：weeks，days，hours，minutes，seconds，microseconds
print(datetime.datetime.now()-datetime.timedelta(days=1))

# 例如：求上个月最后一天(从这个月第一天让时间向前减一天)
print(datetime.date(day=1,month=datetime.date.today().month,year=datetime.date.today().year)-datetime.timedelta(days=1))

# 获取两个时间的时间差
print((datetime.datetime.now()-datetime.datetime.utcnow()).total_seconds())

# datetime转str格式
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# str格式转datetime格式
print(datetime.datetime.strptime("2020-05-26 17:36:35","%Y-%m-%d %H:%M:%S"))