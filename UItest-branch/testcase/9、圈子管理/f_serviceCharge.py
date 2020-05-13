# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/17 14:42

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common import myDecorator
from public.common.rwConfig import read_config_data
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.createGroupPage import CreateGroupPage
from public.page.groupSearchPage import GroupSearchPage
from public.page.visitMemberPage import VisitMemberPage
from public.page.editGroupPage import EditGroupPage
import unittest,ddt

@ddt.ddt
class Service_Charge(unittest.TestCase):

    """ 【圈子收取服务费校验：起收单数/金额/比例/免费】 """

    # 实例化操作类
    readExcel = Read_Excel("serviceCharge")
    # ddt测试用例编号集合
    caseList = [
        "service_charge_001","service_charge_002","service_charge_003",
        "service_charge_004","service_charge_005"
    ]
    ddt_data = readExcel.get_ddt_data(caseList)

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.visit_order = VisitOrderPage(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.create_group = CreateGroupPage(cls.driver)
        cls.group_search = GroupSearchPage(cls.driver)
        cls.visit_member = VisitMemberPage(cls.driver)
        cls.edit_group = EditGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"serviceCharge")
        # 登录网点
        cls.login.login_main("T西安超级售后有限公司")

    def before_operate(self,data):
        # ---前置条件设置圈子收费信息---
        # 点击圈子编辑按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        # 选择收费设置
        self.create_group.select_charge_rule(data["收费规则"])
        # 设置起收单数
        self.create_group.input_start_charge_count(data["起收单数"])
        # 选择收费模式
        self.create_group.select_charge_mode(data["收费模式"])
        # 输入起手单数
        self.create_group.input_start_charge_count(data["起收单数"])
        # 输入费用金额
        self.create_group.input_charge_amount(data["金额比例"])
        # 选择派单方式
        self.create_group.select_send_order_way(data["派单方式"])
        # 点击保存
        self.edit_group.click_save_edit_btn()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_service_charge001(self,ddt_data):
        """服务费管理-按金额/比例/免费收取服务费金额校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 进入我的圈子列表页
        self.group_search.enter_my_group_list_page()
        self.base.refresh_page()
        # ---前置条件设置圈子收费信息---
        self.before_operate(ddt_data)
        self.base.sleep(2)
        # 进入圈子详情页
        self.visit_member.enter_group_details(ddt_data["圈子名称"])
        # 获取当前圈子的总费用
        beforeAllCharge = self.edit_group.get_already_take_charge()
        self.base.refresh_page()
        # 登录派单网点
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()
        # 派单到圈子
        self.send_order.send_order_main(
            self.orderNumber,pageName=ddt_data["圈子名称"],sendType=ddt_data["派单类型"],
            setOrderMoney=True,setPrice=ddt_data["派单价格"]
        )
        self.base.sleep(1)
        self.base.refresh_page()
        # 登录接单网点
        self.login.click_logout_button()
        self.login.login_main("T西安乐家家政")
        # 获取该网点的师傅
        master = read_config_data("T西安乐家家政","master001")
        # 派单给师傅
        self.send_order.send_order_main(self.orderNumber,pageName=master,takeOrder=True)
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        self.base.refresh_page()
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 回访订单
        self.visit_order.visit_order_main(self.orderNumber)
        # 结算订单
        self.settle_order.settle_order_main(self.orderNumber,walletSettle=True)
        # 登录圈主网点
        self.login.click_logout_button()
        self.login.login_main("T西安超级售后有限公司")
        # 进入我的圈子列表页
        self.group_search.enter_my_group_list_page()
        # 进入圈子详情页
        self.visit_member.enter_group_details(ddt_data["圈子名称"])
        # 获取当前圈子的总费用
        afterAllCharge = self.edit_group.get_already_take_charge()
        # 断言
        self.assert_mode.assert_in(ddt_data,str(format((afterAllCharge-beforeAllCharge),".2f")))

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Service_Charge)

    unittest.TextTestRunner().run(suits)
