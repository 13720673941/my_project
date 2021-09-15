# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/12 20:46

"""
显式等待页面元素，等待元素是否可点击，iframe框架，alert弹窗，固定等待时间，隐式等待
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from common.seleniumLibrary.browser import Browser

import time


class Wait(Browser):

    def wait_presence_of_element(self, elementPath: tuple, timeout=10, poll_frequency=1):
        """
        找到页面元素是都存在页面上，不关心是否可见
        :param timeout: 等待超时时间，默认10s
        :param poll_frequency: 步长，每隔几秒检查一次，默认 1s
        :param elementPath: 元素路径，元素类型
        :return: bool
        """
        message = f"当前页面中 {timeout}s 内没有找到对应元素：{elementPath} ！！！"
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(elementPath),
                                                                      message)
        except NoSuchElementException:
            raise NoSuchElementException
        else:
            self.Log.info(f"当前页面中 {timeout}s 内已检索到对应元素：{elementPath}")

    def wait_visibility_of_element(self, elementPath: tuple, timeout=10, poll_frequency=1):
        """
        找到页面元素是都存在页面上，且元素可见
        :param timeout: 等待超时时间，默认10s
        :param poll_frequency: 步长，每隔几秒检查一次，默认 1s
        :param elementPath: 元素路径，元素类型
        :return: bool
        """
        message = f"当前页面中 {timeout}s 内没有找到或不可见对应元素：{elementPath} ！！！"
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(elementPath),
                                                                      message)
        except NoSuchElementException:
            raise NoSuchElementException
        else:
            self.Log.info(f"当前页面中 {timeout}s 内已检索到且可见对应元素：{elementPath}")

    def wait_element_to_be_clickable(self, elementPath: tuple, timeout=10, poll_frequency=1):
        """
        等待页面元素出现判断元素是否可以点击
        :param timeout: 等待超时时间，默认10s
        :param poll_frequency: 步长，每隔几秒检查一次，默认 1s
        :param elementPath: 元素路径，元素类型
        :return: bool
        """
        message = f"当前页面中 {timeout}s 内没有找到或不可点击对应元素：{elementPath} ！！！"
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(elementPath), message)
        except NoSuchElementException:
            raise NoSuchElementException
        else:
            self.Log.info(f"当前页面中 {timeout}s 内已检索到且可以点击对应元素：{elementPath}")

    def wait_frame_to_be_available(self, elementPath: tuple, timeout=10, poll_frequency=1):
        """
        等待iframe框出现并且切换到iframe框架内
        :param timeout: 等待超时时间，默认10s
        :param poll_frequency: 步长，每隔几秒检查一次，默认 1s
        :param elementPath: 元素路径，元素类型
        :return: bool
        """
        message = f"当前页面中 {timeout}s 内没有找到iframe框架对应元素：{elementPath} ！！！"
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(elementPath), message)
        except NoSuchFrameException:
            raise NoSuchFrameException
        else:
            self.Log.info(f"当前页面中 {timeout}s 内已检索到iframe框架并切换进对应元素：{elementPath}")

    def wait_alert_is_present(self, timeout=10, poll_frequency=1):
        """
        等待页面弹窗出现并切入弹窗内
        :param timeout: 等待超时时间，默认10s
        :param poll_frequency: 步长，每隔几秒检查一次，默认 1s
        :return: bool
        """
        message = f"当前页面中 {timeout}s 内没有找到alert弹窗 ！！！"
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present(), message)
        except NoAlertPresentException:
            raise NoAlertPresentException
        else:
            self.Log.info(f"当前页面中 {timeout}s 内已检索到 alert 弹窗")

    def sleep(self, seconds=2):
        """
        等待页面加载死等
        :param seconds: 固定等待时间，默认2s
        :return:
        """
        time.sleep(seconds)
        self.Log.info(f"固定等待 {seconds}s 页面加载...")

    def wait_in_time(self, seconds=10):
        """
        隐式等待页面加载几秒，几秒内等待页面加载，完成后跳过等待
        :param seconds: 超时等待时间，默认10s
        :return:
        """
        self.driver.implicitly_wait(seconds)
        self.Log.info(f"隐式等待 {seconds}s 页面加载...")


if __name__ == '__main__':
    from selenium.webdriver.common.by import By

    element = Wait()
    element.open_url("http://www.baidu.com")
    element.wait_visibility_of_element(elementPath=(By.ID, "kw"))
