# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/17 0:13

"""
浏览器页面切换，切换到当前最新打开的页面，按标题名称切换、关闭窗口
"""

from common.seleniumLibrary.base import Base
from common.tools.decorator import error_collection


class Window(Base):

    def close_current_window(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
        self.Log.info(f"关闭当前名为：{self.driver.title} 页面窗口")

    @error_collection
    def close_window_by_title(self, title: str):
        """
        关闭当前浏览器中指定标题的窗口
        :param title:
        :return:
        """
        handleLs = self.get_window_handles()
        for handle in handleLs:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                self.Log.info(f"关闭当前名为：{self.driver.title} 页面窗口")
                self.close_current_window()
                return
        raise ValueError(f"所有页面中没有找到标题为：{title} 的页面！！！")

    @error_collection
    def switch_window_by_url(self, url: str):
        """
        切换到最新打开的页面中
        :param: 切换页面的url地址
        :return:
        """
        handleLs = self.get_window_handles()
        for handle in handleLs:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                self.Log.info(f"页面切换到当前url为：{self.driver.current_url} 页面窗口")
                return
        raise ValueError(f"所有页面中没有找到地址为：{url} 的页面切换窗口失败！！！")

    @error_collection
    def switch_window_by_title(self, title: str):
        """
        切换当前浏览器中指定标题的窗口
        :param title:
        :return:
        """
        handleLs = self.get_window_handles()
        for handle in handleLs:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                self.Log.info(f"页面切换到当前标题名为：{self.driver.title} 页面窗口")
                return
        raise ValueError(f"所有页面中没有找到标题为：{title} 的页面切换窗口失败！！！")

    def get_window_handles(self) -> list:
        """
        获取浏览器中所有页面的句柄
        :return:
        """
        handles = self.driver.window_handles
        self.Log.info(f"获取浏览器所有页面的句柄：\n{handles}")
        return handles

    def get_current_window_handle(self):
        """
        获取当前页面句柄
        :return:
        """
        handle = self.driver.current_window_handle
        self.Log.info(f"获取浏览器当前页面的句柄：{handle}")
        return handle
