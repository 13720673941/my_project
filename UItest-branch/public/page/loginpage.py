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
    login_url = 'http://www.51shouhou.cn/singleBranch/#/login'
    inputUserName = (By.XPATH,'//input[@type="text"]')
    inputPassWord = (By.XPATH,'//input[@type="password"]')
    clickButton = (By.XPATH,'//a[@class="loginBtn"]')
    logoutText = (By.XPATH,'//a[text()="退出"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_login_page(self):
        '''进入登陆页面'''
        self.open_url(self.login_url)

    def input_username(self,UserName):
        '''输入用户名'''
        self.input_message(self.inputUserName,UserName)
        #log.info('{0}输入用户名: {1}'.format(self.success,UserName))

    def input_password(self,PassWord):
        '''输入密码'''
        self.input_message(self.inputPassWord,PassWord)
        #log.info('{0}输入密码: {1}'.format(self.success,PassWord))

    def click_login_button(self):
        '''点击登陆按钮'''
        self.click_button(self.clickButton)
        #log.info('{0}点击->登录'.format(self.success))

    def click_logout_button(self):
        '''点击退出按钮'''
        self.click_button(self.logoutText)
        #log.info('{0}点击->退出登录'.format(self.success))

    def login_main(self,UserName,PassWord,Url='http://www.51shouhou.cn/singleBranch/#/login'):
        '''
        :param UserName: 登录用户名
        :param PassWord: 登录密码
        :return:
        '''
        #log.info('-=【网点登录】=-')
        self.wait()
        self.open_url(Url)
        self.clear_input(self.inputUserName)
        self.input_username(UserName)
        self.clear_input(self.inputPassWord)
        self.input_password(PassWord)
        self.click_login_button()
        self.sleep(1)
        #断言
        if self.is_display(self.logoutText):
            log.info('{0} *Branch login succss！'.format(self.success))
        else:
            log.error('{0} *Branch login fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))




# if __name__ == '__main__':
#
#     from public.common import driver
#     import time
#     from public.common.basepage import BasePage
#     from public.page.alterpassword import AlterPwdPage
#     from selenium.webdriver.common.action_chains import ActionChains
#
#     DictData = {"OrderNum":"636953272191964103","aa":""}
#     d = driver.browser_driver()
#     b = BasePage(d)
#     a = LoginPage(d)
#     AA = AlterPwdPage(d)
#     a.login_main(UserName='13700000004',PassWord='222222')
#     d.get('http://www.51shouhou.cn/singleBranch/#/customer/list')
#     time.sleep(2)
#     txt = d.find_element_by_xpath('//div/div[2]/table/tbody/tr[1]').text
#     print(txt)

