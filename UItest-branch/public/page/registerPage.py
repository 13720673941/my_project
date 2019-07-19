#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/27 18:03

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from config.urlconfig import *
"""
注册页面信息
"""
class RegisterPage(BasePage):

    # 注册页面所有元素的父路径
    parent_path = '//div[contains(text(),"企业用户注册")]/../form/ul'
    # 免费注册按钮
    free_register_btn = (By.XPATH,'//p[text()="还没有网点账号？"]/a')
    # 用户名输入框
    username_input = (By.XPATH,''+parent_path+'/li[2]/input')
    # 手机号输入框
    phe_num_input = (By.XPATH,''+parent_path+'/li[3]/input')
    # 验证码输入框
    code_num_input = (By.XPATH,''+parent_path+'/li[4]/input')
    # 获取验证码按钮
    get_code_num_btn = (By.XPATH,''+parent_path+'/li[4]/a')
    # 登陆密码输入框
    login_pwd_input = (By.XPATH,''+parent_path+'/li[5]/input')
    # 确定登陆密码输入框
    confirm_pwd_input = (By.XPATH,''+parent_path+'/li[6]/input')
    # 马上注册按钮
    register_btn = (By.XPATH,'//a[text()="马上注册"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_register_page(self):
        """进入注册页面"""
        self.open_url(login_url)

    def click_free_register(self):
        """点击登录页面免费注册"""
        self.click_button(self.free_register_btn)

    def input_username(self,UserName):
        """输入注册用户名"""
        self.input_message(self.username_input,UserName)

    def input_phoneNum(self,PhoneNum):
        """输入注册手机号"""
        self.input_message(self.phe_num_input,PhoneNum)

    def input_codeNum(self,CodeNum):
        """输入验证码"""
        self.input_message(self.code_num_input,CodeNum)

    def input_login_pwd(self,LoginPwd):
        """输入登录密码"""
        self.input_message(self.login_pwd_input,LoginPwd)

    def input_confirm_pwd(self,ConfirmPwd):
        """输入确认密码"""
        self.input_message(self.confirm_pwd_input,ConfirmPwd)

    def click_register_btn(self):
        """'点击注册按钮"""
        self.click_button(self.register_btn)
