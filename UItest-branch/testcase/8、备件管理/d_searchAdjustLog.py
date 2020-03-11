# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 15:36

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.loginPage import LoginPage
import unittest,ddt
"""
网点备件库存调整功能校验：
1、按操作人名称搜索校验    2、成功调整备件库存校验    3、按备件条码搜索校验
4、按备件名称搜索校验      5、按出入库类型搜索校验
"""

@ddt.ddt
class Adjust_Record(unittest.TestCase):

    """ 【库存调整记录日志搜索】 """

    # 实例化操作类
    readExcel = Read_Excel("adjustLogSearch")
    # 用例集合
    caseList = [
        "adjust_log_search_001","adjust_log_search_002",
        "adjust_log_search_003","adjust_log_search_004",
        "adjust_log_search_005"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):

        # 浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        cls.assert_page = Assert(cls.driver,"adjustLogSearch")
        # 时间搜索期望值赋值处理
        cls.ddt_data[1]["期望值"] = cls.base_page.get_now_time()
        cls.ddt_data[1]["操作时间"] = cls.base_page.get_now_time()
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.inventory_adjust.enter_inventory_adjust_log_page()

    @ddt.data(*ddt_data)
    def test_adjust_record001(self,ddt_data):
        """库存调整记录页面搜索功能测试用例"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data)
        # 刷新页面
        self.base_page.refresh_page()
        self.base_page.sleep(1)
        # 选择操作人
        self.inventory_adjust.select_operator_name(ddt_data["操作人"])
        # 输入操作开始日期
        self.inventory_adjust.input_operate_start_date(ddt_data["操作时间"])
        # 输入操作结束日期
        self.inventory_adjust.input_operate_end_date(ddt_data["操作时间"])
        # 输入备件条码
        self.inventory_adjust.input_spare_part_number(ddt_data["备件条码"])
        # 输入备件名称
        self.inventory_adjust.input_spare_part_name(ddt_data["备件名称"])
        # 选择出入库类型
        self.inventory_adjust.select_IO_inventory_type(ddt_data["调整类型"])
        # 点击搜索
        self.inventory_adjust.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(ddt_data,self.inventory_adjust.get_first_log_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Adjust_Record)

    unittest.TextTestRunner().run(suits)