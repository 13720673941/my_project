# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/1/15 20:04

from public.common import rwConfig
from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
from public.page.sendOrderPage import SendOrderPage
from public.common import myDecorator
import unittest,ddt

@ddt.ddt
class Appoint_Order(unittest.TestCase):

    """" 【网点预约/改约工单功能测试用例脚本】 """

    # 获取当前日期后一天修改预约判断用
    alter_date = str(datetime.datetime.now().date()+datetime.timedelta(2))
    # 修改时间写入期望值中
    Update_Excel.update_expect_data("appointOrder","appoint_order_003",alter_date)
    # ddt 测试数据用例编号
    case_list = [
        "appoint_order_001","appoint_order_002"
    ]
    # 实例化类
    read_excel = Read_Excel("appointOrder")
    # 读取ddt数据
    ddt_data = read_excel.get_ddt_data(case_list)
    
    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.order_details = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"appointOrder")
        # 登录网点
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建工单
        cls.create_order.create_not_return_order()
        # 获取工单编号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单师傅
        master_name = rwConfig.read_config_data("T西安好家帮家政有限公司","master001")
        # 派单到师傅
        cls.send_order.send_order_main(cls.orderNumber,pageName=master_name)

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 点击订单进入订单详情页
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_appoint_order001(self,ddt_data):
        """订单预约功能测试用例"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 点击预约按钮
        self.order_details.click_appoint_btn()
        """
        预约时间只能是两天之后，默认当前日期不能选择
        """
        # # 输入预约日期
        # self.order_details.input_appoint_date()
        # # 点击空白区
        # self.order_details.click_white_place()
        self.base.sleep(2)
        # 选择预约时间段
        self.order_details.select_appoint_time(ddt_data["预约时间段"])
        # 点击确定按钮
        self.order_details.click_confirm_appoint_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("appoint_order_003"),"-跳过该用例不执行")
    def test_appoint_order002(self):
        """修改预约时间校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("appoint_order_003")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击改约按钮
        self.order_details.click_alter_appoint_btn()
        self.base.sleep(2)
        # 输入预约日期
        self.order_details.input_appoint_date(alter=True)
        # 点击空白区
        # self.order_details.click_white_place()
        # 选择预约时间段
        self.order_details.select_appoint_time(data["预约时间段"])
        # 点击确定按钮
        self.order_details.click_confirm_appoint_btn()
        self.base.sleep(1)
        # 判断修改的预约时间在订单详情页已经改变
        self.assert_mode.assert_in(data,self.order_details.get_appoint_text())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Appoint_Order)

    unittest.TextTestRunner().run(suit)
