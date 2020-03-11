# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/9/3 15:26

from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.common import myDecorator
from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.page.loginPage import LoginPage
from public.page.AddSparePartPage import AddSparePartPage
from public.page.spartPartListPage import SparePartListPage
import unittest,ddt

@ddt.ddt
class Add_Spare_Part(unittest.TestCase):

    """ 【添加备件功能测试脚本】 """

    # 实例化操作类
    readExcel = Read_Excel("addSparePart")
    # ddt测试数据用例集合
    caseList = [
        "add_sparePart_002","add_sparePart_002","add_sparePart_003",
        "add_sparePart_004","add_sparePart_005","add_sparePart_006",
        "add_sparePart_007","add_sparePart_008","add_sparePart_009",
        "add_sparePart_010","add_sparePart_011","add_sparePart_012",
        "add_sparePart_013"
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
        cls.create_sparePart = AddSparePartPage(cls.driver)
        cls.alter_sparePart = SparePartListPage(cls.driver)
        cls.assert_page = Assert(cls.driver,"addSparePart")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 进入公司库存页面
        cls.create_sparePart.enter_company_inventory_page()

    def setUp(self):

        # 刷新页面
        self.base_page.refresh_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_create_sparePart001(self,ddt_data):
        """创建备件功能"""

        # 打印测试用例名称
        self.base_page.print_case_name(ddt_data)
        # 点击新增备件按钮
        self.create_sparePart.click_add_new_sparePart()
        # 等待加载
        self.base_page.sleep(1)
        # 输入备件名称
        self.create_sparePart.input_add_sparePart_name(ddt_data["名称"])
        # 选择备件类型
        self.create_sparePart.select_add_sparePart_type(ddt_data["类型"])
        # 选择计量单位
        self.create_sparePart.select_measuring_unit(ddt_data["单位"])
        # 输入备件条码
        self.create_sparePart.input_add_sparePart_number(ddt_data["条码"])
        # 输入备件品牌
        self.create_sparePart.input_add_sparePart_brand(ddt_data["品牌"])
        # 选择备件来源
        self.create_sparePart.select_sparePart_from(ddt_data["来源"])
        # 输人备件型号
        self.create_sparePart.input_sparePart_type_number(ddt_data["型号"])
        # 选择适用品类
        self.create_sparePart.select_use_kind(ddt_data["品类"])
        # 上传备件图片
        self.create_sparePart.operate_up_loading_picture(ddt_data["图片"])
        # 输入入库价格
        self.create_sparePart.input_into_inventory_price(ddt_data["入库价"])
        # 输入零售价
        self.create_sparePart.input_user_buy_price(ddt_data["零售价"])
        # 点击保存按钮
        self.create_sparePart.click_add_save_btn()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_equal(ddt_data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("add_sparePart_014"),"-跳过不执行该用例")
    def test_create_sparePart002(self):
        """编辑备件功能校验"""

        # 获取测试数据信息
        data = self.readExcel.get_dict_data("add_sparePart_014")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 点击第一个备件的修改按钮
        self.alter_sparePart.click_alter_button(data["原备件名称"])
        self.base_page.sleep(2)
        # 输入新备件名称
        self.alter_sparePart.input_alter_sparePart_name(data["修改备件名称"])
        # 点击保存
        self.alter_sparePart.click_alter_save_btn()
        self.base_page.sleep(1)
        # 刷新页面重新搜索
        self.base_page.refresh_page()
        # 输入搜索备件名称
        self.alter_sparePart.input_search_sparePart_name(data["修改备件名称"])
        # 点击搜索备件
        self.alter_sparePart.click_search_button()
        self.base_page.sleep(1)
        # 断言
        self.assert_page.assert_in(data,self.alter_sparePart.get_first_row_info())

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Add_Spare_Part)

    unittest.TextTestRunner().run(suits)