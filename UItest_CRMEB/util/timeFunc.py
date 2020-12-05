# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:24

"""
python中time、datetime模块的二次封装
"""

import time
from datetime import datetime


class Time:

    @classmethod
    def get_now_date(cls): return str(datetime.now().date())

    @classmethod
    def get_now_time(cls, timeFormat): return datetime.now().strftime(timeFormat)

    @classmethod
    def get_now_stamp(cls): return int(time.time())

    @classmethod
    def get_now_year(cls): return datetime.now().year

    @classmethod
    def get_now_month(cls): return datetime.now().month

    @classmethod
    def get_now_day(cls): return datetime.now().day

    @classmethod
    def get_now_hour(cls): return datetime.now().hour

    @classmethod
    def get_now_minute(cls): return datetime.now().minute

    @classmethod
    def get_now_seconds(cls): return datetime.now().second

    @classmethod
    def convert_to_timestamp(cls, dateTime):
        return int(time.mktime(time.strptime(dateTime, "%Y-%m-%d %H:%M:%S")))


if __name__ == '__main__':
    # 测试代码
    tm = Time.get_now_stamp()
    print(tm)
