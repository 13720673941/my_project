# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/8 18:08

from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.serverBranchPage import ServerBranchPage
from config.pathconfig import *
import unittest
"""
服务商授权设置功能测试用例：
1、设置服务商客户备注校验 2、合作类型不能为空校验 3、无派单合作类型不能派单校验 4、无报单合作类型不能添加报单校验 
5、无返单合作类型不能添加返单订单校验 6、授权服务类型不能为空校验 7、授权服务品牌不能为空校验 8、授权服务品类不能为空校验
9、授权服务所有类型配置成功校验 10、授权服务区域不能为空校验 11、不在授权区域的订单不能派单校验
"""
# 获取测试数据
set_server_data = get_test_data()["AddServerPage"]["server_set_fnc"]

class Server_Set(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化类
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.server_branch = ServerBranchPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        # 开始脚本
        mytest.start_test()
        # 获取网点登录账号密码
        cls.username = read_config_data("蓝魔科技","username")
        cls.password = read_config_data("蓝魔科技","password")
        # 登录网点
        cls.login.login_main(cls.username, cls.password)
        # 获取订单数据添加订单
        user = read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = read_config_data("NotReturnOrder", "品牌", orderInfo)
        kinds = read_config_data("NotReturnOrder", "品类", orderInfo)
        # 经销商下单程序下单
        cls.create_order.create_order_main(user, phe, address, collage, order_type,
                                           server, brands, kinds)
        # 获取新建工单单号
        cls.order_number = cls.base_page.get_order_number()

    def enter_set_server_page(self,branch_keyword):
        """进入服务配置页面"""

        # 搜索服务商
        self.server_branch.input_search_branch_keyword(branch_keyword)
        # 点击搜索按钮
        self.server_branch.click_search_branch_btn()
        # 向右滚动托条，显示出设置服务按钮
        self.server_branch.click_and_roll_right_page()
        # 点击服务配置按钮
        self.server_branch.click_server_set_btn()
        # 时间加载
        self.base_page.sleep(2)

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
        self.base_page.refresh_page()
        # 进入客户列表页面
        self.server_branch.enter_customer_list_page()
        # 点击服务商table
        self.server_branch.click_server_branch_table()
        # 时间加载
        self.base_page.wait()

    def test_server_set001(self):
        """设置服务商客户备注校验"""

        # 获取测试数据
        data = set_server_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 搜索指定服务商
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 输入新服务商备注
        self.server_branch.input_server_branch_remark(branch_remark=data["BranchRemark"])
        # 点击确定服务设置
        self.server_branch.click_save_set_server()
        # 获取第一行服务商的全部信息
        branch_info = self.server_branch.get_first_branch_info()
        # 判断修改成功
        self.assert_mode.assert_in(data["expect"],branch_info)

    def test_server_set002(self):
        """合作类型选择不能为空校验"""

        # 获取测试数据
        data = set_server_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 点击确定保存按钮
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set003(self):
        """无派单合作类型不能派单校验"""

        # 获取测试数据
        data = set_server_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择合作类型-报单
        self.server_branch.select_teamwork_type_2()
        # 选择合作类型-返单
        self.server_branch.select_teamwork_type_3()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 进入订单派单页面
        self.please_order.enter_please_order_page()
        # 选择派单订单
        self.base_page.select_new_order(self.order_number)
        # 点击派单
        self.please_order.click_pleaseOrder_btn()
        # 选择派单到服务商
        self.please_order.please_to_branch()
        # 输入网点名称
        self.please_order.input_search_branch_name(branch_name=data["SetBranch"])
        # 点击搜索
        self.please_order.click_search_branch()
        self.base_page.sleep(1)
        # 断言-获取服务商是否存在页面的属性 False
        self.assert_mode.assert_el_not_in_page(self.please_order.search_branch_is_display())

    def test_server_set004(self):
        """无返单合作类型不能添加报单订单校验"""

        # 获取测试数据
        data = set_server_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择合作类型-派单
        self.server_branch.select_teamwork_type_1()
        # 选择合作类型-返单
        self.server_branch.select_teamwork_type_3()
        # 保存设置
        self.server_branch.click_save_set_server()
        # 进入创建订单列表页面
        self.create_order.enter_create_order_url()
        # 选择代报单
        self.create_order.select_order_type_for_set(orderType=data["OrderType"])
        self.base_page.sleep(2)
        # 获取服务商列表
        branch_list = self.create_order.get_branch_name_list_for_set()
        # 断言-列表中没有设置过的服务商
        self.assert_mode.assert_not_in(data["SetBranch"],branch_list)

    def test_server_set005(self):
        """无返单合作类型不能添加返单订单校验"""

        # 获取测试数据
        data = set_server_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
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
        # 选需返单
        self.create_order.select_order_type_for_set(orderType=data["OrderType"])
        self.base_page.sleep(2)
        # 获取服务商列表
        branch_list = self.create_order.get_branch_name_list_for_set()
        # 断言-列表中没有设置过的服务商
        self.assert_mode.assert_not_in(data["SetBranch"],branch_list)

    def test_server_set006(self):
        """服务类型授权不能为空"""

        # 获取测试数据
        data = set_server_data["TestCase006"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空选择的授权服务类型
        self.server_branch.clear_server_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set007(self):
        """授权服务品牌不能为空"""

        # 获取测试数据
        data = set_server_data["TestCase007"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空选择的授权服务品牌类型
        self.server_branch.clear_brands_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set008(self):
        """授权服务品类不能为空"""

        # 获取测试数据
        data = set_server_data["TestCase008"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空选择的授权服务类型
        self.server_branch.clear_kinds_type()
        # 点击保存
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set009(self):
        """服务商授权区域为空校验"""

        # 获取测试数据
        data = set_server_data["TestCase009"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入服务商列表页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空该服务商的地址信息
        self.server_branch.clear_server_address_info()
        self.base_page.sleep(1)
        # 点击保存设置
        self.server_branch.click_save_set_server()
        # 获取系统提示信息
        system_message = self.base_page.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],system_message)

    def test_server_set010(self):
        """设置授权全部类型保存成功校验"""

        # 获取测试数据
        data = set_server_data["TestCase010"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入客户列表
        self.server_branch.enter_customer_list_page()
        # 进入授权设置页面
        self.enter_set_server_page(branch_keyword=data["SetBranch"])
        # 清空合作类型
        self.clear_teamwork_type()
        # 选择派单类型
        self.server_branch.select_teamwork_type_1()
        # 清空选择的授权服务类型
        self.server_branch.clear_server_type()
        self.base_page.sleep(1)
        # 选择其他服务类型
        self.server_branch.select_server_type_of_other(server_name=data["ServerType"])
        # 清空授权品牌
        self.server_branch.clear_brands_type()
        # 重新授权品牌
        self.server_branch.select_brands_type_of_other(brands_name=data["Brands"])
        # 清空授权品类
        self.server_branch.clear_kinds_type()
        self.base_page.sleep(1)
        # 选择品类
        self.server_branch.select_kinds_type_of_other(kinds_name=data["Kinds"])
        # 清空授权区域
        self.server_branch.clear_server_address_info()
        # 选择授权区域
        self.server_branch.select_server_province(province_list=data["Province"])
        # 点击保存
        self.server_branch.click_save_set_server()
        self.base_page.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data["expect"],self.base_page.get_system_msg())

    def test_server_set011(self):
        """不在授权区域的订单不能派单给该服务商"""

        # 获取测试数据
        data = set_server_data["TestCase011"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入订单派单页面
        self.please_order.enter_please_order_page()
        # 选择派单订单
        self.base_page.select_new_order(self.order_number)
        # 点击派单
        self.please_order.click_pleaseOrder_btn()
        self.base_page.sleep(1)
        # 选择派单到服务商
        self.please_order.please_to_branch()
        # 输入网点名称
        self.please_order.input_search_branch_name(branch_name=data["BranchName"])
        # 点击搜索
        self.please_order.click_search_branch()
        self.base_page.sleep(1)
        # 断言-获取服务商是否存在页面的属性 False
        self.assert_mode.assert_el_not_in_page(self.please_order.search_branch_is_display())

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suits = unittest.TestSuite()
    suits.addTest(Server_Set("test_server_set001"))
    suits.addTest(Server_Set("test_server_set002"))
    suits.addTest(Server_Set("test_server_set003"))
    suits.addTest(Server_Set("test_server_set004"))
    suits.addTest(Server_Set("test_server_set005"))
    suits.addTest(Server_Set("test_server_set006"))
    suits.addTest(Server_Set("test_server_set007"))
    suits.addTest(Server_Set("test_server_set008"))
    suits.addTest(Server_Set("test_server_set009"))
    suits.addTest(Server_Set("test_server_set010"))
    suits.addTest(Server_Set("test_server_set011"))

    unittest.TextTestRunner().run(suits)

