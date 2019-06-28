# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/6 14:31

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
回访页面信息
'''
class VisitOrderPage(BasePage):

    '''回访页面元素信息'''
    visit_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=全部工单'
    visitBtn = (By.XPATH,'//a[text()="回访"]')
    serverStatus = (By.XPATH,'//div[contains(text(),"服务态度：")]/select')
    safetyAssessment = (By.XPATH,'//div[contains(text(),"安全评价：")]/select')
    visitMoney = (By.XPATH,'//div[contains(text(),"回访总额：")]/div[1]/div[2]/input')
    visitResult = (By.XPATH,'//div[contains(text(),"回访结果：")]/select')
    visitRemark = (By.XPATH,'//div[contains(text(),"回访反馈：")]/textarea')
    rewardOrPunish = (By.XPATH,'//span[text()="订单奖惩"]/../../div[2]/form/div/div[1]/select')
    rewardPunishMoney = (By.XPATH,'//span[text()="订单奖惩"]/../../div[2]/form/div/div[2]/input')
    rewardPunishRemark = (By.XPATH,'//input[@placeholder="请填写备注说明"]')
    confirmBtn = (By.XPATH,'//div[text()="回访"]/../../div[3]/button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_visit_order_page(self):
        self.open_url(self.visit_order_url)

    def click_visit_btn(self):
        '''点击回访按钮'''
        self.click_button(self.visitBtn)
        #log.info('{0}点击->回访'.format(self.success))

    def select_server_status(self,serverStatus):
        '''选择服务态度'''
        self.operate_select(self.serverStatus,serverStatus)
        #log.info('{0}选择服务态度：{1}'.format(self.success,serverStatus))

    def select_safety_assess(self,safetyAssess):
        '''选择安全评价'''
        self.operate_select(self.safetyAssessment,safetyAssess)
        #log.info('{0}选择安全评价：{1}'.format(self.success,safetyAssess))

    def input_visit_money(self,visitMoney='100'):#默认100元
        '''输入回访总额'''
        self.input_message(self.visitMoney,visitMoney)
        #log.info('{0}输入回访总额：{1}'.format(self.success,visitMoney))

    def select_visit_result(self,visitResult):
        '''选择回访结果'''
        self.operate_select(self.visitResult,visitResult)
        #log.info('{0}选择回访结果：{1}'.format(self.success,visitResult))

    def input_visit_remark(self):
        '''输入回访反馈'''
        self.input_message(self.visitRemark,self.get_now_time(Time=True))
        #log.info('{0}输入回访反馈：{1}'.format(self.success,self.get_now_time(Time=True)))

    def select_reward_punish(self,rewardOrPunish='奖励'):
        '''选择奖励/惩罚默认是奖励'''
        self.operate_select(self.rewardOrPunish,rewardOrPunish)
        #log.info('{0}选择奖惩：{1}'.format(self.success,rewardOrPunish))

    def input_reward_punish_money(self,rewardPunishMoney='10'):
        '''输入奖惩金额'''
        self.input_message(self.rewardPunishMoney,rewardPunishMoney)
        #log.info('{0}输入奖惩金额：{1}'.format(self.success,rewardPunishMoney))

    def input_reward_punish_remark(self):
        '''输入奖惩备注'''
        self.input_message(self.rewardPunishRemark,self.get_now_time(Time=True))
        #log.info('{0}输入奖惩备注：{1}'.format(self.success,self.get_now_time(Time=True)))

    def click_confirm_btn(self):
        '''点击确定按钮'''
        self.click_button(self.confirmBtn)
        #log.info('{0}点击->确定'.format(self.success))

    def visit_order_main(self,url,orderNumber,serverStatus,safetyAssess,visitMoney,visitResult):
        '''订单回访主程序'''
        #log.info('-=【订单回访】=-')
        #进入完工订单列表页面
        self.open_url(url)
        #选择工单
        self.select_new_order(orderNumber)
        #点击回访按钮
        self.click_visit_btn()
        #选择服务态度
        self.select_server_status(serverStatus)
        #选择安全评价
        self.select_safety_assess(safetyAssess)
        #输入回访总额
        self.input_visit_money(visitMoney)
        #选择回访结果
        self.select_visit_result(visitResult)
        #输入回访反馈
        self.input_visit_remark()
        #选择奖惩
        self.select_reward_punish()
        #输入奖惩金额
        self.input_reward_punish_money()
        #输入奖惩备注
        self.input_reward_punish_remark()
        #点击提交按钮
        self.click_confirm_btn()
        self.sleep(1)
        #断言
        if self.get_system_msg() == '操作成功':
            log.info('{0} *Visit order is success！'.format(self.success))
        else:
            log.error('{0} *Visit order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))
