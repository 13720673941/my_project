# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2021/1/17 22:42

"""
    宝塔面板登录页面
"""

from action.pageAction import PageAction
from config.varConfig import BaoTaConfig
from util.logConfig import Logger

Log = Logger().logger


class LoginPage(PageAction):

    usernameInput = '//input[@placeholder="账号"]'
    passwordInput = '//input[@placeholder="密码"]'
    loginButton = 'login-button'

    def enter_login_page(self):
        self.open_url(BaoTaConfig.BT_URL)
        Log.info("打开宝塔登录页面：{}".format(BaoTaConfig.BT_URL))

    def input_username(self):
        self.send("xpath", self.usernameInput, BaoTaConfig.BT_USERNAME)
        Log.info("输入宝塔登录账号：{}".format(BaoTaConfig.BT_USERNAME))

    def input_password(self):
        self.send("xpath", self.passwordInput, BaoTaConfig.BT_PASSWORD)
        Log.info("输入宝塔登录密码：{}".format(BaoTaConfig.BT_PASSWORD))

    def click_login(self):
        self.click("id", self.loginButton)
        Log.info("点击登录按钮")


if __name__ == '__main__':
    bt = LoginPage()
    bt.open_browser('pc')
    bt.enter_login_page()
    bt.input_username()
    bt.input_password()
    bt.click_login()
