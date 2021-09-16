# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/13 1:13

"""
鼠标操作方法等
"""

from selenium.webdriver.common.action_chains import ActionChains

from common.seleniumLibrary.find import Find
from common.tools.decorator import error_collection


class Actions(Find):

    @error_collection
    def drag_and_drop(self, firstElement: tuple, secondElement: tuple):
        """
        长按拖拽按钮从某元素到另一个元素
        :param firstElement: 需要长安的按钮
        :param secondElement: 拖拽到的元素
        """
        # 查找页面开始长按的按钮及拖动结束的元素位置
        startElement = self._find_element(firstElement)
        endElement = self._find_element(secondElement)
        try:
            ActionChains(self.driver).drag_and_drop(startElement, endElement).perform()
        except:
            raise Exception(f"长按拖拽按钮：{firstElement} 移动到按钮：{secondElement} 失败！！！")
        else:
            self.Log.info(f"长按拖拽按钮：{firstElement} 移动到按钮：{secondElement} 释放长按按钮")
        # 释放长按按钮
        ActionChains(self.driver).release(startElement)

    @error_collection
    def move_and_click(self, elementPath: tuple):
        """
        移动到某元素上并点击
        :param elementPath:元素定位方式和路径组合
        :return:
        """
        button = self._find_element(elementPath)
        try:
            ActionChains(self.driver).move_to_element(button).click().perform()
        except:
            raise Exception(f"鼠标移动到按钮：{elementPath} 上并点击失败！！！")
        else:
            self.Log.info(f"鼠标移动到按钮: {elementPath} 上并点击按钮")

    @error_collection
    def click_hold_on(self, elementPath: tuple, isRelease: bool = False, holdTime: int = 3):
        """
        点击并长按按钮
        :param holdTime: 按钮长安时间默认 3s
        :param isRelease: 是否释放长安按钮
        :param elementPath:元素定位方式和路径组合
        :return:
        """
        button = self._find_element(elementPath)
        try:
            ActionChains(self.driver).click_and_hold(button).perform()
        except:
            raise Exception(f"点击并长按按钮：{elementPath} 失败！！！")
        else:
            if isRelease:
                self.sleep(holdTime)
                ActionChains(self.driver).release(button).perform()
                self.Log.info(f"点击并长按按钮：{elementPath} 保持 {holdTime}s 释放按钮")
            else:
                self.Log.info(f"点击并长按按钮：{elementPath}")
        pass

    @error_collection
    def drag_and_drop_by_offset(self, elementPath: tuple, x_offset: int, y_offset: int, isRelease: bool = False):
        """
        长按按钮并移动到规定坐标量位置
        :param isRelease: 是否释放长安按钮
        :param elementPath: 元素定位方式和路径组合
        :param x_offset: 移动到所在位置的 x 坐标
        :param y_offset: 移动到所在位置的 y 坐标
        :return:
        """
        button = self._find_element(elementPath)
        try:
            ActionChains(self.driver). \
                drag_and_drop_by_offset(source=button, xoffset=x_offset, yoffset=y_offset).perform()
        except:
            raise Exception(f"长按并拖拽按钮: {elementPath} 到X坐标: {x_offset} ，Y坐标: {y_offset} 失败！！！")
        else:
            if isRelease:
                ActionChains(self.driver).release(button).perform()
                self.Log.info(f"长按并拖拽按钮: {elementPath} 到X坐标: {x_offset} ，Y坐标: {y_offset} 释放按钮")
            else:
                self.Log.info(f"长按并拖拽按钮: {elementPath} 到X坐标: {x_offset} ，Y坐标: {y_offset}")
        pass

    @error_collection
    def move_on_element(self, elementPath: tuple):
        """
        鼠标移动到元素上面
        :param elementPath:
        :return:
        """
        element = self._find_element(elementPath)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            raise Exception(f"鼠标移动到元素：{elementPath} 失败！！！")
        else:
            self.Log.info(f"鼠标移动到元素：{elementPath} 上面")
