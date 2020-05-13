# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/22 16:30

from public.page.brandsPage import BasePage
from config.urlConfig import *

class FinanceManagePage(BasePage):

    """
        财务管理-【我的收入】和【我的支出】页面
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取财务工单支出收入页面元素路径"""
        return read_config_data("income_expend_page",option,elementDataPath)

    def enter_my_income_page(self):
        """进入我的收入页面"""
        self.open_url(my_income_url,self.get_elements("bill_number_input"))

    def enter_my_expend_page(self):
        """进入我的支出页面"""
        self.open_url(my_expend_url,self.get_elements("bill_number_input"))

    def input_bill_number(self,billNumber):
        """输入账单编号"""
        self.input_message(self.get_elements("bill_number_input"),billNumber)

    def input_bill_start_date(self,startDate):
        """输入账单开始日期"""
        self.input_message(self.get_elements("bill_start_date_input"),startDate)

    def input_bill_end_date(self,endDate):
        """输入账单结束日期"""
        self.input_message(self.get_elements("bill_end_date_input"),endDate)

    def input_settle_page(self,pageName):
        """输入结算对象"""
        self.input_message(self.get_elements("settle_page_name_input"),pageName)

    def click_search_button(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_button"))

    def get_bill_number(self,orderNumber):
        """查找账单编号"""

        # 初始化账单编号
        billNumber = None
        # 遍历第一页的账单，默认倒叙排列，否则没有生成账单
        for i in range(1,10):
            try:
                # 点击账单明细按钮进入账详情页
                self.click_button(self.get_elements("bill_details_button").replace("+num+",str(i)))
                self.sleep(1)
                # 搜素工单编号
                self.input_message(self.get_elements("order_number_input"),orderNumber)
                self.click_search_button()
                # 获取搜索后第一行的工单所有信息
                self.sleep(1)
                orderInfo = self.get_text(self.get_elements("first_order_info"))
                self.sleep(1)
                # 返回账单列表页面
                self.back_page()
                if orderNumber in orderInfo:
                    # 获取该行的账单编号
                    billNumber = self.get_text(self.get_elements("bill_number_text").replace("+num+",str(i)))
                    self.log.info(" * Find bill number: {}".format(billNumber))
                    break
            except:
                if i == 9:
                    raise TimeoutError("Not find bill number in bill list page !")
                else:
                    continue
            finally:
                return billNumber

    def get_first_row_info(self):
        """获取第一行所有账单信息-默认获取第一行必须在搜索账单号后获取"""
        try:
            return self.get_text(self.get_elements("first_bill_info"))
        except:
            return "Get first bill info fail !"

    def click_bill_details_btn(self,billNumber):
        """点击账单明细按钮"""

        # 搜索账单编号
        self.input_bill_number(billNumber)
        self.click_search_button()
        # 点击账单明细按钮
        try:
            # 固定搜索接口的第一个账单明细按钮
            self.click_button(self.get_elements("bill_details_button").replace("+num+","1"))
        except:
            raise TimeoutError("Not find bill details button !")
