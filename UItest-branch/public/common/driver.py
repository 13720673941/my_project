# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/8 10:58

from selenium import webdriver
from public.common.rwConfig import read_config_data
from config.pathConfig import *
from public.common.logConfig import Log
import os,warnings
warnings.filterwarnings("ignore")

# 获取配置文件中的浏览器名称
browser = read_config_data("Browser","browser_name",configPath)

def web_driver(browserType=browser):
    """
    根据浏览器类型选择启动，返回driver. 这里只使用 IE Chrome FireFox
    :param browser_type: 浏览器类型
    """
    # 实例化日志
    log = Log()
    # 本地网络校验 尝试ping百度网址
    isConnect = os.popen("ping www.baidu.com")
    if "请求找不到主机" in isConnect.read():
        # 检查网咯连接 源码中已封装日志模块 调用后会冲突
        # checkWifiIsConnect()
        raise TimeoutError("Intent connect is time out !")
    # 判断浏览器类型
    if browserType == "chrome":
        driver = webdriver.Chrome()
    elif browserType.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browserType.lower() == "internet explorer":
        driver = webdriver.Ie()
    else:
        raise NameError(
            "Not find browser: {0}, you can enter: chrome, firefox, internet explorer .".format(browserType))
    log.info(' * Launch browser of "{0}" . '.format(browserType))
    driver.maximize_window()

    return driver