# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/26 10:59

import sys,unittest
from Common.Public import runCase

sys.path.append("../Script/2、OverviewMode")
import test_overview

def run():

    case = unittest.TestSuite()
    case.addTest(test_overview.OverviewMode("test_overview01"))
    case.addTest(test_overview.OverviewMode("test_overview02"))
    case.addTest(test_overview.OverviewMode("test_overview03"))
    case.addTest(test_overview.OverviewMode("test_overview04"))
    case.addTest(test_overview.OverviewMode("test_overview05"))
    case.addTest(test_overview.OverviewMode("test_overview06"))
    case.addTest(test_overview.OverviewMode("test_overview07"))
    case.addTest(test_overview.OverviewMode("test_overview08"))
    case.addTest(test_overview.OverviewMode("test_overview09"))
    case.addTest(test_overview.OverviewMode("test_overview10"))
    case.addTest(test_overview.OverviewMode("test_overview11"))
    case.addTest(test_overview.OverviewMode("test_overview12"))
    case.addTest(test_overview.OverviewMode("test_overview13"))

    runCase(fileName="test_overview",reportName="【正式网点】概览模块",
            titleName="【正式网点】概览模块",scription="网点概览接口测试",case=case)

if __name__ == '__main__':
    run()