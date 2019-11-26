#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/10 18:14

from public.common import rwconfig,mytest
from public.common import driver
from public.common.getdata import get_test_data
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.returnOrderPage import ReturnOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.searchOrderPage import SearchOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest
'''
网点返单结算测试用例：
返单未结算系统提示校验 返单未结算只能选择固定金额校验 厂商结算价格不能编辑校验 厂商未结算提示信息校验
按规则结算结算价格不能编辑校验 按固定金额结算金可以编辑校验 按规则结算比例计算校验 钱包余额不足支付校验
线下成功支付校验 返单结算后系统提示校验 返单结算后结算价格校验 返单结算123结算方式都能选择校验 固定金额线下结算成功校验
'''
# 获取数据
SettleData = get_test_data()["SettleReturnPage"]
before_return_data = SettleData["before_return_settle_fnc"]
return_settle_data = SettleData["return_settle_fnc"]
after_settle_data = SettleData["after_return_settle_fnc"]

class Return_Settle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.base = BasePage(cls.dr)
        cls.login = LoginPage(cls.dr)
        cls.create_order_page = AddOrderPage(cls.dr)
        cls.pleaseOrder = PleaseOrderPage(cls.dr)
        cls.finishOrder = FinishOrder(cls.dr)
        cls.returnOrder = ReturnOrderPage(cls.dr)
        cls.settleOrder = SettleOrderPage(cls.dr)
        cls.search_order = SearchOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        # 登录网点 branch_01
        cls.Use = rwconfig.read_config_data('branch_01',"username")
        cls.Pwd = rwconfig.read_config_data('branch_01',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        #  经销商下单程序下单
        cls.create_order_page.create_return_order()
        cls.base.sleep(2)
        # 获取单号
        cls.OrderNumber = cls.base.get_order_number()
        # 单号写入配置文件后面无效工单使用
        rwconfig.write_config_data('for_invalid_and_search','id',cls.OrderNumber,orderNumPath)
        # 获取派单师傅
        master = rwconfig.read_config_data('branch_01', 'master001')
        # 派单
        cls.pleaseOrder.please_order_main(cls.OrderNumber, master)
        # 完单
        cls.finishOrder.finish_order_main(cls.OrderNumber)

    def setUp(self):
        # 刷新页面时间加载
        self.base.refresh_page()

    def test_return_settle001(self):
        """返单未结算-服务商结算价格提示校验"""
        # 获取测试数据
        data = before_return_data["TestCase001"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入师傅结算工单列表
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 获取未结算提示信息
        msg = self.settleOrder.get_settle_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],msg)

    def test_return_settle002(self):
        """返单未结算-经销商只能选择固定金额结算校验"""
        # 获取测试数据
        data = before_return_data["TestCase002"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入师傅结算工单列表
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()
        # 获取规则结算和固定比例结算方式的禁止选择属性
        settle_type_att1 = self.settleOrder.get_settle_type_1_att()
        settle_type_att2 = self.settleOrder.get_settle_type_1_att()
        # 断言
        self.assert_mode.assert_equal(data["expect"],settle_type_att1)
        self.assert_mode.assert_equal(data["expect"],settle_type_att2)

    def test_return_settle003(self):
        """返单结算-服务商端厂商结算金额不能修改校验"""
        # 获取测试数据
        data = return_settle_data["TestCase001"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 获取返单服务商名称.-修改返单服务商数据中的网点名称关联配置文件中的账号密码
        return_branch_name = rwconfig.read_config_data("ReturnOrder", "服务商", orderInfo)
        # 返单到服务商
        self.returnOrder.return_order_main(self.OrderNumber)
        # 退出经销商登录
        self.login.click_logout_button()
        # 获取配置文件中的账号密码
        self.server_branch_use = rwconfig.read_config_data(return_branch_name,"username")
        self.server_branch_pwd = rwconfig.read_config_data(return_branch_name,"password")
        # 登录服务商：修改返单的服务商中的branchname
        self.login.login_main(self.server_branch_use,self.server_branch_pwd)
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 获取厂商结算价格属性验证不能编辑
        brands_settle_attribute = self.settleOrder.get_brands_settle_money_attribute()
        # 断言
        self.assert_mode.assert_equal(data["expect"],brands_settle_attribute)

    def test_return_settle004(self):
        """返单结算-服务商端厂商未结算提示信息校验"""
        # 获取测试数据
        data = return_settle_data["TestCase002"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 获取红字未结算提示信息
        brands_settle_msg = self.settleOrder.get_settle_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],brands_settle_msg)

    def test_return_settle005(self):
        """返单结算-服务商端按规则结算结算价不能修改校验"""
        # 获取测试数据
        data = return_settle_data["TestCase003"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 获取结算价格属性不能编辑
        settle_attribute = self.settleOrder.get_settle_money_attribute()
        # 断言
        self.assert_mode.assert_equal(data["expect"],settle_attribute)

    def test_return_settle006(self):
        """返单结算-服务商端按固定金额结算结可以修改结算金额校验"""
        # 获取测试数据
        data = return_settle_data["TestCase004"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 选择按固定比例结算
        self.settleOrder.select_settle_type_2()
        # 输入结算价格
        self.settleOrder.input_settle_money(settle_money=data["SettleMoney"])
        self.base.sleep(1)
        # 获取输入价格的value值
        settle_money_value = self.settleOrder.get_settle_money_value()
        # 断言
        self.assert_mode.assert_equal(data["expect"],settle_money_value)

    # def test_return_settle007(self):
    #     """返单结算-按规则结算比例计算校验"""
    #     # 获取测试数据
    #     data = return_settle_data["TestCase005"]
    #     # 打印用例名称
    #     self.base.print_case_name(data["CaseName"])
    #     # 进入代结算工单列表页
    #     self.settleOrder.enter_return_wait_settle()
    #     # 搜索订单
    #     self.search_order.search_order_by_number(self.OrderNumber)
    #     # 进入订单详情页
    #     self.base.open_order_message(self.OrderNumber)
    #     # 点击返单结算
    #     self.settleOrder.click_settle_btn()
    #     self.base.sleep(2)
    #     # 获取返单厂商结算价格
    #     brands_settle_money = int(self.settleOrder.get_brands_settle_value_attribute())
    #     # 获取结算比例
    #     settle_ratio = int(self.settleOrder.get_drop_arrive_text())
    #     # 按比例计算的厂商结算价格支付价格
    #     pay_money = brands_settle_money * (100 - settle_ratio) * 0.01
    #     # 获取最终结算价格. 获取的价格为100.0 不能直接int
    #     finally_settle_money = int(self.settleOrder.get_settle_money_value().split('.')[0])
    #     # 断言
    #     self.assert_mode.assert_equal(pay_money,finally_settle_money)

    def test_return_settle008(self):
        """返单结算-钱包余额不足不能支付校验"""
        # 获取测试数据
        data = return_settle_data["TestCase006"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 选择固定金额结算
        self.settleOrder.select_settle_type_2()
        # 输入结算金额
        self.settleOrder.input_settle_money()
        # 点击确定，默认的为钱包结算
        self.settleOrder.click_confirm_pay()
        # 获取系统提示信息
        msg = self.base.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],msg)

    def test_return_settle009(self):
        """返单结算-线下支付成功校验"""
        # 获取测试数据
        data = return_settle_data["TestCase007"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_return_wait_settle()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击返单结算
        self.settleOrder.click_settle_btn()
        # 选择固定金额结算
        self.settleOrder.select_settle_type_2()
        # 输入结算金额
        self.settleOrder.input_settle_money()
        # 选择线下结算
        self.settleOrder.select_line_down_pay()
        # 点击确定，默认的为钱包结算
        self.settleOrder.click_confirm_pay()
        # 获取系统提示信息
        msg = self.base.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],msg)

    def test_return_settle010(self):
        """返单结算后-经销商端未结算提示信息不显示校验"""
        # 获取测试数据
        data = after_settle_data["TestCase001"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出服务商登录
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.Use,self.Pwd)
        # 进入代结算工单列表页
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        self.base.sleep(1)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算
        self.settleOrder.click_settle_btn()
        # 判断未结算提示信息是否再页面显示
        self.assert_mode.assert_el_not_in_page(self.settleOrder.not_settle_msg_is_display())

    def test_return_settle011(self):
        """返单结算后-经销商端结算价格校验"""
        # 获取测试数据
        data = after_settle_data["TestCase002"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算
        self.settleOrder.click_settle_btn()
        # 获取服务商结算价格
        branch_settle_money = self.settleOrder.get_brands_settle_value_attribute()
        # 判断未结算提示信息是否再页面显示
        self.assert_mode.assert_equal(data["expect"],branch_settle_money)

    def test_return_settle012(self):
        """返单结算后-经销商端123结算方式都可以选择校验"""
        # 获取测试数据
        data = after_settle_data["TestCase003"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入代结算工单列表页
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算
        self.settleOrder.click_settle_btn()
        settle_type_att1 = self.settleOrder.get_settle_type_1_att()
        settle_type_att2 = self.settleOrder.get_settle_type_2_att()
        settle_type_att3 = self.settleOrder.get_settle_type_3_att()
        # 判断未结算提示信息是否再页面显示
        self.assert_mode.assert_att_is_none(settle_type_att1)
        self.assert_mode.assert_att_is_none(settle_type_att2)
        self.assert_mode.assert_att_is_none(settle_type_att3)

    def test_return_settle013(self):
        """经销商师傅结算-线下支付成功校验"""
        # 获取测试数据
        data = after_settle_data["TestCase004"]
        # 打印用例名称
        self.base.print_case_name(data["CaseName"])
        # 进入师傅工单结算页面
        self.settleOrder.enter_master_settle_page()
        # 搜索订单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 进入订单详情页
        self.base.open_order_message(self.OrderNumber)
        # 点击结算
        self.settleOrder.click_settle_btn()
        # 选择固定金额结算
        self.settleOrder.select_settle_type_2()
        # 选择线下结算
        self.settleOrder.select_line_down_pay()
        # 点击确定，默认的为钱包结算
        self.settleOrder.click_confirm_pay()
        # 获取系统提示信息
        msg = self.base.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data["expect"],msg)

    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        cls().base.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    # unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Return_Settle)
    unittest.TextTestRunner().run(suit)