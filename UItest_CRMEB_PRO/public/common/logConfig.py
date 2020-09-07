# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/8/23 15:38

"""
logging日志模块的二次封装
"""

from config.pathConfig import *
import logging,datetime

# 日志名称
timeStr = datetime.datetime.now().strftime("%Y-%m-%d")
# 日志名称保存路径配置
LOG_NAME = LOG_SAVE_PATH+"\\"+timeStr+".log"
# 日志写入方式
WRITE_MODE = "a"
# 打印日志格式
LOG_FORMAT = "%(asctime)s [%(filename)s]-line: %(lineno)d %(levelname)s: %(message)s"


class LogConfig:

    def __init__(self):
        # 创建日志对象
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.INFO)
        # 判断日志句柄列表是否存在已创建的句柄，防止日志重复打印
        if len(self.logger.handlers) == 0:
            # 创建输出对象
            fh = logging.FileHandler(filename=LOG_NAME,mode=WRITE_MODE,encoding='utf-8')
            ch = logging.StreamHandler()
            # 设置日志格式
            format = logging.Formatter(LOG_FORMAT)
            # 添加日志格式
            fh.setFormatter(format)
            ch.setFormatter(format)
            # 添加到句柄中
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger


if __name__ == '__main__':

    log = LogConfig().logger
    log.info("aaaaa")
    log.error("bbbbb")
    log.warning("ccccc")




