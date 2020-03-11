# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/17 21:25

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
class Server_Feedback(unittest.TestCase):

    """" 【工单服务反馈功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("serverFeedback")
    # ddt数据用例编号集合
    case_list = [
        "feedback_001","feedback_002"
    ]
    # 获取ddt测试数据
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
        cls.assert_mode = Assert(cls.driver, "serverFeedback")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单服务商
        cls.serverBranch = rwConfig.read_config_data("T西安好家帮家政有限公司","branch001")
        # 派单到服务商
        cls.send_order.send_order_main(cls.orderNumber,pageName=cls.serverBranch,sendType="服务商")

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_feedback_001(self,ddt_data):
        """添加服务反馈功能校验"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        self.base.refresh_page()
        # 进入全部工单列表页面
        self.send_order.enter_send_order_page()
        self.base.sleep(1)
        # 进入工单详情页
        self.create_order.open_order_details(self.orderNumber)
        # 点击反馈按钮
        self.order_details.click_feedback_btn()
        # 输入反馈内容
        self.order_details.input_feedback_message(ddt_data["反馈内容"])
        # 点击确定反馈
        self.order_details.click_confirm_feedback()
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("feedback_003"),"-跳过不执行该用例")
    def test_feedback_002(self):
        """添加反馈后服务商可以看到内容校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("feedback_003")
        # 打印测试名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 退出登录
        self.login.click_logout_button()
        # 登录服务商
        self.login.login_main(self.serverBranch)
        # 进入全部工单列表页面
        self.send_order.enter_send_order_page()
        # 点击订单进入详情页
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)
        # 断言
        self.assert_mode.assert_in(data,self.order_details.get_feedback_message())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Server_Feedback)
    unittest.TextTestRunner().run(suit)

