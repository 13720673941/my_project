# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/16 23:45

"""
alert弹窗处理操作，接受、取消、输入、获取文本
"""

from selenium.webdriver.common.alert import Alert as _Alert
from selenium.common.exceptions import NoAlertPresentException

from common.seleniumLibrary.base import Base
from common.tools.decorator import error_collection


class Alert(Base):

    def wait_alert(self) -> bool:
        """
        等待alert弹窗出现
        :return:
        """
        try:
            self.wait_alert_is_present()
        except:
            return False
        else:
            return True

    @error_collection
    def switch_into_alert(self) -> _Alert:
        if self.wait_alert():
            self.Log.info("切换进入当前页面对话框")
        else:
            raise NoAlertPresentException("没有浏览器弹窗出现，切入失败！！！")
        return self.driver.switch_to.alert

    @error_collection
    def accept_alert(self):
        """
        接受alert弹窗
        :return:
        """
        try:
            self.switch_into_alert().accept()
        except:
            raise NoAlertPresentException("没有浏览器弹窗出现，接受失败！！！")
        else:
            self.Log.info("接受当前浏览器对话弹窗")

    @error_collection
    def dismiss_alert(self):
        """
        取消alert弹窗
        :return:
        """
        try:
            self.switch_into_alert().dismiss()
        except:
            raise NoAlertPresentException("没有浏览器弹窗出现，取消失败！！！")
        else:
            self.Log.info("取消当前浏览器对话弹窗")

    @error_collection
    def input_alert(self, value: str):
        """
        alert弹窗中输入字段
        :param value: 输入字符串
        :return:
        """
        try:
            self.switch_into_alert().send_keys(value)
        except:
            raise NoAlertPresentException(f"没有浏览器弹窗出现，输入：{value}失败！！！")
        else:
            self.Log.info(f"当前浏览器对话弹窗中输入：{value}")

    @error_collection
    def get_alert_text(self) -> str:
        """
        获取alert弹窗显示字段
        :return:
        """
        try:
            text = self.switch_into_alert().text
            self.Log.info(f"获取对话框内容：{text}")
        except:
            raise NoAlertPresentException("没有浏览器对话弹窗出现，获取信息失败！！！")
        return text
