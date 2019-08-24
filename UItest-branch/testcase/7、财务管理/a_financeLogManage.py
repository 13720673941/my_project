# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/24 10:21

from public.common import rwconfig
from public.common import mytest
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.settleOrderPage import SettleOrderPage
from public.page.financeManagePage import FinanceManagePage
import unittest
"""
结算订单生成收入支出日志记录功能：
1、网点收入日志记录功能校验 2、网点支出日志记录功能校验
"""
# 获取测试数据
test_data = get_test_data()["FinanceManagePage"]

class Finance_Log_Manage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.finance_log = FinanceManagePage(cls.driver)
        # 开始执行
        mytest.start_test()
        # 获取经销商账号
        cls.manage_use = rwconfig.read_config_data("蓝魔科技","username")
        cls.manage_pwd = rwconfig.read_config_data("蓝魔科技","password")
        # 登录经销商
        cls.login.login_main(cls.manage_use,cls.manage_pwd)
        # 创建订单
        cls.create_order.create_not_return_order()
        # 获取工单号
        cls.order_number = cls.base_page.get_order_number()
        # 获取经销商下的服务商
        server_branch_name = rwconfig.read_config_data("蓝魔科技","branch001")
        # 派单到服务商
        cls.please_order.please_order_main(
            ordernumber=cls.order_number,pagename=server_branch_name,please_to_branch=True)
        # 退出经销商登录
        cls.login.click_logout_button()
        # 获取服务商账号密码
        cls.server_use = rwconfig.read_config_data(server_branch_name,"username")
        cls.server_pwd = rwconfig.read_config_data(server_branch_name,"password")
        # 登录服务商
        cls.login.login_main(cls.server_use,cls.server_pwd)
        # 获取服务商的派单师傅名称
        master_name = rwconfig.read_config_data(server_branch_name,"master001")
        # 派单到师傅
        cls.please_order.please_order_main(
            ordernumber=cls.order_number,pagename=master_name)
        # 完成服务
        cls.finish_order.finish_order_main(ordernumber=cls.order_number)

    def test_finance_log_manage001(self):
        """收入结算生成日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.manage_use,self.manage_pwd)
        # 服务商工单结算
        self.settle_order.settle_main(order_number=self.order_number,settle_branch=True)
        # 退出登录
        self.base_page.refresh_page()
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.server_use,self.server_pwd)
        # 进入我的收入记录页面
        self.finance_log.enter_my_income_page()
        # 搜索经销商结算的工单编号
        self.finance_log.input_order_number(order_number=self.order_number)
        # 点击搜索
        self.finance_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取收入列表第一行全部信息
        first_log_info = self.finance_log.get_income_first_row_info()
        # 断言
        self.assert_mode.assert_in(self.order_number,first_log_info)

    def test_finance_log_manage002(self):
        """支出结算生成日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 服务商支出结算
        self.settle_order.settle_main(order_number=self.order_number)
        # 刷新页面
        self.base_page.refresh_page()
        # 进入我的支出页面
        self.finance_log.enter_my_expend_page()
        # 搜索经销商结算的工单编号
        self.finance_log.input_order_number(order_number=self.order_number)
        # 点击搜索
        self.finance_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取支出列表第一行全部信息
        first_log_info = self.finance_log.get_expend_first_row_info()
        # 断言
        self.assert_mode.assert_in(self.order_number,first_log_info)

    @classmethod
    def tearDownClass(cls):

        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Finance_Log_Manage)

    unittest.TextTestRunner(verbosity=2).run(suits)
