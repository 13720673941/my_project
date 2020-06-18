# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/16 18:05

"""
    logging模块的二次封装
"""

from config.pathConfig import *
import logging,datetime

class Log:

    def __init__(self):
        # 定义日志名称
        self.name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".txt"

    def _print(self,level,message):
        # 创建一个对象
        logger = logging.getLogger()
        # 设置日志等级
        logger.setLevel(logging.INFO)
        # 创建日志输出到控制台
        ch = logging.StreamHandler()
        # 创建日志输出到文件夹
        fh = logging.FileHandler(LOG_SAVE_PATH+self.name)
        # 定义日志格式
        format = logging.Formatter("%(asctime)s-%(levelname)s: %(message)s")
        # 设置到控制台和日志中
        ch.setFormatter(format)
        fh.setFormatter(format)
        # 创建handle
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == "info":
            logger.info(message)
        elif level == "warning":
            logger.warning(message)
        elif level == "error":
            logger.error(message)
        elif level == "debug":
            logger.debug(message)
        
        # 清除handle防止日志重复打印
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def info(self,message):
        self._print("info",message)

    def error(self,message):
        self._print("error",message)

    def warning(self,message):
        self._print("warning",message)

    def debug(self,message):
        self._print("debug",message)


if __name__ == '__main__':

    log = Log()

    log.info("aaaaa")
    log.warning("bbbbb")
    log.error("ccccc")