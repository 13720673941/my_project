# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/17 21:17

from common.request import Requests
import unittest

class Login(unittest.TestCase):

    def setUp(self):

        self.test_api = Requests("login")

    def test_login001(self):
        self.test_api.test_main(id="login_001")

    def test_login002(self):
        self.test_api.test_main(id="login_002")

    def test_login003(self):
        self.test_api.test_main(id="login_003")

    def test_login004(self):
        self.test_api.test_main(id="login_004")

    def test_login005(self):
        self.test_api.test_main(id="login_005")

    def tearDown(self):

        pass

if __name__ == '__main__':

    import HTMLTestRunnerCN,time

    suits = unittest.TestSuite()
    suits.addTest(Login("test_login001"))
    suits.addTest(Login("test_login002"))
    # suits.addTest(Login("test_login003"))
    # suits.addTest(Login("test_login004"))
    # suits.addTest(Login("test_login005"))

    tm = time.strftime('%y-%m-%d %H_%M_%S', time.localtime(time.time()))
    Path = '../result/report/'+ tm + '.html'
    fp = open(Path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="gdsah",
                                             description="asdiausdiu",verbosity=2)
    # print('开始时间：{0}'.format(tm))
    runner.run(suits)
    fp.close()