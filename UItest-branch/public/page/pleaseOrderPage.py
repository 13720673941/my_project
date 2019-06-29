# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/31 16:50

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
网点派单页面
'''
class PleaseOrderPage(BasePage):

    """
    元素位置信息
    """
    #工单列表url
    please_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'
    #派单按钮
    please_order_btn = (By.XPATH,'//a[text()="派单"]')
    #派单到师傅按钮
    to_master_btn = (By.XPATH,'//b[text()="派单给师傅"]')
    #派单到服务商按钮
    to_branch_btn = (By.XPATH,'//b[text()="派单给服务商"]')
    #派单页面搜索框
    search_page_input = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]')
    #搜索按钮
    search_btn = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]/following-sibling::a')
    #第一个派单对象名称
    search_after_first_name = (By.XPATH,'//div[3]/table/tbody/tr/td/div/label')
    #预报价输入框
    order_settle_money_input = (By.XPATH,'//input[@placeholder="选填，也可结算时填写"]')
    #确定派单按钮
    confirm_btn = (By.XPATH,'//b[text()="派单给师傅"]/../../../../following-sibling::div[1]/button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_please_order_page(self):
        '''进入派单页面'''
        self.open_url(self.please_order_url)

    def click_pleaseOrder_btn(self):
        '''点击派单按钮'''
        self.click_button(self.please_order_btn)

    def please_to_master(self):
        '''点击派单到师傅'''
        self.click_button(self.to_master_btn)

    def please_to_branch(self):
        '''点击派单到服务商'''
        self.click_button(self.to_branch_btn)

    def set_order_money(self,set_price='100'):
        '''输入结算预报价默认 100 '''
        self.input_message(self.order_settle_money_input,set_price)

    def input_search_name(self,name):
        '''输入搜索师傅/网点'''
        self.input_message(self.search_page_input,name)

    def click_search_btn(self):
        '''点击搜索按钮'''
        self.click_button(self.search_btn)

    def get_search_name(self):
        '''获取搜索后第一个师傅名称'''
        return self.get_text(self.search_after_first_name)

    def select_please_page(self,page_name):
        '''选择派单对象'''
        if page_name != '':
            self.click_button(element=(By.XPATH,'//label[text()=" '+page_name+'"]'))

    def click_confirm_btn(self):
        '''点击确定按钮'''
        self.click_button(self.confirm_btn)

    def please_order_main(self,ordernumber,pagename,please_to_branch=False,
                        Url='http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'):
        '''
        :param OrderNumber:     订单单号
        :param PageName:        派单对象名称
        :param to_branch_btn:  是否派单到服务商默认派单师傅
        :return:
        '''
        #网点派单住程序
        log.info('-=【网点派单】=-')
        #进入订单列表
        self.open_url(Url)
        #选择匹配订单
        self.select_new_order(ordernumber)
        #点击派单按钮
        self.click_pleaseOrder_btn()
        self.sleep(2)
        #选择派单对象默认派单师傅
        if please_to_branch:
            #如果派单到服务商为真则派单到服务商
            self.please_to_branch()
            #输入预结算报价
            self.set_order_money()
        #选择派单服务商/师傅
        self.select_please_page(pagename)
        #点击派单按钮
        self.click_confirm_btn()
        self.sleep(1)
        #获取系统提示
        if self.get_system_msg() == "派工成功" or "派单成功":
            log.info('{0} *Branch please order is success!'.format(self.success))
        else:
            log.error('{0} *Branch please order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
