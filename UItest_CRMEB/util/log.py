# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:24

"""
python中logging模块的二次封装
"""

import logging

from config.varConfig import FilePathConfig
from util.timeTool import Time

# 日志保存路径
logPath = FilePathConfig.LOG_SAVE_PATH


class Log:

    def __init__(self):

        # 创建一个logger对象
        self.logger = logging.getLogger()

        # 设置日志输出格式
        fileLogFormat = logging.Formatter(
            "%(asctime)s-[%(filename)s]-line: %(lineno)d %(levelname)s: %(message)s")

        # 创建输出到文件夹日志句柄
        fileHandle = logging.FileHandler(
            "{}\\{}.log".format(logPath, Time.get_now_date()), "a", encoding='utf-8')
        # 设置日志文件格式
        fileHandle.setFormatter(fileLogFormat)

        # 控制台日志格式
        consoleLogFormat = logging.Formatter(
            "[%(filename)s]-line: %(lineno)d %(levelname)s: %(message)s")

        # 创建输出到控制台日志句柄
        consoleHandle = logging.StreamHandler()
        # 添加控制台日志格式
        consoleHandle.setFormatter(consoleLogFormat)

        # 判断日志句柄列表中是否存在处理器，防止日志重复打印
        if not self.logger.handlers:
            # logger添加日志日志处理器
            self.logger.addHandler(consoleHandle)
            self.logger.addHandler(fileHandle)

        # 定义输出日志等级为最低级别，默认WARNING
        self.logger.setLevel(logging.INFO)


if __name__ == '__main__':
    # 测试代码
    Log().logger.info("定义输出日志等级为最低级别，默认WARNING")
