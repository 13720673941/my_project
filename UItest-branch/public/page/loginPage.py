#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/21 10:45

from public.common.basePage import BasePage
from config.urlConfig import *

class LoginPage(BasePage):

    """
        【登录页面功能】
    """

    def get_elements(self,option):
        """获取element_data文件中登录页面的元素信息"""
        return read_config_data("login_page",option,elementDataPath)

    def enter_login_page(self):
        """进入登陆页面"""
        self.open_url(login_url,self.get_elements("username_input"))

    def enter_first_page_review(self):
        """进入首页工单预览页面"""
        self.open_url(review_url)

    def input_username(self,username):
        """输入用户名"""
        self.clear_input(self.get_elements("username_input"))
        self.input_message(self.get_elements("username_input"),username)

    def input_password(self,password):
        """输入密码"""
        self.clear_input(self.get_elements("password_input"))
        self.input_message(self.get_elements("password_input"),password)

    def click_login_button(self):
        """点击登陆按钮"""
        self.click_button(self.get_elements("login_button"))

    def click_logout_button(self):
        """点击退出按钮"""
        for i in range(5):
            try:
                self.click_button(self.get_elements("logout_button"))
                break
            except:
                if i == 4:
                    raise TimeoutError("Not find logout button in page !")
                else:
                    continue

    def get_system_msg(self):
        """获取系统提示信息"""
        try:
            system_message = self.get_text(self.get_elements("system_message"))
            return system_message
        except:
            return "System message is none."

    def login_main(self,section):
        """
        登录主程序，后面功能直接调用登录的主程序传入用户名密码就好了
        :param section:  只需要传入账号配置文件中section值即可
        :param UserName: 登录用户名
        :param PassWord: 登录密码
        """
        # 获取测试账号
        username = read_config_data(section,"username",accountDataPath)
        password = read_config_data(section,"password",accountDataPath)
        self.log.info('-=【网点登录】=-')
        for i in range(5):
            self.enter_login_page()
            self.input_username(username)
            self.input_password(password)
            self.click_login_button()
            self.sleep(2)
            # 断言
            if self.get_current_url() == review_url:
                self.refresh_page()
                self.log.info(' ** Branch login success！')
                break
            elif i == 4:
                raise TimeoutError(
                    ' ** Branch login fail, system msg: {0}.'.format(self.get_system_msg()))
            else:
                self.refresh_page()

