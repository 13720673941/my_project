# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Common import Driver,Logger
from Common import Pubilc,TestResult
from Page.WAPbranch import Branch
from Page.WAPbrands import Brands
from Page.PCbrands import PC_Brands
from Page.WAPmaster import Master
from Page.WAPmenhu import PPMenHu
import unittest,configparser

'''
【WAP门户下单派单流程】
设置手动派单->WAP门户下品牌单->PC品牌商查找订单编号->WAP品牌商审核派单(门户、品牌商订单状态校验)->网点接单(接单校验,门户、品牌商订单状态校验)
->网点派单师傅(门户、品牌商订单状态校验)->师傅预约订单(品牌商订单状态校验)->师傅上门(品牌商订单状态校验)->师傅完成服务(品牌商订单状态校验)
->师傅收款(门户、品牌商订单状态校验)
'''

isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取配置文件路径
        DataPath = Pubilc.data_dir(filename="OrderMessage.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding="utf-8")

        #设置日志保存路径
        logDirPath = Pubilc.data_dir(file="Log",filename="Brands_OrderFlow03.txt")
        Logger.setFormatter(logFile=logDirPath)

        #默认脚本执行状态
        self.success="Fail"

    def test_PleaseOrder(self):

        '''【WAP门户订单流程】：设置手动派单->WAP门户下品牌单->PC品牌商查找订单编号->WAP品牌商审核派单(门户、品牌商订单状态校验)->网点接单(接单校验,门户、品牌商订单状态校验)->网点派单师傅(门户、品牌商订单状态校验)->师傅预约订单(品牌商订单状态校验)->师傅上门(品牌商订单状态校验)->师傅完成服务(品牌商订单状态校验)->师傅收款(门户、品牌商订单状态校验)'''

        #------------------------------------------------【PC品牌登录】--------------------------------------------------
        #PC品牌登录
        self.PCDriver = Driver.PC_Brower()
        PCHandle = PC_Brands.PCbrands_login(self.PCDriver,'PPS_Login','pps_username','pps_password')
        PC_Brands.PCbrands_SetAddOrder(self.PCDriver,ddfrom='WAP端',model='shou')

        #------------------------------------------------【WAP门户下单】--------------------------------------------------
        #WAP品牌登录
        self.WAPDriver = Driver.WAP_Brower()
        PPHandle = Brands.PPS_login(self.WAPDriver,"PPS_Login","pps_username","pps_password")
        #WAP门户登录
        MHHandle = PPMenHu.MenHu_login(driver=self.WAPDriver,PCdriver=self.PCDriver)
        #WAP门户添加订单
        url = 'http://www.51shouhou.cn/brands3/haodi3/index.php/Home/Reserve/index'
        serverType = self.cf.get("MenHu_OrderMsg","服务类型")
        product = self.cf.get("MenHu_OrderMsg","产品信息")
        JSTM = self.cf.get("MenHu_OrderMsg","机身条码")
        buyPlace = self.cf.get("MenHu_OrderMsg","购买渠道")
        txtRemark = self.cf.get("MenHu_OrderMsg","备注")
        serverAddress = self.cf.get("MenHu_OrderMsg","服务地址")
        addInfo = self.cf.get("MenHu_OrderMsg","具体地址")
        use = self.cf.get("MenHu_OrderMsg","姓名")
        phe = self.cf.get("MenHu_OrderMsg","联系电话")
        PPMenHu.MenHu_AddOrder(self.WAPDriver,url,serverType,product,JSTM,buyPlace,txtRemark,serverAddress,addInfo,use,phe)

        #------------------------------------------------【WAP门户下单校验】----------------------------------------------
        #查找新建订单编号
        self.PCDriver.switch_to.window(PCHandle)
        NewAddOrderNum = PC_Brands.PCbrands_FindOrdernum(self.PCDriver,DD_Status="待审核")
        #门户订单新建订单门户端校验
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="待审核")

        #------------------------------------------------【WAP品牌商派单】------------------------------------------------
        #WAP品牌商派单
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PleaseOrder(self.WAPDriver,OrderNumber=NewAddOrderNum,PDmodel="zi",WDname="测试网点01")
        #PC端订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status="等待网点派单",ExceptWD="测试网点01")
        #WAP门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="等待网点派单")

        #------------------------------------------------【WAP网点派单】--------------------------------------------------
        #WAP网点登录
        Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver)
        #网点接单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=NewAddOrderNum)
        #网点派单到师傅
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=NewAddOrderNum,sfName="张先生")
        #PC端订单状态校验
        self.PCDriver.switch_to.window(PCHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status="等待师傅预约",ExceptSF="张先生")
        #WAP门户订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="等待师傅预约")

        #----------------------------------------------【WAP师傅完成服务】------------------------------------------------
        #WAP师傅登录
        SFHandle = Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #==WAP师傅预约上门时间==
        Master.SF_Order(self.WAPDriver,OrderNumber=NewAddOrderNum)
        #【等待师傅服务】门户订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="等待师傅服务")
        #【等待师傅服务】订单状态校验
        self.PCDriver.switch_to.window(PCHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='等待师傅服务')
        #==WAP师傅上门打卡==
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_DaKa(self.WAPDriver,OrderNumber=NewAddOrderNum)
        #【师傅服务中】门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="师傅服务中")
        #【师傅服务中】订单状态校验
        self.PCDriver.switch_to.window(PCHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='师傅服务中')
        #==WAP师傅处理工单,保存服务内容==
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_Sheet(self.WAPDriver,OrderNumber=NewAddOrderNum)
        #【师傅服务中】门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="师傅服务中")
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='师傅服务中')
        # ==WAP师傅使用备件信息==
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_UseBJ(self.WAPDriver)
        #【师傅服务中】门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="师傅服务中")
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='师傅服务中')
        #==WAP师傅提交服务报价信息==
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_SubmitPay(self.WAPDriver)
        #【等待收款】门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="等待收款")
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='等待收款')
        #==WAP师傅收款==
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_ShouKuan(self.WAPDriver,OrderNumber=NewAddOrderNum)
        #【等待收款】门户端订单状态校验
        self.WAPDriver.switch_to.window(MHHandle)
        PPMenHu.MenHu_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus="等待品牌商结算")
        #【待品牌商结算】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=NewAddOrderNum,DD_Status='等待品牌商结算')
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=NewAddOrderNum,CheckOrderStatus='等待结算')

        #脚本执行成功
        self.success = "Pass"

    def tearDown(self):

        #推出浏览器
        self.WAPDriver.quit()
        self.PCDriver.quit()
        Logger.removeHandler()
        #写入测试结果
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case="Brands_OrderFlow03", run_result=self.success, isWrite=isWrite)
        #写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow03',run_result=self.success)

if __name__ == '__main__':
    unittest.main(verbosity=2)