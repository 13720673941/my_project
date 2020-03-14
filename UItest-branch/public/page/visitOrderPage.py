#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/6 14:31

from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.searchOrderPage import SearchOrderPage
from config.urlConfig import *
from config.pathConfig import *

class VisitOrderPage(BasePage):
    """
        【列表点击回访页面信息】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.login = LoginPage(driver)
        self.create_order = CreateOrderPage(driver)
        self.search_order = SearchOrderPage(driver)

    def get_elements(self,option):
        """获取element_data文件中回访工单页面的元素信息"""
        return read_config_data("visit_order_page",option,elementDataPath)

    def enter_visit_order_page(self):
        self.open_url(wait_visit_order_url,self.get_elements("visit_btn"))

    def click_visit_btn(self):
        """点击回访按钮"""
        self.click_button(self.get_elements("visit_btn"))

    def select_server_status(self,serverStatus):
        """选择服务态度"""
        self.operate_select(self.get_elements("server_status_select"),serverStatus)

    def select_safety_assess(self,safetyAssess):
        """选择安全评价"""
        self.operate_select(self.get_elements("safety_assessment_select"),safetyAssess)

    def input_visit_money(self,visitMoney='100'):# 默认100元
        """输入回访总额"""
        self.input_message(self.get_elements("visit_money_input"),visitMoney)

    def select_visit_result(self,visitResult):
        """选择回访结果"""
        self.operate_select(self.get_elements("visit_result_select"),visitResult)

    def input_visit_remark(self):
        """输入回访反馈"""
        self.input_message(self.get_elements("visit_remark_input"),self.get_now_time(Time=True))

    def select_reward_punish(self,rewardOrPunish='奖励'):
        """选择奖励/惩罚默认是奖励"""
        self.operate_select(self.get_elements("reward_or_punish"),rewardOrPunish)

    def input_reward_punish_money(self,rewardPunishMoney='0.01'):
        """输入奖惩金额"""
        self.input_message(self.get_elements("reward_punish_money"),rewardPunishMoney)

    def input_reward_punish_remark(self):
        """输入奖惩备注"""
        self.input_message(self.get_elements("reward_punish_remark"),self.get_now_time(Time=True))

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.get_elements("confirm_btn"))

    def visit_order_main(self,orderNumber,serverStatus="非常满意",safetyAssess="按安全规范操作",
                         visitMoney="0",visitResult="已完工",rewardPunish=True):
        """订单回访主程序"""

        self.log.info('-=【订单回访】=-')
        # 进入完工订单列表页面
        self.enter_visit_order_page()
        self.refresh_page()
        # 搜索订单
        self.search_order.search_order_by_number(orderNumber)
        # 选择工单
        self.create_order.select_operate_order(orderNumber)
        # 点击回访按钮
        self.click_visit_btn()
        # 选择服务态度
        self.select_server_status(serverStatus)
        # 选择安全评价
        self.select_safety_assess(safetyAssess)
        # 输入回访总额
        self.input_visit_money(visitMoney)
        # 选择回访结果
        self.select_visit_result(visitResult)
        # 输入回访反馈
        self.input_visit_remark()
        if rewardPunish:
            # 选择奖惩
            self.select_reward_punish()
            # 输入奖惩金额
            self.input_reward_punish_money()
            # 输入奖惩备注
            self.input_reward_punish_remark()
        # 点击提交按钮
        self.click_confirm_btn()
        self.sleep(1)
        # 断言
        if self.login.get_system_msg() == '操作成功':
            self.log.info(' ** Visit order is success . ')
        else:
            raise TimeoutError(' ** Visit order is fail ! ')
