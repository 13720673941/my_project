#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/26 15:41

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By

class ForgetPwd(BasePage):
    """
    忘记密码页面
    """
    
    # 忘记密码页面所有元素的父路径
    parent_path = '//div[text()="忘记密码"]/../form/ul'
    # 忘记密码按钮
    forget_pwd_btn = (By.XPATH,'//a[@class="forgetbtn"]')
    # 手机号输入框
    phe_num_input = (By.XPATH,''+parent_path+'/li[1]/input')
    # 验证码输入框
    code_num_input = (By.XPATH,''+parent_path+'/li[2]/input')
    # 获取验证码按钮
    get_code_btn = (By.XPATH,''+parent_path+'/li[2]/a')
    # 新密码输入框
    new_pwd_input = (By.XPATH,''+parent_path+'/li[3]/input')
    # 确定密码输入框
    confirm_pwd_input = (By.XPATH,''+parent_path+'/li[4]/input')
    # 重置密码输入框
    reset_pwd_btn = (By.XPATH,'//a[text()="重置密码"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_forgetPwd_btn(self):
        """点击忘记密码按钮"""
        self.click_button(self.forget_pwd_btn)

    def input_phoneNum(self,PhoneNum):
        """输入手机号"""
        self.input_message(self.phe_num_input,PhoneNum)

    def click_getCode_btn(self):
        """点击获取验证码按钮"""
        self.click_button(self.get_code_btn)

    def input_codeNum(self,CodeNum):
        """输入验证码"""
        self.input_message(self.code_num_input,CodeNum)

    def input_new_pwd(self,NewPwd):
        """输入新设置的密码"""
        self.input_message(self.new_pwd_input,NewPwd)

    def input_confirm_pwd(self,ConfirmPwd):
        """确认输入密码"""
        self.input_message(self.confirm_pwd_input,ConfirmPwd)

    def click_reset_pwd_btn(self):
        """点击重置密码按钮"""
        self.click_button(self.reset_pwd_btn)

    def get_codeBtn_attribute(self,AttrName):
        """获取验证码按钮属性判断是否发送成功"""
        return self.get_att(self.get_code_btn,AttrName)

