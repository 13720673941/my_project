#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/4 17:14

from public.common import rwconfig,mytest
from public.common import driver,getdata
from public.common.basepage import BasePage
from public.page.loginPage import LoginPage
from public.page.searchOrderPage import SearchOrderPage
from config.pathconfig import *
from public.common.assertmode import Assert
import unittest,ddt
"""
网点订单列表搜索订单测试用例：
1、工单搜索-按工单编码搜索工单校验 2、工单搜索-按用户电话搜索工单校验 3、工单搜索-按服务类型搜索工单校验 4、工单搜索-按工单状态搜索工单校验
5、工单搜索-按服务师傅搜索工单校验 6、工单搜索-按多条件混合搜索工单校验 7、工单搜索-按品牌搜索工单校验 8、工单搜索-按品类搜索工单校验
9、工单搜索-按型号搜索工单校验 10、工单搜索-按内机码搜索工单校验 11、工单搜索-按工单来源搜索工单校验 12、工单搜索-按购买渠道搜索工单校验
13、工单搜索-按下单日期搜索工单校验 14、工单搜索-按完成日期搜索工单校验 15、工单搜索-按多条件搜索工单校验
"""
# 获取测试数据信息
Data = getdata.get_test_data()["SearchOrderPage"]
# 获取ddt模式数据
ddtData1 = Data["search_order_fnc"]
ddtData2 = Data["more_search_fnc"]
@ddt.ddt
class Search_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.dr = driver.browser_driver()
        # 实例化
        cls.basePage = BasePage(cls.dr)
        cls.searchOrder = SearchOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        mytest.start_test()
        # 读取订单单号信息，订单单号的搜索取添加订单写入的订单单号
        OrderNum = rwconfig.read_config_data('for_invalid_and_search','id',orderNumPath)
        # 写入工单编码到json,搜索测试数据的第一行
        ddtData1[0]["OrderNum"] = OrderNum
        # 写入当前时间到测试数据中，MoreSearchData->CreateDate\FinishDate
        ddtData2[6]["CreateDate"] = cls.basePage.get_now_time()
        ddtData2[7]["FinishDate"] = cls.basePage.get_now_time() # 待结算写完
        # 获取网点登录数据
        UserName = rwconfig.read_config_data('branch_01','username')
        PassWord = rwconfig.read_config_data('branch_01','password')
        # 网点登录
        cls.loginPage.login_main(UserName,PassWord)
        # 进入全部工单页面
        cls.searchOrder.enter_search_order_page()

    @ddt.data(*ddtData1)
    def test_searchOrder001(self,ddtData1):
        """网点主搜索页面测试用例"""
        self.basePage.print_case_name(ddtData1["CaseName"])
        # 刷新页面
        self.basePage.refresh_page()
        self.basePage.sleep(2)
        # 输入工单编号
        self.searchOrder.input_order_Nnumber(orderNum=ddtData1["OrderNum"])
        # 输入用户姓名
        self.searchOrder.input_username(username=ddtData1["User"])
        # 输入用户电话
        self.searchOrder.input_user_phone(phoneNum=ddtData1["UserPhone"])
        # 选择服务类型
        self.searchOrder.select_server_type(value=ddtData1["ServerType"])
        # 选择工单状态
        self.searchOrder.select_order_status(value=ddtData1["Status"])
        # 选择服务师傅
        self.searchOrder.select_master(value=ddtData1["Master"])
        # 点击搜索按钮
        self.searchOrder.click_search_btn()
        # 时间加载
        self.basePage.sleep(2)
        # 搜索工单条数
        self.searchOrder.search_order_count()
        # 断言
        self.assert_mode.assert_more_str_in(ddtData1,self.searchOrder.get_first_order_info())

    @ddt.data(*ddtData2)
    def test_searchOrder002(self,ddtData2):
        """网点更多搜索页面测试用例"""
        self.basePage.print_case_name(ddtData2["CaseName"])
        # 刷新页面
        self.basePage.refresh_page()
        # 点击更多条件搜索按钮
        self.searchOrder.click_search_more()
        self.basePage.sleep(1)
        # 选择家电品牌
        self.searchOrder.select_product_brand(value=ddtData2["Brand"])
        # 选择家电品类
        self.searchOrder.select_product_kinds(value=ddtData2["Kind"])
        # 输入产品型号
        self.searchOrder.input_product_number(productNum=ddtData2["ProductNum"])
        # 输入内机条码
        self.searchOrder.input_in_pheNum(in_pheNum=ddtData2["InPheNum"])
        # 选择工单来源
        self.searchOrder.select_order_from(value=ddtData2["From"])
        # 选择购买渠道
        self.searchOrder.select_buy_place(value=ddtData2["BuyPlace"])
        # 输入下单开始日期
        self.searchOrder.input_create_start_date(date=ddtData2["CreateDate"])
        # 输入下单结束日期
        self.searchOrder.input_create_end_date(date=ddtData2["CreateDate"])
        # 输入完成工单开始日期
        self.searchOrder.input_finish_start_date(date=ddtData2["FinishDate"])
        # 输入完成工单结束日期
        self.searchOrder.input_finish_end_date(date=ddtData2["FinishDate"])
        # 点击搜索按钮
        self.searchOrder.click_more_search_btn()
        self.basePage.sleep(2)
        # 搜索工单条数
        self.searchOrder.search_order_count()
        # 断言
        self.assert_mode.assert_more_str_in(ddtData2,self.searchOrder.get_first_order_info())

    @classmethod
    def tearDownClass(cls):
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Search_Order("test_searchOrder001"))
    suit.addTest(Search_Order("test_searchOrder002"))
    unittest.TextTestRunner(verbosity=2).run(suit)