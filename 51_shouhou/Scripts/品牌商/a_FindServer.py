#coding=utf-8
#找服务资源

from Page.WAPbrands import Brands
from Common import Driver,TestResult
import unittest,logging,time,random
from Common import Logger
from Common import Pubilc

isWrite = True
class Find_Server(unittest.TestCase):

    def setUp(self):

        #获取日志储存路径
        logPath = Pubilc.data_dir(file="Log",filename="a_FindServer.txt")
        Logger.setFormatter(logFile=logPath)

        #判断脚本是否执行成功
        self.success = 'Fail'

    def test_findserver(self,url='http://www.51shouhou.cn/wapbrand/#/find'):

        '''找资源：随机查找匹配服务商/服务资源信息'''
        #调用wap浏览器和品牌商登录
        global driver
        driver = Driver.WAP_Brower()
        Brands.PPS_login(driver,'PPS_Login','pps_username','pps_password')



    def tearDown(self):

        driver.quit()
        Logger.removeHandler()
        TestResult.Write_Test_Result('a_FindServer', run_result=self.success, isWrite=isWrite)


if __name__ == '__main__':

    suit = unittest.TestSuite()
    suit.addTest(Find_Server('test_find_server'))
    runner = unittest.TextTestRunner()
    runner.run(suit)










