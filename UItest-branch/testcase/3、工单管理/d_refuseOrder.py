# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/12/20 17:22

from public.common import rwConfig
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
import unittest,ddt

@ddt.ddt
class Refuse_Order(unittest.TestCase):

    """" 【网点拒单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("refuseOrder")
    # ddt 测试用例列表
    case_list = [
        "refuse_order_001","refuse_order_002"
    ]
    # 获取ddt数据
    ddt_data = read_excel.get_ddt_data(case_list)
    
    @classmethod
    def setUpClass(cls):
        # 实例化页面对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.order_details = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"refuseOrder")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单网点名称
        server_branch = rwConfig.read_config_data("T西安好家帮家政有限公司","branch002")
        # 派单到网点
        cls.send_order.send_order_main(
            cls.orderNumber,pageName=server_branch,sendType="服务商")
        # 退出网点
        cls.login.click_logout_button()
        # 登录服务商
        cls.login.login_main(server_branch)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_refuse_order001(self,ddt_data):
        """拒单功能校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 刷新页面
        self.base.refresh_page()
        # 进入全部工单页面
        self.send_order.enter_send_order_page()
        self.base.sleep(1)
        # 进入工单详情页
        self.create_order.open_order_details(self.orderNumber)
        # 点击拒单
        self.order_details.click_refuse_order_btn()
        # 输入拒单原因
        self.order_details.input_refuse_reason(ddt_data["拒单原因"])
        # 点击提交拒单
        self.order_details.click_confirm_refuse_btn()
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Refuse_Order)

    unittest.TextTestRunner().run(suits)