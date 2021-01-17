# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/19 16:58

"""
页面元素等待方法，装饰器
"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.keywordDB import KeywordDB as KDB
from config.varConfig import *
from util.logConfig import Logger

Log = Logger().logger


def wait(function):
    def inner(*args, **kwargs):
        """等待页面元素是否在页面显示"""
        if args[1] not in KDB.BY_DB.keys():
            raise Exception(
                "传入的参数中定位方式：{}字段不正确！允许传入字段：id,name,class,text,css,xpath,tag_name".format(args[1]))
        try:
            WebDriverWait(args[0].driver, SysConfig.FIND_TIMEOUT, 1). \
                until(EC.visibility_of_element_located((KDB.BY_DB[args[1]], args[2])))
            # Log.info("检测页面元素成功！方法名称：{} 定位方式：{} 路径：{} ".format(function.__name__, args[1], args[2]))
        except Exception:
            Log.error(
                "{} 秒内页面中没有检测到元素！方法名：{} 定位方式：{} 路径：{} ".format(
                    SysConfig.FIND_TIMEOUT, function.__name__, args[1], args[2]))
            raise
        return function(*args, **kwargs)
    return inner
