# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/26 15:41

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log = Log()
'''
忘记密码页面
'''
class ForgetPwd(BasePage):

    '''忘记密码页面元素路径信息'''
    parentPath = '//div[text()="忘记密码"]/../form/ul' #定位页面元素的父路径
    forgetPwdBtn = (By.XPATH,'//a[@class="forgetbtn"]')
    inputPhone = (By.XPATH,''+parentPath+'/li[1]/input')
    inputCodeNum = (By.XPATH,''+parentPath+'/li[2]/input')
    getCodeBtn = (By.XPATH,''+parentPath+'/li[2]/a')
    inputNewPwd = (By.XPATH,''+parentPath+'/li[3]/input')
    confirmPwd = (By.XPATH,''+parentPath+'/li[4]/input')
    resetPwdBtn = (By.XPATH,'//a[text()="重置密码"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_forgetPwd_btn(self):
        '''点击忘记密码按钮'''
        self.click_button(self.forgetPwdBtn)
        #log.info('{0}点击->忘记密码'.format(self.success))

    def input_phoneNum(self,PhoneNum):
        '''输入手机号'''
        self.input_message(self.inputPhone,PhoneNum)
        #log.info('{0}输入手机号: {1}'.format(self.success,PhoneNum))

    def click_getCode_btn(self):
        '''点击获取验证码按钮'''
        self.click_button(self.getCodeBtn)
        #log.info('{0}点击->获取验证码'.format(self.success))

    def input_codeNum(self,CodeNum):
        '''输入验证码'''
        self.input_message(self.inputCodeNum,CodeNum)
        #log.info('{0}输入验证码: {1}'.format(self.success,CodeNum))

    def input_new_pwd(self,NewPwd):
        '''输入新设置的密码'''
        self.input_message(self.inputNewPwd,NewPwd)
        #log.info('{0}输入新密码: {1}'.format(self.success,NewPwd))

    def input_confirm_pwd(self,ConfirmPwd):
        '''确认输入密码'''
        self.input_message(self.confirmPwd,ConfirmPwd)
        #log.info('{0}确认确认密码: {1}'.format(self.success,ConfirmPwd))

    def click_reset_pwd_btn(self):
        '''点击重置密码按钮'''
        self.click_button(self.resetPwdBtn)
        #log.info('{0}点击->重置密码'.format(self.success))

    def get_codeBtn_attribute(self,AttrName):
        '''获取验证码按钮属性判断是否发送成功'''
        return self.get_att(self.getCodeBtn,AttrName)

