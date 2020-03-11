#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/12 16:31

from public.common import rwConfig
from public.common import myDecorator
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.returnOrderPage import ReturnOrderPage
from public.common.assertMode import Assert
import unittest,ddt

@ddt.ddt
class Return_Order(unittest.TestCase):

    """" 【代结工单返单功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("returnOrder")
    # ddt数据用例编号列表
    case_list = [
        "return_order_001","return_order_002"
    ]
    ddt_data = read_excel.get_ddt_data(case_list)
    
    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.return_order = ReturnOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver, "returnOrder")
        # 网点登录
        cls.login.login_main('T西安好家帮家政有限公司')
        # 经销商下单程序下单
        cls.create_order.create_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单师傅
        master = rwConfig.read_config_data('T西安好家帮家政有限公司','master001')
        # 派单
        cls.send_order.send_order_main(cls.orderNumber,pageName=master)
        # 完单
        cls.finish_order.finish_order_main(cls.orderNumber)

    def setUp(self):
        # 进入待返单页面
        self.return_order.enter_return_order_page()

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_returnOrder001(self,ddt_data):
        """修改返单服务商功能测试用例"""

        # 刷新页面
        self.base.print_case_name(ddt_data)
        self.base.refresh_page()
        # 选择返单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击修改返单服务商
        self.return_order.click_alter_return_branch()
        self.base.sleep(1)
        # 选择服务商
        self.return_order.select_branch_name(ddt_data["服务商"])
        # 点击确定
        self.return_order.click_confirm_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("return_order_003"),"-不执行该测试用例")
    def test_returnOrder002(self):
        """网点成功返单校验"""

        # 获取用例数据
        data = self.read_excel.get_dict_data("return_order_003")
        # 刷新页面
        self.base.print_case_name(data)
        self.base.refresh_page()
        # 选择返单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击返单按钮
        self.return_order.click_return_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("return_order_004"),"-不执行该测试用例")
    def test_returnOrder003(self):
        """撤销返单校验"""

        # 进入撤销返单页面
        self.return_order.enter_finish_return_page()
        # 获取用例数据
        data = self.read_excel.get_dict_data("return_order_004")
        # 刷新页面
        self.base.print_case_name(data)
        self.base.refresh_page()
        # 选择返单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击撤销返单按钮
        self.return_order.click_del_return()
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
    unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Return_Order)
    unittest.TextTestRunner().run(suit)