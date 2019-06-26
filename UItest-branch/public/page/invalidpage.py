# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/3 18:50

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log =Log()
'''
设置无效工单页面
'''

class InvalidOrder(BasePage):

    '''设置无效工单页面元素'''
    invalidOrderBtn = (By.XPATH,'//a[text()="无效工单"]')
    selectInvalidType = (By.XPATH,'//label[text()="无效工单类型："]/../div/select')
    inputInvalidReason = (By.XPATH,'//label[text()="无效工单理由："]/../*/*/textarea')
    confirmBtn = (By.XPATH,'//div[text()="无效工单"]/../../div[3]/button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_invalid_btn(self):
        '''点击无效工单按钮'''
        self.click_button(self.invalidOrderBtn)
        #log.info('{0}点击->无效工单'.format(self.success))

    def select_invalid_type(self,invalidType):
        '''选择无效工单类型'''
        if invalidType != '':
            self.operate_select(self.selectInvalidType,invalidType)
            #log.info('{0}选择无效工单类型：{1}'.format(self.success,invalidType))

    def input_invalid_reason(self):
        '''输入无效工单原因'''
        self.input_message(self.inputInvalidReason,self.get_now_time(Time=True))
        #log.info('{0}输入无效工单原因：{1}'.format(self.success,self.get_now_time(Time=True)))

    def click_confirm_btn(self):
        '''点击确定按钮'''
        self.click_button(self.confirmBtn)
        #log.info('{0}点击->确定'.format(self.success))
