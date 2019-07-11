#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/3 10:24

from public.common.rwconfig import read_config_data
from public.common import driver,getdata,mytest
from public.common.assertmode import Assert
from public.common.basepage import BasePage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.addOrderPage import AddOrderPage
from public.page.loginPage import LoginPage
from config.pathconfig import *
import unittest,ddt
"""
网点派单功能测试用例脚本：
1、派单-选择工单为空点击派单按钮校验 2、派单-按师傅名称搜索校验 3、派单-按手机号搜索校验 4、派单-派单师傅为空校验
5、派单-成功派单到师傅校验 6、派单-派单网点为空校验 7、派单-成功派单到网点校验 8、派单-成功派单到网点校验 
9、派单-成功派单到网点校验 10、派单-师傅转派师傅校验 11、派单-师傅转派网点校验 12、派单-网点转派网点校验
13、派单-网点转派师傅校验 14、派单-派单到返单服务商校验
"""
# 获取ddt模式文件参数信息
Data1 = getdata.get_test_data()["PleaseOrderPage"]["search_fnc"]
Data2 = getdata.get_test_data()["PleaseOrderPage"]["to_branch_fnc"]
Data3 = getdata.get_test_data()["PleaseOrderPage"]["to_master_fnc"]

@ddt.ddt
class Please_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.basePage = BasePage(cls.dr)
        cls.pleaseOrderPage = PleaseOrderPage(cls.dr)
        cls.addOrderPage = AddOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        # 开始
        mytest.start_test()
        # 获取网点登录数据
        UserName = read_config_data('蓝魔科技','username')
        PassWord = read_config_data('蓝魔科技','password')
        # 网点登录
        cls.loginPage.login_main(UserName,PassWord)
        #  获取订单信息
        user = read_config_data("ReturnOrder", "用户姓名", orderInfo)
        phe = read_config_data("ReturnOrder", "联系方式", orderInfo)
        address = read_config_data("ReturnOrder", "服务地址", orderInfo)
        collage = read_config_data("ReturnOrder", "详细地址", orderInfo)
        order_type = read_config_data("ReturnOrder", "工单类型", orderInfo)
        server = read_config_data("ReturnOrder", "服务类型", orderInfo)
        brands = read_config_data("ReturnOrder", "品牌", orderInfo)
        kinds = read_config_data("ReturnOrder", "品类", orderInfo)
        branch_name = read_config_data("ReturnOrder", "服务商", orderInfo)
        #  经销商下单程序下单
        cls.addOrderPage.create_order_main(user, phe, address, collage, order_type, server, brands, kinds,branch_name)
        #  获取单号
        cls.OrderNumber = cls.basePage.get_order_number()
        # 进入派单页面
        cls.pleaseOrderPage.enter_please_order_page()

    def test_pleaseOrder001(self):
        """选择订单为空时派单校验"""
        # 获取测试数据
        TestData1 = getdata.get_test_data()["PleaseOrderPage"]["TestCase001"]
        # 点击派单按钮不选择订单
        self.basePage.print_case_name(TestData1["CaseName"])
        self.basePage.refresh_page()
        # 时间等待
        self.basePage.wait()
        self.pleaseOrderPage.click_pleaseOrder_btn()
        Msg = self.basePage.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(TestData1["expect"],Msg)

    @ddt.data(*Data1)
    def test_pleaseOrder002(self,Data1):
        """网点派单页面搜索师傅/网点测试"""
        # 刷新页面
        self.basePage.refresh_page()
        # 选择新建订单
        self.basePage.print_case_name(Data1["CaseName"])
        self.basePage.select_new_order(self.OrderNumber)
        # 点击派单按钮
        self.pleaseOrderPage.click_pleaseOrder_btn()
        # 输入师傅信息
        self.pleaseOrderPage.input_search_name(name=Data1["MasterName"])
        # 点击搜索
        self.pleaseOrderPage.click_search_btn()
        # 时间等待
        self.basePage.sleep(1)
        # 获取师傅名称
        Name = self.pleaseOrderPage.get_search_name()
        # 断言
        self.assert_mode.assert_equal(Data1["expect"],Name)

    @ddt.data(*Data2)
    def test_pleaseOrder003(self,Data2):
        """派单到网点测试用例"""
        # 刷新页面
        self.basePage.refresh_page()
        # 选择新建订单
        self.basePage.print_case_name(Data2["CaseName"])
        self.basePage.select_new_order(self.OrderNumber)
        # 点击派单按钮
        self.pleaseOrderPage.click_pleaseOrder_btn()
        # 切换服务商
        self.pleaseOrderPage.please_to_branch()
        # 选择派单服务商
        self.pleaseOrderPage.select_please_page(page_name=Data2["BranchName"])
        # 点击派单按钮
        self.pleaseOrderPage.click_confirm_btn()
        self.basePage.sleep(1)
        # 断言
        self.assert_mode.assert_equal(Data2["expect"],self.basePage.get_system_msg())

    @ddt.data(*Data3)
    def test_pleaseOrder004(self,Data3):
        """派单到师傅测试用例"""
        # 刷新页面
        self.basePage.refresh_page()
        # 选择新建订单
        self.basePage.print_case_name(Data3["CaseName"])
        self.basePage.select_new_order(self.OrderNumber)
        # 点击派单按钮
        self.pleaseOrderPage.click_pleaseOrder_btn()
        # 选择派单师傅
        self.pleaseOrderPage.select_please_page(page_name=Data3["MasterName"])
        # 点击派单按钮
        self.pleaseOrderPage.click_confirm_btn()
        self.basePage.sleep(1)
        # 断言
        self.assert_mode.assert_equal(Data3["expect"],self.basePage.get_system_msg())

    def test_pleaseOrder005(self):
        """派到师傅可以转派到服务商校验"""
        # 获取数据
        Data = getdata.get_test_data()["PleaseOrderPage"]["TestCase002"]
        # 刷新页面
        self.basePage.refresh_page()
        # 选择新建订单
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.select_new_order(self.OrderNumber)
        # 点击派单按钮
        self.pleaseOrderPage.click_pleaseOrder_btn()
        # 派单到服务商
        self.pleaseOrderPage.please_to_branch()
        # 选择派单服务商
        self.pleaseOrderPage.select_please_page(page_name=Data["BranchName"])
        # 确定派单
        self.pleaseOrderPage.click_confirm_btn()
        self.basePage.sleep(1)
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())

    def test_pleaseOrder006(self):
        """派到服务商可以转派到师傅校验"""
        # 获取数据
        Data = getdata.get_test_data()["PleaseOrderPage"]["TestCase003"]
        # 刷新页面
        self.basePage.refresh_page()
        # 选择新建订单
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.select_new_order(self.OrderNumber)
        # 点击派单按钮
        self.pleaseOrderPage.click_pleaseOrder_btn()
        # 派单到服务商
        self.pleaseOrderPage.please_to_master()
        # 选择派单服务商
        self.pleaseOrderPage.select_please_page(page_name=Data["MasterName"])
        # 确定派单
        self.pleaseOrderPage.click_confirm_btn()
        self.basePage.sleep(1)
        # 断言
        self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main(verbosity=2)

    suit = unittest.TestSuite()
    suit.addTest(Please_Order('test_pleaseOrder001'))
    suit.addTest(Please_Order('test_pleaseOrder002'))
    suit.addTest(Please_Order('test_pleaseOrder003'))
    suit.addTest(Please_Order('test_pleaseOrder004'))
    suit.addTest(Please_Order('test_pleaseOrder005'))
    suit.addTest(Please_Order('test_pleaseOrder006'))
    unittest.TextTestRunner().run(suit)







