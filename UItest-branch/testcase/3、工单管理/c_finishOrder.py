#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/5 18:07

from public.common import rwconfig,mytest
from public.common import driver,getdata
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.searchOrderPage import SearchOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
"""
网点完成服务页面功能测试用例：
1、完成工单-师傅预约时间为空校验 2、完成工单-师傅上门时间为空校验 3、完成工单-师傅完工时间为空校验 4、完成工单-师傅上传图片为空校验
5、完成工单-网点完成服务校验
"""
# 写入日志
# 获取测试数据信息
Data = getdata.get_test_data()["FinishOrderPage"]
FinishDate = Data["finish_order_fnc"]

@ddt.ddt
class Finish_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.basePage = BasePage(cls.dr)
        cls.pleaseOrderPage = PleaseOrderPage(cls.dr)
        cls.addOrderPage = AddOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.finishOrder = FinishOrder(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        cls.search_order = SearchOrderPage(cls.dr)
        mytest.start_test()
        # 获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        cls.loginPage.login_main(UserName,PassWord)
        #  获取订单信息
        user = rwconfig.read_config_data("NotReturnOrder", "用户姓名", orderInfo)
        phe = rwconfig.read_config_data("NotReturnOrder", "联系方式", orderInfo)
        address = rwconfig.read_config_data("NotReturnOrder", "服务地址", orderInfo)
        collage = rwconfig.read_config_data("NotReturnOrder", "详细地址", orderInfo)
        order_type = rwconfig.read_config_data("NotReturnOrder", "工单类型", orderInfo)
        server = rwconfig.read_config_data("NotReturnOrder", "服务类型", orderInfo)
        brands = rwconfig.read_config_data("NotReturnOrder", "品牌", orderInfo)
        kinds = rwconfig.read_config_data("NotReturnOrder", "品类", orderInfo)
        #  经销商下单程序下单
        cls.addOrderPage.create_order_main(user, phe, address, collage, order_type, server, brands, kinds)
        #  获取单号
        cls.OrderNumber = cls.basePage.get_order_number()
        # 获取派单数据
        Master = rwconfig.read_config_data('蓝魔科技','master001')
        # 进入派单页面
        cls.pleaseOrderPage.enter_please_order_page()
        # 派单
        cls.pleaseOrderPage.please_order_main(cls.OrderNumber,Master)
        # 进入服务中全部工单列表页面
        cls.finishOrder.enter_finish_order_page()

    @ddt.data(*FinishDate)
    def test_finishOrder001(self,FinishDate):
        """网点完成工单功能校验"""
        # 设置参数信息
        for key,value in FinishDate.items():
            if value == '当前时间':
                FinishDate[key] = self.basePage.get_now_time()
        # 用例名称
        self.basePage.print_case_name(FinishDate["CaseName"])
        # 刷新页面
        self.basePage.refresh_page()
        self.basePage.sleep(2)
        # 搜索工单
        self.search_order.search_order_by_number(self.OrderNumber)
        # 选择完成的工单
        self.basePage.select_new_order(OrderNumber=self.OrderNumber)
        # 点击完成工单按钮
        self.finishOrder.click_finish_btn()
        self.basePage.sleep(1)
        # 输入故障类型
        self.finishOrder.input_break_type()
        # 输入师傅预约时间
        self.finishOrder.input_master_orderTime(orderTime=FinishDate["OrderTime"])
        # 输入师傅上门时间
        self.finishOrder.input_master_doorTime(doorTime=FinishDate["DoorTime"])
        # 输入师傅完成服务时间
        self.finishOrder.input_master_finishTime(finishTime=FinishDate["FinishTime"])
        # 完成服务备注
        self.finishOrder.input_remark()
        # 上传图片
        self.finishOrder.up_finish_picture(upLoading=FinishDate["UpLoading"])
        self.basePage.sleep(1)
        # 点击提交信息
        self.finishOrder.click_submit_btn()
        self.basePage.sleep(2)
        # 断言
        self.assert_mode.assert_equal(FinishDate["expect"],self.basePage.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Finish_Order('test_finishOrder001'))
    unittest.TextTestRunner().run(suit)