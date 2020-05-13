# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/18 17:24

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.createGroupPage import CreateGroupPage
from public.page.visitMemberPage import VisitMemberPage
from public.page.editGroupPage import EditGroupPage
import unittest

class Take_Order_Of_Day(unittest.TestCase):

    """ 【圈子接单方日接单量校验】 """

    # 实例化操作类
    readExcel = Read_Excel("takeOrderOfDay")

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.create_group = CreateGroupPage(cls.driver)
        cls.visit_member = VisitMemberPage(cls.driver)
        cls.edit_group = EditGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"takeOrderOfDay")
        # 登录网点
        cls.login.login_main("T西安超级售后有限公司")
        # 进入创建圈子页面
        cls.create_group.enter_my_group_list_page()

    @unittest.skipUnless(readExcel.get_isRun_text("take_order_of_day_001"),"-跳过不执行该用例")
    def test_taker_order_of_day001(self):
        """日接单量-小于日结单量成功接单校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_order_of_day_001")
        # 打印测试用例
        self.base.print_case_name(data)
        # 获取邀请成员数据
        groupName = data["圈子名称"]
        member = data["客户名称"]
        takeCountDay = data["日接单量"]
        brandName = data["服务品牌"]
        serviceArea = data["服务区域"]
        # 邀请新的接单方
        self.visit_member.visit_taker_member_main(
            groupName,member,takeCountDay,brandName,serviceArea)
        # 耍新页面
        self.base.refresh_page()
        # 点击编辑按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        # 设置新邀请的优先级为一级
        self.edit_group.set_take_order_priority(data["客户名称"][0])
        # 点击保存
        self.edit_group.click_save_edit_btn()
        self.base.sleep(2)
        # 登录派单方
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
        self.base.refresh_page()
        # 登录接单方
        self.login.click_logout_button()
        self.login.login_main("T西安瑞晟科技有限公司")
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        # 选择工单
        self.create_order.select_operate_order(self.orderNumber)
        # 接单
        self.send_order.click_take_order()
        self.base.sleep(2)
        # 登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        # 进入订单详情页
        self.create_order.open_order_details(self.orderNumber)
        # 点击过程节点
        self.edit_group.click_process_node_table()
        # 断言
        self.assert_mode.assert_in(data,self.edit_group.get_new_process_node_info())

    @unittest.skipUnless(readExcel.get_isRun_text("take_order_of_day_002"),"-跳过不执行该用例")
    def test_taker_order_of_day002(self):
        """日接单量-大于日接单量不能再次接单校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_order_of_day_002")
        # 打印测试用例
        self.base.print_case_name(data)
        # 耍新页面
        self.base.refresh_page()
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
        self.base.refresh_page()
        # 进入订单详情页
        self.create_order.open_order_details(self.orderNumber)
        # 点击过程节点
        self.edit_group.click_process_node_table()
        # 断言
        self.assert_mode.assert_not_in(data,self.edit_group.get_new_process_node_info())


    @classmethod
    def tearDownClass(cls):
        # 清理缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Take_Order_Of_Day)

    unittest.TextTestRunner().run(suit)