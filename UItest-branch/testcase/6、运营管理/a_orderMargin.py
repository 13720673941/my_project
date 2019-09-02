# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 11:50

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data,write_config_data
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.orderLogPage import OrderLogPage
from config.pathconfig import *
from config.urlconfig import *
import unittest
"""
网点工单扣除记录测试：
1、派单扣除网点单量记记录校验 2、网点工单余量扣除记录日志校验
"""
# 获取测试数据
test_data = get_test_data()["OrderLogPage"]["deduct_order_fnc"]

class Order_Margin_Log(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.order_log = OrderLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 获取网点账号密码
        username = read_config_data("XM科技有限公司", "username")
        password = read_config_data("XM科技有限公司", "password")
        # 网点登录
        cls.login.login_main(username, password)
        # 获取工单余量
        cls.order_count = int(cls.order_log.get_order_count())
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()
        # 写入工单单号后面扣除/短信日志搜索使用
        write_config_data(section="for_operate_log_search",option="id",
                          writeData=cls.order_number,DataPath=orderNumPath)
        # 获取派单师傅
        master = read_config_data("XM科技有限公司", "master001")
        # 派单
        cls.please_order.please_order_main(cls.order_number,master)

    def test_order_margin_log001(self):
        """派单扣除工单余量校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用力名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入首页
        self.base_page.open_url(review_url)
        self.base_page.sleep(2)
        # 获取单量记录
        new_order_count = int(self.order_log.get_order_count())
        # 计算单量前后差值
        diff_count = self.order_count - new_order_count
        # 断言
        self.assert_mode.assert_equal(data["expect"],diff_count)

    def test_order_margin_log002(self):
        """工单单量记录日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用力名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入单量扣除记录页面
        self.order_log.enter_order_log_page()
        self.base_page.sleep(1)
        # 获取第一条记录的内容信息
        first_row_log_info = self.order_log.get_first_row_info()
        # 断言- 判断订单单号在该信息里面
        self.assert_mode.assert_in(self.order_number,first_row_log_info)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Order_Margin_Log)

    unittest.TextTestRunner(verbosity=2).run(suits)