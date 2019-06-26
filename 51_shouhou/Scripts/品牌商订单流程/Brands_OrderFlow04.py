# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Common import Logger
from Common import Pubilc
from Page.PCbrands import PC_Brands
from Page.WAPbrands import Brands
from Page.WAPbranch import Branch
from Page.WAPmaster import Master
from Page.KeFu import KeFu
from Common import Driver,TestResult
import configparser,unittest

"""
【品牌商派单回访流程】-该订单单号用于备件返厂；
【设置手动派单】->PC品牌商下单->下单验证->派单网点->派单验证(订单状态验证)->网点派单师傅->派单验证(订单状态验证)->
师傅预约订单(订单状态验证)->师傅上门(订单状态验证)->师傅服务(订单状态验证)->师傅完成订单(订单状态验证)->客服回访(回访验证)
"""
#默认为真写入测试结果
isWrite = True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取下单配置文件信息
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #配置日志写入路径
        logDirPath = Pubilc.data_dir(file="Log",filename="Brands_OrderFlow01.txt")

        #调用log脚本
        Logger.setFormatter(logFile=logDirPath)

        #判断脚本是否执行成功,默认为File,不写入测试结果
        self.success = 'Fail'

    def test_PleaseOrder(self):

        '''【WAP品牌商订单流程】：设置手动派单->PC品牌商下单->下单验证->派单网点->派单验证(订单状态验证)->网点派单师傅->派单验证(订单状态验证)->师傅预约订单(订单状态验证)->师傅上门(订单状态验证)->师傅服务(订单状态验证)->师傅完成订单(订单状态验证)->客服回访(回访验证)'''

        #-----------------------------------------------【PC品牌商下单】--------------------------------------------------
        #设置浏览器
        self.driver = Driver.PC_Brower()
        #PC品牌商登陆
        PCPPHandle = PC_Brands.PCbrands_login(self.driver,'PPS_Login','pps_username','pps_password')

        #设置品牌商派单方式：手动派单
        PC_Brands.PCbrands_SetAddOrder(self.driver,ddfrom='品牌商提交',model='shou')
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
        PC_Brands.PCbrands_AddOrder(self.driver,url,phone,user,address,area,server,BaoNW,ShouH,pro_mag,buytime,massage)

        #【待审核】查询订单单号/校验添加订单成功订单状态
        ordernumber = PC_Brands.PCbrands_FindOrdernum(self.driver,DD_Status='待审核')

        #------------------------------------------------【WAP品牌商派单】------------------------------------------------
        #WAP品牌商登陆设置wap浏览器driver
        self.dr = Driver.WAP_Brower()
        #WAP品牌商登陆
        PPHandle = Brands.PPS_login(self.dr,'PPS_Login','pps_username','pps_password')
        #WAP端品牌商派单->指定派单网点【测试网点01】
        Brands.PleaseOrder(self.dr,ordernumber,PDmodel='zi',WDname='测试网点01')
        #【待网点派单】订单状态/派单网点校验
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,ordernumber,DD_Status='等待网点派单',ExceptWD='测试网点01')

        #--------------------------------------------【WAP网点派单】------------------------------------------------------
        #WAP网点登陆
        Branch.WD_login(self.dr,'WD_Login','wd_username1',HTdriver=self.driver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.dr, OrderNumber=ordernumber)
        #WAP网点派单给指定师傅->【张先生】
        Branch.PleaseOrder(self.dr,OrderNumber=ordernumber,sfName='张先生')
        #【待师傅预约】订单状态/派单校验
        self.driver.switch_to.window(PCPPHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='等待师傅预约',ExceptSF='张先生')

        #--------------------------------------------【WAP师傅处理订单】--------------------------------------------------
        #WAP师傅登陆
        Master.SF_login(self.dr,'SF_Login','sf_username1','sf_password1')
        #==WAP师傅预约上门时间==
        Master.SF_Order(self.dr,OrderNumber=ordernumber)
        #【等待师傅服务】订单状态校验
        self.driver.switch_to.window(PCPPHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='等待师傅服务')
        #==WAP师傅上门打卡==
        Master.SF_DaKa(self.dr,OrderNumber=ordernumber)
        #【师傅服务中】订单状态校验
        self.driver.switch_to.window(PCPPHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='师傅服务中')
        #==WAP师傅处理工单,保存服务内容==
        Master.SF_Sheet(self.dr,OrderNumber=ordernumber)
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='师傅服务中')
        #==WAP师傅使用备件信息==
        Master.SF_UseBJ(self.dr,BJname='海尔自动化通用备件01')
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='师傅服务中')
        #==WAP师傅提交服务报价信息==
        Master.SF_SubmitPay(self.dr)
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='等待收款')
        #==WAP师傅收款==
        Master.SF_ShouKuan(self.dr,OrderNumber=ordernumber)
        #【师傅服务中】订单状态校验
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,OrderNumber=ordernumber,DD_Status='等待品牌商结算')

        #------------------------------------------------【客服登录回访订单】---------------------------------------------
        #客服登录
        KFHandle = KeFu.kf_login(self.driver)
        #客服回访
        KeFu.KF_HuiFang(self.driver,OrderNumber=ordernumber)
        #切换回客服窗口进行回访验证
        self.driver.switch_to.window(KFHandle)
        #回访验证
        KeFu.KF_CheckHF(self.driver,OrderNumber=ordernumber)

        #写入订单号便于备件返厂
        DataPath = Pubilc.data_dir(filename="Ordernumber.ini")
        cf = configparser.ConfigParser()
        cf.read(DataPath)
        cf.set('FanChang','ordernumber',ordernumber)
        with open(DataPath,"w") as f:
            cf.write(f)
        print('写入订单编号：{0}'.format(ordernumber))

        #脚本执行成功
        self.success = 'Pass'

    def tearDown(self):

        self.driver.quit()
        self.dr.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow04',run_result=self.success,isWrite=isWrite)
        #写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow04',run_result=self.success)


if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Please_Order('test_01'))
    runner = unittest.TextTestRunner()
    runner.run(suit)