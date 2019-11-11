#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/21 14:41

from config.pathconfig import *
import logging,time

"""日志二次封装"""

# 日志写入路径

class Log:

    def __init__(self):
        """输出日志到控制台和日志记录"""
        self.log_file = logSavePath + '{0}.log'.format(time.strftime('%Y-%m-%d'))

    def printConsole(self,level,message):
        # 创建日志，设置日志等级
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 创建一个文件输出到日志,不用追加日志,只保留当天
        fh = logging.FileHandler(self.log_file,'a',encoding='utf-8')
        fh.setLevel(logging.INFO)
        # 创建一个文件输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 添加日志
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        # 清除日志
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self,message):
        self.printConsole('debug',message)

    def info(self,message):
        self.printConsole('info',message)

    def warning(self,message):
        self.printConsole('warning',message)

    def error(self,message):
        self.printConsole('error',message)



#  print(saveLogToFile(logName='mytest'))