# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/16 16:32

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
import unittest

class Prompt_Order(unittest.TestCase):

    """" 【催单工单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("promptOrder")

    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.order_details = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "promptOrder")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取网点下的师傅名称
        master = rwConfig.read_config_data("T西安好家帮家政有限公司","master001")
        # 派单到师傅
        cls.send_order.send_order_main(cls.orderNumber,pageName=master)

    def setUp(self):
        # 刷新
        self.base.refresh_page()
        # 进入订单列表页
        self.send_order.enter_send_order_page()
        # 进入订单详情
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)

    @unittest.skipUnless(read_excel.get_isRun_text("prompt_order_001"),"-跳过不执行该用例")
    def test_prompt_order001(self):
        """派单到师傅催单为空校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("prompt_order_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击催单按钮
        self.order_details.click_cui_order_btn()
        # 点击确定
        self.order_details.click_confirm_cui_order()
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("prompt_order_002"),"-跳过不执行该用例")
    def test_prompt_order002(self):
        """派单到师傅催单成功校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("prompt_order_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击催单按钮
        self.order_details.click_cui_order_btn()
        # 输入催单备注
        self.order_details.input_cui_of_reason(data["催单原因"])
        # 点击确定
        self.order_details.click_confirm_cui_order()
        self.base.sleep(2)
        self.base.refresh_page()
        # 进入无效工单页面
        self.order_details.enter_prompt_list_page()
        # 判断订单是否存在催单工单列表中返回True/False
        isDisplay = self.create_order.assert_order_in_list(self.orderNumber)
        # 断言
        self.assert_mode.assert_el_in_page(data,isDisplay)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Prompt_Order)

    unittest.TextTestRunner().run(suit)