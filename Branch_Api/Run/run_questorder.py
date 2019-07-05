# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/1/29 11:33

from Common.Public import runCase
import unittest,sys,HTMLTestRunnerCN
from Common.Public import data_dir

sys.path.append("../Script/3、OrderMode")
import test_questorder

def run():

    case = unittest.TestSuite()
    case.addTests([test_questorder.QuestOrder("test_question01"),test_questorder.QuestOrder("test_question02"),
                   test_questorder.QuestOrder("test_question03"),test_questorder.QuestOrder("test_question04"),
                   test_questorder.QuestOrder("test_question05"),test_questorder.QuestOrder("test_question06"),
                   test_questorder.QuestOrder("test_question07"),test_questorder.QuestOrder("test_question08"),
                   test_questorder.QuestOrder("test_question09"),test_questorder.QuestOrder("test_question10"),
                   test_questorder.QuestOrder("test_question11"),test_questorder.QuestOrder("test_question12"),
                   test_questorder.QuestOrder("test_question13"),test_questorder.QuestOrder("test_question14"),
                   test_questorder.QuestOrder("test_question15"),test_questorder.QuestOrder("test_question16"),
                   test_questorder.QuestOrder("test_question17"),test_questorder.QuestOrder("test_question18"),
                   test_questorder.QuestOrder("test_question19"),test_questorder.QuestOrder("test_question20"),
                   test_questorder.QuestOrder("test_question21"),test_questorder.QuestOrder("test_question22")
                   ])

    runCase(fileName="test_questorder",reportName="【正式网点】异常订单模块",titleName="【正式网点】异常订单模块",
            scription="网点订单模块,异常订单查询",case=case)


if __name__ == '__main__':
    run()