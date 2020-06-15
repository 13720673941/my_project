# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 11:52

import logging

"""
    logging 模块的使用
    
    级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG 
    默认生成的root logger的level是logging.WARNING,低于该级别的就不输出
"""

def base():
    """
    :param level 日志等级
    :param format 日志格式
    :param asctime 创建时间
    :param filename 文件名称
    :param lineno 行数
    :param levelname 日志等级名称
    :param message 日志信息
    """
    logging.basicConfig(level=logging.DEBUG,
                        #日志格式 %()s
                        format="%(asctime)s - %(filename)s[line: %(lineno)s] - %(levelname)s: %(message)s")

    logging.info("aaaaa")
    logging.debug("bbbbb")
    logging.warning("ccccc")
    logging.error("ddddd")

def log():
    """
    保存日志到txt文件中
    :return:
    """
    # 实例化 创建logger
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(level=logging.DEBUG)
    # 输出到控制台
    printConsole = logging.StreamHandler()
    # 输出到文件
    printFile = logging.FileHandler("test.log")
    # 定义日志格式
    format = logging.Formatter("%(asctime)s-%(filename)s[Line: %(lineno)s] - %(levelname)s: %(message)s")
    # 添加日志格式
    printConsole.setFormatter(format)
    printFile.setFormatter(format)
    # 添加到handle中
    logger.addHandler(printFile)
    logger.addHandler(printConsole)

    return logger


if __name__ == '__main__':

    log = log()


    log.info("aaaaaaaaaaaaa")
    log.error("nnnnnnnnnnnnnn")
    log.warning("ddddddddddddd")

    try:
        print("a"+1)
    except Exception as e:
        log.error(e)