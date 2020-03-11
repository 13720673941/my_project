#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/26 12:00

from public.common.basePage import BasePage
from config.urlConfig import *
from config.pathConfig import *

class DealerPage(BasePage):
    """
        【客户管理-经销商列表页面】
        添加经销商、搜索经销商、服务设置、禁止接单、恢复接单
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中合作经销商页面的元素信息"""
        return read_config_data("dealer_branch_page",option,elementDataPath)

    def enter_dealer_page(self):
        """进入邀请经销商页面"""
        self.open_url(teamwork_branch_list_url,self.get_elements("add_manage_branch_btn"))

    def click_add_manage_branch(self):
        """点击添加经销商"""
        self.click_button(self.get_elements("add_manage_branch_btn"))

    def input_branch_phone_num(self,phone_num):
        """输入客户手机号"""
        self.input_message(self.get_elements("manage_branch_phone_input"),phone_num)

    def input_branch_name(self,branch_name):
        """输入客户名称"""

        self.clear_input(self.get_elements("manage_branch_name_input"))
        self.sleep(1)
        self.input_message(self.get_elements("manage_branch_name_input"),branch_name)

    def get_branch_name(self):
        """获取输入框的网点名称"""
        return self.get_att(self.get_elements("manage_branch_name_input"),'value')

    def click_confirm_add(self):
        """点击确定添加经销"""
        self.click_button(self.get_elements("add_branch_confirm_btn"))

    def input_search_message(self,search_info):
        """输入搜索信息"""
        self.input_message(self.get_elements("search_branch_input"),search_info)

    def click_search(self):
        """点击搜索"""
        self.click_button(self.get_elements("search_branch_btn"))

    def get_first_branch_info(self):
        """获取第一行的网点的信息"""
        return self.get_text(
            self.get_elements("first_branch_info")) + self.get_text(self.get_elements("first_branch_info1"))

    def click_set_server(self):
        """点击服务设置"""
        self.click_button(self.get_elements("set_server_btn"))

    def clear_branch_remark(self):
        """清除旧备注"""
        self.clear_input(self.get_elements("branch_remark"))

    def input_branch_remark(self,branch_remark):
        """输入客户备注"""
        self.input_message(self.get_elements("branch_remark"),branch_remark)

    def get_teamwork_type_attribute(self):
        """获取合作类型选择框的属性(期望不能选择)"""
        return self.get_att(self.get_elements("teamwork_type_select"),"disabled")

    def get_server_type_attribute(self):
        """获取服务类型选择框的属性(期望不能选择)"""
        return self.get_att(self.get_elements("server_type_select"),"disabled")

    def get_brands_type_attribute(self):
        """获取服务品牌选择框的属性(期望不能选择)"""
        return self.get_att(self.get_elements("server_brands_select"),"disabled")

    def get_kinds_type_attribute(self):
        """获取服务品类选择框的属性(期望不能选择)"""
        return self.get_att(self.get_elements("server_kinds_select"),"disabled")

    def click_server_set_confirm(self):
        """点击服务设置的确定"""
        self.sleep(2)
        self.click_button(self.get_elements("set_server_confirm_btn"))

    def click_stop_take_order(self):
        """点击暂停接单"""
        self.sleep(2)
        first_branch_info = self.get_first_branch_info()
        # 判断是否初始化为暂停接单按钮，不是的化先初始化暂停接单
        if "恢复接单" in first_branch_info:
            pass
        elif "暂停接单" in first_branch_info:
            self.sleep(1)
            self.click_button(self.get_elements("stop_take_order_btn"))
            self.click_stop_take_confirm()
        else:
            raise Exception("Stop take order button not in page !")

    def click_stop_take_confirm(self):
        """点击暂停接单确定"""
        self.sleep(1)
        self.click_button(self.get_elements("stop_take_confirm_btn"))

    def click_open_take_order(self):
        """点击开启接单"""
        self.sleep(2)
        first_branch_info = self.get_first_branch_info()
        # 判断是否初始化为暂停接单按钮，不是的化先初始化暂停接单
        if "暂停接单" in first_branch_info:
            pass
        elif "恢复接单" in first_branch_info:
            self.sleep(1)
            self.click_button(self.get_elements("open_take_order_btn"))
            self.click_open_take_confirm()
        else:
            raise Exception("Open take order button not in page !")

    def click_open_take_confirm(self):
        """点击开启接单确定"""
        self.sleep(1)
        self.click_button(self.get_elements("open_take_confirm_btn"))