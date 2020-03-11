# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/19 14:22

from public.common.operateExcel import *
from public.common import myDecorator
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.teamworkNewsPage import TeamWorkNewsPage
import unittest,ddt

@ddt.ddt
class Teamwork_Apply_Search(unittest.TestCase):
    """ 【合作申请搜索统计功能】 """

    # 实例化类
    readExcel = Read_Excel("teamworkSearch")
    # 测试用例编号
    case_list = [
        "teamwork_search_001","teamwork_search_002",
        "teamwork_search_003","teamwork_search_004"
    ]
    # 获取ddt测试类型数据
    ddt_data = readExcel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.teamwork_apply = TeamWorkNewsPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "teamworkSearch")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入客户合作页面
        cls.teamwork_apply.enter_teamwork_news_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_visit_news_search(self,ddt_data):
        """合作申请页面搜索客户校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 刷新页面
        self.base.refresh_page()
        # 切换到发出的申请页面
        self.teamwork_apply.click_table_send_visit()
        # 输入搜索关键字
        self.teamwork_apply.input_customer_name_phone(ddt_data["搜索字段"])
        # 点击搜索
        self.teamwork_apply.click_search_btn()
        self.base.sleep(1)
        # 断言
        self.assertMode.assert_in(ddt_data,self.teamwork_apply.get_first_row_info())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Teamwork_Apply_Search)

    unittest.TextTestRunner().run(suits)







































































































































































































