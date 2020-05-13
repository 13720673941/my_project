# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/19 16:46

from public.common.driver import web_driver
from public.common.operateExcel import *
from public.common.rwConfig import read_config_data
from public.common.assertMode import Assert
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.sendOrderPage import SendOrderPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.editGroupPage import EditGroupPage
import unittest

class Del_Group_Member(unittest.TestCase):

    """ 【删除圈子成员校验】 """

    # 实例化操作类
    readExcel = Read_Excel("delMember")

    @classmethod
    def setUpClass(cls):
        # 实例化对象类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.search_order = SearchOrderPage(cls.driver)
        cls.edit_group = EditGroupPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"delMember")
        # 登录群主网点
        cls.login.login_main("T西安超级售后有限公司")
        # 进入圈子列表页面
        cls.edit_group.enter_my_group_list_page()

    @unittest.skipUnless(readExcel.get_isRun_text("del_member_001"),"-跳过不执行该用例")
    def test_del_member001(self):
        """删除成员-订单未结算的成员不能删除校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("del_member_001")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 点击编辑按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        self.base.sleep(1)
        # 点击所要删除的成员
        self.edit_group.del_send_order_member(data["成员名称"])
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(readExcel.get_isRun_text("del_member_002"),"-跳过不执行该用例")
    def test_del_member002(self):
        """删除成员-成员删除成功校验"""

        # 获取测试数据
        data = self.readExcel.get_dict_data("del_member_002")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 登录删除网点
        self.login.click_logout_button()
        self.login.login_main("T西安瑞晟科技有限公司")
        # 进入全部工单页面
        self.search_order.enter_search_order_page()
        # 点击更多
        self.search_order.click_search_more()
        # 选择圈子名称
        self.search_order.select_group_name(data["圈子名称"])
        # 点击搜索
        self.search_order.click_more_search_btn()
        self.base.sleep(2)
        # 获取圈子订单列表
        orderList = self.search_order.get_search_order_number()
        # 登录派单网点
        self.login.click_logout_button()
        self.login.login_main("T西安好家帮家政有限公司")
        # 获取派单对象
        pageName = read_config_data("T西安好家帮家政有限公司","master001")
        # ----------- 清理圈子订单 ----------
        if orderList is not None:
            # 转派所有订单
            for order in orderList:
                # 刷新页面
                self.base.refresh_page()
                self.base.sleep(2)
                # 循环派单转派出圈子
                self.send_order.send_order_main(orderNumber=order,pageName=pageName)
        # 登录圈主网点
        self.login.click_logout_button()
        self.login.login_main("T西安超级售后有限公司")
        # 进入圈子列表页面
        self.edit_group.enter_my_group_list_page()
        # 点击编辑按钮
        self.edit_group.click_edit_group_btn(data["圈子名称"])
        self.base.sleep(1)
        # 点击所要删除的成员
        self.edit_group.del_take_order_member(data["成员名称"])
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':

    suits = unittest.TestLoader().loadTestsFromTestCase(Del_Group_Member)

    unittest.TextTestRunner().run(suits)

