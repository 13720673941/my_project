# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/10 18:15

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
订单结算页面
'''
class SettleOrderPage(BasePage):

    '''订单结算页面'''
    return_settle_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/branchreturn?tabType=代结待结算&page=1'
    settleBtn = (By.XPATH,'//*[@id="myModalDetails"]/div/div/div[2]/div/div[2]/div[1]/button[3]')
    SettleMoneyAtt = (By.XPATH,'//label[text()="结算价格："]/../div/div/div[2]/input')
    brandsSettleMoney = (By.XPATH,'//label[text()="结算方式："]/../../div/div/input')
    settleMsg = (By.XPATH,'//label[text()="结算方式："]/../../div/div/span[2]')
    settleType1 = (By.XPATH,'//div[2]/div/label[1]')
    settleType2 = (By.XPATH,'//div[2]/div/label[2]')
    settleType3 = (By.XPATH,'//div[2]/div/label[3]')
    dropBtn = (By.XPATH,'//*[@class="ivu-slider-button"]') #滑动按钮的位置
    dropTxt = (By.XPATH,'//*[@class="ivu-tooltip-inner"]') #滑动后比例的输出位置文本
    settleMoney = (By.XPATH,'//label[text()="结算价格："]/../div/div/div[2]/input')
    confirmBtn = (By.XPATH,'//div[contains(.,"钱包余额：")]/../button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_return_wait_settle(self):
        """进入代结订单页"""
        self.open_url(self.return_settle_url)

    def click_settle_btn(self):
        '''点击结算按钮'''
        self.click_button(self.settleBtn)
        #log.info('{0}点击->结算'.format(self.success))

    def brands_settle_money_attribute(self):
        '''获取经销商工单结算价格输入框属性'''
        return self.get_att(self.SettleMoneyAtt,'readonly')

    def settle_money_attribute(self):
        '''获取经销商/服务商返单结算输入框属性/1、经销商端返单结算输入框属性'''
        return self.get_att(self.brandsSettleMoney,'disabled')

    def get_settle_money_msg(self):
        '''获取经销商/服务商是否结算的系统提示'''
        return self.get_text(self.settleMsg)

    def settle_msg_isDisplayed(self):
        '''判断是否存在'''
        return self.is_display(self.settleMsg)

    def get_settleType1_att(self):
        '''获取第一个结算方式属性'''
        return self.get_att(self.settleType1,'disabled')

    def get_settleType3_att(self):
        '''获取第3个结算方式属性'''
        return self.get_att(self.settleType3,'disabled')

    def select_settle_type(self,settleType):#//label[contains(.,'按固定金额')]
        '''选择结算方式'''
        if settleType == '按提成规则':
            self.click_button(self.settleType1)
        elif settleType == '按固定金额':
            self.click_button(self.settleType2)
        elif settleType == '按固定比例':
            self.click_button(self.settleType3)
        else:
            log.error('{0}没有该类型: {1}的结算方式！'.format(self.fail,settleType))
        #log.info('{0}选择: {1} 结算！'.format(self.success,settleType))

    def select_settle_proportion(self,arriveTxt):
        '''选择结算比例'''
        self.drag_button(self.dropBtn,self.dropTxt,arriveTxt)
        #log.info('{0}选择结算比例网点占百分之：{1}0'.format(self.success,arriveTxt))

    def input_settle_money(self,settleMoney='100'):
        '''输入网点结算价格'''
        self.clear_input(self.settleMoney)
        self.input_message(self.settleMoney,settleMoney)
        #log.info('{0}输入结算价格：{1}'.format(self.success,settleMoney))

    def settle_money_att(self):
        '''获取结算价格输入框属性'''
        return self.get_att(self.settleMoney,'readonly')

    def get_settleMoney_text(self):
        '''获取结算价格'''
        return self.get_text(self.settleMoney)

    def select_pay_type(self,payType):
        '''选择支付方式'''
        self.click_button(element=(By.XPATH,'//label[contains(.,"'+payType+'")]'))
        #log.info('{0}选择支付方式：{1}'.format(self.success,payType))

    def click_confirm_btn(self):
        '''点击确定'''
        self.click_button(self.confirmBtn)
        #log.info('{0}点击->确定'.format(self.success))

