# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/13 13:21

from public.common.pySelenium import PySelenium
from public.page.BDSearchPage import BaiDuSearch
from public.common.assertMode import AssertMode
from public.common.operateExcel import *
from public.common import myDecorator
import unittest,ddt
readTestData = ReadTestCase()

# 数据驱动的用例编号
ddtCaseList = ["baidu_search_001","baidu_search_002"]
ddtData = readTestData.get_ddt_data(ddtCaseList)

@ddt.ddt
class TestBaiDuSearch(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.BoxDriver = PySelenium()
        self.baiDuSearch = BaiDuSearch(self.BoxDriver)
        self.assertMode = AssertMode(self.BoxDriver)

    @unittest.skipUnless(readTestData.get_run_data("baidu_search_001"),"跳过不执行该用例")
    def test_baidu_search001(self):
        """测试百度搜索"""

        # 获取测试数据
        testData = readTestData.get_all_data("baidu_search_001")
        # 进入百度首页
        self.baiDuSearch.open_baidu_url()
        # 输入关键字
        self.baiDuSearch.input_text(value=testData["搜索关键字"])
        # 点击搜索
        self.baiDuSearch.click_search()
        # 获取页面 title
        title = self.baiDuSearch.get_title()
        # 断言
        self.assertMode.assert_equal(testData=testData,faction=title)

    @unittest.skipUnless(readTestData.get_run_data("baidu_search_002"),"跳过不执行该用例")
    def test_baidu_search002(self):
        """测试百度搜索"""

        # 获取测试数据
        testData = readTestData.get_all_data("baidu_search_002")
        # 进入百度首页
        self.baiDuSearch.open_baidu_url()
        # 输入关键字
        self.baiDuSearch.input_text(value=testData["搜索关键字"])
        # 点击搜索
        self.baiDuSearch.click_search()
        # 获取页面 title
        title = self.baiDuSearch.get_title()
        # 断言
        self.assertMode.assert_equal(testData=testData,faction=title)

    @ddt.data(*ddtData) # 数据驱动
    @myDecorator.skip_case  # 数据驱动跳过测试用例装饰器
    def test_baidu_search003(self,ddtData):
        """数据驱动 ddt 使用"""

        # 进入百度首页
        self.baiDuSearch.open_baidu_url()
        # 输入关键字
        self.baiDuSearch.input_text(value=ddtData["搜索关键字"])
        # 点击搜索
        self.baiDuSearch.click_search()
        # 获取页面 title
        title = self.baiDuSearch.get_title()
        # 断言
        self.assertMode.assert_equal(testData=ddtData,faction=title)

    def tearDown(self):

        self.BoxDriver.quit()

if __name__ == '__main__':

    suit = unittest.TestLoader().loadTestsFromTestCase(TestBaiDuSearch)
    unittest.TextTestRunner().run(suit)