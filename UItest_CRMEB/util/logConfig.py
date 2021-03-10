# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:24

"""
python中logging模块的二次封装
"""


from util.timeTool import Time
from config.varConfig import SysConfig
import logging


class Logger:

    def __init__(self):

        # 创建一个logger对象
        self.logger = logging.getLogger()

        if SysConfig.LOG_DEBUG:

            # 设置日志输出格式
            fileLogFormat = logging.Formatter(SysConfig.LOG_FILE_FORMATTER)

            # 创建输出到文件夹日志句柄
            fileHandle = logging.FileHandler(
                "{}\\{}.log".format(SysConfig.LOG_SAVE_PATH, Time.get_now_date()),
                SysConfig.LOG_MODE,
                encoding=SysConfig.LOG_ENCODING
            )
            # 设置日志文件格式
            fileHandle.setFormatter(fileLogFormat)

            # 控制台日志格式
            consoleLogFormat = logging.Formatter(SysConfig.LOG_CONSOLE_FORMATTER)

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
        self.logger.setLevel(SysConfig.LOG_LEVEL)

    @property
    def origin_log(self):
        """返回原生logger"""
        return self.logger


if __name__ == '__main__':
    # 测试代码
    Logger().logger.info("定义输出日志等级为最低级别，默认WARNING")
