# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/16 23:00

"""
页面元素相关操作，点击、输入、清除、获取文本、属性、是否可见、是否已选、是否可点
"""

from selenium.webdriver.common.action_chains import ActionChains

from common.seleniumLibrary.base import Base
from common.tools.decorator import error_collection


class Element(Base):

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
        el = self._find_element(elementPath)
        ActionChains(self.driver).context_click(el).perform()
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

    @error_collection
    def send_keys(self, elementPath: tuple, value: str):
        """
        输入关键字
        :param elementPath: 元素路径
        :param value: 输入关键字
        :return:
        """
        self._find_element(elementPath).send_keys(value)
        self.Log.info(f"输入框：{elementPath} 中输入关键字：{value}")

    @error_collection
    def clear(self, elementPath: tuple):
        """
        清除输入框数据
        :param elementPath:
        :return:
        """
        self._find_element(elementPath).clear()
        self.Log.info(f"清除输入框：{elementPath} 数据")

    @error_collection
    def get_text(self, elementPath: tuple) -> str:
        """
        获取元素文本信息
        :param elementPath:
        :return:
        """
        text = self._find_element(elementPath).text
        self.Log.info(f"获取元素：{elementPath} 文本信息：{text}")
        return text

    @error_collection
    def get_attribute(self, elementPath: tuple, name: str) -> str:
        """
        获取页面元素属性信息
        :param elementPath:
        :param name:
        :return:
        """
        attribute = self._find_element(elementPath).get_attribute(name)
        self.Log.info(f"获取元素：{elementPath} 属性：{name} 文本信息：{attribute}")
        return attribute

    @error_collection
    def is_displayed(self, elementPath: tuple) -> bool:
        """
        获取页面元素是否可见
        :param elementPath:
        :return:
        """
        isDisplayed = self._find_element(elementPath).is_displayed()
        self.Log.info(f"获取元素：{elementPath} 是否可见返回：{isDisplayed}")
        return isDisplayed

    @error_collection
    def is_selected(self, elementPath: tuple) -> bool:
        """
        获取页面元素是否已选中
        :param elementPath:
        :return:
        """
        isSelected = self._find_element(elementPath).is_selected()
        self.Log.info(f"获取元素：{elementPath} 是否选中可见返回：{isSelected}")
        return isSelected

    @error_collection
    def is_enabled(self, elementPath: tuple) -> bool:
        """
        获取页面元素是否可点击，有些按钮置灰不能点击，eg：disabled="disabled"
        :param elementPath:
        :return:
        """
        isEnabled = self._find_element(elementPath).is_enabled()
        self.Log.info(f"获取元素：{elementPath} 是否选中可点击返回：{isEnabled}")
        return isEnabled


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    element = Element()
    element.open_url("http://www.baidu.com")
    element.send_keys(elementPath=(By.ID, "kw"), value="python")
    element.click(elementPath=(By.ID, "su"))
