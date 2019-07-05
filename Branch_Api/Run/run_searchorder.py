# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/28 17:20

from Common.Public import runCase
import sys,HTMLTestRunnerCN,unittest

sys.path.append("../Script/3、OrderMode")
import test_searchorder

def run():

    case = unittest.TestSuite()
    case.addTests([test_searchorder.Search_Order("test_search01"),test_searchorder.Search_Order("test_search02"),
                   test_searchorder.Search_Order("test_search03"),test_searchorder.Search_Order("test_search04"),
                   test_searchorder.Search_Order("test_search05"),test_searchorder.Search_Order("test_search06"),
                   test_searchorder.Search_Order("test_search07"),test_searchorder.Search_Order("test_search08"),
                   test_searchorder.Search_Order("test_search09"),test_searchorder.Search_Order("test_search10"),
                   test_searchorder.Search_Order("test_search11"),test_searchorder.Search_Order("test_search12"),
                   test_searchorder.Search_Order("test_search13")
                   ])

    runCase(fileName="test_searchorder",reportName="【正式网点】订单查询模块",
            titleName="【正式网点】订单查询模块",scription="网点订单模块订单查询",case=case)


if __name__ == '__main__':
    run()