#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/12 16:07

from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.common.rwConfig import read_config_data
from config.urlConfig import *
from config.pathConfig import *

class ReturnOrderPage(BasePage):
    """
        【经销商返单返单页面操作】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.login = LoginPage(driver)
        self.create = CreateOrderPage(driver)

    def get_elements(self,option):
        """获取element_data文件中经销商返单页面的元素信息"""
        return read_config_data("return_order_page",option,elementDataPath)

    def enter_return_order_page(self):
        self.open_url(wait_return_url,self.get_elements("return_order_btn"))

    def enter_finish_return_page(self):
        self.open_url(finish_return_url,self.get_elements("del_return_btn"))

    def click_return_btn(self):
        """点击返单按钮"""
        self.click_button(self.get_elements("return_order_btn"))

    def click_alter_return_branch(self):
        """点击修改返单服务商"""
        self.click_button(self.get_elements("alter_return_branch_btn"))

    def select_branch_name(self,branchName):
        """选择返单服务商名称"""
        if branchName != '':
            self.click_button(
                self.get_elements("select_branch_for_alter").replace("+branch_name+",branchName)
            )

    def click_confirm_btn(self):
        """点击确定"""
        self.click_button(self.get_elements("confirm_alter_btn"))

    def click_add_branch(self):
        """点击添加待接单服务商"""
        self.click_button(self.get_elements("add_branch_btn"))

    def click_del_return(self):
        """点击撤销返单"""
        self.click_button(self.get_elements("del_return_btn"))

    def turn_title_isDisplayed(self):
        """判断页面是否跳转添加服务商页面"""
        return self.is_display(self.get_elements("turn_add_branch_title"))

    def return_order_main(self,orderNumber,alterReturnBranch=False,branchName=None):
        """返单主程序"""
        self.log.info('{0} -=【经销商返单】=-'.format(self.success))
        # 进入返单页面
        self.enter_return_order_page()
        self.wait()
        # 选择订单
        self.create.select_operate_order(orderNumber)
        # 返单是否修改返单服务商
        if alterReturnBranch:
            # 点击修改返单服务商
            self.click_alter_return_branch()
            # 选择服务商名称
            self.select_branch_name(branchName)
        # 点击返单按钮
        self.click_return_btn()
        self.sleep(1)
        # 断言
        if '操作成功' in self.login.get_system_msg():
            self.log.info('{0} ** Return order: {1} success . '.format(self.success,orderNumber))
        else:
            raise TimeoutError('{0} ** Return order: {1} fail ! '.format(self.fail,orderNumber))