# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/21 19:07

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.shortMsgLogPage import ShortMsgLogPage
from config.pathconfig import *
from config.urlconfig import *
import unittest
"""
短信发送记录页面：
1、扣除短信余量校验  2、发送成功后日志记录校验
"""
# 获取测试数据
test_data = get_test_data()["ShortMsgLogPage"]["deduct_msg_fnc"]

class Send_ShortMsg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.short_msg_log = ShortMsgLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 获取网点账号密码
        username = read_config_data("西安超级售后有限公司", "username")
        password = read_config_data("西安超级售后有限公司", "password")
        # 网点登录
        cls.login.login_main(username, password)
        # 获取工单余量
        cls.short_msg_count = int(cls.short_msg_log.get_short_msg_count())
        # 经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()
        # 获取派单师傅
        master = read_config_data("西安超级售后有限公司", "master001")
        # 派单
        cls.please_order.please_order_main(cls.order_number, master)

    def test_send_shortMsg001(self):
        """扣除短信数量校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入首页
        self.base_page.open_url(review_url)
        self.base_page.sleep(2)
        # 获取首页短信余量
        new_short_msg_count = int(self.short_msg_log.get_short_msg_count())
        # 计算短信余量差值
        diff_count = self.short_msg_count - new_short_msg_count
        # 断言
        self.assert_mode.assert_equal(data["expect"],diff_count)

    def test_send_shortMsg002(self):
        """发送短信日志记录校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取发送短信的工单单号
        order_number = read_config_data("for_operate_log_search", "id", orderNumPath)
        # 进入短信发送日志记录页面
        self.short_msg_log.enter_short_msg_list_page()
        # 搜索工单发送记录
        self.short_msg_log.input_order_number(order_number=order_number)
        # 点击搜索
        self.short_msg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行日志发送数据
        first_row_msg_info = self.short_msg_log.get_first_row_info()
        # 断言工单编号
        self.assert_mode.assert_in(order_number,first_row_msg_info)
        # 断言发送成功
        self.assert_mode.assert_in(data["expect"],first_row_msg_info)

    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':



    suits = unittest.TestLoader().loadTestsFromTestCase(Send_ShortMsg)

    unittest.TextTestRunner(verbosity=2).run(suits)
