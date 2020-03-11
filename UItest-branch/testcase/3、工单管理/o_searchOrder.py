#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/4 17:14

from public.common import rwConfig
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.searchOrderPage import SearchOrderPage
import unittest,ddt

@ddt.ddt
class Search_Order(unittest.TestCase):

    """" 【工单列表搜索/更多搜索工单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("searchOrder")
    # ddt测试用例编号集合
    case_list1 = [
        "search_order_001","search_order_002","search_order_003","search_order_004",
        "search_order_005","search_order_006","search_order_007"
    ]
    case_list2 = [
        "search_order_008","search_order_009","search_order_010","search_order_011",
        "search_order_012","search_order_013","search_order_014","search_order_015",
        "search_order_016"
    ]
    # 获取ddt测试数据
    ddt_data1 = read_excel.get_ddt_data(case_list1)
    ddt_data2 = read_excel.get_ddt_data(case_list2)
    # 读取订单单号信息，订单单号的搜索取添加订单写入的订单单号
    orderNumber = rwConfig.read_config_data('for_invalid_and_search','id',orderNumPath)
    # 写入工单编码到json,搜索测试数据的第一行
    ddt_data1[0]["工单编号"] = orderNumber
    
    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.search_order = SearchOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "searchOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入全部工单页面
        cls.search_order.enter_search_order_page()

    @ddt.data(*ddt_data1)
    @myDecorator.skipped_case
    def test_search_order001(self,ddt_data1):
        """网点主搜索页面测试用例"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data1)
        self.base.sleep(1)
        # 清除数据
        self.base.refresh_page()
        # 输入工单编号
        self.search_order.input_order_Nnumber(ddt_data1["工单编号"])
        # 输入用户姓名
        self.search_order.input_username(ddt_data1["用户姓名"])
        # 输入用户电话
        self.search_order.input_user_phone(ddt_data1["用户电话"])
        # 选择服务类型
        self.search_order.select_server_type(ddt_data1["服务类型"])
        # 选择工单状态
        self.search_order.select_order_status(ddt_data1["工单状态"])
        # 选择服务师傅
        self.search_order.select_master(ddt_data1["服务师傅"])
        # 点击搜索按钮
        self.search_order.click_search_btn()
        # 时间加载
        self.base.sleep(4)
        # 断言
        self.assert_mode.assert_more_str_in(ddt_data1,self.search_order.get_first_order_info())

    @ddt.data(*ddt_data2)
    @myDecorator.skipped_case
    def test_search_order002(self,ddt_data2):
        """网点更多搜索页面测试用例"""

        self.base.print_case_name(ddt_data2)
        # 刷新页面
        self.base.refresh_page()
        # 点击更多条件搜索按钮
        self.search_order.click_search_more()
        self.base.sleep(1)
        # 选择家电品牌
        self.search_order.select_product_brand(ddt_data2["品牌"])
        # 选择家电品类
        self.search_order.select_product_kinds(ddt_data2["品类"])
        # 输入产品型号
        self.search_order.input_product_number(ddt_data2["型号"])
        # 输入内机条码
        self.search_order.input_in_pheNum(ddt_data2["内机编码"])
        # 选择工单来源
        self.search_order.select_order_from(ddt_data2["工单来源"])
        # 选择购买渠道
        self.search_order.select_buy_place(ddt_data2["购买渠道"])
        # 输入下单开始日期
        self.search_order.input_create_start_date(ddt_data2["创建日期"])
        # 输入下单结束日期
        self.search_order.input_create_end_date(ddt_data2["创建日期"])
        # 输入完成工单开始日期
        self.search_order.input_finish_start_date(ddt_data2["完成日期"])
        # 输入完成工单结束日期
        self.search_order.input_finish_end_date(ddt_data2["完成日期"])
        # 点击搜索按钮
        self.search_order.click_more_search_btn()
        self.base.sleep(2)
        # 获取第一行订单数据
        first_row_info = self.search_order.get_first_order_info()
        # 断言
        self.assert_mode.assert_more_str_in(ddt_data2,first_row_info)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Search_Order)
    unittest.TextTestRunner().run(suit)