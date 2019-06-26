# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/17 11:06

from Common import Driver,Logger,Pubilc,TestResult
from Page.PCbranch import PC_Branch
from Page.WAPbranch import Branch
from Page.WAPmaster import Master
import unittest,configparser

'''
【网点订单流程】
PC网点下单->WAP网点接单校验->网点订单状态校验->网点派单师傅->网点订单状态校验->师傅接单校验->师傅订单状态校验->师傅预约(网点订单状态校验)
->师傅上门(网点订单状态校验)->师傅完成工单(网点订单状态校验)->师傅订单状态校验
'''

isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #读取网点订单配置文件
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #日志写入路径
        logDirPath = Pubilc.data_dir(file='Log',filename='Branch_OrderFlow01.txt')
        #写入日志
        Logger.setFormatter(logFile=logDirPath)

        #默认测试结果
        self.success='Fail'

    def test_PleaseOrder(self):

        '''【网点订单流程】:PC网点下单->WAP网点接单校验->网点订单状态校验->网点派单师傅->网点订单状态校验->师傅接单校验->师傅订单状态校验->师傅预约(网点订单状态校验)->师傅上门(网点订单状态校验)->师傅完成工单(网点订单状态校验)->师傅订单状态校验'''

        #-------------------------------------------【PC网点添加订单】---------------------------------------------------
        #设置PC端浏览器驱动
        self.PCDriver = Driver.PC_Brower()
        #PC网点登陆
        PCBranchHandle = PC_Branch.PCbranch_login(self.PCDriver,'WD_Login','wd_username1','wd_password1',wdHandle='new')
        #PC网点添加订单
        username = self.cf.get('PC_BranchOrderMessage','联系人')
        Phonenums = self.cf.get('PC_BranchOrderMessage','联系方式1')
        address = self.cf.get('PC_BranchOrderMessage','服务地址')
        collage = self.cf.get('PC_BranchOrderMessage','详细地址')
        server = self.cf.get('PC_BranchOrderMessage','服务类型')
        product = self.cf.get('PC_BranchOrderMessage','产品信息')
        JSNumbers = self.cf.get('PC_BranchOrderMessage','机身条码')
        AddOrderInfo = self.cf.get('PC_BranchOrderMessage','备注')
        PC_Branch.PCbranch_AddOrder(self.PCDriver,username,Phonenums,address,collage,server,product,JSNumbers,AddOrderInfo,OrderType='网点')
        #网点获取订单编号
        AddOrderNumber = PC_Branch.FindOrderNumber(self.PCDriver)

        #--------------------------------------------【WAP网点派单】-----------------------------------------------------
        #设置WAP驱动
        self.WAPDriver = Driver.WAP_Brower()
        #WAP网点登陆
        WDHandle = Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver,WDHandle='new')
        #网点收单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=AddOrderNumber)
        #网点订单状态校验
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待派单')
        #网点派单到师傅张先生
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,sfName='张先生')
        #网点订单状态校验
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待预约')

        #---------------------------------------------【师傅完成工单】---------------------------------------------------
        #师傅登陆
        SFHandle = Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #师傅接单校验
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')
        #师傅预约订单
        Master.SF_Order(self.WAPDriver,OrderNumber=AddOrderNumber)
        #网点订单状态校验
        self.WAPDriver.switch_to.window(WDHandle)
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待服务')
        #师傅确认上门工单
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_DaKa(self.WAPDriver,OrderNumber=AddOrderNumber)
        #网点订单状态校验
        self.WAPDriver.switch_to.window(WDHandle)
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='服务中')
        #师傅完成服务
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_Sheet(self.WAPDriver,OrderNumber=AddOrderNumber)
        #师傅不使用备件
        Master.SF_UseBJ(self.WAPDriver)
        #师傅提交服务报价
        Master.SF_SubmitPay(self.WAPDriver)
        #师傅收款
        Master.SF_ShouKuan(self.WAPDriver,OrderNumber=AddOrderNumber)
        #师傅订单状态校验
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待结算')
        #网点订单状态校验
        self.WAPDriver.switch_to.window(WDHandle)
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='已完成')

        #校验执行成功
        self.success='Pass'

    def tearDown(self):

        #退出浏览器
        self.PCDriver.quit()
        self.WAPDriver.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig('BranchOrderFlow',case='Branch_OrderFlow01',run_result=self.success,isWrite=isWrite)
        # 写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite, case='Branch_OrderFlow01', run_result=self.success)

if __name__ == '__main__':
    unittest.main(verbosity=2)