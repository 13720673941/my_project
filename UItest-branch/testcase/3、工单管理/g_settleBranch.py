#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/15 10:42

from public.common import mytest,rwconfig
from public.common import driver,getdata
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.settleOrderPage import SettleOrderPage
from public.page.searchOrderPage import SearchOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest
'''
经销商工单结算测试用例(有预报价)：
14、经销商工单结算(有预报价)-未结算提示信息校验 15、经销商工单结算(有预报价)-未结算1/3结算方式不能选择校验 
16、经销商工单结算(有预报价)-未结算服务商端设置的结算预报价不能修改校验 17、经销商工单结算(有预报价)-经商端设置结算价格不能修改校验
18、经销商工单结算(有预报价)-经商端钱包结算余额不足校验 19、经销商工单结算(有预报价)-经商端线下结算成功校验 
20、经销商工单结算(有预报价)-结算后服务商端提示信息校 21、经销商工单结算(有预报价)-结算后服务商端1/3结算方式不能选择校验
22、经销商工单结算(有预报价)-结算后服务商端设置的结算预报价不能修改校验 23、经销商工单结算(有预报价)-结算后服务商端固定金额线下结算成功校验
24、经销商工单结算(无预报价)-未结算1/3结算方式不能选择校验 25、经销商工单结算(有预报价)-结算后服务商端显示的经销商结算金额校验
'''
# 获取数据
SettleData = getdata.get_test_data()["SettleManagePage"]
have_settle_money = SettleData["have_settle_money_flow"]

