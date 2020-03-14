# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/14 14:30

from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.common import myDecorator
from public.page.loginPage import LoginPage
from public.page.myGroupSearchPage import MyGroupListPage
import unittest,ddt

@ddt.ddt
class Group_Search(unittest.TestCase):

    """ 【我创建的圈子列表页面搜索功能】 """

    # 实例化操作类
    readExcel = Read_Excel("groupSearch")
    # 用例编号集合
    caseList = [
        "group_search_001","group_search_002","group_search_003",
        "group_search_004","group_search_005"
    ]
    # 获取ddt类型测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):
        # 实例化类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.group_search = MyGroupListPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"groupSearch")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入我的圈子列表页面
        cls.group_search.enter_my_group_list_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_group_search001(self,ddt_data):
        """圈子搜索功能校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 刷新页面
        self.base.refresh_page()
        # 输入圈子名称
        self.group_search.input_group_name_search(ddt_data["圈子名称"])
        # 选择服务区域
        self.group_search.select_service_area_search(ddt_data["区域"])
        # 选择服务类型
        self.group_search.select_service_type_search(ddt_data["类型"])
        # 选择服务品牌
        self.group_search.select_service_brand_search(ddt_data["品牌"])
        # 选择服务品类
        self.group_search.select_service_kind_search(ddt_data["品类"])
        # 点击搜索
        self.group_search.click_search_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_in(ddt_data,self.group_search.get_after_search_info())

    @classmethod
    def tearDownClass(cls):
        # 清理缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Group_Search)

    unittest.TextTestRunner().run(suit)