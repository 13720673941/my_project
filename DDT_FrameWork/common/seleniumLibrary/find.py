# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/9 18:14

"""
查找页面元素，查找一组元素，查找父元素路径下根据标签查找一组元素

** 该类为基类，webdriver下的所有操作方法都继承该类 **

"""

from common.seleniumLibrary.wait import Wait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class Find(Wait):

    def _find_element(self, elementPath: tuple) -> WebElement:
        """
        查找页面元素返回元素对象
        :param elementPath: 页面元素路径，eg: (By.ID, "kw")
        :return:
        """
        self.wait_visibility_of_element(elementPath)
        return self.driver.find_element(*elementPath)  # 源码中find_element方法传入两个参数

    def _find_elements(self, elementPath: tuple) -> list:
        """
        查找一组元素返回元素对象列表
        :param elementPath: 页面元素路径，eg: (By.ID, "kw")
        :return:
        """
        self.wait_visibility_of_element(elementPath)
        return self.driver.find_elements(*elementPath)

    def _find_elements_by_tag_name(self, elementPath: tuple, name: str) -> list:
        """
        当前父级元素目录下根据标签查找一组元素对象
        :param elementPath: 页面元素路径，eg: (By.ID, "kw")
        :param name: 标签名
        :return:
        """
        parentElement = self._find_element(elementPath)
        try:
            tagLs = parentElement.find_elements_by_tag_name(name)
            self.Log.info(f"根据元素标签名称：{name} 查找一组元素")
        except NoSuchElementException:
            raise NoSuchElementException(f"根据标签名称：{name} 查找一组元素失败！！！")
        return tagLs


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    el = Find()
    el.open_url("http://www.baidu.com")
    el._find_element(elementPath=(By.ID, "kw")).send_keys("python")
    el._find_element(elementPath=(By.ID, "su")).click()
