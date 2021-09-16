# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/9/16 23:44

"""
浏览器cookie相关操作
"""

from common.seleniumLibrary.browser import Browser


class Cookie(Browser):

    def get_cookie(self, name: str) -> str:
        """
        获取当前浏览器cookie中某一值
        :param name:
        :return:
        """
        cookieValue = self.driver.get_cookie(name)
        self.Log.info(f"获取浏览器cookies中 {name} 的值：{cookieValue}")
        return cookieValue

    def get_cookies(self) -> list:
        """
        获取浏览器所有cookie值
        :return:
        """
        cookiesLs = self.driver.get_cookies()
        self.Log.info(f"获取浏览器所有cookie：\n{cookiesLs}")
        return cookiesLs

    def del_cookie(self, name: str):
        """
        删除cookie中某一项
        :return:
        """
        self.driver.delete_cookie(name)
        self.Log.info(f"删除cookies中name为：{name} 的值")

    def del_cookies(self):
        """
        删除所有cookies
        :return:
        """
        self.driver.delete_all_cookies()
        self.Log.info("删除所有cookies")

    def set_cookies(self, name: str, value: str, path: str = None, domain: str = None, secure: bool = None,
                    expiry: int = None):
        """
        设置浏览器cookies
        :param name: 名称必填
        :param value: 值必填
        :param path: 路径选填
        :param domain: 域名选填
        :param secure: 布尔类型，true cookie只能通过https协议发给服务器
        :param expiry: 有效时间戳
        :return:
        """
        cookiesDict = {"name": name, "value": value}
        if path is not None:
            cookiesDict["path"] = path
        if domain is not None:
            cookiesDict["domain"] = domain
        if secure is not None:
            cookiesDict["secure"] = secure
        if expiry is not None:
            cookiesDict["expiry"] = expiry
        self.Log.info(f"设置浏览器cookie：\n{cookiesDict}")
        self.driver.add_cookie(cookiesDict)
