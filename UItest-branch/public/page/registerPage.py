# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/27 18:03

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log = Log()
'''
注册页面信息
'''

class RegisterPage(BasePage):

    '''网点注册页面信息'''
    register_url = 'http://www.51shouhou.cn/singleBranch/#/login'
    ParentPath = '//div[contains(text(),"企业用户注册")]/../form/ul'
    freeRegister = (By.XPATH,'//p[text()="还没有网点账号？"]/a')
    inputUserName = (By.XPATH,''+ParentPath+'/li[2]/input')
    inputPhoneNum = (By.XPATH,''+ParentPath+'/li[3]/input')
    inputCodeNum = (By.XPATH,''+ParentPath+'/li[4]/input')
    getCodeNumBtn = (By.XPATH,''+ParentPath+'/li[4]/a')
    inputLoginPwd = (By.XPATH,''+ParentPath+'/li[5]/input')
    inputConfirmPwd = (By.XPATH,''+ParentPath+'/li[6]/input')
    registerBtn = (By.XPATH,'//a[text()="马上注册"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_register_page(self):
        '''进入注册页面'''
        self.open_url(self.register_url)

    def click_free_register(self):
        '''点击登录页面免费注册'''
        self.click_button(self.freeRegister)
        #log.info('{0}点击->免费注册'.format(self.success))

    def input_username(self,UserName):
        '''输入注册用户名'''
        self.input_message(self.inputUserName,UserName)
        #log.info('{0}输入注册用户名: {1}'.format(self.success,UserName))

    def input_phoneNum(self,PhoneNum):
        '''输入注册手机号'''
        self.input_message(self.inputPhoneNum,PhoneNum)
        #log.info('{0}输入注册手机号: {1}'.format(self.success,PhoneNum))

    def input_codeNum(self,CodeNum):
        '''输入验证码'''
        self.input_message(self.inputCodeNum,CodeNum)
        #log.info('{0}输入验证码: {1}'.format(self.success,CodeNum))

    def input_login_pwd(self,LoginPwd):
        '''输入登录密码'''
        self.input_message(self.inputLoginPwd,LoginPwd)
        #log.info('{0}输入登录密码: {1}'.format(self.success,LoginPwd))

    def input_confirm_pwd(self,ConfirmPwd):
        '''输入确认密码'''
        self.input_message(self.inputConfirmPwd,ConfirmPwd)
        #log.info('{0}输入确认密码: {1}'.format(self.success,ConfirmPwd))

    def click_register_btn(self):
        ''''点击注册按钮'''
        self.click_button(self.registerBtn)
        #log.info('{0}点击->立即注册'.format(self.success))
