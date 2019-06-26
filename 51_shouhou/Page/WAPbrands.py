# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Common import Driver
from Common import Pubilc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,random,logging,configparser,os

class Brands(object):

    def __init__(self):

        pass

    def Find_ClickButton(driver,Model,OrderNumber,ButtonText):
        '''
        :param Model:       table栏的信息
        :param OrderNumber: 订单单号
        :param ButtonText:  按钮文本信息
        '''

        #查找订单下面的按钮，派单 改派 取消 投诉 催单 操作适用该方法
        #订单审核页面的按钮
        if Model == '待审核':
            #进入待审核页面查找订单，点击按钮操作
            for i in range(10):
                try:
                    driver.get('http://www.51shouhou.cn/wapbrand/#/my/markettrade?tab=%E5%BE%85%E5%AE%A1%E6%A0%B8')
                    driver.refresh()
                    logging.info('.....直接进入待审核订单网址...')
                    time.sleep(1)
                    active = driver.find_element_by_xpath('//header[@class="header"]/div/div/ul/li[1]').get_attribute('class')
                    if active == 'active':
                        break
                except:
                    if i == 9:
                        logging.error('!!!!!进不去待审核页面...')
                        exit()
                    else:
                        pass
            #统计待审核的订单数量
            for i in range(10):
                try:
                    AllCardLists = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]')
                    CardLists = AllCardLists.find_elements_by_tag_name('i')
                    CardListNumber = int(len(CardLists)/3)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!统计订单失败!')
                        exit()
            #遍历所有订单编号查找订单点击派单
            for i in range(1,CardListNumber):
                time.sleep(1)
                try:
                    AllCardLists = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]')
                    AllCardLists.find_element_by_xpath('.//div['+str(i)+']/div[2]').click()
                    time.sleep(1)
                    FindOrderNumber = driver.find_element_by_xpath('//span[text()="订单编号"]/following-sibling::div').text
                    if FindOrderNumber == OrderNumber:
                        logging.info('.....找到派单订单啦！')
                        driver.find_element_by_xpath('//i[@class="icon-left"]').click()#返回
                        #统计该订单的按钮文本点击
                        time.sleep(1)
                        Element = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]')
                        AllButtonLists = Element.find_element_by_xpath('.//div['+str(i)+']/div[3]/div')
                        ButtonList = AllButtonLists.find_elements_by_tag_name('a')
                        for Button in ButtonList:
                            if Button.text == ButtonText:
                                Button.click()
                                logging.info('.....点击->【%s】'%ButtonText)
                                break
                        break
                    else:
                        logging.info('.....该订单不是新建订单！返回！')
                        driver.find_element_by_xpath('//i[@class="icon-left"]').click() #返回
                except:
                    if i == CardListNumber-1:
                        logging.error('!!!!!找不到新建订单！')
                        exit()
                    else:
                        pass
        elif Model == '订单查询':
            #进入订单查询页面查找订单，操作按钮
            for i in range(10):
                try:
                    driver.get('http://www.51shouhou.cn/wapbrand/#/my/markettrade?tab=%E8%AE%A2%E5%8D%95%E6%9F%A5%E8%AF%A2')
                    driver.refresh()
                    time.sleep(1)
                    active = driver.find_element_by_xpath('//header[@class="header"]/div/div/ul/li[3]').get_attribute('class')
                    if active == 'active':
                        logging.info('.....进入订单查询页面...')
                        break
                except:
                    if i == 9:
                        logging.error('!!!!!进入订单查询页面失败...')
                        exit()
                    else:
                        pass
            #统计订单查询页面所有订单单数
            for i in range(10):
                try:
                    CX_AllCardList = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[11]')
                    CX_CardList = CX_AllCardList.find_elements_by_tag_name('i')
                    CX_CardListNumber = int(len(CX_CardList)/3)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!订单查询页面订单统计失败！')
                        exit()
            #循环遍历订单单号，点击改派
            for i in range(1,CX_CardListNumber):
                time.sleep(1)
                try:
                    CX_AllCardList = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[11]')
                    CX_AllCardList.find_element_by_xpath('.//div['+str(i)+']/div[2]').click()
                    time.sleep(1)
                    CX_FindOrderNumber = driver.find_element_by_xpath('//span[text()="订单编号"]/following-sibling::div').text
                    if CX_FindOrderNumber == OrderNumber:
                        logging.info('.....找到改派订单啦！')
                        driver.find_element_by_xpath('//i[@class="icon-left"]').click() #返回
                        time.sleep(1)
                        Element1 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[11]')
                        CX_AllButtons = Element1.find_element_by_xpath('.//div['+str(i)+']/div[3]/div')
                        CX_Buttons = CX_AllButtons.find_elements_by_tag_name('a')
                        for CX_Button in CX_Buttons:
                            if CX_Button.text == ButtonText:
                                CX_Button.click()
                                logging.info('.....点击->【%s】'%ButtonText)
                                break
                        break
                    else:
                        logging.info('.....不是新建订单！返回！')
                        driver.find_element_by_xpath('//i[@class="icon-left"]').click() #返回
                except:
                    if i == CX_CardListNumber-1:
                        logging.error('!!!!!找不到改派订单！')
                        exit()
                    else:
                        pass

    def PPS_login(driver,section,username,password,url='http://www.51shouhou.cn/wapbrand/#/my'):

        #获取品牌商登陆配置
        Data_Path = Pubilc.data_dir(filename='Login.ini')
        data = configparser.ConfigParser()
        data.read(Data_Path, encoding='utf-8')
        use = data.get(section, username)
        pwd = data.get(section, password)

        #--------------------------------------------【WAP品牌商登陆】----------------------------------------------------
        #打开登录页面
        logging.info('<=====>【WAP品牌商登录】<=====>')
        for i in range(20):
            try:
                driver.get(url)
                logging.info('.....打开登录页面...')
                driver.find_element_by_xpath('//div[@class="user-head"]').click()
                break
            except:
                if i == 3:
                    driver.refresh()
                else:
                    pass
            finally:
                if i == 19:
                    logging.error('!!!!!打开登录页失败...')
                    Driver.screen_shop(driver)
                    exit()
                else:
                    pass
        pps_handles = driver.current_window_handle
        #输入账号密码
        for i in range(1):
            try:
                driver.find_element_by_xpath('//input[@type="text"]').clear()
                driver.find_element_by_xpath('//input[@type="text"]').send_keys(use)
                logging.info('.....输入用户：%s'%use)
                driver.find_element_by_xpath('//input[@type="password"]').clear()
                driver.find_element_by_xpath('//input[@type="password"]').send_keys(pwd)
                logging.info('.....输入密码：%s'%pwd)
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入错误...')
                    exit()
                else:
                    pass
        #点击登录获取异常
        for i in range(20):
            try:
                #等待5s判断是否有登录按钮，没有抛出异常
                login = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="pop-login-btn"]')))
                login.click()
                logging.info('.....点击->【登录】')
                break
            except:
                if i == 19:
                    Driver.screen_shop(driver)
                    logging.error('!!!!!点击->【登录】错误...')
                    exit()
                else:
                    pass
        #获取异常
        try:
            msg = WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath('//div[@id="app"]/following-sibling::div[1]/div')).text
            driver.screen_shop(driver)
            logging.info('.....异常信息/截图：%s'%msg)
        except:
            pass
        #判断登录
        for i in range(5):
            time.sleep(1)
            try:
                text = driver.find_element_by_css_selector('a.signout-btn').text
                if text == '退出登录':
                    logging.info('.....品牌商登录成功')
                else:
                    driver.screen_shop(driver)
                    logging.error('!!!!!品牌商登录失败/截图')
                break
            except:
                if i == 4:
                    logging.error('!!!!!品牌商登陆失败')
                    exit()
                else:
                    pass
        return pps_handles

    def PPS_addorder(driver,url,server,BaoN,product,PinX,PinL,GuiG,massage,user,phe,area,address):
        '''
        WAP品牌商下单
        :param url: 添加订单地址
        :param server: 服务类型
        :param BaoN: 宝内保外
        :param product: 产品信息
        :param PinX: 产品线
        :param PinL: 品类
        :param GuiG: 规格
        :param massage: 下单备注
        :param user: 用户名称
        :param phe: 手机号
        :param area: 地址
        :param address: 详细地址
        :return:
        '''
        #--------------------------------------【品牌商添加订单】----------------------------------------
        #进入添加订单页面
        logging.info('<=====>【WAP品牌提交订单】<=====>')
        for i in range(5):
            try:
                driver.get(url)
                if driver.find_element_by_xpath('//div[@class="header-center"]').text == '发订单':
                    logging.info('.....正在进入WAP品牌商添加订单页面...')
                    break
            except:
                if i == 4:
                    logging.info('.....打开添加订单网址失败！')
                    pass
        #固定选取服务类型：安装，质保信息：保内
        time.sleep(1)
        for i in range(5):
            try:
                logging.info('******* Order Massage *******')
                driver.find_element_by_xpath('//div[text()="服务类型"]/../a[contains(text(),"'+server+'")]').click()
                logging.info('服务类型：%s'%server)
                driver.find_element_by_xpath('//div[text()="质保信息"]/../a[contains(text(),"'+server+'")]').click()
                logging.info('质保信息：%s'%BaoN)
                break
            except:
                if i == 4:
                    logging.error('!!!!!服务类型/质保信息选择失败...')
                    exit()
                else:
                    pass
        #选择产品品牌
        try:
            driver.find_element_by_xpath('//div[text()="产品品牌"]').click()
            logging.info('点击->【产品品牌】')
        except:
            logging.error('!!!!!点击产品品牌失败...')
            exit()
        #统计品牌数,排查和订单配置一样的品牌并点击
        time.sleep(1)
        for i in range(10):
            try:
                all_product = driver.find_element_by_xpath('//div[text()="品牌"]/following-sibling::div/ul')
                products = all_product.find_elements_by_tag_name('li')
                for li in products:
                    if li.text == product:
                        li.click()
                        logging.info('产品品牌：%s'%product)
                        try:
                            driver.find_element_by_xpath('//a[contains(text(),"确定")]').click()
                            logging.info('点击->【确定】')
                        except:
                            logging.error('!!!!!点击确定失败...')
                            exit()
                        break
                break
            except:
                if i == 9:
                    Driver.screen_shop(driver)
                    logging.error('!!!!!选择产品品牌失败...')
                    exit()
                else:
                    pass
        #选择产品线
        Element = driver.find_element_by_xpath('//div[text()="产品品牌"]/../../..')
        Element.find_element_by_xpath('.//li[2]').click()
        logging.info('.....点击->【产品品线】')
        time.sleep(1)
        for i in range(10):
            try:
                Element1 = driver.find_element_by_xpath('//*[@class="header"]/following-sibling::div[3]')
                All_PX = Element1.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                PXList = All_PX.find_elements_by_tag_name('li')
                for PXText in PXList:
                    if PXText.text == PinX:
                        PXText.click()
                        logging.info('.....产品线：%s'%PinX)
                        time.sleep(1)
                        Element1.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                        logging.info('.....点击->【确定】')
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择品线失败！')
                    exit()
        #选择产品品类
        Element.find_element_by_xpath('.//li[3]').click()
        logging.info('.....点击->【产品品类】')
        time.sleep(1)
        for i in range(10):
            try:
                Element2 = driver.find_element_by_xpath('//*[@class="header"]/following-sibling::div[4]')
                All_PL = Element2.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                PLList = All_PL.find_elements_by_tag_name('li')
                for PLText in PLList:
                    if PLText.text == PinL:
                        PLText.click()
                        logging.info('.....产品线：%s'%PinL)
                        time.sleep(1)
                        Element2.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                        logging.info('.....点击->【确定】')
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择品线失败！')
                    exit()
        #选择规格信息
        time.sleep(1)
        Element.find_element_by_xpath('.//li[4]').click()
        logging.info('.....点击->【产品规格】')
        time.sleep(1)
        for i in range(10):
            try:
                Element3 = driver.find_element_by_xpath('//*[@class="header"]/following-sibling::div[6]')
                All_GG = Element3.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                GGList = All_GG.find_elements_by_tag_name('li')
                for GGText in GGList:
                    if GGText.text == GuiG:
                        GGText.click()
                        logging.info('.....产品线：%s'%GuiG)
                        time.sleep(1)
                        Element3.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                        logging.info('.....点击->【确定】')
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择品线失败！')
                    exit()
        #打开选择界面
        try:
            driver.find_element_by_xpath('//div[text()="抢单时效"]/following-sibling::div').click()
            logging.info('点击->【抢单时效】')
        except:
            logging.error('!!!!!点击抢单时效失败...')
            exit()
        #随机选择抢单时效
        for i in range(10):
            try:
                Element4 = driver.find_element_by_xpath('//*[@class="header"]/following-sibling::div[5]')
                AllTimeSX = Element4.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                Times = AllTimeSX.find_elements_by_tag_name('li')
                TimeCount = random.randint(1,len(Times))
                num = 1
                for Time in Times:
                    Time.click()
                    if num == TimeCount:
                        time.sleep(0.5)
                        tm = Time.text
                        logging.info('抢单时效：%s'%tm)
                        Element4.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                        logging.info('点击->【确认】')
                        break
                    num += 1
                break
            except:
                if i == 9:
                    Driver.screen_shop(driver)
                    logging.error('!!!!!选择时效失败...')
                    exit()
                else:
                    pass
        #填写服务描述信息
        times = time.strptime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        write_msg = massage.split('+')[0] + times
        try:
            driver.find_element_by_xpath('//textarea').send_keys(write_msg)
            logging.info('服务描述：%s'%write_msg)
        except:
            logging.error('!!!!!输入备注失败...')
            pass
        #点击->下一步，填写用户信息
        for i in range(10):
            try:
                driver.find_element_by_xpath('//a[text()="下一步,填写用户信息"]').click()
                logging.info('点击->【下一步】')
                break
            except:
                if i == 10:
                    logging.error('!!!!!点击下一步失败...')
                    exit()
                else:
                    pass
        #填写用户信息，姓名、手机、详细地址
        time.sleep(1)
        for i in range(5):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请输入用户姓名"]').send_keys(user)
                logging.info('联系人：%s'%user)
                driver.find_element_by_xpath('//input[@placeholder="请输入用户手机号"]').send_keys(phe)
                logging.info('联系电话：%s'%phe)
                driver.find_element_by_xpath('//input[@placeholder="请输入详细地址"]').send_keys(area)
                logging.info('详细地址：%s'%area)
                break
            except:
                if i == 4:
                    Driver.screen_shop(driver)
                    logging.error('!!!!!输入基本信息失败...')
                    exit()
                else:
                    pass
        #点击打开选择狂
        try:
            driver.find_element_by_xpath('//div[starts-with(text(),"选择省份")]').click()
            logging.info('点击->【选择地址】')
        except:
            logging.error('!!!!!点击选择地址失败...')
            exit()
        #获取配置文件地址信息
        pro,city,collage = address.split('-')
        #匹配省市区
        time.sleep(1)
        for i in range(1,4):
            try:
                Element5 = driver.find_element_by_xpath('//*[@class="header"]/following-sibling::div[7]')
                AllPlaces = Element5.find_element_by_xpath('.//div[@class="van-picker__columns"]/div['+str(i)+']/ul')
                PlaceList = AllPlaces.find_elements_by_tag_name('li')
                for Place in PlaceList:
                    Place.click()
                    if Place.text == pro or Place.text == city or Place.text == collage:
                        if i == 3:
                            logging.info('.....服务地址：%s'%address)
                            Element5.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                            logging.info('.....点击->【确定】')
                        break
            except:
                logging.error('!!!!!选择省市区失败！')
                exit()
        #用户预约时间选择当天时间
        try:
            driver.find_element_by_xpath('//i[@class="icon-rl2"]').click()
            logging.info('点击->【用户预约】')
            time.sleep(1)
            Element5.find_element_by_xpath('./following-sibling::div[1]/./div[@class="van-picker__confirm"]').click()
            logging.info('点击->【确认】')
            logging.info('预约时间：%s'%times)
        except:
            Driver.screen_shop(driver)
            logging.error('!!!!!预约时间失败...')
            exit()
        #选择预约时间段，随机选择当天的某一时间段
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//i[@class="icon-time"]').click()
            logging.info('点击->【选择时间段】')
        except:
            logging.error('!!!!!点击预约时间段失败...')
            exit()
        #随机选择时间段
        for i in range(10):#随机筛选预约时间段
            try:
                Element6 = driver.find_element_by_xpath('//div[@class="van-modal"]/preceding-sibling::div[1]')
                AllDay = Element6.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                Days = AllDay.find_elements_by_tag_name('li')
                SelectDay = random.randint(1,len(Days)) #统计所有的时间段随机筛选并选择
                num = 1
                for Day in Days:
                    Day.click()
                    if num == SelectDay:
                        DayInfo = Day.text
                        logging.info('预约时间段：%s'%DayInfo)
                        Element6.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                        logging.info('点击->【确认】')
                        break
                    num += 1
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择预约时间段失败...')
                    exit()
                else:
                    pass
        #点击->【下一步，设置价格】按钮
        try:
            WebDriverWait(driver,5).until(lambda x:x.find_element_by_css_selector('a.btn.btn-blue.submit-btn.col-6')).click()
            logging.info('点击->【下一步,设置价格】')
        except:
            logging.error('!!!!!点击设置价格失败...')
            exit()
        #点击->【立即派单】按钮
        try:
            WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath('//a[contains(text(),"立即派单")]')).click()
            logging.info('点击->【立即派单】')
        except:
            logging.error('!!!!!点击立即派单失败...')
            exit()
        #点击确认支付->【确认】按钮
        try:
            WebDriverWait(driver,5).until(
                lambda x:x.find_element_by_xpath('//div[contains(text(),"确认支付"]/following-sibling::div[2]/button[2]')).click()
            logging.info('点击->【确认】')
        except:
            logging.error('!!!!!确认支付失败...')
            exit()
        #判断订单价格和钱包余额选择支付方式并确认支付
        for i in range(5):
            try:
                time.sleep(2)
                pay = driver.find_element_by_xpath('//span[@class="payorder-number"]').text
                logging.info('订单总价：%s'%pay)
                attribute = driver.find_element_by_xpath('//div[@class="pay-method content-block"]/ul/li[1]').get_attribute('class')
                if attribute == 'active': #只选择钱包支付其他不考虑
                    logging.info('钱包余额充足可以支付')
                    try:
                        driver.find_element_by_xpath('//div[@class="btn btn-blue"and@text()="确认支付"]').click()
                        logging.info('点击->【确认支付】')
                    except:
                        logging.error('!!!!!点击确认支付失败...')
                elif attribute == 'disabled':
                    logging.info('钱包余额不足,请充值...')
                    exit()
                break
            except:
                if i == 4:
                    logging.error('!!!!!支付失败...')
                    exit()
                else:
                    pass
        #点击确认支付->【确认】按钮
        try:
            WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//div[contains(text(),"确认支付"]/following-sibling::div[2]/button[2]')).click()
            logging.info('点击->【确认】')
        except:
            logging.error('!!!!!确认支付失败...')
            exit()
        #点击支付成功->【立即前往】按钮
        try:
            WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//div[contains(text(),"支付成功"]/following-sibling::div[2]/button[2]')).click()
            logging.info('点击->【确认】')
        except:
            logging.error('!!!!!确认支付失败...')
            exit()

    def PleaseOrder(driver,OrderNumber,PDmodel,GaiPai='no',WDname=None):

        '''
        WAP品牌商派单
        :param OrderNumber: 派单单号
        :param PDmodel: 派单方式，自有网店和市场
        :param GaiPai:默认不改派，yes为点击改派订单按钮
        :param WDname: 派单网店名称
        :param url: 地址
        :return:
        '''
        #-----------------------------------------------------【品牌商派订单】--------------------------------------------
        #打开待审核订单的页面派单
        driver.implicitly_wait(20)
        if GaiPai == 'no':
            #默认点击派单按钮，实行派单流程
            logging.info('<=====>【WAP品牌商派单】<=====>')
            Brands.Find_ClickButton(driver,Model='待审核',OrderNumber=OrderNumber,ButtonText='派单')
        #如果是改派就打开订单查询页面改派
        elif GaiPai == 'yes':
            #yes执行改派流程点击【改派】按钮了
            logging.info('<=====>【WAP品牌商改派订单】<=====>')
            Brands.Find_ClickButton(driver,Model='订单查询',OrderNumber=OrderNumber,ButtonText='改派')
        #指定派单网点信息 ->派单到【测试网点01】 系统单固定选择保内 、自有网点
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//a[text()="保内"]').click()
            logging.info('.....点击->【保内】')
        except:
            pass
        #判断派单到网点，还是市场，zi = 自有网点 shi = 枪弹市场
        if PDmodel == 'zi':
            #点击-【自由网点】
            driver.find_element_by_xpath('//a[text()="自有网点"]').click()
            logging.info('.....派单到：【自有网点】')
            #派单到自由网点情况
            #统计师傅数量
            for i in range(10):
                try:
                    AllBranchList = driver.find_element_by_xpath('//div[@class="leaflets-list"]/ul')
                    Branchs = AllBranchList.find_elements_by_tag_name('li')
                    BranchCount = len(Branchs)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!统计师傅失败！')
                        exit()
            #遍历师傅名称信息，选择师傅
            for i in range(BranchCount):
                try:
                    FindBranchName = Branchs[i].find_element_by_xpath('.//div[2]/p').text
                    if FindBranchName == WDname:
                        Branchs[i].find_element_by_xpath('.//div[3]/label/input').click()
                        logging.info('.....派单到网点：%s'%FindBranchName)
                        break
                except:
                    logging.error('!!!!!选择网点失败！')
                    pass
            #点击确定派单
            try:
                driver.find_element_by_xpath('//a[@class="btn btn-blue submit-btn"]').click()
                logging.info('.....点击->【确定】')
            except:
                logging.error('!!!!!!点击确定失败...')
                exit()
            #获取系统提示信息
            try:
                PDmsg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="app"]/following-sibling::div/div')).text
                logging.info('.....系统提示：%s'%PDmsg)
            except:
                pass
        #派单到抢单市场，默认网点名称为空
        elif PDmodel == 'shi':
            #点击选择抢单市场
            try:
                driver.find_element_by_xpath('//a[text()="抢单市场"]').click()
                logging.info('.....派单到：【抢单市场】')
            except:
                logging.error('!!!!!派单到失败...')
                exit()
            #直接点击确定
            try:
                driver.find_element_by_xpath('//a[@class="btn btn-blue submit-btn"]').click()
                logging.info('.....点击->【确定】')
            except:
                logging.error('!!!!!!点击确定失败...')
                exit()
            #点击->【下一步，设置价格】
            time.sleep(2)#必须等待加载完
            click = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//a[text()="下一步，设置价格"]'))
            click.click()
            logging.info('.....点击->【下一步，设置价格】')
            #随机抢单时效选择【6、12、24小时】
            for i in range(5):
                try:
                    all_lis = driver.find_element_by_xpath('//*[@class="col-w3  clearfix"]/ul')
                    lis = all_lis.find_elements_by_tag_name('li')
                    sel_li = random.randint(1,len(lis))
                    #选择抢单时效
                    shixiao = driver.find_element_by_xpath('//*[@class="col-w3  clearfix"]/ul/li[' +str(sel_li)+ ']')
                    SXinfo = shixiao.text
                    shixiao.click()
                    logging.info('.....选择抢单时效：%s'%SXinfo)
                    break
                except:
                    if i == 4:
                        logging.error('!!!!!选择抢单时效失败...')
                        exit()
                    else:
                        pass
            #点击->【立即派单】按钮
            driver.find_element_by_css_selector('a.btn.btn-blue.submit-btn.col-6').click()
            #获取系统提示信息
            try:
                PDmsg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="app"]/following-sibling::div/div')).text
                logging.info('.....系统提示：%s'%PDmsg)
            except:
                pass
            #选择支付方式，默认的钱包支付
            for i in range(5):
                try:
                    QBactive = driver.find_element_by_xpath('//div[@class="pay-method content-block"]/ul/li[1]').get_attribute('class')
                    if QBactive == 'active':
                        try:
                            driver.find_element_by_xpath('//a[text()="确认支付"]').click()
                            logging.info('.....点击->【确认支付】')
                            # 点击确认
                            WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//button[2]')).click()
                            logging.info('.....点击->【确认】')
                        except:
                            logging.error('!!!!!点击确认支付失败...')
                            exit()
                    else:
                        logging.warning('!!!!!钱包余额不足，请充值...')
                        pass
                    break
                except:
                    if i == 4:
                        logging.error('!!!!!选择支付方式失败...')
                        exit()
                    else:
                        pass
            #获取系统提示信息
            try:
                PDmsg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="app"]/following-sibling::div/div')).text
                logging.info('.....系统提示：%s' % PDmsg)
            except:
                pass

    def FindOrderNumber(driver):

        #---------------------------------------------【查找订单号】-----------------------------------------------------
        #进入WAP品牌商订单审核页面
        logging.info('<=====>【查找订单编号】<=====>')
        driver.get('http://www.51shouhou.cn/wapbrand/#/my/markettrade?tab=%E5%BE%85%E5%AE%A1%E6%A0%B8')
        driver.refresh()
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="card-list-content"][1]').click()
        #默认第一个订单为最新订单
        for i in range(10):
            time.sleep(2)
            try:
                #获取下单时间转化为时间戳判断下单时间小于60就是新建订单
                FindAddTime = driver.find_element_by_xpath('//span[text()="下单时间"]/following-sibling::div').text
                OldTime = time.mktime(time.strptime(FindAddTime,'%Y-%m-%d %H:%M:%S'))
                NewTime = time.time()
                Time = NewTime - OldTime
                if Time < 60:
                    FindOrderNumber = driver.find_element_by_xpath('//span[text()="订单编号"]/following-sibling::div').text
                    logging.info('.....该订单为新建订单,订单单号：%s'%FindOrderNumber)
                    break
                else:
                    logging.error('!!!!!该订单创建时间大于60不是新建订单')
                    exit()
            except:
                if i == 9:
                    logging.error('!!!!!获取订单单号失败')
                    exit()
                else:
                    pass
        return FindOrderNumber

    def PPS_CheckOrderStatus(driver,CheckOrderNumber,CheckOrderStatus):

        #---------------------------------------------【品牌商订单状态校验】---------------------------------------------

        #进入订单查询页面,品牌商wap端没有全部订单栏，url拼接查询符合订单状态的订单列表查找订单单号，验证订单状态
        logging.info('<=====>【WAP品牌端订单状态校验】<=====>')
        if CheckOrderStatus == '待审核':
            driver.get('http://www.51shouhou.cn/wapbrand/#/my/markettrade?tab=%E5%BE%85%E5%AE%A1%E6%A0%B8')
        elif CheckOrderStatus != '待审核':
            if CheckOrderStatus == '等待网点派单':
                url = '%E5%BE%85%E6%B4%BE%E5%8D%95'
            elif CheckOrderStatus == '等待师傅预约':
                url = '%E5%BE%85%E9%A2%84%E7%BA%A6'
            elif CheckOrderStatus == '等待师傅服务':
                url = '%E5%BE%85%E6%9C%8D%E5%8A%A1'
            elif CheckOrderStatus == '师傅服务中':
                url = '%E6%9C%8D%E5%8A%A1%E4%B8%AD'
            elif CheckOrderStatus == '等待收款':
                url = '%E5%BE%85%E6%94%B6%E6%AC%BE'
            elif CheckOrderStatus == '等待品牌商结算':
                url = '%E5%BE%85%E7%BB%93%E7%AE%97'
            elif CheckOrderStatus == '已完成':
                url = '%E5%B7%B2%E5%AE%8C%E6%88%90'
            elif CheckOrderStatus == '已取消':
                url = '%E5%B7%B2%E5%8F%96%E6%B6%88'
            driver.get('http://www.51shouhou.cn/wapbrand/#/my/markettrade?tab=%E8%AE%A2%E5%8D%95%E6%9F%A5%E8%AF%A2&ddctl='+url+'&from=dingdan')
        else:
            logging.error('!!!!!品牌商订单状态校验url拼接失败')
        driver.refresh()
        time.sleep(2)
        #统计全部订单数量信息
        for i in range(10):
            try:
                if CheckOrderStatus == '待审核':
                    OrderList = driver.find_element_by_xpath('//div[@class="wrap "]/div[2]')
                else:
                    OrderList = driver.find_element_by_xpath('//div[@class="wrap u-mfooter"]/div[11]')
                Orders = OrderList.find_elements_by_tag_name('i')
                OrderNumber = int(len(Orders)/3)
                break
            except:
                if i == 9:
                    logging.error('!!!!!订单统计失败')
                    exit()
                else:
                    pass
        #查找订单单号校验订单状态
        for i in range(1,OrderNumber):
            time.sleep(1)
            try:
                driver.find_element_by_xpath('//div[@class="card-list"]['+str(i)+']/div[2]/a/div').click()
                time.sleep(2)
                FindOrderNumber = WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath('//span[text()="订单编号"]/following-sibling::div')).text
                if FindOrderNumber == CheckOrderNumber:
                    #找到订单验证订单状态，没有找到返回订单列表
                    logging.info('.....找到订单了！订单编号：%s'%FindOrderNumber)
                    FindOrderStatus = driver.find_element_by_xpath('//span[text()="订单状态"]/following-sibling::div').text
                    if FindOrderStatus == CheckOrderStatus:
                        logging.info('.....订单状态验证成功！当前订单状态：%s'%FindOrderStatus)
                    else:
                        logging.error('!!!!!订单状态验证失败！当前订单状态：%s,验证订单状态：%s'%(FindOrderStatus,CheckOrderStatus))
                    break
                else:
                    #返回继续循环
                    driver.find_element_by_xpath('//i[@class="icon-left"]').click()
            except:
                if i == OrderNumber-1:
                    logging.error('!!!!!找不到订单单号')
                    exit()
                else:
                    pass




# if __name__ == '__main__':
#     from Common import Driver
#     D = Driver.WAP_Brower()
#     Brands.PPS_login(D,'PPS_Login','pps_username','pps_password')
#     Brands.PleaseOrder(D,OrderNumber='AZ19031400000066',PDmodel='shi',GaiPai='yes')























