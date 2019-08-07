# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/2 17:59

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common import rwconfig
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.settleOrderPage import SettleOrderPage
import unittest
"""
师傅工单状态统计测试用例：
1、师傅已接单订单数量校验 2、师傅已完单订单数量校验 3、师傅未完单订单数量校验 
4、师傅待结算订单数量校验 5、师傅差评单订单数量校验
"""
class Order_Statistics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