class Manage_Settle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.base = BasePage(cls.dr)
        cls.login = LoginPage(cls.dr)
        cls.createOrder = AddOrderPage(cls.dr)
        cls.pleaseOrder = PleaseOrderPage(cls.dr)
        cls.finishOrder = FinishOrder(cls.dr)
        cls.settleOrder = SettleOrderPage(cls.dr)
        cls.search_order = SearchOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        # 登录网点 蓝魔科技
        cls.Use = rwconfig.read_config_data('蓝魔科技',"username")
        cls.Pwd = rwconfig.read_config_data('蓝魔科技',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        # 新建工单-获取订单信息
        user = rwconfig.read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = rwconfig.read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = rwconfig.read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = rwconfig.read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = rwconfig.read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = rwconfig.read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = rwconfig.read_config_data("NotReturnOrder", "品牌", orderInfo)
        kinds = rwconfig.read_config_data("NotReturnOrder", "品类", orderInfo)
        # 经销商下单程序下单
        cls.createOrder.create_order_main(user, phe, address, collage, order_type, server, brands, kinds)
        # 获取工单单号
        cls.OrderNum = cls.base.get_order_number()
        # 获取派单到服务商数据 关联派单数据中的信息
        BranchName1 = rwconfig.read_config_data('蓝魔科技','branch001')
        # 派单到服务商1-自动化测试网点01
        cls.pleaseOrder.please_order_main(cls.OrderNum,BranchName1,please_to_branch=True)
        # 退出登录
        cls.login.click_logout_button()
        # 获取服务商1账号密码
        cls.Use1 = rwconfig.read_config_data(BranchName1,'username')
        cls.Pwd1 = rwconfig.read_config_data(BranchName1,'password')
        # 登录派单服务商1
        cls.login.login_main(cls.Use1,cls.Pwd1)
        # 获取派单到服务商数据 关联派单数据中的信息
        BranchName2 = rwconfig.read_config_data(BranchName1,'branch001')
        # 派单到服务商2-自动化测试网点02
        cls.pleaseOrder.please_order_main(cls.OrderNum,BranchName2,please_to_branch=True)
        # 退出登录
        cls.login.click_logout_button()
        # 获取服务商2账号密码
        cls.Use2 = rwconfig.read_config_data(BranchName2,'username')
        cls.Pwd2 = rwconfig.read_config_data(BranchName2,'password')
        # 登录派单服务商2
        cls.login.login_main(cls.Use2, cls.Pwd2)
        # 获取派单师傅
        MasterName = rwconfig.read_config_data(BranchName2,'master001')
        # 服务商派单到师傅
        cls.pleaseOrder.please_order_main(cls.OrderNum,MasterName)
        # 网点完成服务
        cls.finishOrder.finish_order_main(cls.OrderNum)
        # 进入全部订单列表页
        cls.pleaseOrder.enter_please_order_page()

    def setUp(self):
        # 刷新页面时间加载
        self.base.refresh_page()

    def test_manage_settle001(self):
        """经销商工单结算(有预报价)-未结算提示信息校验"""
        # 获取测试数据
        data = have_settle_money["TestCase001"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出登录
        self.login.click_logout_button()
        # 登录服务商1
        self.login.login_main(self.Use1,self.Pwd1)
        # 进入服务撒工单结算列表页面
        self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],self.settleOrder.get_settle_msg())

    def test_manage_settle002(self):
        """经销商工单结算(有预报价)-未结算1/3结算方式不能选择校验"""
        # 获取测试数据
        data = have_settle_money["TestCase002"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(2)
        # 获取结算方式1、3的选择属性
        settle_type_att1 = self.settleOrder.get_settle_type_1_att()
        settle_type_att2 = self.settleOrder.get_settle_type_3_att()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_type_att1)
        self.assert_mode.assert_equal(data["expect"],settle_type_att2)

    def test_manage_settle003(self):
        """经销商工单结算(有预报价)-未结算服务商端设置的结算预报价不能修改校验"""
        # 获取测试数据
        data = have_settle_money["TestCase003"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(2)
        # 获取固定结算金额不能编辑的属性
        settle_money_attribute = self.settleOrder.get_settle_money_attribute()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_money_attribute)

    def test_manage_settle004(self):
        """经销商工单结算(有预报价)-经商端设置结算价格不能修改校验"""
        # 获取测试数据
        data = have_settle_money["TestCase004"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.Use,self.Pwd)
        # 进入服务撒工单结算列表页面
        self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 获取经销商结算金额属性不能编辑
        settle_money_attribute = self.settleOrder.get_settle_money_attribute()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_money_attribute)

    def test_manage_settle005(self):
        """经销商工单结算(有预报价)-经商端钱包结算余额不足校验"""
        # 获取测试数据
        data = have_settle_money["TestCase005"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 选择钱包支付
        self.settleOrder.select_wallet_pay()
        # 点击确定结算
        self.settleOrder.click_confirm_pay()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],self.base.get_system_msg())

    def test_manage_settle006(self):
        """经销商工单结算(有预报价)-经商端线下结算成功校验"""
        # 获取测试数据
        data = have_settle_money["TestCase006"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 选择线下支付
        self.settleOrder.select_line_down_pay()
        # 点击确定结算
        self.settleOrder.click_confirm_pay()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],self.base.get_system_msg())

    def test_manage_settle007(self):
        """经销商工单结算(有预报价)-结算后服务商端提示信息校验"""
        # 获取测试数据
        data = have_settle_money["TestCase007"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出经销商登录
        self.login.click_logout_button()
        # 登录服务商1
        self.login.login_main(self.Use1,self.Pwd1)
        # 进入服务撒工单结算列表页面
        self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_el_not_in_page(self.settleOrder.get_settle_msg())

    def test_manage_settle008(self):
        """经销商工单结算(有预报价)-结算后服务商端显示的经销商结算金额校验"""
        # 获取测试数据
        data = have_settle_money["TestCase008"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(2)
        # 获取上级结算价格
        brands_settle_money = self.settleOrder.get_brands_settle_value_attribute()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],brands_settle_money)

    def test_manage_settle009(self):
        """经销商工单结算(有预报价)-结算后服务商端1/3结算方式不能选择校验"""
        # 获取测试数据
        data = have_settle_money["TestCase009"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        # 获取结算方式1、3的选择属性
        settle_type_att1 = self.settleOrder.get_settle_type_1_att()
        settle_type_att2 = self.settleOrder.get_settle_type_3_att()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_type_att1)
        self.assert_mode.assert_equal(data["expect"],settle_type_att2)

    def test_manage_settle010(self):
        """经销商工单结算(有预报价)-结算后服务商端设置的结算预报价不能修改100校验"""
        # 获取测试数据
        data = have_settle_money["TestCase010"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        self.base.sleep(1)
        # 获取固定结算金额不能编辑的属性
        settle_money_attribute = self.settleOrder.get_settle_money_attribute()
        # 获取结算金额
        set_money = self.settleOrder.get_settle_money_value()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_money_attribute)
        self.assert_mode.assert_equal(data["expect1"],set_money)

    def test_manage_settle011(self):
        """经销商工单结算(有预报价)-服务商端线下结算成功校验"""
        # 获取测试数据
        data = have_settle_money["TestCase011"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # # 进入服务撒工单结算列表页面
        # self.settleOrder.enter_branch_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 选择线下支付
        self.settleOrder.select_line_down_pay()
        # 点击确定结算
        self.settleOrder.click_confirm_pay()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],self.base.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls.base.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Manage_Settle("test_manage_settle001"))
    suit.addTest(Manage_Settle("test_manage_settle002"))
    suit.addTest(Manage_Settle("test_manage_settle003"))
    suit.addTest(Manage_Settle("test_manage_settle004"))
    suit.addTest(Manage_Settle("test_manage_settle005"))
    suit.addTest(Manage_Settle("test_manage_settle006"))
    suit.addTest(Manage_Settle("test_manage_settle007"))
    suit.addTest(Manage_Settle("test_manage_settle008"))
    suit.addTest(Manage_Settle("test_manage_settle009"))
    suit.addTest(Manage_Settle("test_manage_settle010"))
    suit.addTest(Manage_Settle("test_manage_settle011"))
    unittest.TextTestRunner().run(suit)


