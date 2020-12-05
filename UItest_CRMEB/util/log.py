# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:24

"""
python中logging模块的二次封装
"""

import logging

from config.fileConfig import *
from util.timeFunc import Time


class Log:

    def __init__(self):
        # 日志配置信息
        self.logFile = LOG_SAVE_PATH + "\\" + Time.get_now_date() + ".log"
        self.logFormat = "%(asctime)s - [%(filename)s] - line: %(lineno)d - %(levelname)s: %(message)s"
        self.writeMode = "a"
        # 创建一个logger对象
        self.logger = logging.getLogger()

    @property
    def log(self):
        # 定义输出日志等级
        self.logger.setLevel(logging.INFO)
        # 判断句柄是否已存在防止日志重复打印
        if len(self.logger.handlers) == 0:
            # 创建输出到控制台日志句柄
            consoleHandle = logging.StreamHandler()
            # 创建输出到文件夹日志句柄
            fileHandle = logging.FileHandler(self.logFile, "a", encoding='utf-8')
            # 设置日志输出格式
            logFormat = logging.Formatter(self.logFormat)
            # 添加日志格式
            consoleHandle.setFormatter(logFormat)
            fileHandle.setFormatter(logFormat)
            # 添加日志
            self.logger.addHandler(consoleHandle)
            self.logger.addHandler(fileHandle)

        return self.logger


if __name__ == '__main__':
    # 测试代码
    log = Log().log
    log.info("aaaa")
    log.error("bbbb")
    log.warning("cccc")
