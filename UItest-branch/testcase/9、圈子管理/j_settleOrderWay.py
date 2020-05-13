# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/19 15:44

from public.common.driver import web_driver
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.myWalletPage import MyWalletPage
from public.page.createGroupPage import CreateGroupPage
from public.page.editGroupPage import EditGroupPage
import unittest,ddt

@ddt.ddt
class Group_Settle_Order_Way(unittest.TestCase):

    """ 【圈子结算方式设置校验】 """

    # 实例化操作类
    readExcel = Read_Excel("settleOrderWay")
    # 获取测试用例集合
    ddt_data = readExcel.get_ddt_data(["settle_order_way_001","settle_order_way_002"])

    def setUp(self):
        # 实例化对象类
        self.driver = web_driver()
        self.base = BasePage(self.driver)
        self.login = LoginPage(self.driver)
        self.create_order = CreateOrderPage(self.driver)
        self.send_order = SendOrderPage(self.driver)
        self.wallet = MyWalletPage(self.driver)
        self.create_group = CreateGroupPage(self.driver)
        self.edit_group = EditGroupPage(self.driver)
        self.assert_mode = Assert(self.driver,"settleOrderWay")
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
        # 选择结算方式
        self.create_group.select_settle_way(data["结算方式"])
        # 点击保存
        self.edit_group.click_save_edit_btn()
        self.base.sleep(1)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_settle_order_way001(self,ddt_data):
        """结算方式-无需预支付平台校验"""

        # 打印测试用例
        self.base.print_case_name(ddt_data)
        # 选择派单方式
        self.set_send_way(ddt_data)
        # 退出群主登录派单方
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 刷新页面
        self.base.refresh_page()
        # 进入我的钱包页面
        self.wallet.enter_my_wallet_page()
        # 获取我的钱包冻结金额
        beforeNotUseMoney = self.wallet.get_my_not_use_balance_number()
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 派单到圈子
        self.send_order.send_order_main(
            self.orderNumber, pageName=ddt_data["圈子名称"], sendType=ddt_data["派单类型"],
            setOrderMoney=True, setPrice=ddt_data["派单价格"]
        )
        self.base.sleep(2)
        # 进入我的钱包页面
        self.wallet.enter_my_wallet_page()
        # 获取我的钱包冻结金额
        afterNotUseMoney = self.wallet.get_my_not_use_balance_number()
        # 断言 无需预支付的金额不变
        self.assert_mode.assert_equal(ddt_data,str(format((afterNotUseMoney-beforeNotUseMoney),".2f")))

    def tearDown(self):
        # 清除缓存
        self.base.clear_catch()
        # 退出浏览器
        self.base.quit_browser()


if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Group_Settle_Order_Way)

    unittest.TextTestRunner().run(suit)