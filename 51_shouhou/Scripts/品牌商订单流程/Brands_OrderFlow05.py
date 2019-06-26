# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/6 11:54

from Common import Driver,Logger
from Common import Pubilc,TestResult
from Page.WAPbranch import Branch
from Page.WAPbrands import Brands
from Page.PCbrands import PC_Brands
from Page.WAPmaster import Master
import unittest,configparser

'''
【品牌商自动派单流程】-该订单号用于WAP品牌商催单、投诉、取消订单
品牌商设置自动派单->PC端添加订单(WAP品牌订单状态校验)->WAP网点端接单校验->WAP网点派单(WAP品牌、网点订单状态校验)
'''
isWrite=True
class Please_Order(unittest.TestCase):

    def setUp(self):

        #获取下单配置文件信息
        DataPath = Pubilc.data_dir(filename='OrderMessage.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(DataPath,encoding='utf-8')

        #配置日志写入路径
        logDirPath = Pubilc.data_dir(file="Log",filename="Brands_OrderFlow05.txt")

        #调用log脚本
        Logger.setFormatter(logFile=logDirPath)

        #判断脚本是否执行成功,默认为File,不写入测试结果
        self.success = 'Fail'

    def test_PleaseOrder(self):

        '''【品牌商自动派单流程】:品牌商设置自动派单->PC端添加订单(WAP品牌订单状态校验)->WAP网点端接单校验->WAP网点派单(WAP品牌、网点订单状态校验)'''

        #-----------------------------------------------【PC品牌商下单】--------------------------------------------------
        #设置浏览器
        self.PCDriver = Driver.PC_Brower()
        # PC品牌商登陆
        PCPPHandle = PC_Brands.PCbrands_login(self.PCDriver,'PPS_Login','pps_username','pps_password')

        #设置品牌商派单方式：手动派单
        PC_Brands.PCbrands_SetAddOrder(self.PCDriver,ddfrom='品牌商提交',model='zi')
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
        #查询订单单号/校验添加订单成功订单状态
        AddOrderNumber = PC_Brands.PCbrands_FindOrdernum(self.PCDriver,DD_Status='待网点派单',OrderModel='zi')
        #WAP品牌商端订单状态校验
        self.WAPDriver = Driver.WAP_Brower()
        #WAP品牌商登陆
        PPHandle = Brands.PPS_login(self.WAPDriver,'PPS_Login','pps_username','pps_password')
        #WAP品牌商端订单状态校验
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待网点派单')

        #------------------------------------------------【WAP网点派单】-------------------------------------------------
        #WAP网点登陆
        Branch.WD_login(self.WAPDriver,'WD_Login','wd_username1',HTdriver=self.PCDriver)
        #WAP网点接单校验
        Branch.WD_ShouD(self.WAPDriver,OrderNumber=AddOrderNumber)
        #WAP网点派单
        Branch.PleaseOrder(self.WAPDriver,OrderNumber=AddOrderNumber,sfName='张先生')
        #PC端品牌订单状态校验
        self.PCDriver.switch_to.window(PCPPHandle)
        PC_Brands.PCbrands_CheckOrderStatus(self.PCDriver,OrderNumber=AddOrderNumber,DD_Status='等待师傅预约',ExceptSF='张先生')
        #WAP品牌商订单状态校验
        self.WAPDriver.switch_to.window(PPHandle)
        Brands.PPS_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')

        #--------------------------------------------------【师傅订单状态校验】------------------------------------------
        #师傅登陆
        Master.SF_login(self.WAPDriver,'SF_Login','sf_username1','sf_password1')
        #师傅端订单状态校验
        Master.SF_CheckOrderStatus(self.WAPDriver,CheckOrderNumber=AddOrderNumber,CheckOrderStatus='等待师傅预约')

        #写入订单单号品牌商催单、投诉、取消订单使用
        DataPath = Pubilc.data_dir(filename="Ordernumber.ini")
        cf = configparser.ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        cf.set('PPS_Operate','ordernumber',AddOrderNumber)
        with open(DataPath,'w') as f:
            cf.write(f)
        print('写入订单编号:{0}'.format(AddOrderNumber))

        #脚本执行成功
        self.success='Pass'

    def tearDown(self):

        #推出浏览器
        self.PCDriver.quit()
        self.WAPDriver.quit()
        Logger.removeHandler()
        TestResult.WriteResultToConfig(section='BrandsOrderFlow',case='Brands_OrderFlow05', run_result=self.success, isWrite=isWrite)
        # 写入测试结果txt
        TestResult.WriteResultToTxt(isWrite=isWrite,case='Brands_OrderFlow05',run_result=self.success)

if __name__ == '__main__':
    unittest.main(verbosity=2)





