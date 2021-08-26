# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/26 21:57

"""
时间格式相关处理
"""

import time

standardDateTime = "%Y-%m-%d %H:%M:%S"


class TimeTools:

    @staticmethod
    def get_now_time() -> int:
        """
        获取当前时间戳
        :return:
        """
        return int(time.time())

    @staticmethod
    def get_now_date(timeFormat=standardDateTime) -> str:
        """
        获取当前日期时间
        :param timeFormat: 标准年月日时分秒格式
        :return:
        """
        return time.strftime(timeFormat, time.localtime(time.time()))

    @staticmethod
    def change_time_stamp(dataTime: str, dataFormat=standardDateTime) -> int:
        """
        转化成时间戳
        :param dataTime: 具体时间
        :param dataFormat: 默认标准格式
        :return:
        """
        return int(time.mktime(time.strptime(dataTime, dataFormat)))

    @staticmethod
    def change_data_time(timeStamp: int, timeFormat=standardDateTime) -> str:
        """
        转化成时间格式
        :param timeStamp: 时间戳
        :param timeFormat: 默认标准格式
        :return:
        """
        return time.strftime(timeFormat, time.localtime(timeStamp))


if __name__ == '__main__':
    t = TimeTools.get_now_date()
    print(t)
