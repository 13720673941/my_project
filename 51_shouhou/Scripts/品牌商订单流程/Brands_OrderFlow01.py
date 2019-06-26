# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/4 11:38

from Common import Driver,Logger
from Common import Pubilc,TestResult
from Page.WAPbranch import Branch
from Page.WAPbrands import Brands
from Page.PCbrands import PC_Brands
from Page.WAPmaster import Master
from Page.WAPuser import HDServer
import unittest,configparser

'''
【WAP用户端品牌商订单流程】
品牌商设置手动派单->用户WAP端添加品牌商订单(品牌、用户订单校验)->WAP品牌派单(品牌、用户订单校验)->WAP网点接单校验->WAP网点派单(品牌、用户订单校验)
->师傅预约订单(品牌、网点订单校验)->师傅上门(品牌、网点订单校验)->师傅打卡->师傅填写工单->师傅收款(品牌、用户订单状态校验)->师傅完成服务(品牌、网点订单状态校验)
'''

isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #读取配置文件信息
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #设置日志保存路径文件名
        Logger.setFormatter(logFile=Pubilc.data_dir(file='Log',filename='Brands_OrderFlow01.txt'))

        #默认脚本执行失败
        self.success = 'Fail'

    def test_PleaseOrder(self):

        '''【WAP用户端订单流程】：品牌商设置手动派单->用户WAP端添加品牌商订单(品牌、用户订单校验)->WAP品牌派单(品牌、用户订单校验)->WAP网点接单校验->WAP网点派单(品牌、用户订单校验)->师傅预约订单(品牌、网点订单校验)->师傅上门(品牌、网点订单校验)->师傅打卡->师傅填写工单->师傅收款(品牌、用户订单状态校验)->师傅完成服务(品牌、网点订单状态校验)'''

        #设置PC端浏览器的驱动
        self.PCDriver = Driver.PC_Brower()
        #PC端品牌商登录
        PCHandle = PC_Brands.PCbrands_login(self.PCDriver,'PPS_Login','pps_username','pps_password')
        #设置品牌商派单方式
        PC_Brands.PCbrands_SetAddOrder(self.PCDriver,ddfrom='WAP端',model='shou')
        #设置WAP端浏览器驱动
        self.WAPDriver = Driver.WAP_Brower()
        #WAP品牌商登录
        PPHandle = Brands.PPS_login(self.WAPDriver,'PPS_Login','pps_username','pps_password')

        #---------------------------------------------【WAP用户端新建订单】-------------------------------------------------
        #WAP用户端登陆
        HDHandle = HDServer.User_login(self.WAPDriver,HT_driver=self.PCDriver)
        #WAP用户端添加订单
        WDName = self.cf.get('User_OrderMsg','网点名称')
        PPName = self.cf.get('User_OrderMsg','授权品牌')
        serverType = self.cf.get('User_OrderMsg','服务类型')
        product = self.cf.get('User_OrderMsg','产品信息')
        XHInfo = self.cf.get('User_OrderMsg','产品型号')
        JSTM = self.cf.get('User_OrderMsg','机身条码')
        buyTime = self.cf.get('User_OrderMsg','购买时间')
        NewAddress = self.cf.get('User_OrderMsg','地址')
        NewUser = self.cf.get('User_OrderMsg','联系人1')
        NewPhe = self.cf.get('User_OrderMsg','电话')
        use = self.cf.get('User_OrderMsg','联系人')
        phe = self.cf.get('User_OrderMsg','联系电话')
        BeiZhu = self.cf.get('User_OrderMsg','备注')
        HDServer.User_AddOrder(self.WAPDriver,WDName,PPName,serverType,product,XHInfo,JSTM,buyTime,NewAddress,NewUser,NewPhe,use,phe,BeiZhu)
        #PC端查找订单单号信息
        self.PCDriver.switch_to.window(PCHandle)
        AddOrderNumber = PC_Brands.PCbrands_FindOrdernum(self.PCDriver,DD_Status='待审核')
        #用户端等待状态校验
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待品牌商审核')
        #WAP品牌端订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待审核')

        #---------------------------------------------------【WAP品牌派单】----------------------------------------------
        #WAP品牌商派单到网点：测试网点01
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,PDmodel='zi',WDname='测试网点01')
        #【等待网点派单】品牌、用户端订单状态校验
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待网点派单')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待网点派单')

        #---------------------------------------------------【WAP网点派单】----------------------------------------------
        #WAP网点登陆
        Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=AddOrderNumber)
        #WAP网点派单到师傅：张先生
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,sfName='张先生')
        #【待师傅预约】品牌、用户端等待状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')

        #--------------------------------------------------【师傅处理订单】----------------------------------------------
        #师傅登陆
        SFHandle = Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #师傅预约订单
        Master.SF_Order(self.WAPDriver,OrderNumber=AddOrderNumber)
        #【待师傅服务】品牌、用户端订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅服务')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅服务')
        #师傅上门打卡
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_DaKa(self.WAPDriver,OrderNumber=AddOrderNumber)
        #【师傅服务中】品牌、用户端订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='师傅服务中')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='师傅服务中')
        #师傅填写工单
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_Sheet(self.WAPDriver,OrderNumber=AddOrderNumber)
        #师傅使用备件(不使用备件直接下一步)
        Master.SF_UseBJ(self.WAPDriver)
        #师傅提交服务报价
        Master.SF_SubmitPay(self.WAPDriver)
        #【等待收款】品牌、用户端订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待收款')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待收款')
        #师傅收款
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_ShouKuan(self.WAPDriver,OrderNumber=AddOrderNumber)
        #【等待品牌商结算】品牌、用户订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待品牌商结算')
        self.WAPDriver.switch_to.window(HDHandle)
        HDServer.User_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待品牌商结算')
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待结算')

        #脚本执行成功
        self.success='Pass'

    def tearDown(self):

        #推出浏览器
        self.PCDriver.quit()
        self.WAPDriver.quit()
        Logger.removeHandler()
        #写入测试结果
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow01', run_result=self.success, isWrite=isWrite)
        # 写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow01',run_result=self.success)

if __name__ == '__main__':
    unittest.main(verbosity=2)


















