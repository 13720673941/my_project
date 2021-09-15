# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/26 23:47

"""
浏览器相关操作二次封装，打开浏览器、退出浏览器、打开网址、获取标题、获取url、刷新浏览器等。
"""

from common.tools.operateConfigData import OperateConfigData
from config.filePathConfig import *
from common.tools.logConfig import Logger

from selenium import webdriver


class Browser:
    # 实例化类
    rc = OperateConfigData(browserConfigPath).read_config_data()
    Log = Logger().origin_logger
    # 获取浏览器名称
    browserName = rc.get("browser", "name", fallback="Chrome")
    waitTime = rc.getint("browser", "wait_time", fallback=10)

    # 浏览器配置
    isHeadless = rc.getboolean("browser_config", "headless", fallback=False)
    isDisable = rc.getboolean("browser_config", "disable_info", fallback=False)
    automation = rc.getboolean("browser_config", "automation", fallback=False)

    # H5模式配置信息
    iPhoneName = rc.get("H5", "iPhone_name", fallback="iPhone 8")
    iPhoneWith = rc.getint("H5", "with", fallback=350)
    iPhoneHeight = rc.getint("H5", "height", fallback=700)

    # 谷歌驱动文件目录
    driverStart = rc.get("driver_path", "path", fallback=None)

    def __init__(self, isH5: bool = False):
        """
        实例化webdriver类
        :param isH5:  是否打开为手机模式
        """
        if self.driverStart is None:
            raise TypeError("文件：browser.ini 下谷歌驱动路径：driver_path 配置异常！！！")
        # 是否打开浏览器为手机模式
        optionSet = self.set_driver(isH5)
        # 打开浏览器实例
        try:
            self.driver = getattr(webdriver, self.browserName)(executable_path=self.driverStart, options=optionSet)
            self.Log.info(f"正在打开：{self.browserName} 浏览器...")
        except:
            self.driver = webdriver.Chrome(executable_path=self.driverStart, options=optionSet)
            self.Log.warning(f"浏览器名称：{self.browserName} 配置不正确，默认打开 Chrome 浏览器...")

        self.Log.info(f"设置隐式等待：{self.waitTime}s")
        self.driver.implicitly_wait(self.waitTime)

        # 设置浏览器大小
        if isH5:
            self.window_set_size(self.iPhoneWith, self.iPhoneHeight)
        else:
            self.window_max_size()

    def set_driver(self, isH5: bool) -> object:
        """
        设置浏览器配置相关信息
        :param isH5: 是否打开为手机模式
        :return:
        """
        # 打开浏览器类型
        if self.browserName.lower() == "chrome":
            optionSet = webdriver.ChromeOptions()
        elif self.browserName.lower() == "firefox":
            optionSet = webdriver.FirefoxOptions()
        elif self.browserName.lower() == "ie":
            optionSet = webdriver.IeOptions()
        else:
            optionSet = webdriver.ChromeOptions()

        # 是否无头模式运行
        optionSet.headless = self.isHeadless

        # 关闭密码保存询问弹窗
        configData = {
            "credentials_enable_service": self.isDisable,
            "profile.password_manager_enabled": self.isDisable
        }

        # H5模式打开手机类型配置
        mobileEmulation = {"deviceName": self.iPhoneName}

        # 添加配置
        optionSet.add_experimental_option("prefs", configData)
        # 是否打开H5模式
        if isH5:
            optionSet.add_experimental_option("mobileEmulation", mobileEmulation)
            self.Log.info(f"设置浏览器打开模式为：{self.iPhoneName} 手机模式")
        # 关闭自动化控制提示条
        if not self.automation:
            optionSet.add_experimental_option("excludeSwitches", ['enable-automation'])

        return optionSet

    def open_url(self, url: str, new: bool = False):
        """打开地址"""
        if new:
            self.driver.execute_script(f"window.open('{url}')")
            self.Log.info(f"新打开一个网页地址：{url}")
        else:
            self.driver.get(url)
            self.Log.info(f"当前窗口打开地址：{url}")

    def close(self):
        """关闭窗口"""
        self.driver.close()
        self.Log.info("关闭当前页面窗口")

    def quit(self):
        """退出浏览器"""
        self.driver.quit()
        self.Log.info("退出当前浏览器")

    def refresh_browser(self):
        """刷新浏览器"""
        self.driver.refresh()
        self.Log.info("刷新当前浏览器")

    def get_current_url(self) -> str:
        """获取当前页面url"""
        url = self.driver.current_url
        self.Log.info(f"获取当前页面url地址：{url}")
        return url

    def get_page_title(self) -> str:
        """获取页面标题"""
        title = self.driver.title
        self.Log.info(f"获取当前页面标题信息：{title}")
        return title

    def back(self):
        """返回上一级页面"""
        self.driver.back()
        self.Log.info("返回浏览器上一级操作页面")

    def forward_page(self):
        """前进一级页面"""
        self.driver.forward()
        self.Log.info("前进浏览器下一个操作页面")

    def window_max_size(self):
        """浏览器最大化"""
        self.driver.maximize_window()
        self.Log.info("当前浏览器窗口最大化")

    def window_set_size(self, windowWith, windowHeight):
        """设置浏览器尺寸大小"""
        self.driver.set_window_size(windowWith, windowHeight)
        self.Log.info(f"设置当前浏览器尺寸，宽：{windowWith} 高：{windowHeight} ")

    @property
    def origin_driver(self):
        return self.driver


if __name__ == '__main__':
    Browser(isH5=True).open_url(url="https://www.baidu.com")
