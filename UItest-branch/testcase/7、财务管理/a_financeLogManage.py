# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/24 10:21

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.financeManagePage import FinanceManagePage
from config.pathConfig import *
import unittest

class Finance_Log_Manage(unittest.TestCase):

    """ 【回访账单日志、确认账单、结算账单校验】 """

    # 实例化操作excel类
    readExcel = Read_Excel("financeLog")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.please_order = SendOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.finance_log = FinanceManagePage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"financeLog")
        # 登录经销商
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        cls.create_order.create_not_return_order()
        # 获取工单号
        cls.order_number = cls.create_order.get_order_number()
        # 获取经销商下的服务商
        cls.server_branch_name = rwConfig.read_config_data("T西安好家帮家政有限公司", "branch001")
        # 派单到服务商
        cls.please_order.send_order_main(
            cls.order_number,sendType="服务商",pageName=cls.server_branch_name)
        # 退出经销商登录
        cls.login.click_logout_button()
        # 登录服务商
        cls.login.login_main(cls.server_branch_name)
        # 获取服务商的派单师傅名称
        master_name = rwConfig.read_config_data(cls.server_branch_name,"master001")
        # 接单
        cls.please_order.enter_send_order_page()
        # 选择订单接单
        cls.create_order.select_operate_order(cls.order_number)
        cls.please_order.click_take_order()
        # 派单到师傅
        cls.please_order.send_order_main(cls.order_number,pageName=master_name)
        # 完成服务
        cls.finish_order.finish_order_main(cls.order_number)

    @unittest.skipUnless(readExcel.get_isRun_text("finance_log_001"),"-跳过不执行该用例")
    def test_finance_log_manage001(self):
        """支出结算生成日志记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("finance_log_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main("T西安好家帮家政有限公司")
        # 回访
        self.visit_order.visit_order_main(self.order_number)
        # 进入支出页面
        self.finance_log.enter_my_expend_page()
        # 查找账单号
        global billNumber
        billNumber = self.finance_log.get_bill_number(self.order_number)
        # 写入账单编号后面搜索功能使用
        rwConfig.write_config_data("for_finance_manage_search","id",billNumber,orderNumPath)
        # 输入账单号
        self.finance_log.input_bill_number(billNumber)
        # 点击搜索
        self.finance_log.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.finance_log.get_first_row_info())

    @unittest.skipUnless(readExcel.get_isRun_text("finance_log_002"),"-跳过不执行该用例")
    def test_finance_log_manage002(self):
        """收入结算生成日志记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("finance_log_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 退出登录
        self.base_page.refresh_page()
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.server_branch_name)
        # 回访
        self.visit_order.visit_order_main(self.order_number)
        # 进入我的收入记录页面
        self.finance_log.enter_my_income_page()
        # 搜索账单号
        self.base_page.sleep(2)
        self.finance_log.input_bill_number(billNumber)
        # 点击搜索
        self.finance_log.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_in(data,self.finance_log.get_first_row_info())

    @unittest.skipUnless(readExcel.get_isRun_text("finance_log_003"),"-跳过不执行该用例")
    def test_finance_log_manage003(self):
        """确认账单成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("finance_log_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 登录经销商
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入支出页面
        self.finance_log.enter_my_expend_page()
        # 进入账单明细
        self.finance_log.click_bill_details_btn(billNumber)
        self.base_page.sleep(1)
        # 点击确认账单
        self.settle_order.click_confirm_bill_btn()
        # 确定确认
        self.settle_order.click_confirm_bill_confirm_btn()
        self.base_page.sleep(1)
        # 刷新页面
        self.base_page.refresh_page()
        # 断言
        self.assert_mode.assert_in(data,self.settle_order.get_bill_settle_status())

    @unittest.skipUnless(readExcel.get_isRun_text("finance_log_004"),"-跳过不执行该用例")
    def test_finance_log_manage004(self):
        """结算账单成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("finance_log_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 刷新页面
        self.base_page.refresh_page()
        # 点击立即结算
        self.settle_order.click_promptly_settle_btn()
        # 选择线下结算
        self.settle_order.select_line_down_settle()
        # 确认结算
        self.settle_order.click_confirm_settle_btn()
        self.base_page.sleep(1)
        # 刷新页面
        self.base_page.refresh_page()
        # 断言
        self.assert_mode.assert_in(data,self.settle_order.get_bill_settle_status())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Finance_Log_Manage)

    unittest.TextTestRunner(verbosity=2).run(suits)
