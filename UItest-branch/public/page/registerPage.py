#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/27 18:03

from public.common.basePage import BasePage
from config.urlConfig import *
from config.pathConfig import *

class RegisterPage(BasePage):
    """
        【注册页面功能】
    """

    def get_elements(self,option):
        """获取element_data文件中注册页面的元素信息"""
        return read_config_data("register_page",option,elementDataPath)

    def enter_register_page(self):
        """进入注册页面"""
        self.open_url(login_url,self.get_elements("free_register_btn"))

    def click_free_register(self):
        """点击登录页面免费注册"""
        self.click_button(self.get_elements("free_register_btn"))

    def input_username(self,username):
        """输入注册用户名"""
        self.input_message(self.get_elements("username_input"),username)

    def input_phone_number(self,phone_number):
        """输入注册手机号"""
        self.input_message(self.get_elements("phone_number_input"),phone_number)

    def input_code_number(self,code_number):
        """输入验证码"""
        self.input_message(self.get_elements("verification_code_input"),code_number)

    def input_login_pwd(self,login_pwd):
        """输入登录密码"""
        self.input_message(self.get_elements("login_pwd_input"),login_pwd)

    def input_confirm_pwd(self,confirm_pwd):
        """输入确认密码"""
        self.input_message(self.get_elements("confirm_pwd_input"),confirm_pwd)

    def click_register_btn(self):
        """'点击注册按钮"""
        self.click_button(self.get_elements("register_btn"))

    def get_system_message(self):
        """获取系统提示信息"""
        return self.get_text(self.get_elements("system_message"))