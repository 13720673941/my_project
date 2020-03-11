#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/3 10:24

from public.common import myDecorator
from public.common import rwConfig
from public.common.operateExcel import Read_Excel
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
import unittest,ddt

@ddt.ddt
class Send_Order(unittest.TestCase):

    """" 【网点派单/转派工单功能测试用例脚本】 """

    # 获取派单/转派ddt测试数据的用例id
    case_id_list1 = [
        "send_order_002","send_order_003","send_order_004",
        "send_order_005","send_order_006","send_order_007",
        "send_order_008","send_order_009","send_order_010",
        "send_order_011","send_order_012"
    ]
    # 获取派单页面搜索功能ddt测试数据的用例id
    case_id_list2 = [
        "send_order_013","send_order_014"
    ]
    # 实例化操作类
    read_excel = Read_Excel("sendOrder")
    # 获取ddt类型测试数据集合
    ddt_data1 = read_excel.get_ddt_data(case_id_list1)
    ddt_data2 = read_excel.get_ddt_data(case_id_list2)

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"sendOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        # 创建订单
        cls.create_order.create_return_order()
        # 获取单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 进入派单页面
        cls.send_order.enter_send_order_page()

    @unittest.skipUnless(read_excel.get_isRun_text("send_order_001"),"-跳过不执行该用例")
    def test_send_order001(self):
        """选择订单为空时派单校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("send_order_001")
        # 点击派单按钮不选择订单
        self.base.print_case_name(data)
        self.base.refresh_page()
        # 点击派单按钮
        self.send_order.click_send_order_btn()
        # 获取系统提示信息
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @ddt.data(*ddt_data1)
    @myDecorator.skipped_case # 跳过ddt数据中不执行的测试用例
    def test_send_order002(self,ddt_data1):
        """派单到网点测试用例"""

        # 刷新页面
        self.base.refresh_page()
        # 选择新建订单
        self.base.print_case_name(ddt_data1)
        # 选择派单订单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单按钮
        self.send_order.click_send_order_btn()
        # 切换服务商
        self.send_order.select_send_type(ddt_data1["派单类型"])
        # 选择派单服务商
        self.send_order.select_send_page(ddt_data1["派单对象"])
        # 点击派单按钮
        self.send_order.click_confirm_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(ddt_data1,self.login.get_system_msg())

    @ddt.data(*ddt_data2)
    @myDecorator.skipped_case
    def test_send_order003(self,ddt_data2):
        """网点派单页面搜索师傅/网点测试"""

        # 刷新页面
        self.base.refresh_page()
        # 选择新建订单
        self.base.print_case_name(ddt_data2)
        self.create_order.select_operate_order(self.orderNumber)
        # 点击派单按钮
        self.send_order.click_send_order_btn()
        # 输入师傅信息
        self.send_order.input_search_name(ddt_data2["搜索对象"])
        # 点击搜索
        self.send_order.click_search_btn()
        # 时间等待
        self.base.sleep(1)
        # 获取师傅名称
        search_result = self.send_order.get_search_name()
        # 断言
        self.assert_mode.assert_in(ddt_data2,search_result)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Send_Order)

    unittest.TextTestRunner().run(suit)







