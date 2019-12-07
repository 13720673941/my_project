# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/5 11:20

from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest
from public.common import rwconfig
from public.page.loginPage import LoginPage
from public.page.companyInventoryPage import CompanyInventoryPage
import unittest,ddt
"""
备件删除功能测试用例：
1、有库存的备件不能删除校验  2、成功删除备件校验
"""
# 获取测试数据
data = get_test_data()["CompanyInventoryPage"]["del_sparePart_fnc"]

@ddt.ddt
class Del_Spare_Part(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.assert_page = Assert(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.del_sparePart = CompanyInventoryPage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行测试用例
        mytest.start_test()
        # 获取测试账号信息
        username = rwconfig.read_config_data("西安好家帮家政有限公司", "username")
        password = rwconfig.read_config_data("西安好家帮家政有限公司", "password")
        # 登录网点
        cls.login.login_main(username, password)
        # 进入公司库存页面
        cls.del_sparePart.enter_company_inventory_page()

    @ddt.data(*data)
    def test_del_sparePart001(self,data):
        """删除备件功能测试用例"""

        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 刷新页面
        self.base_page.refresh_page()
        # 输入备件编码
        self.del_sparePart.input_search_sparePart_number(sparePart_number=data["SP_Num"])
        # 点击搜索
        self.del_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 选择第一个备件
        self.del_sparePart.select_first_sparePart()
        # 点击删除按钮
        self.del_sparePart.click_del_sparePart_btn()
        # 确定删除备件
        self.del_sparePart.click_confirm_del_btn()
        # 获取系统提示信息
        systemMsg = self.base_page.get_system_msg()
        # 断言
        self.assert_page.assert_equal(data["expect"],systemMsg)



    @classmethod
    def tearDownClass(cls):
        cls().assert_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Del_Spare_Part)

    unittest.TextTestRunner().run(suits)