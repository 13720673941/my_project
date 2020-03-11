# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 11:37

from public.page.brandsPage import BasePage
from config.urlConfig import *

class TeamWorkNewsPage(BasePage):
    """
        【合作申请页面】: 搜索消息、拒绝、撤销、申请、再次申请
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中合作申请页面的元素信息"""
        return read_config_data("teamwork_messages_page",option,elementDataPath)

    def enter_teamwork_news_page(self):
        """进入申请消息页面"""
        self.open_url(teamwork_news_list_url,self.get_elements("table_send_apply_btn"))

    def click_table_send_visit(self):
        """点击切换发出的申请"""
        self.click_button(self.get_elements("table_send_apply_btn"))

    def input_customer_name_phone(self,searchWord):
        """输入客户名称或者手机号"""
        self.input_message(self.get_elements("customer_search_input"),searchWord)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def get_first_row_info(self):
        """获取第一行搜索的所有字段信息"""
        return self.get_text(self.get_elements("first_row_info"))

    def click_refuse_btn(self):
        """点击拒绝按钮"""
        self.click_button(self.get_elements("refuse_manage_visit"))
        self.click_button(self.get_elements("confirm_refuse_del_btn"))

    def get_refuse_text(self):
        """获取已拒绝字段-我方"""
        return self.get_text(self.get_elements("refuse_text"))

    def click_del_teamwork_visit(self):
        """点击撤销所有的邀请,邀请功能中有两个申请这里全部删除"""
        for i in range(2):
            try:
                self.sleep(1)
                self.click_button(self.get_elements("del_teamwork_btn"))
                self.click_button(self.get_elements("confirm_refuse_del_btn"))
            except:
                raise TimeoutError("Not find del teamwork of del button: {} ".format(str(i+1)))

    def click_again_visit_teamwork(self):
        """点击再次邀请"""
        self.click_button(self.get_elements("del_teamwork_btn"))
        self.click_button(self.get_elements("confirm_refuse_del_btn"))

    def get_first_row_isDisplayed(self):
        """判断搜索是否为空"""
        return self.is_display(self.get_elements("first_row_message"))

