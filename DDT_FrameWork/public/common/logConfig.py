# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 14:41

from config.pathConfig import *
import logging,datetime

"""
    logging 日志模块的二次封装
"""

class Log:

    def __init__(self):
        # 配置生成日志名称后缀 .log / .txt
        self.logName = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt"
    def printConsole(self,level,message):

        # 实例化日志类
        logger = logging.getLogger()
        # 每次使用都需要清除之前的handle否则会打印重复
        # logger.handlers.clear()
        # 设置日志等级，级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
        logger.setLevel(logging.INFO)
        # 创建日志输出到文件中保存
        fh = logging.FileHandler(LOG_SAVE_PATH+self.logName,"a",encoding="utf-8")
        # 创建日志输出到控制台
        ch = logging.StreamHandler()
        # 定义日志输出格式
        format =logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        # 设置日志格式
        fh.setFormatter(format)
        ch.setFormatter(format)
        # 添加到logger中
        logger.addHandler(fh)
        logger.addHandler(ch)

        if level == "info":
            logger.info(message)
        elif level == "error":
            logger.error(message)
        elif level == "warning":
            logger.warning(message)
        elif level == 'debug':
            logger.debug(message)

        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def info(self,message):
        self.printConsole("info",message)

    def error(self,message):
        self.printConsole("error",message)

    def warning(self,message):
        self.printConsole("warning",message)

    def debug(self,message):
        self.printConsole("debug",message)



if __name__ == '__main__':

    # 代码测试
    log = Log()
    log.info("aaaaaaaa")
    log.error("bbbbbbb")
    log.warning("ccccccc")