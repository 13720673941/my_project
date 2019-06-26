# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/8 12:46

from Common import Driver,Logger,Pubilc
from Common import TestResult
from Page.PCbrands import PC_Brands
from Page.PCbranch import PC_Branch
from Page.WAPbrands import Brands
from Page.WAPbranch import Branch
from Page.WAPmaster import Master
import unittest,configparser

'''
【PC端网点添加品牌商订单流程】
品牌商设置手动派单->网点添加品牌商订单->PC/WAP品牌商订单校验获取单号->WAP品牌商派单(WAP品牌商订单状态校验)->WAP网点接单校验
->WAP网点派单师傅(品牌商/网点订单状态校验)->师傅接单校验->师傅预约订单(品牌网点订单状态校验)->师傅上门打卡->师傅处理工单
->师傅提交服务报价(品牌网点订单状态校验)
'''

isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取订单信息配置文件
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #设置日志保存路径
        logDirPath = Pubilc.data_dir(file='Log',filename='Brands_OrderFlow06.txt')
        Logger.setFormatter(logFile=logDirPath)

        #初始化脚本执行结果
        self.success='Fail'

    def test_PleaseOrder(self):

        '''【网点添加品牌商订单流程】:品牌商设置手动派单->网点添加品牌商订单->PC/WAP品牌商订单校验获取单号->WAP品牌商派单(WAP品牌商订单状态校验)->WAP网点接单校验->WAP网点派单师傅(品牌商/网点订单状态校验)->师傅接单校验->师傅预约订单(品牌网点订单状态校验)->师傅上门打卡->师傅处理工单->师傅提交服务报价(品牌网点订单状态校验)'''

        #PC品牌商登陆设置派单方式
        self.PCDriver = Driver.PC_Brower()
        PCHandle = PC_Brands.PCbrands_login(self.PCDriver,'PPS_Login','pps_username','pps_password')
        #设置派单方式
        PC_Brands.PCbrands_SetAddOrder(self.PCDriver,ddfrom='网点提交',model='shou')

        #-------------------------------------------【PC网点添加品牌订单】------------------------------------------------
        #PC网点登陆
        PC_Branch.PCbranch_login(self.PCDriver,'WD_Login','wd_username1','wd_password1')
        #PC网点添加订单
        username = self.cf.get('PC_BranchOrderMessage','联系人')
        Phonenums = self.cf.get('PC_BranchOrderMessage','联系方式1')
        address = self.cf.get('PC_BranchOrderMessage','服务地址')
        collage = self.cf.get('PC_BranchOrderMessage','详细地址')
        server = self.cf.get('PC_BranchOrderMessage','服务类型')
        product = self.cf.get('PC_BranchOrderMessage','产品信息')
        JSNumbers = self.cf.get('PC_BranchOrderMessage','机身条码')
        AddOrderInfo = self.cf.get('PC_BranchOrderMessage','备注')
        PPName = self.cf.get('PC_BranchOrderMessage','订单来源')
        PC_Branch.PCbranch_AddOrder(self.PCDriver,username,Phonenums,address,collage,server,product,JSNumbers,AddOrderInfo,PPName)

        #---------------------------------------------【WAP品牌商订单校验派单】-------------------------------------------
        #设置WAP端浏览器驱动
        self.WAPDriver = Driver.WAP_Brower()
        #WAP品牌商登陆
        PPHandle = Brands.PPS_login(self.WAPDriver,'PPS_Login','pps_username','pps_password')
        #获取订单编号
        AddOrderNumber = Brands.FindOrderNumber(self.WAPDriver)
        #WAP品牌商订单状态校验
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待审核')
        #WAP品牌商派单
        Brands.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,PDmodel='zi',WDname='测试网点01')
        #WAP品牌商订单状态校验
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待网点派单')

        #---------------------------------------------【WAP网点订单校验派单】--------------------------------------------
        #WAP网点登陆
        WDHandle = Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=AddOrderNumber)
        #WAP网点派单到师傅
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,sfName='张先生')
        #WAP网点订单状态校验
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待预约')
        #WAP品牌订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')

        #-----------------------------------------------【师傅端处理工单】-----------------------------------------------
        #师傅登陆
        SFHandle = Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #师傅接单校验
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')
        #师傅预约订单
        Master.SF_Order(self.WAPDriver, OrderNumber=AddOrderNumber)
        #师傅上门打卡
        Master.SF_DaKa(self.WAPDriver, OrderNumber=AddOrderNumber)
        #师傅填写工单
        Master.SF_Sheet(self.WAPDriver, OrderNumber=AddOrderNumber)
        #师傅使用备件(不使用备件直接下一步)
        Master.SF_UseBJ(self.WAPDriver)
        #师傅提交服务报价
        Master.SF_SubmitPay(self.WAPDriver)
        #师傅收款
        Master.SF_ShouKuan(self.WAPDriver, OrderNumber=AddOrderNumber)
        #待结算校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver, CheckOrderNumber=AddOrderNumber, CheckOrderStatus='等待品牌商结算')
        self.WAPDriver.switch_to.window(WDHandle)
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待结算')
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_CheckOrderStatus(self.WAPDriver, CheckOrderNumber=AddOrderNumber, CheckOrderStatus='等待结算')

        #默认脚本执行成功
        self.success='Pass'

    def tearDown(self):

        #推出浏览器
        self.PCDriver.quit()
        self.WAPDriver.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow06', run_result=self.success, isWrite=isWrite)
        # 写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow06',run_result=self.success)

if __name__ == '__main__':
    unittest.main(verbosity=2)