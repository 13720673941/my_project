# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Page.PCbrands import PC_Brands
from Page.WAPbrands import Brands
from Page.WAPbranch import Branch
from Page.WAPmaster import Master
from Common import Driver,TestResult
import configparser,unittest
from Common import Logger
from Common import Pubilc

'''
【WAP品牌商派单改派流程】
PC品牌商下单->下单校验->WAP品牌商派单->派单校验/接单网店校验->WAP品牌商改派订单->派单校验/派单网店校验
'''

#默认写入脚本执行结果
isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取下单信息的配置文件路径
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #日志写入文件设置
        logPath = Pubilc.data_dir(file="Log",filename="Brands_OrderFlow02.txt")

        #配置写入日志
        Logger.setFormatter(logFile=logPath)

        #默认写入结果是Fail
        self.success = 'Fail'

    def test_PleaseOrder(self):

        '''【WAP品牌商订单改派流程】：设置手动派单->PC品牌商下单->下单校验->WAP品牌商派单->派单校验/接单网店校验->WAP品牌商改派订单->派单校验/派单网店校验'''

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

        #---------------------------------------------【WAP网点1接单校验】-------------------------------------------------
        #WAP网点1登录
        WDHandle = Branch.WD_login(self.dr,'WD_Login','wd_username1',HTdriver=self.driver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.dr, OrderNumber=ordernumber)
        Branch.WD_logout(self.dr)

        #-------------------------------------------------【WAP品牌商改派】-----------------------------------------------
        #切换回品牌商窗口
        self.dr.switch_to.window(PPHandle)
        #WAP端品牌商改派->改派网点【测试网点02】
        Brands.PleaseOrder(self.dr,ordernumber,PDmodel='zi',GaiPai='yes',WDname='测试网点02')
        #【待网点派单】订单状态/派单网点校验
        self.driver.switch_to.window(PCPPHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.driver,ordernumber,DD_Status='等待网点派单',ExceptWD='测试网点02')

        #-------------------------------------------------【WAP网点2接单校验】-------------------------------------------
        #WAP网点2登录
        Branch.WD_login(self.dr,'WD_Login','wd_username2',HTdriver=self.driver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.dr,OrderNumber=ordernumber)
        #WAP网点2派单到师傅2
        Branch.PleaseOrder(self.dr,OrderNumber=ordernumber,sfName='张先生')
        #【待师傅预约】品牌商状态订单校验
        self.dr.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.dr,CheckOrderNumber=ordernumber,CheckOrderStatus='等待师傅预约')

        #--------------------------------------------------【师傅处理工单】----------------------------------------------
        #WAP师傅登录
        SFHandle = Master.SF_login(self.dr,'SF_Login','sf_username2','sf_password2')
        #师傅接单校验
        Master.SF_CheckOrderStatus(self.dr,CheckOrderNumber=ordernumber,CheckOrderStatus='等待师傅预约')
        #师傅预约订单
        Master.SF_Order(self.dr,OrderNumber=ordernumber)
        #师傅上门打卡
        Master.SF_DaKa(self.dr,OrderNumber=ordernumber)
        #师傅填写工单
        Master.SF_Sheet(self.dr,OrderNumber=ordernumber)
        #师傅使用备件(不使用备件直接下一步)
        Master.SF_UseBJ(self.dr)
        #师傅提交服务报价
        Master.SF_SubmitPay(self.dr)
        #师傅收款
        Master.SF_ShouKuan(self.dr,OrderNumber=ordernumber)
        #待结算校验
        self.dr.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.dr,CheckOrderNumber=ordernumber,CheckOrderStatus='等待品牌商结算')
        self.dr.switch_to.window(SFHandle)
        Master.SF_CheckOrderStatus(self.dr,CheckOrderNumber=ordernumber,CheckOrderStatus='等待结算')

        #执行结果pass
        self.success='Pass'

    def tearDown(self):

        self.driver.quit()
        self.dr.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow02', run_result=self.success, isWrite=isWrite)
        #写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow02',run_result=self.success)

if __name__ == '__main__':

    case = unittest.TestSuite()
    case.addTest(Please_Order('test_01'))
    runner = unittest.TextTestRunner()
    runner.run(case)