# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/6 16:00

"""
封装浏览器驱动driver方法，浏览器H5页面切换，目前只支持chrome
"""

from selenium import webdriver

from config.varConfig import *
from util.logConfig import Logger

Log = Logger().logger


class BrowserDriver:

    def __init__(self, openBrowserType="pc", iPhoneType="iPhone 8"):
        # 浏览器类型为pc打开浏览器为pc模式
        if openBrowserType == "pc":
            # 判断浏览器类型选择驱动
            if SysConfig.BROWSER_TYPE.lower() == "chrome":
                self.driver = webdriver.Chrome()
            elif SysConfig.BROWSER_TYPE.lower() == "firefox":
                self.driver = webdriver.Firefox()
            elif SysConfig.BROWSER_TYPE.lower() == "ie":
                self.driver = webdriver.Ie()
            else:
                raise NameError("浏览器类型字段错误，允许字段类型：chrome、firefox、ie ")
            # 浏览器最大化
            self.driver.maximize_window()
            Log.info("正在打开 {} 浏览器...".format(SysConfig.BROWSER_TYPE))
        # 浏览器类型为h5打开浏览器为手机模式，默认iphone8
        elif openBrowserType == "h5":
            mobileEmulation = {'deviceName': iPhoneType}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobileEmulation)
            self.driver = webdriver.Chrome(options=options)
            Log.info("正在打开谷歌浏览器切换: {} 手机模式...".format(iPhoneType))
        else:
            raise NameError("打开浏览器类型传入字段不正确，系统允许字段：pc、h5 ")

    @property
    def origin_driver(self):
        """返回原生driver"""
        return self.driver


if __name__ == '__main__':
    # 测试代码
    dr = BrowserDriver(openBrowserType="h5").origin_driver
    dr.get("http://www.baidu.com")
    print(dr.capabilities['browserVersion'])