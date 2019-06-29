# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/10 18:15

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
'''
订单结算页面
'''
class SettleOrderPage(BasePage):

    '''
    订单结算页面
    '''
    #代结算订单列表页
    return_settle_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/branchreturn?tabType=代结待结算&page=1'
    #结算按钮
    settle_btn = (By.XPATH,'//*[@id="myModalDetails"]/div/div/div[2]/div/div[2]/div[1]/button[3]')
    #结算价格输入框
    settle_money_input = (By.XPATH,'//label[text()="结算价格："]/../div/div/div[2]/input')
    #上级结算价格
    brands_settle_input = (By.XPATH,'//label[text()="结算方式："]/../../div/div/input')
    #未结算提示信息
    settle_red_msg = (By.XPATH,'//label[text()="结算方式："]/../../div/div/span[2]')
    #三种结算方式
    settle_type_1 = (By.XPATH,'//div[2]/div/label[1]')
    settle_type_2 = (By.XPATH,'//div[2]/div/label[2]')
    settle_type_3 = (By.XPATH,'//div[2]/div/label[3]')
    #滑动按钮
    drop_btn = (By.XPATH,'//*[@class="ivu-slider-button"]')
    #滑动后比例的输出位置文本
    drop_arrive_text = (By.XPATH,'//*[@class="ivu-tooltip-inner"]')
    #确定结算
    confirm_btn = (By.XPATH,'//div[contains(.,"钱包余额：")]/../button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_return_wait_settle(self):
        """进入代结订单页"""
        self.open_url(self.return_settle_url)

    def click_settle_btn(self):
        '''点击结算按钮'''
        self.click_button(self.settle_btn)

    def brands_settle_money_attribute(self):
        '''获取经销商工单结算价格输入框属性'''
        return self.get_att(self.settle_money_input,'readonly')

    def settle_money_attribute(self):
        '''获取经销商/服务商返单结算输入框属性/1、经销商端返单结算输入框属性'''
        return self.get_att(self.brands_settle_input,'disabled')

    def get_settle_money_msg(self):
        '''获取经销商/服务商是否结算的系统提示'''
        return self.get_text(self.settle_red_msg)

    def settle_msg_isDisplayed(self):
        '''判断是否存在'''
        return self.is_display(self.settle_red_msg)

    def get_settleType1_att(self):
        '''获取第一个结算方式属性'''
        return self.get_att(self.settle_type_1,'disabled')

    def get_settleType3_att(self):
        '''获取第3个结算方式属性'''
        return self.get_att(self.settle_type_3,'disabled')

    def select_settle_type(self,settleType):#//label[contains(.,'按固定金额')]
        '''选择结算方式'''
        if settleType == '按提成规则':
            self.click_button(self.settle_type_1)
        elif settleType == '按固定金额':
            self.click_button(self.settle_type_2)
        elif settleType == '按固定比例':
            self.click_button(self.settle_type_3)

    def select_settle_proportion(self,arriveTxt):
        '''选择结算比例'''
        self.drag_button(self.drop_btn,self.drop_arrive_text,arriveTxt)

    def input_settle_money(self,settleMoney='100'):
        '''输入网点结算价格'''
        self.clear_input(self.settle_money_input)
        self.input_message(self.settle_money_input,settleMoney)

    def get_settleMoney_text(self):
        '''获取结算价格'''
        return self.get_text(self.settle_money_input)

    def select_pay_type(self,payType):
        '''选择支付方式'''
        self.click_button(element=(By.XPATH,'//label[contains(.,"'+payType+'")]'))

    def click_confirm_btn(self):
        '''点击确定'''
        self.click_button(self.confirm_btn)

