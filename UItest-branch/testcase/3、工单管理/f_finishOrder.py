#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/5 18:07

from public.common import myDecorator
from public.common import rwConfig
from public.common.operateExcel import *
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.finishOrderPage import FinishOrder
from public.common.assertMode import Assert
import unittest,ddt

@ddt.ddt
class Finish_Order(unittest.TestCase):

    """" 【网点完成服务功能测试用例脚本】 """

    # 实例化类
    read_excel = Read_Excel("finishOrder")
    # 设置ddt测试数据用例编号集合
    case_list = [
        "finish_order_001","finish_order_002","finish_order_003",
        "finish_order_004"
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
        cls.finish_order = FinishOrder(cls.driver)
        cls.assert_mode = Assert(cls.driver,"finishOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        #  获取单号
        cls.orderNumber = cls.create_order.get_order_number()
        # 获取派单数据
        master = rwConfig.read_config_data('T西安好家帮家政有限公司','master001')
        # 进入派单页面
        cls.send_order.enter_send_order_page()
        # 派单
        cls.send_order.send_order_main(cls.orderNumber,pageName=master)
        # 进入服务中全部工单列表页面
        cls.finish_order.enter_serving_order_page()

    def setUp(self):
        # 刷新页面
        self.base.refresh_page()
        # 选择完成的工单
        self.create_order.select_operate_order(self.orderNumber)
        # 点击完成工单按钮
        self.finish_order.click_finish_btn()
        self.base.sleep(1)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_finish_order001(self,ddt_data):
        """网点完成工单功能必填项校验"""

        # 设置参数信息
        for key,value in ddt_data.items():
            if value == "当前时间":
                ddt_data[key] = self.base.get_now_time()
        # 用例名称
        self.base.print_case_name(ddt_data)
        # # 搜索工单
        # self.search_order.search_order_by_number(self.OrderNumber)
        # 输入故障类型
        self.finish_order.input_break_type()
        # 输入师傅预约时间
        self.finish_order.input_master_orderTime(ddt_data["预约时间"])
        # 输入师傅上门时间
        self.finish_order.input_master_doorTime(ddt_data["上门时间"])
        # 输入师傅完成服务时间
        self.finish_order.input_master_finishTime(ddt_data["完成时间"])
        # 完成服务备注
        self.finish_order.input_remark()
        # 上传图片
        self.finish_order.up_finish_picture(ddt_data["上传图片"])
        self.base.sleep(1)
        # 点击提交信息
        self.finish_order.click_submit_btn()
        self.base.sleep(2)
        # 断言
        self.assert_mode.assert_equal(ddt_data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("finish_order_005"),"-跳过不执行该用例")
    def test_finish_order002(self):
        """成功完成服务校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("finish_order_005")
        # 设置参数信息
        for key,value in data.items():
            if value == "当前时间":
                data[key] = self.base.get_now_time()
        # 用例名称
        self.base.print_case_name(data)
        # 输入故障类型
        self.finish_order.input_break_type()
        # 输入师傅预约时间
        self.finish_order.input_master_orderTime(data["预约时间"])
        # 输入师傅上门时间
        self.finish_order.input_master_doorTime(data["上门时间"])
        # 输入师傅完成服务时间
        self.finish_order.input_master_finishTime(data["完成时间"])
        # 完成服务备注
        self.finish_order.input_remark()
        # 上传图片
        self.finish_order.up_finish_picture(data["上传图片"])
        self.base.sleep(1)
        # 点击提交信息
        self.finish_order.click_submit_btn()
        self.base.sleep(1)
        # 进入完工页面
        self.finish_order.enter_finish_order_page()
        # 进入工单详情页
        self.create_order.open_order_details(self.orderNumber)
        self.base.sleep(2)
        # 断言
        self.assert_mode.assert_in(data,self.finish_order.get_finish_order_text())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(Finish_Order)

    unittest.TextTestRunner().run(suit)