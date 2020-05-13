# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/30 18:21

from public.common import myDecorator
from public.common import rwConfig
from public.common.operateExcel import Read_Excel
from public.common.assertMode import Assert
from public.common.driver import web_driver
from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.createOrderPage import CreateOrderPage
from public.page.sendOrderPage import SendOrderPage
import unittest,ddt

@ddt.ddt
class Create_Order(unittest.TestCase):

    """" 【创建工单功能测试用例脚本】 """

    # 测试用例编号列表
    case_list = [
        "create_order_001", "create_order_002", "create_order_003", "create_order_004",
        "create_order_005", "create_order_006", "create_order_007", "create_order_008",
        "create_order_009", "create_order_010", "create_order_011", "create_order_012",
        "create_order_013"
    ]
    # 获取ddt测试数据
    read_excel = Read_Excel("createOrder")
    ddt_data = read_excel.get_ddt_data(case_list)

    @classmethod
    def setUpClass(cls):
        # 实例化断言类
        cls.driver = web_driver()
        cls.base = BasePage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.create_order = CreateOrderPage(cls.driver)
        cls.send_order = SendOrderPage(cls.driver)
        cls.assert_mode = Assert(cls.driver,"createOrder")
        # 网点登录
        cls.login.login_main("T西安好家帮家政有限公司")

    def public_operation(self,name,phoneNum,serverAddress,orderType,collage,serverType,
                         brands,big_kinds,kinds,small_kinds,branchName=None):
        """工共操作下单"""

        # 进入添加订单页面
        self.create_order.enter_create_order_url()
        # 刷新页面
        self.base.refresh_page()
        # 输入联系人名称
        self.create_order.input_username(name)
        # 输入联系方式
        self.create_order.input_phoneNum(phoneNum)
        # 选择服务地址
        self.create_order.select_server_address(serverAddress)
        # 选择工单类型
        self.create_order.select_order_type(orderType,branchName)
        # 输入详细地址
        self.create_order.input_add_collage(collage)
        # 选择服务类型
        self.create_order.select_server_type(serverType)
        # 选择预约时间和时间段
        # self.create_order.input_orderTime()
        # 选择家电品牌
        self.create_order.input_brands(brands)
        # 选择产品大类
        self.create_order.select_product_big_kinds(big_kinds)
        # 选择家电品类
        self.create_order.select_product_kinds(kinds)
        # 选择小类
        self.create_order.select_product_small_kinds(small_kinds)

    @ddt.data(*ddt_data)
    @myDecorator.skipped_case
    def test_create_order001(self,ddt_data):
        """网点新建订单测试用例脚本"""

        # 打印测试用例名称
        self.base.print_case_name(ddt_data)
        # 获取订单信息
        name=ddt_data["用户姓名"]
        phoneNum=ddt_data["手机号"]
        serverAddress=ddt_data["服务地址"]
        collage=ddt_data["详细地址"]
        orderType=ddt_data["工单类型"]
        branchName=ddt_data["服务商"]
        serverType=ddt_data["服务类型"]
        brands=ddt_data["品牌"]
        big_kinds=ddt_data["大类"]
        kinds=ddt_data["品类"]
        small_kinds=ddt_data["小类"]
        self.public_operation(name,phoneNum,serverAddress,orderType,collage,serverType,
                              brands,big_kinds,kinds,small_kinds,branchName)
        # 点击保存按钮
        self.create_order.click_save_btn()
        self.base.sleep(1)
        Msg = self.login.get_system_msg()
        # 断言结果
        self.assert_mode.assert_equal(ddt_data,Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_014"),"-跳过不执行该用例")
    def test_create_order002(self):
        """添加订单页面智能文本为空校验"""

        # 进入添加订单页面
        self.create_order.enter_create_order_url()
        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_014")
        # 加载用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 点击打开输入智能识别的按钮
        self.create_order.click_recognition_btn()
        # 点击提交识别文本
        self.create_order.click_recognition_submit()
        self.base.sleep(1)
        # 获取系统提示信息
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data, Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_015"),"-跳过不执行该用例")
    def test_create_order003(self):
        """添加订单页面智能文本成功下单校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_015")
        # 加载用例名称
        self.base.print_case_name(data)
        # 刷新页面
        self.base.refresh_page()
        # 点击打开输入智能识别的按钮
        self.create_order.click_recognition_btn()
        # 输入文本
        self.create_order.input_text_recognition(data["只能识别文本"])
        # 点击提交识别文本
        self.create_order.click_recognition_submit()
        self.base.sleep(1)
        # 点击保存按钮
        self.create_order.click_save_btn()
        # 获取系统提示信息
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data, Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_016"),"-跳过不执行该用例")
    def test_create_order004(self):
        """添加工单页面重置功能校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_016")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取订单信息
        name = data["用户姓名"]
        phoneNum=data["手机号"]
        serverAddress=data["服务地址"]
        collage=data["详细地址"]
        orderType=data["工单类型"]
        branchName=data["服务商"]
        serverType=data["服务类型"]
        brands=data["品牌"]
        big_kinds=data["大类"]
        kinds=data["品类"]
        small_kinds=data["小类"]
        self.public_operation(name,phoneNum,serverAddress,orderType,collage,serverType,
                              brands,big_kinds,kinds,small_kinds,branchName)
        # 点击重置按钮
        self.create_order.click_reset_btn()
        # 点击保存
        self.create_order.click_save_btn()
        self.base.sleep(1)
        Msg = self.login.get_system_msg()
        # 断言
        self.assert_mode.assert_equal(data,Msg)

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_017"),"-跳过不执行该用例")
    def test_create_order005(self):
        """直接派单功能校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_017")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取订单信息
        name = data["用户姓名"]
        phoneNum = data["手机号"]
        serverAddress = data["服务地址"]
        collage = data["详细地址"]
        orderType = data["工单类型"]
        branchName = data["服务商"]
        serverType = data["服务类型"]
        brands = data["品牌"]
        big_kinds = data["大类"]
        kinds = data["品类"]
        small_kinds = data["小类"]
        self.public_operation(name,phoneNum,serverAddress,orderType,collage,serverType,
                              brands,big_kinds,kinds,small_kinds,branchName)
        # 点击直接派单
        self.create_order.click_please_btn()
        self.base.sleep(1)
        # 获取派单师傅
        master = rwConfig.read_config_data('T西安好家帮家政有限公司','master001')
        # 选择师傅派单
        self.send_order.select_send_page(pageName=master)
        # 点击确定
        self.send_order.click_confirm_btn()
        self.base.sleep(1)
        # 断言
        self.assert_mode.assert_equal(data,self.login.get_system_msg())

    @unittest.skipUnless(read_excel.get_isRun_text("create_order_018"),"-跳过不执行该用例")
    def test_create_order006(self):
        """添加订单页面添加并继续功能校验"""

        # 获取测试数据
        data = self.read_excel.get_dict_data("create_order_018")
        # 打印测试用例名称
        self.base.print_case_name(data)
        # 获取订单信息
        name = data["用户姓名"]
        phoneNum = data["手机号"]
        serverAddress = data["服务地址"]
        collage = data["详细地址"]
        orderType = data["工单类型"]
        branchName = data["服务商"]
        serverType = data["服务类型"]
        brands = data["品牌"]
        big_kinds = data["大类"]
        kinds = data["品类"]
        small_kinds = data["小类"]
        self.public_operation(name,phoneNum,serverAddress,orderType,collage,serverType,
                              brands,big_kinds,kinds,small_kinds,branchName)
        # 点击添加并继续
        self.create_order.click_save_and_add()
        self.base.sleep(1)
        # 获取table是否关闭
        isTrue = self.create_order.create_title_is_displayed()
        msg = self.login.get_system_msg()
        # # 断言
        self.assert_mode.assert_equal(data,msg)
        self.assert_mode.assert_el_in_page(data,isTrue)

    @classmethod
    def tearDownClass(cls):
        # 清除缓存
        cls().base.clear_catch()
        # 退出浏览器
        cls().base.quit_browser()


if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestLoader().loadTestsFromTestCase(Create_Order)

    unittest.TextTestRunner().run(suit)
