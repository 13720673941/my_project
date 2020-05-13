# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/19 11:54

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.createGroupPage import CreateGroupPage
from public.page.groupSearchPage import GroupSearchPage
from public.page.visitMemberPage import VisitMemberPage
from public.page.editGroupPage import EditGroupPage
import unittest

class Group_Send_Order_Way(unittest.TestCase):

    """ 【圈子四种派单方式校验】 """

    # 实例化操作类
    readExcel = Read_Excel("sendOrderWay")

    def setUp(self):
        # 实例化对象类
        self.driver = web_driver()
        self.base = BasePage(self.driver)
        self.login = LoginPage(self.driver)
        self.create_order = CreateOrderPage(self.driver)
        self.send_order = SendOrderPage(self.driver)
        self.search_order = SearchOrderPage(self.driver)
        self.create_group = CreateGroupPage(self.driver)
        self.group_search = GroupSearchPage(self.driver)
        self.visit_member = VisitMemberPage(self.driver)
        self.edit_group = EditGroupPage(self.driver)
        self.assert_mode = Assert(self.driver,"sendOrderWay")
        # 登录群主网点
        self.login.login_main("T西安超级售后有限公司")

    def set_send_way(self,data):
        """设置派单方式"""

        # 进入圈子列表页面
        self.create_group.enter_my_group_list_page()
        # 点击编辑按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        self.base.sleep(2)
        # 选择派单方式
        self.create_group.select_send_order_way(data["派单方式"])
        # 点击保存
        self.edit_group.click_save_edit_btn()
        self.base.sleep(1)

    @unittest.skipUnless(readExcel.get_dict_data("send_order_way_001"),"-跳过不执行该用例")
    def test_send_order_way001(self):
        """派单方式-派单方自主派单方式选择校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_way_001")
        # 打印测试用例
        self.base.print_case_name(data)
        # 选择派单方式
        self.set_send_way(data)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 选择订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单
        self.send_order.click_send_order_btn()
        # 选择派单圈子
        self.send_order.select_send_type(data["派单类型"])
        # 选择派单对象
        self.send_order.select_send_page(
            pageName=data["接单成员"],groupOrder=True,groupName=data["圈子名称"])
        # 输入派单价格
        self.send_order.set_order_money(data["派单价格"])
        # 点击派单
        self.send_order.click_confirm_btn()
        self.base.sleep(1)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安乐家家政")
        # 进入全部工单页面
        self.search_order.enter_search_order_page()
        # 断言判断订单是否在列表中
        self.assert_mode.assert_el_in_page(data,self.create_order.assert_order_in_list(self.orderNumber))

    @unittest.skipUnless(readExcel.get_dict_data("send_order_way_002"),"-跳过不执行该用例")
    def test_send_order_way002(self):
        """派单方式-自动派单方式选择校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_way_002")
        # 打印测试用例
        self.base.print_case_name(data)
        # 选择派单方式
        self.set_send_way(data)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 派单到圈子
        self.send_order.send_order_main(
            self.orderNumber, pageName=data["圈子名称"], sendType=data["派单类型"],
            setOrderMoney=True, setPrice=data["派单价格"]
        )
        self.base.sleep(1)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安乐家家政")
        # 进入全部工单页面
        self.search_order.enter_search_order_page()
        # 断言判断订单是否在列表中
        self.assert_mode.assert_el_in_page(data,self.create_order.assert_order_in_list(self.orderNumber))

    @unittest.skipUnless(readExcel.get_dict_data("send_order_way_003"),"-跳过不执行该用例")
    def test_send_order_way003(self):
        """派单方式-群内抢单方式选择校验验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_way_003")
        # 打印测试用例
        self.base.print_case_name(data)
        # 选择派单方式
        self.set_send_way(data)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 派单到圈子
        self.send_order.send_order_main(
            self.orderNumber, pageName=data["圈子名称"], sendType=data["派单类型"],
            setOrderMoney=True, setPrice=data["派单价格"]
        )
        self.base.sleep(1)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安乐家家政")
        # 进入圈子抢单页面
        self.edit_group.enter_group_order_market_page()
        # 断言判断订单是否在列表中
        self.assert_mode.assert_el_in_page(data,self.create_order.assert_order_in_list(self.orderNumber))

    @unittest.skipUnless(readExcel.get_dict_data("send_order_way_004"),"-跳过不执行该用例")
    def test_send_order_way004(self):
        """派单方式-群主派单方式选择校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("send_order_way_004")
        # 打印测试用例
        self.base.print_case_name(data)
        # 选择派单方式
        self.set_send_way(data)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 派单到圈子
        self.send_order.send_order_main(
            self.orderNumber, pageName=data["圈子名称"], sendType=data["派单类型"],
            setOrderMoney=True, setPrice=data["派单价格"]
        )
        self.base.sleep(1)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安超级售后有限公司")
        # 进入全部工单页面
        self.search_order.enter_search_order_page()
        # 断言判断订单是否在列表中
        self.assert_mode.assert_el_in_page(data,self.create_order.assert_order_in_list(self.orderNumber))

    def tearDown(self):
        # 清除缓存
        self.base.clear_catch()
        # 退出浏览器
        self.base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Group_Send_Order_Way)

    unittest.TextTestRunner().run(suit)