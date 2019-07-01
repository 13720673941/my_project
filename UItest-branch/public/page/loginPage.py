# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/21 10:45

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
#实例化
log = Log()

'''
登录页面信息
'''
class LoginPage(BasePage):#所有的操作继承Base基类

    '''网点登录界面信息'''
    #系统登陆页面url
    login_url = 'http://www.51shouhou.cn/singleBranch/#/login'
    #用户名输入框
    username_input = (By.XPATH,'//input[@type="text"]')
    #密码输入框
    password_input = (By.XPATH,'//input[@type="password"]')
    #登陆按钮
    login_btn = (By.XPATH,'//a[@class="loginBtn"]')
    #退出按钮
    logout_btn = (By.XPATH,'//a[text()="退出"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_login_page(self):
        '''进入登陆页面'''
        self.open_url(self.login_url)

    def input_username(self,UserName):
        '''输入用户名'''
        self.clear_input(self.username_input)
        self.input_message(self.username_input,UserName)

    def input_password(self,PassWord):
        '''输入密码'''
        self.clear_input(self.password_input)
        self.input_message(self.password_input,PassWord)

    def click_login_button(self):
        '''点击登陆按钮'''
        self.click_button(self.login_btn)

    def click_logout_button(self):
        '''点击退出按钮'''
        self.click_button(self.logout_btn)

    def login_main(self,UserName,PassWord,Url='http://www.51shouhou.cn/singleBranch/#/login'):
        '''
        :param UserName: 登录用户名
        :param PassWord: 登录密码
        :return:
        '''
        log.info('-=【网点登录】=-')
        self.wait()
        self.open_url(Url)
        self.input_username(UserName)
        self.input_password(PassWord)
        self.click_login_button()
        self.sleep(1)
        #断言
        if self.is_display(self.logout_btn):
            log.info('{0} *Branch login success！'.format(self.success))
        else:
            log.error('{0} *Branch login fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
