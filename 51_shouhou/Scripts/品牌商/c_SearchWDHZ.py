#coding=utf-8
#找服务资源

from Page.WAPbrands import Brands
from Common import Driver,TestResult
from Common import Logger
from Common import Pubilc
import unittest,os,logging,time,random
from selenium.webdriver.support.wait import WebDriverWait

isWrite=True
class SearchWD(unittest.TestCase):

    def setUp(self):

        #获取日志储存路径
        logPath = Pubilc.data_dir(file="Log",filename="c_SearchWDHZ.txt")
        Logger.setFormatter(logFile=logPath)

        #判断脚本是否执行成功
        self.success = 'Fail'

    def test_SearchWD(self, url='http://www.51shouhou.cn/wapbrand/?#/branch/list?branchname='):
        '''搜索服务商：随机匹配服务商信息，搜索并申请合作'''

        # 调用wap浏览器和品牌商登录
        self.driver = Driver.WAP_Brower()
        Brands.PPS_login(self.driver, 'PPS_Login', 'pps_username', 'pps_password')

        # 进入搜索服务商页面
        for i in range(5):
            try:
                self.driver.find_element_by_xpath('//*[@id="footer"]/ul/li[4]')
                logging.info('.....点击->【网点】')
                self.driver.find_element_by_xpath('//a[@class="search-btn"and@text()="搜索"]').click()
                logging.info('.....点击->【搜索】')
                break
            except:
                if i == 4:
                    self.driver.get(url)
                    logging.info('.....正在进入搜索服务商网址...')
                    title = self.driver.find_element_by_xpath('//div[@class="header-center"]').text
                    if title == '全国网店列表':
                        logging.info('.....打开搜索服务商页面')
                    else:
                        logging.error('!!!!!进不去搜索服务商页面')
                        exit()
                else:
                    pass
        # 打开【区域】搜索框
        try:
            self.driver.find_elements_by_tag_name('//div[@class="container-fluid"]ul/li[1]').click()
            logging.info('.....点击->【全国】')
        except:
            logging.error('!!!!!点击全国失败')
            exit()
        # 省市区随机选择三联动
        server_address = []
        logging.info('**************【搜索服务商条件】**************')
        for j in range(5):
            for i in range(4):
                try:
                    if i > 0:
                        all_lis = self.driver.find_element_by_xpath(
                            '//div[@class="van-picker van-area"]/div[2]/div[' + str(i) + ']/ul')
                        lis = all_lis.find_elements_by_tag_name('li')
                        # 随机选择匹配区域的数字
                        sel_li = random.randint(1, len(lis))
                        # 从0开始第一个选不中
                        num = 1
                        for li in lis:
                            time.sleep(0.5)
                            li.click()
                            if num == sel_li:
                                ad_info = li.text
                                # 把选择的区域添加到列表中
                                server_address.append(ad_info)
                                break
                            num += 1
                    else:
                        pass
                except:
                    if i == 3:
                        logging.info('筛选服务商的区域：%s' % server_address)
                        try:
                            self.driver.find_element_by_xpath('//div[@class="van-picker__confirm"and@text()="确认"]').click()
                            logging.info('点击->【确认】')
                        except:
                            logging.error('!!!!!点击确定失败')
                    else:
                        pass
            if j == 4:
                logging.error('!!!!!筛选服务商区域失败')
                exit()
            else:
                pass
        # 打开服务商【产品】筛选框
        try:
            self.driver.find_element_by_xpath('//div[@class="container-fluid"]ul/li[2]').click()
            logging.info('点击->【产品】')
        except:
            logging.error('!!!!!点击产品失败')
            exit()
        # 随机选择服务商产品筛选条件信息
        prodect_line = []
        for i in range(5):
            try:
                if i > 0:
                    all_divs = self.driver.find_element_by_xpath(
                        '//div[@class="van-tree-select productcategory"]/div[' + str(i) + ']')
                    divs = all_divs.find_elements_by_tag_name('div')
                    sel_prodect = random.randint(1, len(divs))
                    for j in range(5):
                        try:
                            prodect = self.driver.find_element_by_xpath(
                                '//div[@class="van-tree-select productcategory"]/div[' + str(i) + ']/div[' + str(
                                    sel_prodect) + ']')
                            # 品类有可能会有滚动条
                            self.driver.execute_script("arguments[0].scrollIntoView();", prodect)
                            prodectInfo = prodect.text
                            prodect.click()
                            prodect_line.append(prodectInfo)
                            break
                        except:
                            if j == 4:
                                logging.error('!!!!!点击产品信息失败')
                                exit()
                            else:
                                pass
                if i == 2:
                    logging.info('筛选服务商产品信息：%s' % prodect_line)
                    break
            except:
                pass
        # 随机选择【服务类型】、【综合】信息
        for i in range(5):
            try:
                if i > 2:
                    try:
                        model = self.driver.find_element_by_xpath(
                            '//div[@class="container-fluid"]/ul/li[' + str(i) + ']/a').text
                        model.click()
                    except:
                        logging.error('!!!!!点击：%s失败' % model)
                        exit()
                    k = i + 1
                    all_lis = self.driver.find_element_by_xpath('.//div[' + str(k) + ']/div/div/div[1]/ul')
                    lis = all_lis.find_elements_by_tag_name('li')
                    sel_num = random.randint(0, len(lis))
                    num = 0
                    for li in lis:
                        try:
                            if num > 0:
                                # 第1次点击的时候选择框会关闭，所以第2次再次打开选择框
                                model.click()
                            time.sleep(1)
                            li.click()
                        except:
                            logging.error('!!!!!循环点击失败')
                            exit()
                        if num == sel_num:
                            massage = li.text
                            logging.info('%s：%s' % (model, massage))
                            break
                        num += 1
                else:
                    pass
            except:
                pass
        # 统计筛选的服务商的总数
        try:
            all_wd = self.driver.find_element_by_xpath('//div[@class="container-pro-list choise-list"]/ul')
            FuWu = all_wd.find_elements_by_tag_name('input')
            count = len(FuWu)
            logging.info('.....搜索服务商：%s个' % count)
        except:
            logging.error('!!!!!统计服务商失败')
            exit()
        # 勾选搜索的服务商批量申请
        for input in FuWu:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", input)
                input.click()
            except:
                logging.error('!!!!!勾选服务商失败')
                exit()
        # 点击批量合作
        try:
            self.driver.find_elements_by_tag_name('//span[contains(),"批量合作"]').click()
            logging.info('.....点击->【批量合作】')
        except:
            logging.error('!!!!!点击批量合作失败')
            exit()
        # 获取批量申请后的系统提示信息
        try:
            system_msg = WebDriverWait(self.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath('//*[@id="qb-sougou-search"]/following-sibling::div/div')).text
            logging.info('.....系统提示：%s' % system_msg)
        except:
            logging.error('!!!!!获取系统提示失败')
            pass

        # 脚本执行成功
        self.success = 'Pass'

    def tearDown(self):

        self.driver.quit()
        Logger.removeHandler()
        TestResult.Write_Test_Result('c_SearchWDHZ', run_result=self.success, isWrite=isWrite)

if __name__ == '__main__':
    unittest.main()