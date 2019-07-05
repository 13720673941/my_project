# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import logging

def logFormat(logFile):

    if logFile == None:
        pass
    else:
        #输出日志到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s[%(filename)s(line:%(lineno)d)]%(levelname)s:%(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

def setFormatter(logFile):

    global logger, fh, ch
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    #创建一个handler，用于写入日志文件
    fh = logging.FileHandler(logFile,'w')
    #创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    #定义handler的输出格式format
    format1 = logging.Formatter('%(asctime)s[%(filename)s(line:%(lineno)d)]%(levelname)s:%(message)s')
    format2 = logging.Formatter('[%(filename)s-(line:%(lineno)d)]%(levelname)s:%(message)s')

    #给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    fh.setFormatter(format1)
    ch.setFormatter(format2)

def removeHandler():
    #避免日志重复
    logger.removeHandler(fh)
    logger.removeHandler(ch)

