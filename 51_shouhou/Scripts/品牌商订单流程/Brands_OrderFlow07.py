# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Common import Driver,Logger,Pubilc
from Common import TestResult
from Page.PCbrands import PC_Brands
from Page.WAPbrands import Brands
from Page.WAPbranch import Branch
from Page.WAPmaster import Master
import unittest,configparser

'''
【WAP网点完成订单流程】
品牌商设置手动派单->订单审核派单到网点->网点接单校验->网点派单到师傅->师傅预约校验->网点派单校验->网点完成服务->品牌、网点、师傅订单结算校验
'''

isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取品牌商订单配置文件
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #设置日志文件写入路径
        logDirPath = Pubilc.data_dir(file='Log',filename='Brands_OrderFlow07.txt')
        #调用脚本
        Logger.setFormatter(logFile=logDirPath)

        #默认脚本执行状态
        self.success='Fail'

    def test_PleaseOrder(self):

        '''【WAP网点完成订单流程】:品牌商设置手动派单->订单审核派单到网点->网点接单校验->网点派单到师傅->师傅预约校验->网点派单校验->网点完成服务->品牌、网点、师傅订单结算校验'''

        #-----------------------------------------------【PC品牌商下单】--------------------------------------------------
        #设置浏览器
        self.PCDriver = Driver.PC_Brower()
        #PC品牌商登陆
        PC_Brands.PCbrands_login(self.PCDriver,'PPS_Login','pps_username','pps_password')

        #设置品牌商派单方式：手动派单
        PC_Brands.PCbrands_SetAddOrder(self.PCDriver,ddfrom='品牌商提交',model='shou')
        #品牌商添加订单
        url = 'http://www.51shouhou.cn/brands3/haodi3/index.php/Admin/Order/Order/addmerorder'
        phone = self.cf.get('PC_BrandsOrderMessage','联系方式')
        user = self.cf.get('PC_BrandsOrderMessage','联系人')
        address = self.cf.get('PC_BrandsOrderMessage','所在地区')
        area = self.cf.get('PC_BrandsOrderMessage','详细地址')
        server = self.cf.get('PC_BrandsOrderMessage','预约服务类型')
        BaoNW = self.cf.get('PC_BrandsOrderMessage','保内保外')
        ShouH = self.cf.get('PC_BrandsOrderMessage','售后类型')
        pro_mag = self.cf.get('PC_BrandsOrderMessage','产品信息')
        buytime = self.cf.get('PC_BrandsOrderMessage','购买时间')
        massage = self.cf.get('PC_BrandsOrderMessage','反馈情况')
        PC_Brands.PCbrands_AddOrder(self.PCDriver,url,phone,user,address,area,server,BaoNW,ShouH,pro_mag,buytime,massage)
        #【待审核】查询订单单号/校验添加订单成功订单状态
        AddOrderNumber = PC_Brands.PCbrands_FindOrdernum(self.PCDriver,DD_Status='待审核')

        #----------------------------------------------【WAP品牌商派单】-------------------------------------------------
        #设置WAP驱动
        self.WAPDriver = Driver.WAP_Brower()
        #WAP品牌商登陆
        PPHandle = Brands.PPS_login(self.WAPDriver,'PPS_Login','pps_username','pps_password')
        #WAP品牌商派单
        Brands.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,PDmodel='zi',WDname='测试网点01')

        #----------------------------------------------【WAP网点派单】--------------------------------------------------
        #WAP网点登陆
        WDHandle = Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=AddOrderNumber)
        #WAP网点派单
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,sfName='张先生')
        #WAP网点订单状态校验
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待预约')

        #------------------------------------------------【网点完成订单】------------------------------------------------
        #师傅登陆
        SFHandle = Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #师傅接单校验
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')
        #网点搜索订单
        self.WAPDriver.switch_to.window(WDHandle)
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,ButtonText='完成服务')
        #网点完成服务
        Branch.WD_FinishServer(self.WAPDriver,BJName='海尔自动化通用备件01',BJ_UseNumber=2)
        #网点订单结算校验
        Branch.WD_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='待结算')
        #师傅订单状态校验
        self.WAPDriver.switch_to.window(SFHandle)
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待结算')
        #品牌商订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待品牌商结算')

        #脚本执行成功
        self.success='Pass'

    def tearDown(self):

        #推出浏览器
        self.WAPDriver.quit()
        self.PCDriver.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow07',run_result=self.success,isWrite=isWrite)
        # 写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow07',run_result=self.success,NewLine=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)