# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/5 14:09

from public.common import getdata,mytest
from public.common.rwconfig import read_config_data
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.common.driver import browser_driver
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.orderDetailsPage import OrderDetailsPage
from config.pathconfig import *
import unittest,ddt,datetime
"""
订单详情页按钮功能测试用例：
1、预约订单-预约时间为空校验 2、预约订单-预约成功校验 3、修改预约-成功修改预约校验 4、修改订单-修改订单手机号校验
5、催单-催单信息内容为空校验 6、催单-催单成功校验 7、新建工单-直接新建工单校验" 8、打印工单-打印工单页面跳转校验
"""
# 获取ddt测试数据
data = getdata.get_test_data()["OrderDetailPage"]
appoint_data = data["appoint_order_fnc"]
cui_data = data["cui_order_fnc"]
@ddt.ddt
class Order_Details(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.order_detail = OrderDetailsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 登录网点 branch_01
        cls.Use = read_config_data('branch_01',"username")
        cls.Pwd = read_config_data('branch_01',"password")
        cls.login.login_main(cls.Use,cls.Pwd)
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取工单单号
        cls.order_number = cls.base_page.get_order_number()
        # 获取派单师傅
        master = read_config_data('branch_01','master001')
        # 派单到师傅
        cls.please_order.please_order_main(cls.order_number,master)

    def setUp(self):
        """工共操作"""
        # 刷新
        self.base_page.refresh_page()
        # 进入订单列表页
        self.please_order.enter_please_order_page()
        # 进入订单详情
        self.base_page.open_order_message(self.order_number)
        self.base_page.sleep(2)

    @ddt.data(*appoint_data)
    def test_order_details001(self,appoint_data):
        """订单详情页预约功能测试用例"""
        # 打印测试用例名称
        self.base_page.print_case_name(appoint_data["CaseName"])
        # 点击预约按钮
        self.order_detail.click_appoint_btn()
        """
        产品修改：默认预约时间为当前日期，不用选择
        """
        # 清除预约日期
        # self.order_detail.clear_appoint_date()
        # 输入预约日期
        # self.order_detail.input_appoint_date()
        # 点击空白区
        # self.order_detail.click_white_place()
        # 选择预约时间
        self.order_detail.select_appoint_time(appoint_data["AppointTime"])
        # 点击确定预约
        self.order_detail.click_confirm_appoint_btn()
        # 断言
        self.assert_mode.assert_equal(appoint_data["expect"],self.base_page.get_system_msg())

    def test_order_details002(self):
        """订单详情页修改预约功能测试用例"""
        # 获取测试数据
        alter_appoint_data = data["alter_appoint_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(alter_appoint_data["CaseName"])
        # 点击修改预约按钮
        self.order_detail.click_alter_appoint_btn()
        # 清除预约日期
        self.order_detail.clear_appoint_date()
        # 输入预约日期
        self.order_detail.input_appoint_date(alter=True)
        self.base_page.sleep(1)
        # 点击空白区
        self.order_detail.click_white_place()
        # 选择预约时间段
        self.order_detail.select_appoint_time(alter_appoint_data["AppointTime"])
        # 点击确定预约
        self.order_detail.click_confirm_appoint_btn()
        # 断言
        self.assert_mode.assert_equal(alter_appoint_data["expect"],self.base_page.get_system_msg())
        self.base_page.sleep(1)
        # 获取当前日期后一天修改预约判断用
        alter_date = str(datetime.datetime.now().date()+datetime.timedelta(2))
        # 判断修改的预约时间在订单详情页已经改变
        self.assert_mode.assert_in(alter_date,self.order_detail.get_appoint_text())

    def test_order_details003(self):
        """订单详情页修改订单内容功能用例"""
        # 获取测试数据
        alter_order_data = data["alter_order_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(alter_order_data["CaseName"])
        # 点击修改订单
        self.order_detail.click_alter_order_btn()
        # 页面加载慢等待原始数据加载出来再修改
        self.base_page.sleep(3)
        # 输入手机号
        self.create_order.input_phoneNum(alter_order_data["PhoneNum"])
        # 点击保存订单
        self.create_order.click_save_btn()
        # 进入订单详情判断
        self.base_page.open_order_message(self.order_number)
        # 加载
        self.base_page.sleep(1)
        # 获取修改字段
        alter_text = self.order_detail.get_alter_text_of_order()
        # 判断修改订单成功
        self.assert_mode.assert_in(alter_order_data["expect"],alter_text)

    @ddt.data(*cui_data)
    def test_order_details004(self,cui_data):
        """订单详情催单功能测试用例"""
        # 打印测试用例名称
        self.base_page.print_case_name(cui_data["CaseName"])
        # 点击催单按钮
        self.order_detail.click_cui_order_btn()
        # 输入催单备注
        self.order_detail.input_cui_of_reason(cui_data["CuiReason"])
        # 点击确定催单
        self.order_detail.click_confirm_cui_order()
        # 断言
        self.assert_mode.assert_equal(cui_data["expect"],self.base_page.get_system_msg())

    def test_order_details005(self):
        """订单详情页新建订单功能用例"""
        # 获取测试数据
        create_order_data = data["new_create_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(create_order_data["CaseName"])
        # 点击新建订单
        self.order_detail.click_new_create_btn()
        self.base_page.sleep(3)
        # 点击保存订单
        self.create_order.click_save_btn()
        # 判断新建订单成功
        self.assert_mode.assert_equal(create_order_data["expect"],self.base_page.get_system_msg())

    def test_order_details006(self):
        """订单详情页打印订单功能用例"""
        # 获取测试数据
        print_order_data = data["print_order_fnc"]
        # 打印测试用例名称
        self.base_page.print_case_name(print_order_data["CaseName"])
        # 获取当前窗口handle
        old_handle = self.base_page.get_current_handle()
        # 点击打印订单
        self.order_detail.click_print_order_btn()
        # 获取全部handles
        handles = self.base_page.get_all_handles()
        # 切换页面
        self.base_page.switch_window_handle(handles,old_handle)
        # 判断新建订单成功
        self.assert_mode.assert_equal(print_order_data["expect"],self.base_page.get_title())

    @classmethod
    def tearDownClass(cls):
        cls.base_page.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Order_Details("test_order_details001"))
    suit.addTest(Order_Details("test_order_details002"))
    suit.addTest(Order_Details("test_order_details003"))
    suit.addTest(Order_Details("test_order_details004"))
    suit.addTest(Order_Details("test_order_details005"))
    suit.addTest(Order_Details("test_order_details006"))

    unittest.TextTestRunner().run(suit)