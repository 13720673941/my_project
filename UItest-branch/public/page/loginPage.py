#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/21 10:45

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from config.urlconfig import *
# 实例化
log = Log()

class LoginPage(BasePage): # 所有的操作继承Base基类

    """
    登录页面信息
    """
    
    # 用户名输入框
    username_input = (By.XPATH,'//input[@type="text"]')
    # 密码输入框
    password_input = (By.XPATH,'//input[@type="password"]')
    # 登陆按钮
    login_btn = (By.XPATH,'//a[@class="loginBtn"]')
    # 退出按钮
    logout_btn = (By.XPATH,'//a[text()="退出"]')
    # 弹窗
    dump_windows = (By.XPATH,'//div[@class="modal-dialog"]//a[text()="关闭"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_login_page(self):
        """进入登陆页面"""
        self.open_url(login_url)

    def input_username(self,UserName):
        """输入用户名"""
        self.clear_input(self.username_input)
        self.input_message(self.username_input,UserName)

    def input_password(self,PassWord):
        """输入密码"""
        self.clear_input(self.password_input)
        self.input_message(self.password_input,PassWord)

    def click_login_button(self):
        """点击登陆按钮"""
        self.click_button(self.login_btn)

    def click_logout_button(self):
        """点击退出按钮"""
        self.click_button(self.logout_btn)

    def dumps_window_close(self):
        """判断是否有提醒充值的弹窗并且关闭"""

        # 如果弹窗出现
        if self.is_display(self.dump_windows):
            # 点击关闭
            self.click_button(self.dump_windows)
        else:
            pass


    def login_main(self,UserName,PassWord):
        """
        :param UserName: 登录用户名
        :param PassWord: 登录密码
        :return:
        """
        log.info('-=【网点登录】=-')
        for i in range(10):
            self.wait()
            self.enter_login_page()
            self.input_username(UserName)
            self.input_password(PassWord)
            self.click_login_button()
            self.sleep(1)
            # 断言
            if self.get_current_url() == review_url:
                self.refresh_page()
                log.info('{0} ** Branch login success！'.format(self.success))
                break
            elif i == 9:
                log.error('{0} ** Branch login fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
                break
            else:
                self.refresh_page()

# if __name__ == '__main__':
#
#
#     from selenium import webdriver
#
#     d = webdriver.Chrome()
#
#     d.maximize_window()
#
#     login = LoginPage(d)
#
#     login.login_main("13700000004","11111")

