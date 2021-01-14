# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:36

"""
webdriver类中操作浏览器方法二次封装
"""

from selenium import webdriver

from config.varConfig import SysConfig
from util.logConfig import Logger
from util.waitUtil import wait
from config.keywordDB import KeywordDB as KDB

Log = Logger().logger


class PageAction:

    def __init__(self):
        self.driver = None

    def open_browser(self, openBrowserType):
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
            mobileEmulation = {'deviceName': SysConfig.MOBILE_TYPE}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobileEmulation)
            self.driver = webdriver.Chrome(options=options)
            Log.info("正在打开谷歌浏览器切换: {} 手机模式...".format(SysConfig.MOBILE_TYPE))
        else:
            raise NameError("打开浏览器类型传入字段不正确，系统允许字段：pc、h5 ")

    def get_element(self, by, value):
        """查找页面元素"""
        return self.driver.find_element(KDB.BY_DB[by], value)

    def get_elements(self, by, value):
        """获取一组元素"""
        return self.driver.find_elements(by, value)

    def open_url(self, url):
        """打开网页地址"""
        self.driver.get(url)

    @wait
    def clear(self, by, value):
        """清除输入框"""
        self.get_element(by, value).clear()

    @wait
    def send(self, by, value, text):
        """输入字段"""
        self.get_element(by, value).send_keys(text)

    @wait
    def click(self, by, value):
        """点击按钮"""
        self.get_element(by, value).click()

    @wait
    def click_text(self, by, value, text, like=False):
        """
        点击文本，下拉模糊匹配等
        :param by: 定位方式
        :param value: 元素路径
        :param text: 匹配文本
        :param like: 是否开启模糊匹配
        :return:
        """
        elementsList = self.get_elements(by, value)
        # 判断元素文本点击元素
        for el in elementsList:
            if like and el.text == text:
                el.click()
                break
            elif not like and text in el.text:
                el.click()
                break
        else:
            raise Exception("根据定位：{}->{}, 没有找到带文本：{} 的元素".format(by,value,text))

    def switch_handle(self):
        """切换新窗口"""
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
        else:
            raise Exception("没有可以切换的窗口！")

    def switch_frame(self, by, value):
        """切换到iframe"""
        frame = self.get_element(by, value)
        self.driver.switch_to.frame(frame)

    def out_frame(self):
        """切换出iframe"""
        self.driver.switch_to.default_content()

    def alert_confirm(self):
        """接受alert弹窗"""
        self.driver.switch_to.alert().accept()

    def alert_refuse(self):
        """取消alert弹窗"""
        self.driver.switch_to.alert().dismiss()

    @wait
    def get_text(self, by, value):
        """获取元素文本信息"""
        return self.get_element(by, value).text

    @wait
    def get_attr(self, by, value, keyName):
        """获取元素属性"""
        return self.get_element(by, value).get_attribute(keyName)

    def set_attr(self, by, value, attribute, attValue):
        """
        设置标签的属性值
        :param by: 定位方式
        :param value: 元素路径
        :param attribute: 属性名称
        :param attValue: 属性值
        :return:
        """
        element = self.get_element(by, value)
        self.driver.execute_script("arguments[0].{}='{}';".format(attribute, attValue), element)

    def get_title(self):
        """获取页面title"""
        return self.driver.get_title



if __name__ == '__main__':
    pass
