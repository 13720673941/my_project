# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/29 17:52


from Common.Public import runCase
import unittest,sys,HTMLTestRunnerCN

sys.path.append("../Script/3、OrderMode")
import test_THorder

def run():

    case = unittest.TestSuite()
    case.addTests([test_THorder.THOrder("test_TH01"),test_THorder.THOrder("test_TH02"),
                   test_THorder.THOrder("test_TH03"),test_THorder.THOrder("test_TH04"),
                   test_THorder.THOrder("test_TH05"),test_THorder.THOrder("test_TH06"),
                   test_THorder.THOrder("test_TH07"),test_THorder.THOrder("test_TH08"),
                   test_THorder.THOrder("test_TH09"),test_THorder.THOrder("test_TH10")
                   ])

    runCase(fileName="test_THorder",reportName="【正式网点】整机退换模块",titleName="【正式网点】整机退换模块",
            scription="网点整机退换模块接口",case=case)

if __name__ == '__main__':
    run()