#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/7/3 17:13

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
"""
经销商工单结算测试用例(无预报价):
25、经销商工单结算(无预报价)-未结算服务商端结算价格可以输入校
26、经销商工单结算(无预报价)-经商端设置结算价格可以随便输入校验 27、经销商工单结算(无预报价)-经商端线下结算成功校验
28、经销商工单结算(无预报价)-服务商端经销商结算价格校验 29、经销商工单结算(无预报价)-服务商端1/3结算方式可以选择校验
30、经销商工单结算(无预报价)-服务商端按固定比例结算校验
"""
# 获取数据
SettleData = getdata.get_test_data()["SettleManagePage"]
no_settle_money = SettleData["no_settle_money_flow"]
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
        cls.searchOrder = SearchOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        # 获取定单订单号::新建工单时添加的无需返单订单
        #  cls.OrderNum = rwconfig.read_config_data('NotReturnOrder','id',orderNumPath)
        # 登录网点 蓝魔科技
        cls.Use = rwconfig.read_config_data('蓝魔科技',"username")
        cls.Pwd = rwconfig.read_config_data('蓝魔科技',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        #  经销商下单程序下单
        cls.createOrder.create_not_return_order()
        # 获取工单单号
        cls.OrderNum = cls.base.get_order_number()
        # 订单号写入配置文件，后面财务管理中收入支出使用
        # rwconfig.write_config_data("for_finance_manage_search","id",cls.OrderNum,orderNumPath)
        # 获取派单到服务商数据 关联派单数据中的信息
        BranchName1 = rwconfig.read_config_data('蓝魔科技','branch001')
        # 派单到服务商1-XM-服务撒 //派单到服务商不设置结算预报价
        cls.pleaseOrder.please_order_main(cls.OrderNum,BranchName1,please_to_branch=True,
                                          set_order_money=False)
        # 退出登录
        cls.login.click_logout_button()
        # 获取服务商1账号密码
        cls.Use1 = rwconfig.read_config_data(BranchName1,'username')
        cls.Pwd1 = rwconfig.read_config_data(BranchName1,'password')
        # 登录派单服务商1
        cls.login.login_main(cls.Use1,cls.Pwd1)
        # 获取派单到服务商数据 关联派单数据中的信息
        BranchName2 = rwconfig.read_config_data(BranchName1,'branch001')
        # 派单到服务商2-branch03 //派单到服务商不设置结算预报价
        cls.pleaseOrder.please_order_main(cls.OrderNum,BranchName2,please_to_branch=True,
                                          set_order_money=False)
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

    def public_operation(self):
        """工共操作:: 进入服务商订单结算列表->点击单号进入订单详情->点击结算按钮"""
        # 进入服务撒工单结算列表页面
        self.settleOrder.enter_branch_settle_page()
        # 刷新页面-有时进不去网点结算页面
        self.base.refresh_page()
        self.base.sleep(1)
        # 搜索工单
        self.searchOrder.search_order_by_number(self.OrderNum)
        # 进入工单详情页
        self.base.open_order_message(self.OrderNum)
        # 点击结算按钮
        self.settleOrder.click_settle_btn()

    def test_manage_settle001(self):
        """经销商工单结算(无预报价)-未结算1/3结算方式不能选择校验"""
        # 获取测试数据
        data = no_settle_money["TestCase001"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出服务商2
        self.login.click_logout_button()
        # 登录服务商1
        self.login.login_main(self.Use1,self.Pwd1)
        # 调用工共操作
        self.public_operation()
        self.base.sleep(2)
        # 获取结算方式1、3的选择属性
        settle_type_att1 = self.settleOrder.get_settle_type_1_att()
        settle_type_att3 = self.settleOrder.get_settle_type_3_att()
        # 获取经销商未结算提示进行断言
        self.assert_mode.assert_equal(data["expect"],settle_type_att1)
        self.assert_mode.assert_equal(data["expect"],settle_type_att3)

    def test_manage_settle002(self):
        """经销商工单结算(无预报价)-未结算服务商端结算价格可以输入校验"""
        # 获取测试数据
        data = no_settle_money["TestCase002"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 调用工共操作
        self.public_operation()
        # 获取结算价格框的属性//可以输入
        settle_input_attribute = self.settleOrder.get_settle_money_attribute()
        # 断言
        self.assert_mode.assert_att_is_none(settle_input_attribute)

    def test_manage_settle003(self):
        """经销商工单结算(无预报价)-经商端线下结算成功校验"""
        # 获取测试数据
        data = no_settle_money["TestCase003"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 退出服务商
        self.login.click_logout_button()
        # 登录经销商
        self.login.login_main(self.Use,self.Pwd)
        # 调用工共操作
        self.public_operation()
        # 输入结算价格
        self.settleOrder.input_settle_money(data["SettleMoney"])
        # 获取结算价格框的属性//可以输入
        settle_input_attribute = self.settleOrder.get_settle_money_attribute()
        # 断言
        self.assert_mode.assert_att_is_none(settle_input_attribute)
        self.assert_mode.assert_equal(data["expect"],self.settleOrder.get_settle_money_value())

    def test_manage_settle004(self):
        """经销商工单结算(无预报价)-服务商端经销商结算价格校验"""
        # 获取测试数据
        data = no_settle_money["TestCase004"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 调用工共操作
        self.public_operation()
        # 输入结算金额
        self.settleOrder.input_settle_money(data["expect"])
        # 选择线下结算
        self.settleOrder.select_line_down_pay()
        # 确定支付
        self.settleOrder.click_confirm_pay()
        self.base.sleep(2)
        # 结算完订单详情页没有关闭刷新页面关闭退出登录
        self.base.refresh_page()
        # 退出经销商
        self.login.click_logout_button()
        # 登录服务商1
        self.login.login_main(self.Use1,self.Pwd1)
        # 调用工共操作
        self.public_operation()
        self.base.sleep(2)
        # 获取经销商结算价格
        brands_settle_value = self.settleOrder.get_brands_settle_value_attribute()
        # 断言
        self.assert_mode.assert_equal(data["expect"],brands_settle_value)

    def test_manage_settle005(self):
        """经销商工单结算(无预报价)-服务商端1/2/3结算方式可以选择校验"""
        # 获取测试数据
        data = no_settle_money["TestCase005"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 调用工共操作
        self.public_operation()
        # 判断123种结算方式属性为None
        settle_type_1 = self.settleOrder.get_settle_type_1_att()
        settle_type_2 = self.settleOrder.get_settle_type_2_att()
        settle_type_3 = self.settleOrder.get_settle_type_3_att()
        # 断言为None
        self.assert_mode.assert_att_is_none(settle_type_1)
        self.assert_mode.assert_att_is_none(settle_type_2)
        self.assert_mode.assert_att_is_none(settle_type_3)

    def test_manage_settle006(self):
        """经销商工单结算(无预报价)-服务商端按固定比例60-40结算校验"""
        # 获取测试数据
        data = no_settle_money["TestCase006"]
        # 打印测试用例名称
        self.base.print_case_name(data["CaseName"])
        # 调用工共操作
        self.public_operation()
        # 选择固定比例结算
        self.settleOrder.select_settle_type_3()
        # 滑动比例按钮
        self.settleOrder.sliding_scale_button(data["ArriveNum"])
        # 选择线下结算
        self.settleOrder.select_line_down_pay()
        # 点击支付
        self.settleOrder.click_confirm_pay()
        # 断言
        self.assert_mode.assert_equal(data["expect"],self.base.get_system_msg())

    @classmethod
    def tearDownClass(cls):
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

    unittest.TextTestRunner().run(suit)