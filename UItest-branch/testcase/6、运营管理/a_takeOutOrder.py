# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/7/23 11:50

from public.common import rwConfig
from public.common.operateExcel import *
from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common.assertMode import Assert
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.orderLogPage import OrderLogPage
import unittest

class Take_Out_Order(unittest.TestCase):

    """ 【派单扣除单量功能】 """

    # 实例化excel操作类
    readExcel = Read_Excel("takeOutOrder")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.please_order = SendOrderPage(cls.driver)
        cls.order_log = OrderLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"takeOutOrder")
        # 网点登录
        cls.login.login_main("T西安超级售后有限公司")
        # 获取工单余量
        cls.order_count = int(cls.order_log.get_order_count())
        #  经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.create_order.get_order_number()
        # 单号写入第二个测试用例的期望值中
        Update_Excel.update_expect_data("takeOutOrder","take_out_order_002",cls.order_number)
        # 写入工单单号后面扣除单量日志搜索使用
        rwConfig.write_config_data("for_order_log_search","id",cls.order_number,orderNumPath)
        # 获取派单师傅
        master = rwConfig.read_config_data("T西安超级售后有限公司", "master001")
        # 派单
        cls.please_order.send_order_main(cls.order_number,pageName=master)

    @unittest.skipUnless(readExcel.get_isRun_text("take_out_order_001"),"-跳过不执行")
    def test_takeOut_order001(self):
        """派单扣除工单余量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_out_order_001")
        # 打印测试用力名称
        self.base_page.print_case_name(data)
        # 进入首页
        self.login.enter_first_page_review()
        self.base_page.sleep(2)
        # 获取单量记录
        new_order_count = int(self.order_log.get_order_count())
        # 计算单量前后差值
        diff_count = self.order_count - new_order_count
        # 断言
        self.assert_mode.assert_equal(data,str(diff_count))

    @unittest.skipUnless(readExcel.get_isRun_text("take_out_order_002"),"-跳过不执行")
    def test_takeOut_order002(self):
        """工单单量记录日志记录校验"""

        # 获取测试数据
        data = Read_Excel("takeOutOrder").get_dict_data("take_out_order_002")
        # 打印测试用力名称
        self.base_page.print_case_name(data)
        # 进入单量扣除记录页面
        self.order_log.enter_order_log_page()
        self.base_page.sleep(1)
        # 获取第一条记录的内容信息
        first_row_log_info = self.order_log.get_first_row_info()
        # 断言- 判断订单单号在该信息里面
        self.assert_mode.assert_in(data,first_row_log_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':


    suits = unittest.TestLoader().loadTestsFromTestCase(Take_Out_Order)

    unittest.TextTestRunner(verbosity=2).run(suits)