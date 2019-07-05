# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

from Common.Requests import Method
import unittest,json,logging
from Common import WriteResult
from Common import Public
from Common import Logger
from Common.OperationConfig import operationConfig
from Common.Public import data_dir
config = operationConfig()

'''
登录模块的登录测试验证:1、账号错误 2、密码错误 3、账号为空 4、密码为空 5、账号密码正确登录
'''

#默认写入测试结果
isWrite=True
class BranchLogin(unittest.TestCase):

    def setUp(self):
        '''类实例化'''
        self.obj = Method()
        self.isOk = "Fail"

    def test_login01(self):
        '''登录密码为空验证'''
        #设置日志路径信息
        Logger.setFormatter(logFile=data_dir(data="Log", filename="test_login.txt"))
        r = self.obj.testApi(row=5)
        self.obj.isContent(r=r,row=5,isWrite=isWrite)

    def test_login02(self):
        '''登录账号错误验证'''
        r = self.obj.testApi(row=2)
        self.obj.isContent(r=r,row=2,isWrite=isWrite)

    def test_login03(self):
        '''登录密码错误验证'''
        r = self.obj.testApi(row=3)
        self.obj.isContent(r=r,row=3,isWrite=isWrite)

    def test_login04(self):
        '''登录账号为空验证'''
        r = self.obj.testApi(row=4)
        self.obj.isContent(r=r,row=4,isWrite=isWrite)

    def test_login05(self):
        '''登录账号密码正确验证'''
        r = self.obj.testApi(row=1)
        self.obj.isContent(r=r,row=1,isWrite=isWrite)
        #获取登录成功后返回的token apiToken PkId,写入配置文件中
        config.writeConfig(section="Globals",option="token",value=r.json()["access_token"])
        config.writeConfig(section="Globals",option="apitoken",value=r.json()["api_Token"])
        config.writeConfig(section="Globals",option="pkid",value=r.json()["PkId"])
        Logger.removeHandler()

    def tearDown(self):
        #从第一个到最后一个执行成功结果写入配置文件中
        self.isOk = "Pass"
        #只要有一个不通过就是整体不通过写入整体py文件的执行结果
        WriteResult.write_to_Config(isWrite=isWrite,run_result=self.isOk,case="test_login")


if __name__ == '__main__':
    unittest.main(verbosity=2)
