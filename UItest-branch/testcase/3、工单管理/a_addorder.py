#-*- coding: utf-8 -*-

#@Author  : Mr.Deng
#@Time    : 2019/5/30 18:21

from public.common import rwconfig,mytest
from config.pathconfig import *
from public.common.assertmode import Assert
from public.common import driver,getdata,writetestresult
from public.page.addorderpage import AddOrderPage
from public.page.pleaseorderpage import PleaseOrderPage
from public.page.loginpage import LoginPage
from public.common.basepage import BasePage
import unittest,ddt
'''
网点添加订单测试用例脚本：
1、新建订单-联系人为空校验 2、新建订单-联系方式为空校验 3、新建订单-服务地址为空校验 4、新建订单-选择服务商为空校验
5、新建订单-服务类型为空校验 6、新建订单-家电品牌为空校验 7、新建订单-家电品类为空校验 8、新建订单-手机号左边界值校验
9、新建订单-手机号右边界值校验 10、新建订单-手机号格式校验 11、新建订单-下单成功校验 12、新建订单-添加需返单订单校验
13、新建订单-添加仅报单订单校验 14、新建订单-智能文本识别为空校验 15、新建订单-智能文本识别功能校验 16、新建订单-添加订单重置功能校验
17、新建订单-直接派单功能校验 18、新建订单-保存并继续添加订单功能校验
'''
#获取添加订单信息数据
Data1 = getdata.get_test_data()["CreateOrder"]["CreateData"]
Data2 = getdata.get_test_data()["CreateOrder"]["TextRecognition"]
#默认写入执行结果
isWrite=True
@ddt.ddt
class Add_Order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #设置浏览器驱动
        cls.dr = driver.browser_driver()
        #实例化
        cls.basePage = BasePage(cls.dr)
        cls.addOrderPage = AddOrderPage(cls.dr)
        cls.loginPage = LoginPage(cls.dr)
        cls.pleaseOrder = PleaseOrderPage(cls.dr)
        cls.assert_mode = Assert(cls.dr)
        #开始
        mytest.start_test()
        #获取网点登录数据
        UserName = rwconfig.read_config_data('蓝魔科技','username')
        PassWord = rwconfig.read_config_data('蓝魔科技','password')
        #网点登录
        cls.loginPage.login_main(UserName,PassWord)
        cls.basePage.sleep(2)

    def setUp(self):
        #进入添加订单页面
        self.addOrderPage.enter_create_order_url()
        #刷新页面
        self.basePage.refresh_page()

    @ddt.data(*Data1)
    def test_addOrder001(self,Data1):
        '''网点新建订单测试用例脚本'''
        #打印测试用例名称
        self.basePage.print_case_name(Data1["CaseName"])
        self.basePage.refresh_page()
        #等待页面加载
        self.basePage.wait()
        #输入联系人名称
        self.addOrderPage.input_username(name=Data1["username"])
        #输入联系方式
        self.addOrderPage.input_phoneNum(phoneNum=Data1["PhoneNum"])
        #选择服务地址
        self.addOrderPage.select_server_address(serverAddress=Data1["ServerAddress"])
        #输入详细地址
        self.addOrderPage.input_add_collage(collage=Data1["Collage"])
        #选择工单类型
        self.addOrderPage.select_order_type(orderType=Data1["OrderType"],branchName=Data1["Branch"])
        #选择服务类型
        self.addOrderPage.select_server_type(serverType=Data1["ServerType"])
        #选择预约时间和时间段
        self.addOrderPage.input_orderTime()
        #选择家电品牌
        self.addOrderPage.input_brands(brands=Data1["Brands"])
        #选择家电品类
        self.addOrderPage.input_kinds(kinds=Data1["Kinds"])
        # #输入产品型号
        # self.addOrderPage.input_productNum()
        # #输入内机条码
        # self.addOrderPage.input_in_phoneNum()
        # #输入外机条码
        # self.addOrderPage.input_out_phoneNum()
        # #输入购买时间
        # self.addOrderPage.select_buyTime()
        # #选择购买渠道
        # self.addOrderPage.select_buyPlace()
        # #选择信息来源
        # self.addOrderPage.select_info_from()
        # #输入服务描述信息
        # self.addOrderPage.input_remark()
        # #上传图片
        # self.addOrderPage.update_picture()
        #点击保存按钮
        self.addOrderPage.click_save_btn()
        self.basePage.sleep(2)
        #断言结果
        isSuccess = self.assert_mode.assert_equal(Data1["expect"],self.basePage.get_system_msg())
        #写入订单单号
        if Data1["expect"] == '创建成功':
            #获取创建成功的订单单号
            sec = ''
            OrderNumber = ''
            if '11' in Data1["CaseName"]:
                sec = 'NotReturnOrder'
                OrderNumber = self.basePage.get_order_number()
            elif '13' in Data1["CaseName"]:
                sec = 'ReturnOrder'
                OrderNumber = self.basePage.get_order_number()
            elif '12' in Data1["CaseName"]:
                sec = 'OnlyInsteadOrder'
                OrderNumber = self.basePage.get_order_number(insteadOrder=True)
                #写入配置文件orderNumber中
            rwconfig.write_config_data(sec,'id',OrderNumber,orderNumPath)
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data1["CaseName"])

    @ddt.data(*Data2)
    def test_addOrder002(self,Data2):
        '''添加订单页面智能文本识别功能跳转校验'''
        #加载用例名称
        self.basePage.print_case_name(Data2["CaseName"])
        #点击打开输入智能识别的按钮
        self.addOrderPage.click_recognition_btn()
        #等待页面加载
        self.basePage.wait()
        #输入之内识别文本
        self.addOrderPage.input_text_recognition(textRecognition=Data2["TextMsg"])
        #点击提交识别文本
        self.addOrderPage.click_recognition_submit()
        self.basePage.sleep(1)
        #点击保存
        if '15' in Data2["CaseName"]:
            self.addOrderPage.click_save_btn()
        #断言
        isSuccess = self.assert_mode.assert_equal(Data2["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data2["CaseName"])

    def test_addOrder003(self):
        '''添加工单页面重置功能校验'''
        #获取测试数据
        Data = getdata.get_test_data()["CreateOrder"]["ResetFunction"]
        #打印测试用例名称
        self.basePage.print_case_name(Data["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #等待页面加载
        self.basePage.wait()
        #输入联系人名称
        self.addOrderPage.input_username(name=Data["username"])
        #输入联系方式
        self.addOrderPage.input_phoneNum(phoneNum=Data["PhoneNum"])
        #选择服务地址
        self.addOrderPage.select_server_address(serverAddress=Data["ServerAddress"])
        #输入详细地址
        self.addOrderPage.input_add_collage(collage=Data["Collage"])
        #选择工单类型
        self.addOrderPage.select_order_type(orderType=Data["OrderType"],branchName=Data["Branch"])
        #选择服务类型
        self.addOrderPage.select_server_type(serverType=Data["ServerType"])
        #选择家电品牌
        self.addOrderPage.input_brands(brands=Data["Brands"])
        #选择家电品类
        self.addOrderPage.input_kinds(kinds=Data["Kinds"])
        #点击重置按钮
        self.addOrderPage.click_reset_btn()
        #点击保存
        self.addOrderPage.click_save_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data["CaseName"])

    def test_addOrder004(self):
        '''直接派单功能校验'''
        #获取测试数据
        Data = getdata.get_test_data()["CreateOrder"]["DirectPleaseOrder"]
        #打印测试用例名称
        self.basePage.print_case_name(Data["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #等待页面加载
        self.basePage.wait()
        #输入联系人名称
        self.addOrderPage.input_username(name=Data["username"])
        #输入联系方式
        self.addOrderPage.input_phoneNum(phoneNum=Data["PhoneNum"])
        #选择服务地址
        self.addOrderPage.select_server_address(serverAddress=Data["ServerAddress"])
        #输入详细地址
        self.addOrderPage.input_add_collage(collage=Data["Collage"])
        #选择工单类型
        self.addOrderPage.select_order_type(orderType=Data["OrderType"], branchName=Data["Branch"])
        #选择服务类型
        self.addOrderPage.select_server_type(serverType=Data["ServerType"])
        #选择家电品牌
        self.addOrderPage.input_brands(brands=Data["Brands"])
        #选择家电品类
        self.addOrderPage.input_kinds(kinds=Data["Kinds"])
        #点击直接派单
        self.addOrderPage.click_please_btn()
        self.basePage.sleep(1)
        #获取派单师傅
        master = rwconfig.read_config_data('蓝魔科技','master001')
        #选择师傅派单
        self.pleaseOrder.select_please_page(page_name=master)
        #点击确定
        self.pleaseOrder.click_confirm_btn()
        self.basePage.sleep(1)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data["expect"],self.basePage.get_system_msg())
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data["CaseName"])

    def test_addOrder005(self):
        '''添加订单页面添加并继续功能校验'''
        #获取测试数据
        Data = getdata.get_test_data()["CreateOrder"]["SaveAndAddOrder"]
        #打印测试用例名称
        self.basePage.print_case_name(Data["CaseName"])
        #刷新页面
        self.basePage.refresh_page()
        #等待页面加载
        self.basePage.wait()
        #输入联系人名称
        self.addOrderPage.input_username(name=Data["username"])
        #输入联系方式
        self.addOrderPage.input_phoneNum(phoneNum=Data["PhoneNum"])
        #选择服务地址
        self.addOrderPage.select_server_address(serverAddress=Data["ServerAddress"])
        #输入详细地址
        self.addOrderPage.input_add_collage(collage=Data["Collage"])
        #选择工单类型
        self.addOrderPage.select_order_type(orderType=Data["OrderType"], branchName=Data["Branch"])
        #选择服务类型
        self.addOrderPage.select_server_type(serverType=Data["ServerType"])
        #选择家电品牌
        self.addOrderPage.input_brands(brands=Data["Brands"])
        #选择家电品类
        self.addOrderPage.input_kinds(kinds=Data["Kinds"])
        #点击添加并继续
        self.addOrderPage.click_save_and_add()
        self.basePage.sleep(1)
        #获取table是否关闭
        isTrue = self.addOrderPage.create_title_is_displayed()
        msg = self.basePage.get_system_msg()
        ##断言
        isSuccess1 = self.assert_mode.assert_equal(Data["expect"],msg)
        isSuccess2 = self.assert_mode.assert_el_in_page(isTrue)
        #并列条件判断
        if isSuccess1 == 'PASS' and isSuccess2 == 'PASS':
            isSuccess = 'PASS'
        else:
            isSuccess = 'FAIL'
        #写入测试结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data["CaseName"])

    def test_addOrder006(self):
        '''打印工单页面跳转'''
        #获取测试数据
        Data = getdata.get_test_data()["CreateOrder"]["PrintOrderInfo"]
        #打印用例名称
        self.basePage.print_case_name(Data["CaseName"])
        self.basePage.sleep(1)
        #进入全部工单列表
        self.basePage.open_url(getdata.get_test_data()["PleaseOrder"]["PleaseUrl"])
        self.basePage.refresh_page()
        #获取工单单号
        order_number = rwconfig.read_config_data('ReturnOrder','id',orderNumPath)
        #进入工单详情页
        self.basePage.open_order_message(order_number)
        #获取旧的窗口句柄
        old_handle = self.basePage.get_current_handle()
        #点击打印
        self.addOrderPage.print_order_info()
        #获取所有窗口句柄
        all_handle = self.basePage.get_all_handles()
        #切换窗口
        self.basePage.switch_window_handle(all_handle,old_handle)
        #断言
        isSuccess = self.assert_mode.assert_equal(Data["expect"],self.basePage.get_title())
        #写入结果
        writetestresult.write_test_result(isWrite,isSuccess,'AddOrder',Data["CaseName"])

    @classmethod
    def tearDownClass(cls):
        #退出浏览器
        cls.basePage.quit_browser()
        mytest.end_test()

if __name__ == '__main__':
    unittest.main()

    suit = unittest.TestSuite()
    suit.addTest(Add_Order("test_addOrder001"))
    suit.addTest(Add_Order("test_addOrder002"))
    suit.addTest(Add_Order("test_addOrder003"))
    suit.addTest(Add_Order("test_addOrder004"))
    suit.addTest(Add_Order("test_addOrder005"))
    unittest.TextTestRunner().run(suit)

