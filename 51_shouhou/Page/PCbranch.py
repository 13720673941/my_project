# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/7 9:45

import time,os,configparser,random,logging
from Common import Pubilc
from selenium.webdriver.support.wait import WebDriverWait

class PC_Branch(object):

    def method(driver,SelectWord,element=None,text=None):
        '''
        :param SelectWord: 筛选的关键字
        :param element:    父节点元素位置
        :param text:       元素文本信息
        '''

        #网点下单页面选择方法都一样用这个方法直接调用优化
        time.sleep(1)
        for i in range(10):
            try:
                if element == None and text != None:
                    element = driver.find_element_by_xpath('//span[text()="'+text+'"]/../..')
                element.click()
                time.sleep(1)
                All_PPName = element.find_element_by_xpath('.//div[@class="ivu-select-dropdown"]/ul[2]')
                PPNames = All_PPName.find_elements_by_tag_name('li')
                for name in PPNames:
                    if name.text == SelectWord:
                        name.click()
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择%s失败'%SelectWord)
                    exit()
                else:
                    pass

    def PCbranch_login(driver,section,username,password,wdHandle='table',url='http://www.51shouhou.cn/nweb/sign/login'):
        '''
        :param section:  配置文件中section值
        :param username: 用户名
        :param password: 密码
        :param wdHandle: 网点窗口是否切换
        '''

        #-------------------------------------------------【PC端网点登陆】-----------------------------------------------
        #获取配置文件
        DataPath = Pubilc.data_dir(filename='Login.ini')
        cf = configparser.ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        use = cf.get(section,username)
        pwd = cf.get(section,password)

        #打开PC网点登陆地址信息
        logging.info('<=====>【PC网点登录】<=====>')
        if wdHandle == 'new':
            driver.get(url)
        elif wdHandle == 'table':
            Pubilc.table_handle(driver,url=url)
        logging.info('.....正在打开网址...')
        #获取网点handle
        WDHandle = driver.current_window_handle

        #点击【网点登陆】切换网点
        try:
            WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//div[@class="login-tab"]/ul/li[2]')).click()
            logging.info('.....切换网点登陆页面')
        except:
            pass
        #输入用户名密码点击登陆
        for i in range(10):
            try:
                element = driver.find_element_by_xpath("//input[@placeholder='请输入用户名/手机号']/../../../..")
                element.find_element_by_xpath('.//input[@class="login-text txtUser"]').clear()
                element.find_element_by_xpath('.//input[@class="login-text txtUser"]').send_keys(use)
                logging.info('.....输入用户名：%s'%use)
                element.find_element_by_xpath('.//input[@class="login-text txtPass"]').clear()
                element.find_element_by_xpath('.//input[@class="login-text txtPass"]').send_keys(pwd)
                logging.info('.....输入密码：%s'%pwd)
                time.sleep(1)
                element.find_element_by_xpath('.//a[@class="login-btn"]').click()
                logging.info('.....点击->【登录】')
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入用户名密码失败')
                    exit()
                else:
                    pass
        #获取登录异常信息提示
        try:
            systemMsg = driver.find_element_by_xpath('//div[@type="dialog"]/div').text
            logging.warning('!!!!!系统提示：%s'%systemMsg)
        except:
            pass
        #PC网点登录校验
        for i in range(10):
            time.sleep(5)
            try:
                BranchTitle = driver.title
                if '超级网点' in BranchTitle:
                    logging.info('.....PC网点登录成功！')
                else:
                    logging.error('!!!!!PC网点登录失败！')
                    exit()
                break
            except:
                pass
        return WDHandle

    def PCbranch_AddOrder(driver,username,Phonenums,address,collage,server,product,JSNumbers,AddOrderInfo,PPName=None,OrderType='品牌商'):
        '''
        :param username:    联系人
        :param Phonenums:   联系方式
        :param address:     服务地址信息
        :param collage:     详细地址
        :param server:      服务类型
        :param product:     产品信息带产品型号
        :param JSNumbers:   机身条码
        :param AddOrderInfo: 备注
        :param PPName:      网点添加品牌商订单品牌商名称
        :param OrderType:   是否添加品牌订单或者网点订单
        '''
        #---------------------------------------------【网点添加订单】---------------------------------------------------
        #进入网点添加订单页面
        logging.info('<=====>【PC网点添加订单】<=====>')
        driver.get('http://www.51shouhou.cn/newBranch/#/order/add')
        time.sleep(1)
        logging.info('.....正在进入添加订单页面...')
        #选择订单来源品牌商订单/网点自营订单
        if OrderType == '品牌商':
            logging.info('.....添加品牌商订单')
            #选择品牌商【测试品牌01】品牌订单
            element = driver.find_element_by_xpath('//span[text()="请选择订单来源"]/following-sibling::span/../..')
            logging.info('.....选择品牌商：%s'%PPName)
            PC_Branch.method(driver,element=element,SelectWord=PPName)
        elif OrderType == '网点':
            logging.info('.....添加网点自营订单')
        #选择购买渠道信息
        for i in range(10):
            try:
                element1 = driver.find_element_by_xpath('//span[text()="请选择购买渠道"]/../..')
                element1.click()
                logging.info('.....点击->【购买渠道】')
                time.sleep(1)
                All_BuyPlaces = element1.find_element_by_xpath('.//div[@class="ivu-select-dropdown"]/ul[2]')
                BuyPlaces = All_BuyPlaces.find_elements_by_xpath('li')
                select_num = random.randint(2,len(BuyPlaces))
                Place = All_BuyPlaces.find_element_by_xpath('.//li['+str(select_num)+']')
                logging.info('.....选择购买渠道：%s'%Place.text)
                Place.click()
                break
            except:
                if i == 9:
                    logging.info('.....选择购买渠道失败')
                    exit()
                else:
                    pass
        #输入联系人和联系方式信息
        BuyTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        use = username.split('+')[0] + BuyTime
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请输入联系人"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入联系人"]').send_keys(use)
                logging.info('.....联系人：%s'%use)
                driver.find_element_by_xpath('//input[@placeholder="请输入联系方式1"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入联系方式1"]').send_keys(Phonenums)
                logging.info('.....联系方式：%s'%Phonenums)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入联系人电话失败')
                    exit()
                else:
                    pass
        #选择省市区信息
        province,city,area = address.split('-')
        #选择省份信息
        PC_Branch.method(driver,SelectWord=province,text='请选择省')
        #选择市区信息
        PC_Branch.method(driver,SelectWord=city,text='请选择市')
        #选择区县信息
        PC_Branch.method(driver,SelectWord=area,text='请选择区')
        #输入详细地址信息
        driver.find_element_by_xpath('//input[@placeholder="请输入详细地址"]').send_keys(collage)
        logging.info('.....服务地址：%s,%s'%(address,collage))
        #选择服务类型、报内外、售后类型 默认选择项
        for i in range(10):
            try:
                driver.find_element_by_xpath('//label[contains(text(),"'+server+'")]').click()
                logging.info('.....预约服务类型：%s'%server)
                if OrderType == '品牌商':
                    driver.find_element_by_xpath('//label[contains(text(),"保内")]').click()
                    logging.info('.....保内保外：保内')
                    driver.find_element_by_xpath('//label[contains(text(),"售后机")]').click()
                    logging.info('.....保内保外：售后机')
                break
            except:
                pass
        #获取配置文件中产品信息
        PinPai,PinXian,PinLei,XH = product.split(',')
        #选择产品品牌
        if OrderType == '品牌商':
            PC_Branch.method(driver,SelectWord=PinPai,text='请选择产品品牌')
        #选择产品线
        time.sleep(1)
        PC_Branch.method(driver,SelectWord=PinXian,text='请选择产品线')
        #选择产品品类
        time.sleep(1)
        PC_Branch.method(driver,SelectWord=PinLei,text='请选择产品品类')
        #选择产品型号信息
        if OrderType == '品牌商':
            time.sleep(1)
            PC_Branch.method(driver,SelectWord=XH,text='请选择产品型号')
        logging.info('.....产品信息：%s'%product)
        #获取机身条码信息
        tm = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        JSNumber = JSNumbers.split('+')[0] + tm
        #输入机身条码
        driver.find_element_by_xpath('//input[@placeholder="请输入机身条码"]').send_keys(JSNumber)
        logging.info('.....机身条码：%s'%JSNumber)
        #如果是维修要选择故障类型
        if server == '维修':
            #随机选择故障类型
            for i in range(10):
                try:
                    element2 = driver.find_element_by_xpath('//span[text()="请选择故障类型"]/../..')
                    element2.click()
                    time.sleep(1)
                    All_BadPlaces = element2.find_element_by_xpath('.//div[@class="ivu-select-dropdown"]/ul[2]')
                    BadPlaces = All_BadPlaces.find_elements_by_xpath('li')
                    select_num2 = random.randint(2,len(BadPlaces))
                    BadPlace = All_BadPlaces.find_element_by_xpath('.//li['+str(select_num2)+']')
                    logging.info('.....选择故障类型：%s'%BadPlace.text)
                    BadPlace.click()
                    break
                except:
                    if i == 9:
                        logging.info('.....选择故障类型失败')
                        exit()
                    else:
                        pass
        #输入购买时间/预约时间
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请选择购买时间"]').send_keys(BuyTime)
                logging.info('.....购买时间：%s'%BuyTime)
                driver.find_element_by_xpath('//input[@placeholder="请选择预约服务时间"]').send_keys(BuyTime)
                logging.info('.....预约时间：%s'%BuyTime)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入时间失败')
                    exit()
                else:
                    pass
        #选择时间段
        PC_Branch.method(driver,SelectWord='下午',text='上午')
        logging.info('.....选择时间段：下午')
        #输入反馈信息
        BeiZhu = AddOrderInfo.split('+')[0] + BuyTime
        try:
            driver.find_element_by_xpath('//textarea[@class="form-control"]').send_keys(BeiZhu)
            logging.info('.....备注：%s'%BeiZhu)
        except:
            pass
        #点击提交按钮
        driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
        logging.info('.....点击->【提交】')
        #获取系统提示信息
        try:
            AddOrderMsg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="ivu-message"]')).text
            logging.info('.....系统提示：%s'%AddOrderMsg)
        except:
            pass

    def FindOrderNumber(driver):

        #---------------------------------------------【PC网点获取订单号】-----------------------------------------------
        #进入网点订单查询页面
        logging.info('===========【查找订单号】===========')
        for i in range(10):
            try:
                driver.get('http://www.51shouhou.cn/newBranch/#/order/search')
                driver.refresh()
                time.sleep(1)
                active = driver.find_element_by_xpath('//div[@class="panel-options"]/ul/li[1]').get_attribute('class')
                if active == 'active':
                    logging.info('.....正在进入订单查询页面...')
                    break
            except:
                if i == 9:
                    logging.error('!!!!!进入网点订单查询页面失败！')
                    exit()
                else:
                    pass
        #查找第一个订单时间，60s内就是新建订单保存订单单号
        time.sleep(2)
        for i in range(10):
            try:
                # Element = driver.find_element_by_xpath('//*[@class="ivu-table-tbody"][1]/tr[1]/td[7]/div/span/../../../..')
                #输出第一个订单创建时间
                AddOrderTime = driver.find_element_by_xpath('//*[@class="ivu-table-tbody"][1]/tr[1]/td[7]/div/span').text
                AddOrderTimeNumber = time.mktime(time.strptime(AddOrderTime,'%Y-%m-%d %H:%M:%S'))
                NowTimeNumber = time.time()
                ChaTime = NowTimeNumber-AddOrderTimeNumber
                if ChaTime < 60:
                    FindOrderNumber = driver.find_element_by_xpath('//div[@class="ivu-table-fixed-body"][1]/table/tbody/tr[1]/td[3]/div/a').text
                    logging.info('.....该订单为新建订单！订单单号：%s'%FindOrderNumber)
                    break
                elif ChaTime >= 60:
                    logging.info('.....获取订单超时...')
            except:
                if i == 9:
                    logging.error('!!!!!获取新建订单单号失败！')
                    exit()
                else:
                    pass
        return FindOrderNumber





















# if __name__ == '__main__':
#
#     from Common import Driver
#     d = Driver.PC_Brower()
#     PC_Branch.PCbranch_login(d,'WD_Login','wd_username1','wd_password1',wdHandle='new')
#     PC_Branch.PCbranch_AddOrder(d,username='11111',Phonenums='11111111111',PPName='测试公司01',address='陕西省-西安市-未央区',collage='333'
#                                 ,server='维修',product='海尔,空调,变频分体壁挂式,Haier-KT-05',JSNumbers='jstm+riqi',AddOrderInfo='AAA',OrderType='网点')
#
#

