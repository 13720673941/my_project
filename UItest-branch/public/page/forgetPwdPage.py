#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/26 15:41

from public.common.basePage import BasePage
from public.common.rwConfig import read_config_data
from config.pathConfig import *

class ForgetPwd(BasePage):
    """
        【忘记密码页面】
    """

    def get_elements(self,option):
        """获取element_data文件中登录页面的元素信息"""
        return read_config_data("forget_pwd_page",option,elementDataPath)

    def click_forgetPwd_btn(self):
        """点击忘记密码按钮"""
        self.click_button(self.get_elements("forget_pwd_btn"))

    def input_phoneNum(self,PhoneNum):
        """输入手机号"""
        self.input_message(self.get_elements("register_phone_input"),PhoneNum)

    def click_getCode_btn(self):
        """点击获取验证码按钮"""
        self.click_button(self.get_elements("send_code_btn"))

    def input_codeNum(self,CodeNum):
        """输入验证码"""
        self.input_message(self.get_elements("verification_code_input"),CodeNum)

    def input_new_pwd(self,NewPwd):
        """输入新设置的密码"""
        self.input_message(self.get_elements("new_pwd_input"),NewPwd)

    def input_confirm_pwd(self,ConfirmPwd):
        """确认输入密码"""
        self.input_message(self.get_elements("confirm_pwd_input"),ConfirmPwd)

    def click_reset_pwd_btn(self):
        """点击重置密码按钮"""
        self.click_button(self.get_elements("reset_pwd_btn"))

    def get_codeBtn_attribute(self,AttrName="class"):
        """获取验证码按钮属性判断是否发送成功,默认class属性"""
        return self.get_att(self.get_elements("send_code_btn"),AttrName)

