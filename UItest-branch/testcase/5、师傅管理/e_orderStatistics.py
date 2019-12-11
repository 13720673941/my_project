# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/2 17:59

from public.common.basepage import BasePage
from public.common.getdata import get_test_data
from public.common.driver import browser_driver
from public.common.assertmode import Assert
from public.common import mytest
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.addOrderPage import AddOrderPage
from public.page.pleaseOrderPage import PleaseOrderPage
from public.page.finishOrderPage import FinishOrder
from public.page.settleOrderPage import SettleOrderPage
from public.page.masterStatisticsPage import MasterStatisticsPage
import unittest
"""
师傅工单状态统计测试用例：
1、师傅已接单订单数量校验 2、师傅已完单订单数量校验 3、师傅未完单订单数量校验 
4、师傅待结算订单数量校验 5、师傅差评单订单数量校验
"""
# 获取测试数据
test_data = get_test_data()["MasterStatisticsPage"]["order_statistic_fnc"]

class Order_Statistics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = browser_driver()
        # 实例化
        cls.login = LoginPage(cls.driver)
        cls.create_order = AddOrderPage(cls.driver)
        cls.please_order = PleaseOrderPage(cls.driver)
        cls.finish_order = FinishOrder(cls.driver)
        cls.settle_order = SettleOrderPage(cls.driver)
        cls.order_statistics = MasterStatisticsPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        cls.base_page = BasePage(cls.driver)
        # 清除浏览器缓存
        cls.base_page.clear_catch()
        # 开始执行测试用例
        mytest.start_test()
        # 获取服务商账号信息
        cls.server_use = read_config_data("西安好家帮家政有限公司","username")
        cls.server_pwd = read_config_data("西安好家帮家政有限公司","password")
        # 登录服务商
        cls.login.login_main(cls.server_use, cls.server_pwd)
        # 进入师傅统计列表页面
        cls.order_statistics.enter_master_order_statistics_page()
        # 获取师傅名称
        cls.master_name = read_config_data("西安好家帮家政有限公司","master001")
        # 搜索师傅
        cls.order_statistics.input_master_keyword_search(search_word=cls.master_name)
        cls.order_statistics.click_search_btn()
        cls.base_page.sleep(1)
        # 师傅初始化接单数量
        cls.take_order_count = cls.order_statistics.get_master_take_order_count()
        # 师傅初始化已完单数量
        cls.finish_order_count = cls.order_statistics.get_master_finished_count()
        # 师傅初始化待结算数量
        cls.wait_settle_count = cls.order_statistics.get_master_wait_settle_count()
        # 师傅初始化已结算数量
        cls.already_settle_count = cls.order_statistics.get_master_already_settle_count()
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.base_page.get_order_number()
        # 网点派单
        cls.please_order.please_order_main(ordernumber=cls.order_number,pagename=cls.master_name)
        # 网点完成服务
        cls.finish_order.finish_order_main(ordernumber=cls.order_number)

    def search_master(self):
        # 搜索师傅
        self.order_statistics.input_master_keyword_search(self.master_name)
        self.order_statistics.click_search_btn()
        self.base_page.sleep(1)

    def test_order_statistics001(self):
        """师傅接单数量同步校验"""

        # 获取测试数据
        data = test_data["TestCase001"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅工单统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新数据
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        # 获取师傅接单数量
        new_master_count = int(self.order_statistics.get_master_take_order_count())
        # 获取差异值
        diff_count = new_master_count-int(self.take_order_count)
        # 断言
        self.assert_mode.assert_equal(data["expect"],diff_count)

    def test_order_statistics002(self):
        """师傅已完单数量校验"""

        # 获取测试数据
        data = test_data["TestCase002"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取师傅已完单数量
        new_order_count = int(self.order_statistics.get_master_finished_count())
        # 前后差异值
        diff_count = new_order_count - int(self.finish_order_count)
        # 断言
        self.assert_mode.assert_equal(data["expect"],diff_count)

    def test_order_statistics003(self):
        """师傅待结算数量校验"""

        # 获取测试数据
        data = test_data["TestCase003"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 获取师傅待结算数量
        new_order_count = int(self.order_statistics.get_master_wait_settle_count())
        # 前后差异值
        diff_count = new_order_count - int(self.wait_settle_count)
        # 断言
        self.assert_mode.assert_equal(data["expect"],diff_count)

    def test_order_statistics004(self):
        """师傅已结算数量校验"""

        # 获取测试数据
        data = test_data["TestCase004"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入订单结算页面
        self.settle_order.enter_master_settle_page()
        # 选择订单进入订单详情
        self.base_page.open_order_message(OrderNumber=self.order_number)
        # 点击结算
        self.settle_order.click_settle_btn()
        # 输入支付金额
        self.settle_order.input_settle_money()
        # 选择线下结算
        self.settle_order.select_line_down_pay()
        # 确定结算
        self.settle_order.click_confirm_pay()
        # 返回师傅统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新数据
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        self.base_page.sleep(1)
        # 获取已经结算订单数量
        already_settle_count = int(self.order_statistics.get_master_already_settle_count())
        # 获取完单待结算订单数量
        wait_settle_count = int(self.order_statistics.get_master_wait_settle_count())
        # 计算结算前后的订单数量差值
        diff_number = already_settle_count - int(self.already_settle_count)
        # 断言1 已结算订单 +1
        self.assert_mode.assert_equal(data["expect"],diff_number)
        # 断言2 待结算订单 -1
        self.assert_mode.assert_equal(int(self.wait_settle_count),wait_settle_count)

    def test_order_statistics005(self):
        """师傅好评率校验"""

        # 获取测试数据
        data = test_data["TestCase005"]
        # 打印测试用例名称
        self.base_page.print_case_name(data["CaseName"])
        # 进入师傅统计页面
        self.order_statistics.enter_master_order_statistics_page()
        # 刷新页面
        self.base_page.refresh_page()
        # 搜索师傅
        self.search_master()
        self.base_page.sleep(1)
        # 获取师傅订单总数
        master_all_finish_orders = int(self.order_statistics.get_master_finished_count())
        # 获取师傅好评订单数量
        master_favorable_orders = int(self.order_statistics.get_master_good_talk_count())
        # 获取师傅好评率
        master_favorable_rate = self.order_statistics.get_master_favorable_rate_count()
        # 计算好评率
        favorable_rate = float((round(master_favorable_orders/master_all_finish_orders,5))*100)
        # 对好评率进行处理 判断小数点后2位是否大于5 进行四舍五入
        if len(str(favorable_rate).split(".")[1]) >= 3:
            if int(str(favorable_rate).split(".")[1][2]) >= 5:
                # 系统代码中计算好评没有四舍五入直接取后两位就好了
                favorable_rate += 0.01
                pass
            # 拼接好评率字符串
            last_number = str(favorable_rate).split(".")[0]+"."+str(favorable_rate).split(".")[1][:2]
        else:
            last_number = str(favorable_rate)
        # 断言
        self.assert_mode.assert_equal(last_number+"%",master_favorable_rate)


    @classmethod
    def tearDownClass(cls):

        cls().base_page.quit_browser()
        mytest.end_test()



if __name__ == '__main__':
    # unittest.main()


    suits = unittest.TestLoader().loadTestsFromTestCase(Order_Statistics)

    unittest.TextTestRunner().run(suits)