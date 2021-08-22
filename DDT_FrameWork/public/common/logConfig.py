# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 17:58

"""
python中logging模块二次封装
"""

from config.filePathConfig import logSavePath

import logging
import datetime


class Logger:

    def __init__(self):
        # 实例化
        self.logger = logging.getLogger()
        # 清除日志handles中缓存的句柄
        self.logger.handlers.clear()
        # 设置日志等级
        self.logger.setLevel(logging.INFO)

        # 创建一个日志句柄输出到文件中
        fileHandle = logging.FileHandler(
            filename=logSavePath + datetime.datetime.now().strftime("%Y-%m-%d") + ".log",
            mode="a",
            encoding="utf-8"
        )
        # 创建一个日志句柄输出到控制台
        consoleHandle = logging.StreamHandler()

        # 添加日志输出格式
        printFormat = logging.Formatter("%(asctime)s-[%(filename)s]-Line: %(lineno)d %(levelname)s: %(message)s")

        # 日志打印格式添加到句柄中
        fileHandle.setFormatter(printFormat)
        consoleHandle.setFormatter(printFormat)

        # 添加句柄
        self.logger.addHandler(fileHandle)
        self.logger.addHandler(consoleHandle)

    @property
    def origin_logger(self):
        return self.logger


if __name__ == '__main__':
    Log = Logger().origin_logger
    Log.info("info")
    Log.error("error")
    Log.warning("warning")
