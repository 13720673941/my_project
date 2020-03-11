# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/8 18:08

from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.facilitatorPage import FacilitatorPage
import unittest

class Facilitator_Set(unittest.TestCase):

    """ 【合作服务商服务设置功能】 """

    # 实例化类
    readExcel = Read_Excel("facilitatorSet")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.server_branch = FacilitatorPage(cls.driver)
        cls.assertMode = Assert(cls.driver, "facilitatorSet")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建自建单
        cls.create_order.create_not_return_order()
        # 获取新建工单单号
        cls.orderNumber = cls.create_order.get_order_number()

    def enter_set_server_page(self,branch_keyword):
        """进入服务配置页面"""

        # 搜索服务商
        self.server_branch.input_search_branch_keyword(branch_keyword)
        # 点击搜索按钮
        self.server_branch.click_search_branch_btn()
        # # 向右滚动托条，显示出设置服务按钮
        # self.server_branch.click_and_roll_right_page()
        # 点击服务配置按钮
        self.server_branch.click_server_set_btn()
        # 时间加载
        self.base.sleep(2)

    def clear_teamwork_type(self):
        """清空合作类型选择"""

        # 清空合作类型-派单
        self.server_branch.clear_teamwork_type_1()
        # 清空合作类型-报单
        self.server_branch.clear_teamwork_type_2()
        # 清空合作类型-返单
        self.server_branch.clear_teamwork_type_3()

    def setUp(self):

        # 刷新页面
        self.base.refresh_page()
        self.base.sleep(2)
        # 进入客户列表页面
        self.server_branch.enter_customer_list_page()
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 时间加载
        self.base.wait()

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_001"),"-跳过不执行该用例")
    def test_facilitator_set001(self):
        """设置服务商客户备注校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 搜索指定服务商
        self.enter_set_server_page(data["服务商名称"])
        # 输入新服务商备注
        self.server_branch.input_server_branch_remark(data["客户备注"])
        # 点击确定服务设置
        self.server_branch.click_save_set_server()
        self.base.sleep(1)
        # 判断修改成功
        self.assertMode.assert_in(data,self.server_branch.get_first_branch_info())

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_002"),"-跳过不执行该用例")
    def test_facilitator_set002(self):
        """合作类型选择不能为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 点击确定保存按钮
        self.server_branch.click_save_set_server()
        # 断言
        self.assertMode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_003"),"-跳过不执行该用例")
    def test_facilitator_set003(self):
        """无派单合作类型不能派单校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择合作类型-报单
        self.server_branch.select_teamwork_type_2()
        # 选择合作类型-返单
        self.server_branch.select_teamwork_type_3()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 进入订单派单页面
        self.send_order.enter_send_order_page()
        # 选择派单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        # 选择派单到服务商
        self.send_order.select_send_type(data["派单类型"])
        self.base.sleep(1)
        # 输入网点名称
        self.send_order.input_search_name(data["派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(2)
        # 断言-获取服务商是否存在页面的属性 False
        self.assertMode.assert_el_not_in_page(data,self.send_order.search_branch_is_display())

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_004"),"-跳过不执行该用例")
    def test_facilitator_set004(self):
        """无报单合作类型不能添加报单订单校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择合作类型-派单
        self.server_branch.select_teamwork_type_1()
        # 选择合作类型-返单
        self.server_branch.select_teamwork_type_3()
        # 保存设置
        self.server_branch.click_save_set_server()
        self.base.sleep(1)
        # 进入创建订单列表页面
        self.create_order.enter_create_order_url()
        # 选择代报单
        self.create_order.select_order_type(data["工单类型"])
        self.base.sleep(2)
        # 获取服务商列表
        branch_list = self.create_order.get_branch_name_list_for_set()
        # 断言-列表仅报单创建创建订单时不能选择该服务商
        self.assertMode.assert_not_in(data,branch_list)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_005"),"-跳过不执行该用例")
    def test_facilitator_set005(self):
        """无返单合作类型不能添加返单订单校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_005")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择合作类型-派单
        self.server_branch.select_teamwork_type_1()
        # 选择合作类型-报单
        self.server_branch.select_teamwork_type_2()
        # 保存设置
        self.server_branch.click_save_set_server()
        # 进入创建订单列表页面
        self.create_order.enter_create_order_url()
        self.base.sleep(1)
        # 选需返单
        self.create_order.select_order_type(data["工单类型"])
        self.base.sleep(2)
        # 获取服务商列表
        branch_list = self.create_order.get_branch_name_list_for_set()
        # 断言-列表中没有设置过的服务商
        self.assertMode.assert_not_in(data,branch_list)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_006"),"-跳过不执行该用例")
    def test_facilitator_set006(self):
        """服务类型授权不能为空"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_006")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空选择的授权服务类型
        self.server_branch.clear_server_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.login.get_system_msg()
        # 断言
        self.assertMode.assert_equal(data,system_message)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_007"),"-跳过不执行该用例")
    def test_facilitator_set007(self):
        """授权服务品牌不能为空"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_007")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空选择的授权服务品牌类型
        self.server_branch.clear_brands_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.login.get_system_msg()
        # 断言
        self.assertMode.assert_equal(data,system_message)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_008"),"-跳过不执行该用例")
    def test_facilitator_set008(self):
        """授权服务品类不能为空"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_008")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空选择的授权服务类型
        self.server_branch.clear_kinds_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.login.get_system_msg()
        # 断言
        self.assertMode.assert_equal(data,system_message)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_009"),"-跳过不执行该用例")
    def test_facilitator_set009(self):
        """服务商授权区域为空校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_009")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入服务商列表页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空该服务商的地址信息
        self.server_branch.clear_server_address_info()
        self.base.sleep(1)
        # 点击保存设置
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.login.get_system_msg()
        # 断言
        self.assertMode.assert_equal(data,system_message)

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_010"),"-跳过不执行该用例")
    def test_facilitator_set010(self):
        """设置授权全部类型保存成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_010")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入客户列表
        self.server_branch.enter_customer_list_page()
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择派单类型
        self.server_branch.select_teamwork_type_1()
        # 清空选择的授权服务类型
        self.server_branch.clear_server_type()
        self.base.sleep(1)
        # 选择其他服务类型
        self.server_branch.select_server_type_of_other(data["服务类型"])
        # 清空授权品牌
        self.server_branch.clear_brands_type()
        # 重新授权品牌
        self.server_branch.select_brands_type_of_other(data["品牌"])
        # 清空授权品类
        self.server_branch.clear_kinds_type()
        self.base.sleep(1)
        # 选择品类
        self.server_branch.select_kinds_type_of_other(data["品类"])
        # 清空授权区域
        self.server_branch.clear_server_address_info()
        # 选择授权区域
        self.server_branch.select_server_province(data["省份"])
        # 点击保存
        self.server_branch.click_save_set_server()
        self.base.sleep(1)
        # 断言
        self.assertMode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("facilitator_set_011"),"-跳过不执行该用例")
    def test_facilitator_set011(self):
        """不在授权区域的订单不能派单给该服务商"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("facilitator_set_011")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 进入客户列表
        self.server_branch.enter_customer_list_page()
        # 进入授权设置页面
        self.enter_set_server_page(data["服务商名称"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择派单类型
        self.server_branch.select_teamwork_type_1()
        # 点击保存
        self.server_branch.click_save_set_server()
        self.base.sleep(1)
        # 进入订单派单页面
        self.send_order.enter_send_order_page()
        # 选择派单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        self.base.sleep(1)
        # 选择派单到服务商
        self.send_order.select_send_type(data["派单类型"])
        # 输入网点名称
        self.send_order.input_search_name(data["派单网点"])
        # 点击搜索
        self.send_order.click_search_btn()
        self.base.sleep(1)
        # 断言-获取服务商是否存在页面的属性 False
        self.assertMode.assert_el_not_in_page(data,self.send_order.search_branch_is_display())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestLoader().loadTestsFromTestCase(Facilitator_Set)

    unittest.TextTestRunner().run(suits)

