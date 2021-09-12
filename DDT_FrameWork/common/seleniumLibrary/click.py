# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/13 0:40

"""
点击页面元素：左键单击、左键双击、右键单击
"""

from selenium.webdriver.common.action_chains import ActionChains
from common.seleniumLibrary.base import Base


class Click(Base):

    def click(self, elementPath: tuple):
        """
        点击页面元素按钮
        :param elementPath:
        :return:
        """
        self._find_element(elementPath).click()
        self.Log.info(f"点击页面元素：{elementPath[1]}")

    def double_click(self, elementPath: tuple):
        """
        鼠标左键双击按钮
        :param elementPath:
        :return:
        """
        element = self._find_element(elementPath)
        ActionChains(self.driver).double_click(element).perform()
        self.Log.info(f"双击页面按钮元素：{elementPath}")

    def right_click(self, elementPath: tuple):
        """
        右键点击按钮
        :param elementPath:
        :return:
        """
        element = self._find_element(elementPath)
        ActionChains(self.driver).context_click(element).perform()
        self.Log.info(f"鼠标右键点击页面按钮元素：{elementPath}")


if __name__ == '__main__':
    from selenium.webdriver.common.by import By
    from common.seleniumLibrary import PySelenium

    el = PySelenium()
    el.open_url("http://www.baidu.com")
    el.input(elementPath=(By.ID, "kw"), value="python")
    el.click((By.ID, "su"))