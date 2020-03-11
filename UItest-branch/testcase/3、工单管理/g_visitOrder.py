#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/10 15:44

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.visitOrderPage import VisitOrderPage
from public.common.assertMode import Assert
import unittest

class Visit_Order(unittest.TestCase):

    """" 【网点回访工单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("visitOrder")
    
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
        cls.assert_mode = Assert(cls.driver,"visitOrder")
        # 网点登录
        cls.login.login_main('T西安好家帮家政有限公司')
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        #  获取单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单数据
        master = rwConfig.read_config_data('T西安好家帮家政有限公司','master001')
        # 派单
        cls.send_order.send_order_main(cls.orderNumber,pageName=master)
        # 完成服务
        cls.finish_order.finish_order_main(cls.orderNumber)
        # 进入回访页面
        cls.visit_order.enter_visit_order_page()

    @unittest.skipUnless(read_excel.get_isRun_text("visit_order_001"),"-跳过不执行该用例")
    def test_visitOrder001(self):
        """订单回访功能校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("visit_order_001")
        # 用例名称
        self.base.print_case_name(data)
        # # 刷新页面
        # self.base.refresh_page()
        # self.base.sleep(1)
        # # 搜索订单
        # # 输入工单编号
        # self.search_order.input_order_Nnumber(orderNum=self.OrderNumber)
        # # 点击搜索
        # self.search_order.click_search_btn()
        # 选择完成的工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击回访
        self.visit_order.click_visit_btn()
        # 选择服务态度
        self.visit_order.select_server_status(data["服务态度"])
        # 选择安全评价
        self.visit_order.select_safety_assess(data["安全评价"])
        # 输入回访总额
        self.visit_order.input_visit_money()
        # 选择回访结果
        self.visit_order.select_visit_result(data["回访结果"])
        # 输入回访反馈
        self.visit_order.input_visit_remark()
        # 选择奖惩
        self.visit_order.select_reward_punish(data["订单奖惩"])
        # 输入奖惩金额
        self.visit_order.input_reward_punish_money(data["金额"])
        # 输入奖惩备注
        self.visit_order.input_reward_punish_remark()
        # 点击提交按钮
        self.visit_order.click_confirm_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Visit_Order)

    unittest.TextTestRunner().run(suit)