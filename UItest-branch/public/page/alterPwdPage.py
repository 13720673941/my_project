#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/21 18:25

from public.common.basePage import BasePage
from config.urlConfig import *
from config.pathConfig import *

class AlterPwdPage(BasePage):
    """
        【网点登录后修改密码/手机号页面】
    """

    def get_elements(self,option):
        """获取element_data文件中修改密码/手机号页面的元素信息"""
        return read_config_data("alter_pwd_page",option,elementDataPath)

    def enter_alterPwd_page(self):
        """进入修改密码页面"""
        self.open_url(alter_pwd_url,self.get_elements("alter_of_phe_btn"))

    def click_alter_pheNum(self):
        """点击修改手机号->修改"""
        self.click_button(self.get_elements("alter_of_phe_btn"))

    def input_login_pwd(self,login_pwd):
        """输入登录密码"""
        self.input_message(self.get_elements("login_pwd_input"),login_pwd)

    def get_login_pwd_msg(self):
        """获取登录密码提示信息"""
        return self.get_text(self.get_elements("login_pwd_none_msg"))

    def input_phe_num(self,phone_num):
        """输入手机号"""
        self.input_message(self.get_elements("phone_number_input"),phone_num)

    def get_phone_num_msg(self):
        """获取输入手机号提示"""
        return self.get_text(self.get_elements("phone_num_none_msg"))

    def click_code_button(self):
        """点击获取验证码"""
        self.click_button(self.get_elements("send_verification_code_btn"))

    def get_code_button_att(self):
        """获取发送验证码后: 获取验证码按钮-disabled属性"""
        return self.get_att(self.get_elements("send_verification_code_btn"),'disabled')

    def input_code_number(self,code_num):
        """输入验证码"""
        self.input_message(self.get_elements("verification_code_input"),code_num)

    def get_code_input_msg(self):
        """获取验证码输入框系统提示"""
        return self.get_text(self.get_elements("code_none_msg"))

    def click_confirm_alter(self):
        """点击确定修改"""
        self.click_button(self.get_elements("confirm_alter_phe_btn"))

    def click_alter_pwd(self):
        """点击修改密码->修改"""
        self.click_button(self.get_elements("alter_of_pwd_btn"))

    def input_old_pwd(self,old_pwd):
        """输入旧密码"""
        self.input_message(self.get_elements("old_pwd_input"),old_pwd)

    @property
    def get_old_pwd_msg(self):
        """获取旧密码为空的系统提示"""
        return self.get_text(self.get_elements("old_pwd_none_msg"))

    def input_new_pwd(self,new_pwd):
        """输入新密码"""
        self.input_message(self.get_elements("new_pwd_input"),new_pwd)

    @property
    def get_new_pwd_msg(self):
        """获取新密码为空提示"""
        return self.get_text(self.get_elements("new_pwd_none_msg"))
    
    def input_confirm_pwd(self,confirm_pwd):
        """输入确认密码"""
        self.input_message(self.get_elements("confirm_pwd_input"),confirm_pwd)

    @property
    def get_confirm_pwd_msg(self):
        """获取确认密码为空提示"""
        return self.get_text(self.get_elements("confirm_pwd_none_msg"))

    def click_confirm_alterPwd(self):
        """修改密码下面的确定修改"""
        self.click_button(self.get_elements("confirm_alter_pwd_btn"))

