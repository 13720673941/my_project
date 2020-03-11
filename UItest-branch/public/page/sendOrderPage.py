#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/31 16:50

from public.common.basePage import BasePage
from public.page.searchOrderPage import SearchOrderPage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from config.urlConfig import *
from config.pathConfig import *

class SendOrderPage(BasePage):
    """
        【网点派单页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.create_order = CreateOrderPage(driver)
        self.login = LoginPage(driver)
        self.search_order = SearchOrderPage(driver)

    def get_elements(self,option):
        """获取element_data文件中派单页面的元素信息"""
        return read_config_data("send_order_page",option,elementDataPath)

    def enter_send_order_page(self):
        """进入派单页面"""
        self.open_url(all_order_list_url,self.get_elements("send_order_btn"))

    def enter_wait_grad_order_page(self):
        """进入待抢单页面"""
        self.open_url(wait_grad_order_url,self.get_elements("grad_order_market_table"))

    def click_take_order(self):
        """服务商接单"""
        self.click_button(self.get_elements("branch_take_order_btn"))

    def click_send_order_btn(self):
        """点击派单按钮"""
        self.click_button(self.get_elements("send_order_btn"))

    def select_send_type(self,send_type):
        """选择派单类型：派单师傅、服务商、圈子、市场"""
        path = self.get_elements("send_type_select")
        for i in range(1,3):
            try:
                self.sleep(1)
                if send_type != "":
                    self.click_button(path.replace("+send_type+",send_type).replace("+num+",str(i)))
                elif send_type not in ["师傅","服务商","圈子","市场",""]:
                    raise Exception(
                        "Send type text is not in page, you can enter: 师傅、服务商、圈子、市场.")
                break
            except:
                if i < 2:
                    continue
                else:
                    raise TimeoutError("Select send type timeout not find button .")

    def select_send_page(self,page_name):
        """选择派单对象"""
        path = self.get_elements("send_page_select")
        try:
            if page_name != "":
                self.click_button(path.replace("+page_name+",page_name))
        except:
            raise Exception("Not find send page name in this page list .")

    def set_order_money(self,set_price='100'):
        """输入结算预报价默认 100 """
        self.sleep(2)
        self.click_button(self.get_elements("order_settle_input"))
        self.input_message(self.get_elements("order_settle_input"),set_price)

    def input_search_name(self,search_word):
        """输入搜索派单对象"""
        for i in range(1,3):
            try:
                self.input_message(
                    self.get_elements("search_page_input").replace("+num+",str(i)),search_word)
                break
            except:
                if i == 2:
                    raise TimeoutError("Not find send order page search input !")
                else:
                    continue

    def click_search_btn(self):
        """点击搜索派单对象按钮"""
        for i in range(1,3):
            try:
                self.click_button(self.get_elements("search_page_btn").replace("+num+",str(i)))
                break
            except:
                if i == 2:
                    raise TimeoutError("Not find send order page search input !")
                else:
                    continue

    def get_search_name(self):
        """获取搜索后第一行名称"""
        return self.get_text(self.get_elements("after_search_page_name"))

    def search_branch_is_display(self):
        """授权服务商判断没有派单权限的网点是否可以派单-验证搜索的网点是否在页面显示"""
        return self.is_display(self.get_elements("after_search_page_name"))

    def stop_take_order_is_displayed(self):
        """暂停接单是否在页面上"""
        return self.is_display(self.get_elements("stop_take_order_text"))

    def click_confirm_btn(self):
        """点击确定按钮"""
        path = self.get_elements("confirm_please_btn")
        # 这里页面元素的位置不确定 1，2，3 位置
        for i in range(1,4):
            try:
                self.click_button(path.replace("+num+",str(i)))
                break
            except:
                if i < 3:
                    continue
                else:
                    raise TimeoutError("Click confirm send timeout not find button .")

    def click_grad_order_btn(self):
        """点击抢单按钮"""
        self.click_button(self.get_elements("grad_order_btn"))

    def click_confirm_grad_order_btn(self):
        """点击确认抢单按钮"""
        self.click_button(self.get_elements("confirm_grad_order_btn"))

    def get_msg_of_send_market(self):
        """获取余额不足提示"""
        return self.get_text(self.get_elements("wallet_not_enough_msg"))

    def send_order_main(
            self,orderNumber,pageName="",takeOrder=False,sendType="师傅",setOrderMoney=False,setPrice="1"):
        """
        :param OrderNumber:     订单单号
        :param PageName:        派单对象名称
        :param to_branch_btn:  是否派单到服务商默认派单师
        """

        # 网点派单住程序
        self.log.info('-=【网点派单】=-')
        # 进入订单列表
        self.enter_send_order_page()
        # 搜索订单
        self.search_order.search_order_by_number(orderNumber)
        # 选择匹配订单
        self.create_order.select_operate_order(orderNumber)
        # 是否需要接单
        if takeOrder:
            self.click_take_order()
            # 选择匹配订单
            self.create_order.select_operate_order(orderNumber)
            self.sleep(1)
        # 点击派单按钮
        self.click_send_order_btn()
        self.sleep(2)
        # 选择派单类型
        self.select_send_type(sendType)
        # 选择派单服务商/师傅
        self.select_send_page(pageName)
        # 设置派单价格
        if setOrderMoney:
            self.set_order_money(setPrice)
        # 点击派单按钮
        self.click_confirm_btn()
        self.sleep(1)
        # 获取系统提示
        if self.login.get_system_msg() == "派工成功" or "派单成功":
            self.log.info(' ** Branch please order is success!')
        else:
            raise Exception(' ** Branch please order is fail, system msg: {0}.'
                            .format(self.login.get_system_msg()))