# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/16 23:45

"""
切入、切出页面中的frame框架
"""

from selenium.common.exceptions import NoSuchFrameException

from common.seleniumLibrary.base import Base
from common.tools.decorator import error_collection


class Frame(Base):

    def wait_frame(self, elementPath: tuple) -> bool:
        """
        等待页面frame框架加载
        :return:
        """
        try:
            self.wait_frame_to_be_available(elementPath)
        except:
            return False
        else:
            return True

    @error_collection
    def switch_into_frame(self, elementPath: tuple):
        """
        切换进入页面frame框架
        :param elementPath:
        :return:
        """
        frameElement = self._find_element(elementPath)
        if self.wait_frame(elementPath):
            self.driver.switch_to_frame(frameElement)
            self.Log.info(f"切换进入frame框架：{elementPath}")
        else:
            raise NoSuchFrameException(f"切换进入frame框架：{elementPath} 失败！！！")

    @error_collection
    def switch_out_frame(self, elementPath: tuple):
        """
        切换出页面frame框架
        :param elementPath:
        :return:
        """
        frameElement = self._find_element(elementPath)
        if self.wait_frame(elementPath):
            self.driver.switch_to.default_content(frameElement)
            self.Log.info(f"切换出去frame框架：{elementPath}")
        else:
            raise NoSuchFrameException(f"切换出frame框架：{elementPath} 失败！！！")
