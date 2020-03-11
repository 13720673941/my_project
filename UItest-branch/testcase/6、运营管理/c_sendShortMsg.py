# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/8/21 19:07

from public.common.basePage import BasePage
from public.common.driver import web_driver
from public.common import rwConfig
from public.common.assertMode import Assert
from public.common.operateExcel import *
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
from public.page.shortMsgLogPage import ShortMsgLogPage
from config.urlConfig import *
import unittest

class Send_ShortMsg(unittest.TestCase):

    """ 【扣除短信日志功能】 """

    # 实例化类
    readExcel = Read_Excel("takeOutShortMsg")

    @classmethod
    def setUpClass(cls):
        # 设置浏览器驱动
        cls.driver = web_driver()
        # 实例化
        cls.base_page = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.please_order = SendOrderPage(cls.driver)
        cls.short_msg_log = ShortMsgLogPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"takeOutShortMsg")
        # 网点登录
        cls.login.login_main("T西安超级售后有限公司")
        # 获取短信余量
        cls.short_msg_count = int(cls.short_msg_log.get_short_msg_count())

        """
        ---------- 关联默认开启短信发送按钮脚本 ---------
        """

        # 经销商下单程序下单
        cls.create_order.create_not_return_order()
        # 获取单号
        cls.order_number = cls.create_order.get_order_number()
        # 单号写入关联文件，搜索短信日志使用
        rwConfig.write_config_data(
            "for_shortMsg_log_search","id",cls.order_number,orderNumPath)
        # 获取派单师傅
        master = read_config_data("T西安超级售后有限公司","master001")
        # 派单
        cls.please_order.send_order_main(cls.order_number,pageName=master)

    @unittest.skipUnless(readExcel.get_isRun_text("take_out_shortMsg_001"),"-跳过不执行")
    def test_send_shortMsg001(self):
        """扣除短信数量校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_out_shortMsg_001")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入首页
        self.login.enter_first_page_review()
        self.base_page.sleep(2)
        # 获取首页短信余量
        new_short_msg_count = int(self.short_msg_log.get_short_msg_count())
        # 计算短信余量差值
        diff_count = self.short_msg_count - new_short_msg_count
        # 断言
        self.assert_mode.assert_equal(data,str(diff_count))

    @unittest.skipUnless(readExcel.get_isRun_text("take_out_shortMsg_002"),"-跳过不执行")
    def test_send_shortMsg002(self):
        """发送短信日志记录校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("take_out_shortMsg_002")
        # 打印测试用例名称
        self.base_page.print_case_name(data)
        # 进入短信发送日志记录页面
        self.short_msg_log.enter_short_msg_list_page()
        # 搜索工单发送记录
        self.short_msg_log.input_order_number(self.order_number)
        # 点击搜索
        self.short_msg_log.click_search_btn()
        self.base_page.sleep(1)
        # 获取第一行日志发送数据
        first_row_msg_info = self.short_msg_log.get_first_row_info()
        # 断言发送成功
        self.assert_mode.assert_in(data,first_row_msg_info)

    @classmethod
    def tearDownClass(cls):
        # 清除浏览器缓存
        cls().base_page.clear_catch()
        # 退出浏览器
        cls().base_page.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Send_ShortMsg)

    unittest.TextTestRunner(verbosity=2).run(suits)
