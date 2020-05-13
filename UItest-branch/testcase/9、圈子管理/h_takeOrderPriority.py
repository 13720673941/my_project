# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/19 11:17

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.createGroupPage import CreateGroupPage
from public.page.editGroupPage import EditGroupPage
import unittest

class Take_Order_Priority (unittest.TestCase):

    """ 【圈子接单方优先级设置校验】 """

    # 实例化操作类
    readExcel = Read_Excel("takeOrderPriority")

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.create_group = CreateGroupPage(cls.driver)
        cls.edit_group = EditGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"takeOrderPriority")
        # 登录网点
        cls.login.login_main("T西安超级售后有限公司")
        # 进入创建圈子页面
        cls.create_group.enter_my_group_list_page()

    @unittest.skipUnless(readExcel.get_dict_data("take_order_priority_001"),"-跳过不执行该用例")
    def test_take_order_priority(self):
        """接单优先级-设置圈子接单优先级校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_order_priority_001")
        # 打印测试用例
        self.base.print_case_name(data)
        # 点击编辑圈子按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        self.base.sleep(1)
        # 优先级的前提是自动派单
        self.create_group.select_send_order_way(data["派单方式"])
        # 设置接单成员优先级
        self.edit_group.set_take_order_priority(data["接单成员"])
        # 保存设置
        self.edit_group.click_save_edit_btn()
        self.base.sleep(1)
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
        # 刷新页面
        self.base.refresh_page()
        self.base.sleep(1)
        # 进入订单详情页
        self.create_order.open_order_details(self.orderNumber)
        # 点击过程节点
        self.edit_group.click_process_node_table()
        # 断言
        self.assert_mode.assert_in(data, self.edit_group.get_new_process_node_info())

    @classmethod
    def tearDownClass(cls):
        # 清理缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Take_Order_Priority)

    unittest.TextTestRunner().run(suit)
