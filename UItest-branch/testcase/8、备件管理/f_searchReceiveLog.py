# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/12 10:56

from public.common import myDecorator
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.page.loginPage import LoginPage
from public.page.masterReceivePage import MasterReceivePage
import unittest,ddt

@ddt.ddt
class Search_Receive_Log(unittest.TestCase):

    """ 【师傅领用记录页面搜索功能】 """

    # 操作实例化
    readExcel = Read_Excel("receiveLogSearch")
    # ddt数据用例编号集合
    caseList = [
        "receive_search_001","receive_search_002",
        "receive_search_003","receive_search_004",
        "receive_search_005"
    ]
    # 获取测试数据
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.receive_sparePart = MasterReceivePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"receiveLogSearch")
        # 设置测试数据中的数值
        cls.ddt_data[1]["领用时间"] = cls.base_page.get_now_time()
        cls.ddt_data[4]["领用时间"] = cls.base_page.get_now_time()
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")

    def setUp(self):
        # 刷新清除数据
        self.base_page.refresh_page()
        # 进入师傅领取记录页面
        self.receive_sparePart.enter_receive_log_page()
        self.base_page.sleep(1)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_search_receive_log001(self,ddt_data):
        """师傅领取备件记录页面搜索功能"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data)
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(ddt_data["师傅名称"])
        # 输入开始日期
        self.receive_sparePart.input_receive_start_time(ddt_data["领用时间"])
        # 输入结束日期
        self.receive_sparePart.input_receive_end_time(ddt_data["领用时间"])
        # 输入备件条码
        self.receive_sparePart.input_sparePart_number(ddt_data["备件条码"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(ddt_data["备件名称"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(1)
        # 获取搜索结果第一行数据
        first_search_info = self.receive_sparePart.get_first_search_info()
        # 断言
        self.assert_page.assert_in(ddt_data,first_search_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Search_Receive_Log)

    unittest.TextTestRunner(verbosity=2).run(suits)