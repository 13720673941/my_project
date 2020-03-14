#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/10 18:15

from public.common.basePage import BasePage
from config.urlConfig import *

class SettleOrderPage(BasePage):
    """
        【订单结算页面】 -工单结算按回访结算
    """

    def get_elements(self,option):
        """获取element_data文件中工单支出页面的元素信息"""
        return read_config_data("order_expenditure_page",option,elementDataPath)

    def enter_bill_out_going_url(self):
        """进入工单支出页面"""
        self.open_url(bill_out_going_url)

    def get_row_bill_message(self,rowNumber):
        """获取全部账单列表中一行的全部信息"""
        return self.get_text(self.get_elements("row_bill_message").replace("+num+",rowNumber))

    # def get_bill_message_of_orderNumber(self,orderNumber):
    #     """以工单编号获取账单列表中的的行信息"""
    #     for i in range(1,10):
    #         try:
    #             billMessage = self.get_row_bill_message(str(i))
    #             if orderNumber in billMessage:
    #                 return billMessage
    #         except:
    #             raise TimeoutError("Not find bill message of order number: {}".format(orderNumber))

    def click_bill_details_of_orderNumber(self,orderNumber):
        """点击账单明细按钮"""

        # 循环遍历账单列表中的订单信息
        for i in range(1,10):
            try:
                # 点击账单明细按钮
                self.click_button(self.get_elements("bill_details_btn").replace("+num+",str(i)))
                # 输入工单号
                self.input_message(self.get_elements("bill_details_search_input"),orderNumber)
                self.sleep(1)
                # 点击搜索
                self.click_button(self.get_elements("bill_details_search_btn"))
                self.sleep(2)
                # 获取搜索后的第一行的订单信息
                if self.is_display(self.get_elements("null_order_count_message")):
                    self.sleep(1)
                    self.click_button(self.get_elements("return_front_page"))
                else:
                    self.log.info("Find bill message success !")
                    break
            except:
                if i == 9:
                    raise TimeoutError("Not find bill of order number：{}".format(orderNumber))
                else:
                    continue

    def click_confirm_bill_btn(self):
        """点击确认账单按钮"""
        self.sleep(1)
        self.click_button(self.get_elements("confirm_bill_btn"))

    def click_confirm_bill_confirm_btn(self):
        """点击确认账单弹窗的确认按钮"""
        self.click_button(self.get_elements("confirm_bill_confirm_btn"))

    def click_promptly_settle_btn(self):
        """点击立即结算按钮"""
        self.sleep(4)
        self.click_button(self.get_elements("promptly_settle_btn"))

    def select_money_wattle_settle(self):
        """选择钱包结算"""
        self.click_button(self.get_elements("money_wattle_settle_btn"))

    def select_line_down_settle(self):
        """选择线下结算"""
        self.click_button(self.get_elements("down_line_settle_btn"))

    def click_confirm_settle_btn(self):
        """点击确认结算按钮"""
        self.sleep(4)
        self.click_button(self.get_elements("confirm_settle_btn"))

    def get_bill_settle_status(self):
        """获取账单结算状态"""
        self.sleep(2)
        return self.get_text(self.get_elements("bill_settle_status"))

    def get_down_line_att(self):
        """市场单结算时获取线下结算属性，判断是否支持线下结算"""
        self.sleep(2)
        return self.get_att(self.get_elements("down_line_settle_btn"),attribute="style")

    def get_bill_reward_first_record(self):
        """获取账单奖惩最后的统计一整行信息,删除换行符"""
        return self.get_text(self.get_elements("bill_reward_count")).replace("\n","")

    def settle_order_main(self,orderNumber):
        """订单结算主程序"""

        self.log.info("-=【工单结算】=-")
        # 进入订单支出页面
        self.enter_bill_out_going_url()
        self.sleep(1)
        # 点击账单明细
        self.click_bill_details_of_orderNumber(orderNumber)
        # 如果能搜索出来点击确认账单
        self.click_confirm_bill_btn()
        self.click_confirm_bill_confirm_btn()
        # 点击立即结算
        self.click_promptly_settle_btn()
        # 选择线下结算
        self.select_line_down_settle()
        self.click_confirm_settle_btn()
        self.sleep(2)
        # 结算成功刷新页面
        self.refresh_page()
        # 判断是否结算成功
        if "已结算" in self.get_bill_settle_status():
            self.log.info(" ** Bill settle success !")
        else:
            raise Exception(" ** Bill settle fail !")

