# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/13 0:21

"""
输入框操作相关方法
"""

from common.seleniumLibrary.find import Find
from common.tools.decorator import error_collection


class Input(Find):

    @error_collection
    def input(self, elementPath: tuple, value: str):
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


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    element = Input()
    element.open_url("http://www.baidu.com")
    element.input(elementPath=(By.ID, "kw"), value="python")
