#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/6 14:31

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from public.page.searchOrderPage import SearchOrderPage
from config.urlconfig import *
log=Log()

class VisitOrderPage(BasePage):

    """回访页面信息"""
    
    # 回访按钮
    visit_btn = (By.XPATH,'//a[text()="回访"]')
    # 服务态度选择
    server_status_select = (By.XPATH,'//div[contains(text(),"服务态度：")]/select')
    # 安全评价选择
    safety_assessment_select = (By.XPATH,'//div[contains(text(),"安全评价：")]/select')
    # 回访价格
    visit_money_input = (By.XPATH,'//div[contains(text(),"回访总额：")]/div[1]/div[2]/input')
    # 回访结果
    visit_result_select = (By.XPATH,'//div[contains(text(),"回访结果：")]/select')
    # 回访备注
    visit_remark_input = (By.XPATH,'//div[contains(text(),"回访反馈：")]/textarea')
    # 奖惩选择
    reward_or_punish = (By.XPATH,'//span[text()="订单奖惩"]/../../div[2]/form/div/div[1]/select')
    # 奖惩金钱输入框
    reward_punish_money = (By.XPATH,'//span[text()="订单奖惩"]/../../div[2]/form/div/div[2]//input')
    # 奖惩备注
    reward_punish_remark = (By.XPATH,'//input[@placeholder="请填写备注说明"]')
    # 确定回访
    confirm_btn = (By.XPATH,'//div[text()="回访"]/../../div[3]/button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search_order = SearchOrderPage(driver)

    def enter_visit_order_page(self):
        self.open_url(wait_visit_order_url)

    def click_visit_btn(self):
        """点击回访按钮"""
        self.click_button(self.visit_btn)

    def select_server_status(self,serverStatus):
        """选择服务态度"""
        self.operate_select(self.server_status_select,serverStatus)

    def select_safety_assess(self,safetyAssess):
        """选择安全评价"""
        self.operate_select(self.safety_assessment_select,safetyAssess)

    def input_visit_money(self,visitMoney='100'):# 默认100元
        """输入回访总额"""
        self.input_message(self.visit_money_input,visitMoney)

    def select_visit_result(self,visitResult):
        """选择回访结果"""
        self.operate_select(self.visit_result_select,visitResult)

    def input_visit_remark(self):
        """输入回访反馈"""
        self.input_message(self.visit_remark_input,self.get_now_time(Time=True))

    def select_reward_punish(self,rewardOrPunish='奖励'):
        """选择奖励/惩罚默认是奖励"""
        self.operate_select(self.reward_or_punish,rewardOrPunish)

    def input_reward_punish_money(self,rewardPunishMoney='10'):
        """输入奖惩金额"""
        self.input_message(self.reward_punish_money,rewardPunishMoney)

    def input_reward_punish_remark(self):
        """输入奖惩备注"""
        self.input_message(self.reward_punish_remark,self.get_now_time(Time=True))

    def click_confirm_btn(self):
        """点击确定按钮"""
        self.click_button(self.confirm_btn)

    def visit_order_main(self,orderNumber,serverStatus,safetyAssess="按安全规范操作",
                         visitMoney="100",visitResult="已完工"):
        """订单回访主程序"""

        log.info('-=【订单回访】=-')
        # 进入完工订单列表页面
        self.enter_visit_order_page()
        # 搜索订单
        self.search_order.search_order_by_number(orderNumber)
        # 选择工单
        self.select_new_order(orderNumber)
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
        if self.get_system_msg() == '操作成功':
            log.info('{0} ** Visit order is success！'.format(self.success))
        else:
            log.error('{0} ** Visit order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
