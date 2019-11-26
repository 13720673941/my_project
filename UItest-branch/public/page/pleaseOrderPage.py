#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/31 16:50

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from public.page.searchOrderPage import SearchOrderPage
from config.urlconfig import *
log=Log()

class PleaseOrderPage(BasePage):
    """
    网点派单页面
    """
    
    # 派单按钮
    please_order_btn = (By.XPATH,'//a[text()="派单"]')
    # 派单到师傅按钮
    to_master_btn = (By.XPATH,'//b[text()="派单给师傅"]')
    # 派单到服务商按钮
    to_branch_btn = (By.XPATH,'//b[text()="派单给服务商"]')
    # 派单页面搜索框
    search_page_input = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]')
    # 搜索按钮
    search_btn = (By.XPATH,'//input[@placeholder="输入师傅姓名/手机号进行查询"]/following-sibling::a')
    # 搜索服务商
    search_branch_input = (By.XPATH,'//input[@placeholder="输入服务商名称/手机号进行查询"]')
    # 搜索按钮
    search_branch_btn = (By.XPATH,'//input[@placeholder="输入服务商名称/手机号进行查询"]/following-sibling::a')
    # 第一个派单对象名称
    search_after_first_name = (By.XPATH,'//div[contains(text(),"列表")]/../..//tbody/tr[1]')
    # 预报价输入框
    order_settle_money_input = (By.XPATH,'//input[@placeholder="选填，也可结算时填写"]')
    # 确定派单按钮
    confirm_btn = (By.XPATH,'//b[text()="派单给师傅"]/../../../../following-sibling::div[1]/button[2]')
    # 暂停接单后师傅标记暂停接单字段
    stop_take_order_text = (By.XPATH,'//span[text()="（暂停接单）"]')
    # 点击接单按钮
    take_order_btn = (By.XPATH,'//a[contains(text(),"接单")]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search_order = SearchOrderPage(driver)

    def enter_please_order_page(self):
        """进入派单页面"""
        self.open_url(all_order_list_url)

    def click_pleaseOrder_btn(self):
        """点击派单按钮"""
        self.click_button(self.please_order_btn)

    def please_to_master(self):
        """点击派单到师傅"""
        self.click_button(self.to_master_btn)

    def please_to_branch(self):
        """点击派单到服务商"""
        self.sleep(1)
        self.click_button(self.to_branch_btn)

    def set_order_money(self,set_price='100'):
        """输入结算预报价默认 100 """
        self.input_message(self.order_settle_money_input,set_price)

    def input_search_name(self,name):
        """输入搜索师傅/网点"""
        self.input_message(self.search_page_input,name)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.search_btn)

    def input_search_branch_name(self,branch_name):
        """搜索服务商输入"""
        self.input_message(self.search_branch_input,branch_name)

    def click_search_branch(self):
        """点击搜索服务撒"""
        self.click_button(self.search_branch_btn)

    def get_search_name(self):
        """获取搜索后第一个师傅名称"""
        return self.get_text(self.search_after_first_name)

    def search_branch_is_display(self):
        """授权服务商判断没有派单权限的网点是否可以派单-验证搜索的网点是否在页面显示"""
        return self.is_display(self.search_after_first_name)

    def select_please_page(self,page_name):
        """选择派单对象"""
        if page_name != '':
            self.click_button(element=(By.XPATH,'//label[text()=" '+page_name+'"]'))

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.confirm_btn)

    def stop_take_order_is_displayed(self):
        """暂停接单是否在页面上"""
        return self.is_display(self.stop_take_order_text)

    def click_take_order(self):
        """服务商接单"""
        self.click_button(self.take_order_btn)

    def please_order_main(self,ordernumber,pagename,please_to_branch=False,set_order_money=True):
        """
        :param OrderNumber:     订单单号
        :param PageName:        派单对象名称
        :param to_branch_btn:  是否派单到服务商默认派单师傅
        :return:
        """
        # 网点派单住程序
        log.info('-=【网点派单】=-')
        # 进入订单列表
        self.enter_please_order_page()
        # 搜索订单
        self.search_order.search_order_by_number(ordernumber)
        # 选择匹配订单
        self.select_new_order(ordernumber)
        # 点击派单按钮
        self.click_pleaseOrder_btn()
        self.sleep(2)
        # 选择派单对象默认派单师傅
        if please_to_branch:
            # 如果派单到服务商为真则派单到服务商
            self.please_to_branch()
            if set_order_money:
                # 输入预结算报价
                self.set_order_money()
        # 选择派单服务商/师傅
        self.select_please_page(pagename)
        # 点击派单按钮
        self.click_confirm_btn()
        self.sleep(1)
        # 获取系统提示
        if self.get_system_msg() == "派工成功" or "派单成功":
            log.info('{0} ** Branch please order is success!'.format(self.success))
        else:
            log.error('{0} ** Branch please order is fail, system msg: {1}.'
                      .format(self.fail,self.get_system_msg()))

