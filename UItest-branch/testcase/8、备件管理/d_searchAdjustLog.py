# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/15 15:36

from public.common import mytest
from public.common import rwconfig
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.page.inventoryAdjustPage import InventoryAdjust
from public.page.loginPage import LoginPage
import unittest,ddt
"""
网点备件库存调整功能校验：
1、按操作人名称搜索校验    2、成功调整备件库存校验    3、按备件条码搜索校验
4、按备件名称搜索校验      5、按出入库类型搜索校验
"""
# 获取测试数据
test_data = get_test_data()["InventoryAdjustPage"]["search_log"]

@ddt.ddt
class Adjust_Record(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.inventory_adjust = InventoryAdjust(cls.driver)
        # 开始执行测试用例
        mytest.start_test()
        # 时间搜索期望值赋值处理
        test_data[1]["expect"] = cls.base_page.get_now_time()
        # 获取测试账号信息
        username = rwconfig.read_config_data("西安好家帮家政有限公司", "username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.inventory_adjust.enter_inventory_adjust_log_page()

    @ddt.data(*test_data)
    def test_adjust_record001(self,test_data):
        """库存调整记录页面搜索功能测试用例"""

        # 打印测试用例名称
        self.base_page.print_case_name(test_data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        self.base_page.sleep(1)
        # 选择操作人
        self.inventory_adjust.select_operator_name(operator_name=test_data["Operator"])
        # 输入操作开始日期
        self.inventory_adjust.input_operate_start_date(start_date=test_data["OperateDate"])
        # 输入操作结束日期
        self.inventory_adjust.input_operate_end_date(end_date=test_data["OperateDate"])
        # 输入备件条码
        self.inventory_adjust.input_spare_part_number(spare_part_number=test_data["SP_Number"])
        # 输入备件名称
        self.inventory_adjust.input_spare_part_name(spare_part_name=test_data["SP_Name"])
        # 选择出入库类型
        self.inventory_adjust.select_IO_inventory_type(inventory_type=test_data["IO_Type"])
        # 点击搜索
        self.inventory_adjust.click_search_button()
        self.base_page.sleep(1)
        # 获取第一行所有信息
        after_search_info = self.inventory_adjust.get_first_log_info()
        # 断言
        self.assert_page.assert_in(test_data["expect"],after_search_info)

    @classmethod
    def tearDownClass(cls):

        # 退出浏览器
        cls().base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Adjust_Record)

    unittest.TextTestRunner().run(suits)