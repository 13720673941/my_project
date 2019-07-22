#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/10 18:15

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from config.urlconfig import *
import time
log=Log()

class SettleOrderPage(BasePage):
    """
    订单结算页面
    """

    # 结算按钮
    settle_btn = (By.XPATH,'//*[@id="myModalDetails"]/.//button[contains(.,"结算")]')
    # 结算价格输入框,厂商/经销商结算价格输入框
    brands_settle_money_input = (By.XPATH,'//label[contains(.,"结算方式：")]/../../div[1]/.//input[@type="text"]')
    # 未结算提示信息
    settle_red_msg = (By.XPATH,'//label[text()="结算方式："]/../../div/div/span[2]')
    # 三种结算方式属性元素
    settle_type_1_att = (By.XPATH,'//div[2]/div/label[1]/input')
    settle_type_2_att = (By.XPATH,'//div[2]/div/label[2]/input')
    settle_type_3_att = (By.XPATH,'//div[2]/div/label[3]/input')
    # 三种结算方式选择按钮元素
    settle_type_1 = (By.XPATH,'//div[2]/div/label[1]')
    settle_type_2 = (By.XPATH,'//div[2]/div/label[2]')
    settle_type_3 = (By.XPATH,'//div[2]/div/label[3]')
    # 滑动按钮
    drop_btn = (By.XPATH,'//*[@class="ivu-slider-button"]')
    # 滑动后比例的输出位置文本
    drop_arrive_text = (By.XPATH,'//div[@class="ivu-slider-bar"]/preceding-sibling::input')
    # 结算价格输入框
    settle_money_input = (By.XPATH,'//label[contains(.,"结算价格：")]/.././/input[@class="ivu-input-number-input"]')
    # 钱包结算
    wallet_settle = (By.XPATH,'//label[contains(.,"付款方式：")]/.././/label[1]')
    # 线下结算
    line_down_settle = (By.XPATH,'//label[contains(.,"付款方式：")]/.././/label[2]')
    # 确定结算
    confirm_btn = (By.XPATH,'//div[contains(.,"钱包余额：")]/../button[2]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_master_settle_page(self):
        """进入师傅待结算订单页面"""
        self.open_url(master_wait_settle_url)

    def enter_branch_settle_page(self):
        """进入服务商待结算订单页面"""
        self.open_url(branch_wait_settle_url)

    def enter_return_wait_settle(self):
        """进入代结订单页"""
        self.open_url(return_settle_url)

    def click_settle_btn(self):
        """点击结算按钮"""
        self.click_button(self.settle_btn)

    def get_brands_settle_money_attribute(self):
        """
        获取上级结算价格输入框/经销商、厂商结算价格输入框属性
        判断价格不能编辑
        """
        return self.get_att(self.brands_settle_money_input,"disabled")

    def get_brands_settle_value_attribute(self):
        """
        获取上级结算价格输入框/经销商、厂商结算价格value值
        """
        return self.get_att(self.brands_settle_money_input,"value")

    def not_settle_msg_is_display(self):
        """未结算提示是否显示"""
        return self.is_display(self.settle_red_msg)

    def get_settle_msg(self):
        """获取为结算提示字段信息"""
        return self.get_text(self.settle_red_msg)

    def select_settle_type_1(self):
        """选择按规则结算"""
        self.click_button(self.settle_type_1)

    def get_settle_type_1_att(self):
        """获取规则结算方式选择属性"""
        return self.get_att(self.settle_type_1_att,"disabled")

    def select_settle_type_2(self):
        """选择按固定金额结算"""
        self.click_button(self.settle_type_2)

    def get_settle_type_2_att(self):
        """获取固定金额结算方式选择属性"""
        return self.get_att(self.settle_type_2_att,"disabled")

    def select_settle_type_3(self):
        """选择按固定比例结算"""
        self.click_button(self.settle_type_3)

    def get_settle_type_3_att(self):
        """获取固定比例结算方式选择属性"""
        return self.get_att(self.settle_type_3_att,"disabled")

    def get_drop_arrive_text(self):
        """获取我方的比例"""
        return self.get_att(self.drop_arrive_text,"value").split(',')[0]

    def input_settle_money(self,settle_money='100'):
        """输入结算价格"""
        self.clear_input(self.settle_money_input)
        self.input_message(self.settle_money_input,settle_money)

    def get_settle_money_value(self):
        """获取结算价格输入框的value"""
        return self.get_att(self.settle_money_input,"value")

    def get_settle_money_attribute(self):
        """获取结算价格输入框的属性不能编辑"""
        return self.get_att(self.settle_money_input,"readonly")

    def select_wallet_pay(self):
        """选择钱包支付"""
        self.click_button(self.wallet_settle)

    def select_line_down_pay(self):
        """选择线下支付"""
        self.click_button(self.line_down_settle)

    def click_confirm_pay(self):
        """点击确定结算"""
        self.click_button(self.confirm_btn)

    def sliding_scale_button(self,arrive_txt):
        """
        结算页面固定比例结算按钮左右滑动封装
        :param txtelement 判断所用获取的文本
        :param arrivetxt  索要滑动的位置文本
        """
        t1 = time.time()
        # 等待按钮加载
        self.sleep(2)
        dragButton = self.get_element(self.drop_btn)
        # 获取滑块y坐标位置
        dragButton_y = dragButton.location['y']
        actions = self.click_and_hold_btn(dragButton)
        # 归零0，y
        while True:
            self.sleep(2)
            # 获取移动后的文本
            txt1 = self.get_drop_arrive_text()
            # 滑块x坐标归零
            if txt1 == '0':
                break
            else:
                actions.move_by_offset(-1,dragButton_y).perform()
        # 清除缓存操作
        actions.reset_actions()
        log.info('{0} Button: <{1}>, remove zero, Spend {2} seconds.'
                 .format(self.success,self.drop_btn,time.time()-t1))
        while True:
            self.sleep(2)
            txt2 = self.get_drop_arrive_text()
            # 滑动的像素源代码中取的正整数，页面滑动1实际滑动不确定，
            # 只能判断大于期望的比例
            if int(txt2) > int(arrive_txt):
                actions.release(dragButton).perform() # 释放左键
                break
            else:
                actions.move_by_offset(1,dragButton_y).perform()
        log.info('{0} Button: {1}, remove right arrive {2}, Spend {3} seconds.'
                 .format(self.success,self.drop_btn,self.drop_arrive_text,time.time()-t1))







