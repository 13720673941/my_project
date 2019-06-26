#coding=utf-8
#品牌商招募\搜索服务商申请合作

from Page.WAPbrands import Brands
from Common import Driver,TestResult
from Common import Logger
from Common import Pubilc
import unittest,os,logging,time,random
from selenium.webdriver.support.wait import WebDriverWait

isWrite=True
class Zhao_Mu(unittest.TestCase):

    def setUp(self):

        #获取日志储存路径
        logPath = Pubilc.data_dir(file="Log", filename="b_ZhaoMu.txt")
        Logger.setFormatter(logFile=logPath)

        #判断脚本是否执行成功
        self.success = 'Fail'

    def test_ZM(self,url='http://www.51shouhou.cn/wapbrand/#/recruit'):

        '''招募服务商：随机选择筛选条件招募服务商'''

        # 调用wap浏览器和品牌商登录
        self.driver = Driver.WAP_Brower()
        Brands.PPS_login(self.driver, 'PPS_Login', 'pps_username', 'pps_password')

        #进入招募页面
        for i in range(5):
            try:
                self.driver.find_element_by_xpath('//*[@id="footer"]/ul/li[4]').click()
                logging.info('.....点击->【网点】')
                self.driver.find_element_by_xpath('//h4[contains(text(),"一键招募")]').click()
                logging.info('.....点击->【一键招募】')
                break
            except:
                if i == 4:
                    self.driver.get(url)
                    header = self.driver.find_element_by_xpath('//div[@class="header-center"]').text
                    if header == '发招募':
                        logging.info('.....直接打开招募网址...')
                    else:
                        logging.error('!!!!!进不去招募页面')
                        exit()
                else:
                    pass
        #选择招募区域随机选取
        try:
            logging.info('**********【招募信息】**********')
            time.sleep(2)
            self.driver.find_element_by_xpath('//p[text()="选择区域"]').click()
            logging.info('点击->【选择区域】')
        except:
            logging.error('!!!!!点击选择区域失败')
            exit()
        #随机选择省市区，随机匹配数字选取省市区三级联动
        address = []
        for i in range(4):
            time.sleep(2)
            try:
                if i > 0:
                    all_lis = self.driver.find_element_by_xpath('//div[@class="droplist-area"]/div['+str(i)+']/ul')
                    lis = all_lis.find_elements_by_tag_name('li')
                    #统计所有的区域，随机选择匹配数字
                    sel_lisNum = random.randint(1,len(lis))
                    areaInfo = self.driver.find_element_by_xpath('.//div[' +str(i)+']/ul/li[' +str(sel_lisNum)+ ']/span')
                    #滚动到元素可见位置
                    self.driver.execute_script("arguments[0].scrollIntoView();",areaInfo)
                    areaInfo.click()
                    area = areaInfo.text
                    #把省市区添加到数组中去打印出来
                    address.append(area)
                    #有些市区没有区县，市区合计为0时直接选区市区，区县不选
                    if i == 3 and len(lis) != 0:
                        self.driver.find_element_by_xpath('.//div[' +str(i)+']/ul/li[' +str(sel_lisNum)+ ']/label/input').click()
                        logging.info('招募区域：%s'%address)
                        try:
                            self.driver.find_element_by_xpath('//a[contains(),"确定"and@class="modal-qd"]').click()
                            logging.info('点击->【确定】')
                        except:
                            logging.error('!!!!!点击确定失败')
                            exit()
                        break
                else:
                    pass
            except:
                    pass
        #随机选择服务类型
        for i in range(5):
            try:
                all_servers = self.driver.find_element_by_xpath('//div[contains(text(),"师傅数量")]/preceding-sibling::div[2]/ul')
                servers = all_servers.find_elements_by_tag_name('li')
                sel_server = random.randint(1,len(servers))
                #选择服务类型
                server = self.driver.find_element_by_xpath('.//form/div[2]/div/ul/li[' +str(sel_server)+ ']').text
                server.click()
                logging.info('服务类型：%s'%server)
                break
            except:
                if i == 4:
                    logging.error('!!!!!选择服务类型失败')
                    exit()
                else:
                    pass
        #点击打开产品线选择框
        try:
            self.driver.find_element_by_xpath('//p[text()="选择产品线"]').click()
            logging.info('点击->【选择产品线】')
        except:
            logging.error('!!!!!打开产品线选择框失败')
            exit()
        #随机选择产品线信息
        productInfo = []
        for i in range(5):
            for j in range(3):#循环选择产品线
                try:
                    if j > 0:
                        products = self.driver.find_element_by_xpath('//div[@class="modal-product"]/div['+str(j)+']/ul')
                        product = products.find_elements_by_tag_name('li')
                        sel_productNum = random.randint(1,len(product))
                        productName = self.driver.find_element_by_xpath('//div[@class="modal-product"]/div['+str(j)+']/ul/li['+str(sel_productNum)+']').text
                        productName.click()
                        if productName == '全部':
                            #如果品类选择全部，则循环添加全部的品类到数组中去
                            for li in product:
                                PinLei = li.text
                                productInfo.append(PinLei)
                        else:
                            productInfo.append(productName)
                        if j == 2:
                            logging.info('选择招募产品信息：%s'%productInfo)
                            try:
                                self.driver.find_element_by_xpath('//a[text()=="确定"]').click()
                                logging.info('点击->【确定】')
                            except:
                                logging.error('!!!!!确定失败')
                                exit()
                            break
                    else:
                        pass
                except:
                    pass
            if i == 4:
                logging.error('!!!!!选择产品线失败')
                exit()
            else:
                pass
        #随机选择招募的服务商的师傅数量
        try:
            Master_nums = self.driver.find_element_by_xpath('//div[contains(),"师傅数量"]/following-sibling::div[1]/div')
            all_nums = Master_nums.find_elements_by_tag_name('div')
            sel_num = random.randint(1,len(all_nums))
            try:
                Master_info = self.driver.find_element_by_xpath('//div[contains(),"师傅数量"]/following-sibling::div[1]/div['+str(sel_num)+']').text
                Master_info.click()
                logging.info('招募服务商师傅数：%s'%Master_info)
            except:
                logging.error('!!!!!选择师傅数失败')
                exit()
        except:
            pass
        #填写招募备注信息
        try:
            tm = time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))
            self.driver.find_element_by_xpath('.//textarea').send_keys(tm)
            logging.info('备注：%s'%tm)
        except:
            logging.error('!!!!!填写招募备注失败')
            pass
        #点击发布按钮
        try:
            logging.info('*************************')
            WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_xpath('//a[text()="发布"]')).click()
            logging.info('点击->【发布】')
        except:
            logging.error('!!!!!点击发布失败')
            exit()
        #获取招募发布后的系统消息
        try:
            msg = WebDriverWait(self.driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="qb-sougou-search"]/following-sibling::div/div')).text
            logging.info('.....系统提示：%s'%msg)
        except:
            pass

        #脚本执行成功
        self.success = 'Pass'

    def tearDown(self):

        self.driver.quit()
        Logger.removeHandler()
        TestResult.Write_Test_Result('b_ZhaoMu', run_result=self.success, isWrite=isWrite)

if __name__ == '__main__':
    unittest.main()