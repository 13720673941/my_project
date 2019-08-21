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
from public.page.orderLogPage import OrderLogPage
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
        # 获取派单师傅
        master = read_config_data("XM科技有限公司", "master001")
        # 派单
        cls.please_order.please_order_main(cls.order_number, master)

    def test_send_shortMsg001(self):
        """扣除短信数量校验"""

