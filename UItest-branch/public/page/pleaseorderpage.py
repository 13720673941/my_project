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

    #页面元素信息
    please_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'
    pleaseOrderBtn = (By.XPATH,'//a[text()="派单"]')
    pleaseToMaster = (By.XPATH,'//b[text()="派单给师傅"]')
    pleaseToBranch = (By.XPATH,'//b[text()="派单给服务商"]')
    inputMasterOrBranch = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]')
    searchBtn = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]/following-sibling::a')
    pleasePageName = (By.XPATH,'//div[3]/table/tbody/tr/td/div/label')
    inputOrderMoney = (By.XPATH,'//input[@placeholder="选填，也可结算时填写"]')
    confirmBtn = (By.XPATH,'//b[text()="派单给师傅"]/../../../../following-sibling::div[1]/button[2]')
    ToBranchAtt = (By.XPATH,'//b[text()="派单给服务商"]/../input')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_please_order_page(self):
        '''进入派单页面'''
        self.open_url(self.please_order_url)

    def click_pleaseOrder_btn(self):
        '''点击派单按钮'''
        self.click_button(self.pleaseOrderBtn)
        #log.info('{0}点击->派单'.format(self.success))

    def please_to_master(self):
        '''点击派单到师傅'''
        self.click_button(self.pleaseToMaster)
        #log.info('{0}点击->派单到师傅'.format(self.success))

    def please_to_branch(self):
        '''点击派单到服务商'''
        self.click_button(self.pleaseToBranch)
        #log.info('{0}点击->派单到服务商'.format(self.success))

    def set_order_money(self,set_price='100'):
        '''输入结算预报价默认 100 '''
        self.input_message(self.inputOrderMoney,set_price)
        #log.info('{0}输入结算预报价：{1}'.format(self.success,set_price))

    def input_search_name(self,name):
        '''输入搜索师傅/网点'''
        self.input_message(self.inputMasterOrBranch,name)
        #log.info('{0}输入派单对象：{1}'.format(self.success,name))

    def click_search_btn(self):
        '''点击搜索按钮'''
        self.click_button(self.searchBtn)
        #log.info('{0}点击->搜索'.format(self.success))

    def get_search_name(self):
        '''获取搜索后第一个师傅名称'''
        return self.get_text(self.pleasePageName)

    def select_please_page(self,page_name):
        '''选择派单对象'''
        if page_name != '':
            self.click_button(element=(By.XPATH,'//label[text()=" '+page_name+'"]'))
            #log.info('{0}选择派单对象：{1}'.format(self.success,page_name))

    def click_confirm_btn(self):
        '''点击确定按钮'''
        self.click_button(self.confirmBtn)
        #log.info('{0}点击->确定'.format(self.success))

    def get_to_branch_attribute(self):
        '''获取师傅转派网点时选择派单网点的属性'''
        return self.get_att(self.ToBranchAtt,"disabled")

    def please_order_main(self,ordernumber,pagename,please_to_branch=False,
                        Url='http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'):
        '''
        :param OrderNumber:     订单单号
        :param PageName:        派单对象名称
        :param PleaseToBranch:  是否派单到服务商默认派单师傅
        :return:
        '''
        #网点派单住程序
        #log.info('-=【网点派单】=-')
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

