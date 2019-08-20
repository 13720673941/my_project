# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/20 17:08

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.orderLogPage import OrderLogPage
from config.pathconfig import *
from unittest import TestCase
"""
工单余量日志记录页面搜索筛选:
1、按照创建订单日期搜索校验  2、按照派单类型搜索校验"  3、按照订单单号搜索校验"  4、混合搜索扣除记录校验
"""
# 获取测试数据
test_data = get_test_data()["OrderLogPage"]["search_log_fnc"]

class Search_Order_Log(TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.order_log = OrderLogPage(cls.driver)
        