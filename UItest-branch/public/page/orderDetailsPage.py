#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/7/5 14:11

from public.common.basePage import BasePage
from config.urlConfig import *
import datetime

class OrderDetailsPage(BasePage):
    """
    订单详情页面
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取element_data文件中工单详情页面的元素信息"""
        return read_config_data("order_details_page",option,elementDataPath)

    def enter_refuse_list_page(self):
        """拒单列表页面"""
        self.open_url(refuse_order_list_url)

    def enter_prompt_list_page(self):
        """催单工单列表页面"""
        self.open_url(prompt_order_url)

    def click_refuse_order_btn(self):
        """点击拒单按钮"""
        self.click_button(self.get_elements("refuse_order_btn"))

    def input_refuse_reason(self,reason):
        """输入拒单原因"""
        self.input_message(self.get_elements("refuse_order_input"),reason)

    def click_confirm_refuse_btn(self):
        """点击确认拒单"""
        self.click_button(self.get_elements("confirm_refuse_submit"))

    def click_appoint_btn(self):
        """点击预约按钮"""
        self.click_button(self.get_elements("appoint_order_btn"))

    def click_alter_appoint_btn(self):
        """点击修改预约按钮"""
        self.click_button(self.get_elements("alter_appoint_time_btn"))

    def clear_appoint_date(self):
        """清除预约日期"""
        self.mouse_move_and_click(self.get_elements("appoint_date_clear"))

    def input_appoint_date(self,alter=False):
        """输入预约日期"""
        self.clear_appoint_date()
        self.sleep(1)
        if alter:
            appoint_date = str(datetime.datetime.now().date() + datetime.timedelta(2))
        else:
            appoint_date = self.get_now_time()
        self.input_message(self.get_elements("appoint_time_input"),appoint_date)

    def select_appoint_time(self,appoint_time):
        """选择预约时间段默认选择第一个"""
        if appoint_time == "True":
            self.click_button(self.get_elements("open_appoint_select"))
            self.sleep(2)
            self.mouse_move_and_click(self.get_elements("first_appoint_time"))

    def click_confirm_appoint_btn(self):
        """点击确定预约按钮"""
        self.click_button(self.get_elements("confirm_appoint_btn"))

    def get_appoint_text(self):
        """获取订单详情的预约字段，判断预约成功"""
        return self.get_text(self.get_elements("appoint_time_text"))

    def click_alter_order_btn(self):
        """点击修改订单按钮"""
        self.click_button(self.get_elements("alter_order_btn"))

    def get_alter_text_of_order(self):
        """获取修改订单的字段验证"""
        return self.get_text(self.get_elements("order_info_of_pheNum"))

    def click_cui_order_btn(self):
        """点击催单按钮"""
        self.click_button(self.get_elements("cui_order_btn"))

    def input_cui_of_reason(self,prompt_reason):
        """输入催单原因"""
        if prompt_reason != '':
            self.input_message(self.get_elements("cui_reason_input"),prompt_reason)

    def click_confirm_cui_order(self):
        """点击确定催单"""
        self.click_button(self.get_elements("confirm_cui_button"))

    def click_new_create_btn(self):
        """点击新建工单"""
        self.click_button(self.get_elements("new_create_order_btn"))

    def click_print_order_btn(self):
        """点击打印工单按钮"""
        self.click_button(self.get_elements("print_order_btn"))

    def click_feedback_btn(self):
        """点击服务反馈按钮"""
        self.click_button(self.get_elements("feedback_btn"))

    def input_feedback_message(self,feedbackMsg):
        """输入反馈内容"""
        self.input_message(self.get_elements("feedback_input"),feedbackMsg)

    def click_confirm_feedback(self):
        """确认反馈内容"""
        self.click_button(self.get_elements("confirm_feedback_btn"))

    def get_feedback_message(self):
        """获取反馈信息"""
        return self.get_text(self.get_elements("feedback_message"))

    def click_alter_charge(self):
        """点击修改服务费按钮"""
        self.click_button(self.get_elements("alter_server_money_btn"))

    def input_server_charge(self,serverCharge="100"):
        """输入修改服务费"""
        self.input_message(self.get_elements("server_money_input"),serverCharge)

    def click_confirm_alter_charge(self):
        """点击确认修改服务费按钮"""
        self.click_button(self.get_elements("confirm_alter_charge_btn"))

    def get_order_charge(self):
        """获取工单详情页的派单预报价字段"""
        return self.get_text(self.get_elements("settle_money_text"))