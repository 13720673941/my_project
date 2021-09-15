# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/13 0:40

"""
点击页面元素：左键单击、左键双击、右键单击
"""

from selenium.webdriver.common.action_chains import ActionChains

from common.seleniumLibrary.find import Find
from common.tools.decorator import error_collection


class Click(Find):

    @error_collection
    def click(self, elementPath: tuple):
        """
        点击页面元素按钮
        :param elementPath:
        :return:
        """
        self._find_element(elementPath).click()
        self.Log.info(f"点击页面元素：{elementPath[1]}")

    @error_collection
    def double_click(self, elementPath: tuple):
        """
        鼠标左键双击按钮
        :param elementPath:
        :return:
        """
        element = self._find_element(elementPath)
        ActionChains(self.driver).double_click(element).perform()
        self.Log.info(f"双击页面按钮元素：{elementPath}")

    @error_collection
    def right_click(self, elementPath: tuple):
        """
        右键点击按钮
        :param elementPath:
        :return:
        """
        element = self._find_element(elementPath)
        ActionChains(self.driver).context_click(element).perform()
        self.Log.info(f"鼠标右键点击页面按钮元素：{elementPath}")

    @error_collection
    def submit(self, elementPath: tuple):
        """
        提交表单，此源码需要在一个表单（Form）中，并且type需要时submit类型
        :param elementPath:
        :return:
        """
        self._find_element(elementPath).submit()
        self.Log.info(f"点击提交按钮：{elementPath} 提交页面表单")


if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    from common.seleniumLibrary import PySelenium

    el = PySelenium()
    el.open_url("http://www.baidu.com")
    el.input(elementPath=(By.ID, "kw0"), value="python")
    el.click((By.ID, "su"))
