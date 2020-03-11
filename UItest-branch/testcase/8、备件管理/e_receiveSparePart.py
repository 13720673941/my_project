# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/10/11 17:08

from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.page.loginPage import LoginPage
from public.page.masterReceivePage import MasterReceivePage
from public.page.spartPartListPage import SparePartListPage
import unittest

class Receive_Spare_Part(unittest.TestCase):

    """ 【师傅领用备件功能】 """

    # 实例化操作类
    readExcel = Read_Excel("masterReceive")

    @classmethod
    def setUpClass(cls):

        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.company_sparePart = SparePartListPage(cls.driver)
        cls.receive_sparePart = MasterReceivePage(cls.driver)
        cls.assert_page = Assert(cls.driver,"masterReceive")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.company_sparePart.enter_company_inventory_page()

    def setUp(self):
        # 刷新页面
        self.base_page.refresh_page()

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_001"),"-跳过不执行")
    def test_receive_sparePart001(self):
        """备件领取数量为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索选择备件
        self.company_sparePart.select_first_sparePart(data["备件名称"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(data["师傅名称"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_002"),"-跳过不执行")
    def test_receive_sparePart002(self):
        """备件名称为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(data["师傅名称"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_003"),"-跳过不执行")
    def test_receive_sparePart003(self):
        """领取备件师傅名称为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_003")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索选择备件
        self.company_sparePart.select_first_sparePart(data["备件名称"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 点击保存
        self.receive_sparePart.click_save_receive()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_004"),"-跳过不执行")
    def test_receive_sparePart004(self):
        """师傅领取备件页面删除备件校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_004")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 搜索选择备件
        self.company_sparePart.select_first_sparePart(data["备件名称"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(data["师傅名称"])
        # 点击删除选择的备件
        self.receive_sparePart.click_delete_sparePart()
        # 点击保存
        self.receive_sparePart.click_save_receive()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_005"),"-跳过不执行")
    def test_receive_sparePart005(self):
        """师傅成功领取备件校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_005")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入师傅库存页面
        self.receive_sparePart.enter_master_inventory_page()
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(data["师傅名称"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(data["备件名称"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(2)
        # 获取师傅库存数量
        global master_before_receive,company_before_receive
        # 未搜索到就是 0
        master_before_receive = self.receive_sparePart.get_master_inventory_count()
        # 进入公司库存页面
        self.company_sparePart.enter_company_inventory_page()
        # 搜索备件
        self.company_sparePart.input_search_sparePart_name(data["备件名称"])
        self.company_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 获取备件库存数量
        company_before_receive = self.receive_sparePart.get_company_inventory_count()
        # 刷新页面
        self.base_page.refresh_page()
        # 搜索选择备件
        self.company_sparePart.select_first_sparePart(data["备件名称"])
        # 点击师傅领用备件按钮
        self.receive_sparePart.click_master_receive_btn()
        # 选择领用师傅名称
        self.receive_sparePart.select_receive_master_name(data["师傅名称"])
        # 输入备件数量
        self.receive_sparePart.input_receive_count(data["领用数量"])
        # 点击保存
        self.receive_sparePart.click_save_receive()
        # 断言
        self.assert_page.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_006"),"-跳过不执行")
    def test_receive_sparePart006(self):
        """师傅领取成功后领取记录中生成日志校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_006")
        # 赋值处理
        data["领用时间"] = self.base_page.get_now_time()
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 点击师傅领取记录table页面
        self.receive_sparePart.enter_receive_log_page()
        # 输入领取开始日期搜索领取记录
        self.receive_sparePart.input_receive_start_time(data["领用时间"])
        # 输入领取结束日期搜索领取记录
        self.receive_sparePart.input_receive_end_time(data["领用时间"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(2)
        self.assert_page.assert_in(data,self.receive_sparePart.get_first_search_info())

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_007"),"-跳过不执行")
    def test_receive_sparePart007(self):
        """师傅领取成功后公司库存校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_007")
        # 搜索备件
        self.company_sparePart.input_search_sparePart_name(data["备件名称"])
        # 点击搜索
        self.company_sparePart.click_search_button()
        self.base_page.sleep(2)
        # 获取公司库存
        company_after_receive = self.receive_sparePart.get_company_inventory_count()
        # 计算差值
        diff_count = str(company_before_receive - company_after_receive)
        # 断言
        self.assert_page.assert_equal(data,diff_count)

    @unittest.skipUnless(readExcel.get_isRun_text("master_receive_008"),"-跳过不执行")
    def test_receive_sparePart008(self):
        """师傅领取成功后师傅库存校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("master_receive_008")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入师傅库存页面
        self.receive_sparePart.enter_master_inventory_page()
        self.base_page.sleep(1)
        # 选择师傅名称
        self.receive_sparePart.select_search_master_name(data["师傅名称"])
        # 输入备件名称
        self.receive_sparePart.input_sparePart_name(data["备件名称"])
        # 点击搜索
        self.receive_sparePart.click_search_btn()
        self.base_page.sleep(3)
        # 获取师傅备件库存
        master_after_receive = int(self.receive_sparePart.get_master_inventory_count())
        # 计算差值
        diff_count = str(master_after_receive - master_before_receive)
        # 断言
        self.assert_page.assert_equal(data,diff_count)


    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Receive_Spare_Part)

    unittest.TextTestRunner(verbosity=2).run(suits)