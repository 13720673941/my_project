#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/29 16:36
from public.common.basepage import BasePage
from public.common.assertmode import Assert
from public.common.driver import browser_driver
from public.common.getdata import get_test_data
from public.common import mytest,writetestresult
from public.common.rwconfig import read_config_data
from public.page.loginPage import LoginPage
from public.page.manageBranchPage import DealerBranchPage
import unittest,ddt
"""
经销商服务设置功能：
1、经销商备注可以编辑校验 2、合作类型不能编辑校验 3、服务类型不能编辑校验 
4、服务品牌不能编辑校验 5、服务品类不能编辑校验
"""
# 获取数据
dealer_page_data = get_test_data()["AddDealerPage"]["server_set_fnc"]
# 默认写入测试结果
isWrite=True
@ddt.ddt
class Set_Server(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 设置浏览驱动
        cls.driver = browser_driver()
        # 实例化
        cls.login = LoginPage(cls.driver)
        cls.base_page = BasePage(cls.driver)
        cls.dealer_page = DealerBranchPage(cls.driver)
        cls.assert_mode = Assert(cls.driver)
        mytest.start_test()
        # 获取网点账号密码
        cls.username = read_config_data("蓝魔科技","username")
        cls.password = read_config_data("蓝魔科技","password")
        # 登录网点
        cls.login.login_main(cls.username,cls.password)
        # 进入邀请经销商页面
        cls.dealer_page.enter_dealer_page()

    def setUp(self):
        self.base_page.refresh_page()
        # 点击设置服务
        self.dealer_page.click_set_server()

    def test_Set_Server001(self):
        """设置经销商的备注校验"""
        # 获取测试数据
        set_server_data = dealer_page_data["test_case001"]
        # 打印测试名称
        self.base_page.print_case_name(set_server_data["CaseName"])
        # 清除输入框
        self.dealer_page.clear_branch_remark()
        # 输入备注
        self.dealer_page.input_branch_remark(branch_remark=set_server_data["BranchRemark"])
        # 点击确定
        self.dealer_page.click_server_set_confirm()
        self.base_page.sleep(1)
        # 输出第一行的所有数据字段
        first_branch_info = self.dealer_page.get_first_branch_info()
        # 断言
        isSuccess = self.assert_mode.assert_in(set_server_data["expect"],first_branch_info)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",set_server_data["CaseName"])

    def test_Set_Server002(self):
        """经销商服务设置合作类型不能编辑"""
        # 获取测试数据
        set_server_data = dealer_page_data["test_case002"]
        # 打印测试名称
        self.base_page.print_case_name(set_server_data["CaseName"])
        # 获取合作类型选择属性
        teamwork_attribute = self.dealer_page.get_teamwork_type_attribute()
        # 断言
        isSuccess = self.assert_mode.assert_equal(set_server_data["expect"],teamwork_attribute)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",set_server_data["CaseName"])

    def test_Set_Server003(self):
        """经销商服务设置服务类型不能编辑"""
        # 获取测试数据
        set_server_data = dealer_page_data["test_case003"]
        # 打印测试名称
        self.base_page.print_case_name(set_server_data["CaseName"])
        # 获取合作类型选择属性
        server_type_attribute = self.dealer_page.get_server_type_attribute()
        # 断言
        isSuccess = self.assert_mode.assert_equal(set_server_data["expect"],server_type_attribute)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",set_server_data["CaseName"])

    def test_Set_Server004(self):
        """经销商服务设置服务品牌不能编辑"""
        # 获取测试数据
        set_server_data = dealer_page_data["test_case004"]
        # 打印测试名称
        self.base_page.print_case_name(set_server_data["CaseName"])
        # 获取合作类型选择属性
        server_brands_attribute = self.dealer_page.get_brands_type_attribute()
        # 断言
        isSuccess = self.assert_mode.assert_equal(set_server_data["expect"],server_brands_attribute)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",set_server_data["CaseName"])

    def test_Set_Server005(self):
        """经销商服务设置服务品类不能编辑"""
        # 获取测试数据
        set_server_data = dealer_page_data["test_case005"]
        # 打印测试名称
        self.base_page.print_case_name(set_server_data["CaseName"])
        # 获取合作类型选择属性
        server_kinds_attribute = self.dealer_page.get_kinds_type_attribute()
        # 断言
        isSuccess = self.assert_mode.assert_equal(set_server_data["expect"],server_kinds_attribute)
        # 写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,"VisitDealer",set_server_data["CaseName"])

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览
        cls.base_page.quit_browser()
        mytest.end_test()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Set_Server("test_Set_Server001"))
    suit.addTest(Set_Server("test_Set_Server002"))
    suit.addTest(Set_Server("test_Set_Server003"))
    suit.addTest(Set_Server("test_Set_Server004"))
    suit.addTest(Set_Server("test_Set_Server005"))
    unittest.TextTestRunner().run(suit)