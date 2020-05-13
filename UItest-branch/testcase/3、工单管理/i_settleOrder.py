# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/18 9:11

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.page.settleOrderPage import SettleOrderPage
from public.page.marketOrderPage import MarketOrderPage
from public.page.userEvaluatePage import UserEvaluatePage
from public.common.assertMode import Assert
import unittest

class Order_Settle(unittest.TestCase):

    """ 【工单结算功能】 """

    """
        ------ 这里引入设置中的结算设置: 按回访日结算 ------
    """
    # 实例化类
    read_excel = Read_Excel("orderSettle")

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
        cls.market_order = MarketOrderPage(cls.driver)
        cls.user_evaluate = UserEvaluatePage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"orderSettle")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")

    def setUp(self):
        # 创建工单
        self.create_order.create_not_return_order()
        # 获取工单编号
        self.orderNumber = self.create_order.get_order_number()

    @unittest.skipUnless(read_excel.get_isRun_text("order_settle_001"),"-不执行该测试用例")
    def test_order_settle001(self):
        """工单结算-市场单不能线下结算校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("order_settle_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 派单到市场
        self.market_order.send_to_market_main(self.orderNumber,fixedPrice=data["抢单价格"])
        # 退出网点账号
        self.login.click_logout_button()
        # 登录抢单网点
        self.login.login_main("T西安超级售后有限公司")
        # 抢单
        self.market_order.grad_order_main(self.orderNumber)
        self.base.sleep(2)
        # 恢复页面
        self.base.refresh_page()
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        # 获取派单师傅
        masterName = rwConfig.read_config_data("T西安超级售后有限公司","master001")
        # 派单到师傅
        self.send_order.send_order_main(self.orderNumber,pageName=masterName)
        self.base.refresh_page()
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        self.base.refresh_page()
        # 退出网点账号
        self.login.click_logout_button()
        # 登录派单网点
        self.login.login_main("T西安好家帮家政有限公司")
        # 回访订单
        self.visit_order.visit_order_main(self.orderNumber)
        # 进入财务支出页面
        self.settle_order.enter_bill_out_going_url()
        # 点击账单明细按钮
        self.settle_order.click_bill_details_of_orderNumber(self.orderNumber)
        # 点击确认账单
        self.settle_order.click_confirm_bill_btn()
        # 确定
        self.settle_order.click_confirm_bill_confirm_btn()
        self.base.sleep(1)
        # 点击立即结算
        self.settle_order.click_promptly_settle_btn()
        # 断言
        self.assert_mode.assert_equal(data,self.settle_order.get_down_line_att())

    @unittest.skipUnless(read_excel.get_isRun_text("order_settle_002"),"-跳过不执行该用例")
    def test_order_settle002(self):
        """工单结算-钱包不足不能结算校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("order_settle_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取派单师傅名称
        masterName = rwConfig.read_config_data("T西安好家帮家政有限公司","master001")
        # 派单到师傅设置价格
        self.send_order.send_order_main(
            self.orderNumber,pageName=masterName,setOrderMoney=True,setPrice=data["派单价格"])
        # 刷新页面
        self.base.refresh_page()
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        # 回访工单
        self.visit_order.visit_order_main(self.orderNumber)
        # 进入财务支出页面
        self.settle_order.enter_bill_out_going_url()
        # 点击账单明细按钮
        self.settle_order.click_bill_details_of_orderNumber(self.orderNumber)
        # 点击确认账单
        self.settle_order.click_confirm_bill_btn()
        # 确定
        self.settle_order.click_confirm_bill_confirm_btn()
        self.base.sleep(1)
        # 点击立即结算
        self.settle_order.click_promptly_settle_btn()
        # 默认钱包结算点击确认
        self.settle_order.click_confirm_settle_btn()
        # 获取系统提示信息
        system_message = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data,system_message)

    @unittest.skipUnless(read_excel.get_isRun_text("order_settle_003"),"-跳过不执行该用例")
    def test_order_settle003(self):
        """工单结算-成功结算校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("order_settle_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取派单师傅名称
        masterName = rwConfig.read_config_data("T西安好家帮家政有限公司","master001")
        # 派单到师傅设置价格
        self.send_order.send_order_main(
            self.orderNumber,pageName=masterName,setOrderMoney=True,setPrice=data["派单价格"])
        # 刷新页面
        self.base.refresh_page()
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        # 回访工单
        self.visit_order.visit_order_main(self.orderNumber)
        # 进入财务支出页面
        self.settle_order.enter_bill_out_going_url()
        # 点击账单明细按钮
        self.settle_order.click_bill_details_of_orderNumber(self.orderNumber)
        # 点击确认账单
        self.settle_order.click_confirm_bill_btn()
        # 确定
        self.settle_order.click_confirm_bill_confirm_btn()
        self.base.sleep(1)
        # 点击立即结算
        self.settle_order.click_promptly_settle_btn()
        # 选择线下结算
        self.settle_order.select_line_down_settle()
        # 点击确认
        self.settle_order.click_confirm_settle_btn()
        # 等待结算成功
        self.base.sleep(2)
        self.base.refresh_page()
        # 获取账单状态
        billStatus = self.settle_order.get_bill_settle_status()
        # 断言
        self.assert_mode.assert_in(data,billStatus)
        # 写入工单已结算的工单编号无效工单使用
        if billStatus == "已结算":
            rwConfig.write_config_data("for_invalid_and_search","id",self.orderNumber,orderNumPath)

    @unittest.skipUnless(read_excel.get_isRun_text("order_settle_004"),"-跳过不执行该用例")
    def test_order_settle004(self):
        """工单结算-加急费用结算校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("order_settle_004")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 派单到市场
        self.market_order.send_to_market_main(
            self.orderNumber,fixedPrice=data["抢单价格"],emergencyPrice=data["加急费用"])
        # 退出网点账号
        self.login.click_logout_button()
        # 登录抢单网点
        self.login.login_main("T西安超级售后有限公司")
        # 抢单
        self.market_order.grad_order_main(self.orderNumber)
        self.base.sleep(2)
        # 恢复页面
        self.base.refresh_page()
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        # 获取派单师傅
        masterName = rwConfig.read_config_data("T西安超级售后有限公司","master001")
        # 派单到师傅
        self.send_order.send_order_main(self.orderNumber, pageName=masterName)
        self.base.refresh_page()
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        self.base.refresh_page()
        # 退出网点账号
        self.login.click_logout_button()
        # 登录派单网点
        self.login.login_main("T西安好家帮家政有限公司")
        # 回访订单
        self.visit_order.visit_order_main(self.orderNumber,rewardPunish=False)
        # 进入财务支出页面
        self.settle_order.enter_bill_out_going_url()
        # 点击账单明细按钮
        self.settle_order.click_bill_details_of_orderNumber(self.orderNumber)
        # 断言
        self.assert_mode.assert_in(data,self.settle_order.get_bill_reward_first_record())

    @unittest.skipUnless(read_excel.get_isRun_text("order_settle_005"),"-跳过不执行该用例")
    def test_order_settle005(self):
        """工单结算-好评返现结算校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("order_settle_005")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 派单到市场
        self.market_order.send_to_market_main(
            self.orderNumber,fixedPrice=data["抢单价格"],cashBackPrice=data["好评返现"])
        # 退出网点账号
        self.login.click_logout_button()
        # 登录抢单网点
        self.login.login_main("T西安超级售后有限公司")
        # 抢单
        self.market_order.grad_order_main(self.orderNumber)
        self.base.sleep(2)
        # 恢复页面
        self.base.refresh_page()
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        # 获取派单师傅
        masterName = rwConfig.read_config_data("T西安超级售后有限公司", "master001")
        # 派单到师傅
        self.send_order.send_order_main(self.orderNumber, pageName=masterName)
        self.base.refresh_page()
        # 完成服务
        self.finish_order.finish_order_main(self.orderNumber)
        self.base.refresh_page()
        # 退出网点账号
        self.login.click_logout_button()
        # 登录派单网点
        self.login.login_main("T西安好家帮家政有限公司")
        # 用户好评
        self.user_evaluate.user_evaluate_main(self.orderNumber)
        # 切换回原页面
        self.base.switch_to_new_handle()
        # 回访订单
        self.visit_order.visit_order_main(self.orderNumber,rewardPunish=False)
        # 进入财务支出页面
        self.settle_order.enter_bill_out_going_url()
        # 点击账单明细按钮
        self.settle_order.click_bill_details_of_orderNumber(self.orderNumber)
        # 断言
        self.assert_mode.assert_in(data,self.settle_order.get_bill_reward_first_record())


    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Order_Settle)

    unittest.TextTestRunner().run(suit)