# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

import logging,time,random,configparser
from Common import Pubilc
from selenium.webdriver.support.wait import WebDriverWait

class KeFu(object):

    def __init__(self):

        pass

    def kf_login(driver,KFHandle='table',url='http://www.51shouhou.cn/nweb/sign/login'):

        #-----------------------------------------------【客服登录】------------------------------------------------------
        #获取客服账号密码
        DataPath = Pubilc.data_dir(filename='Login.ini')
        cf = configparser.ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        username = cf.get('KF_Login','kf_username')
        password = cf.get('KF_Login','kf_password')

        #客服登录
        logging.info('<=====>【客服登录】<=====>')
        if KFHandle == 'table':
            Pubilc.table_handle(driver=driver,url=url)
        elif KFHandle == 'new':
            driver.get(url)
            logging.info('.....正在进入客服...')
        KFhandle = driver.current_window_handle
        #登录->客服子账号登录
        for i in range(5):
            try:
                driver.find_element_by_xpath('//input[@type="text"]').clear()
                driver.find_element_by_xpath('//input[@type="text"]').send_keys(username)
                logging.info('.....输入用户名：%s'%username)
                driver.find_element_by_xpath('//input[@type="password"]').clear()
                driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
                logging.info('.....输入密码：%s'%password)
                driver.find_element_by_css_selector('a.login-btn').click()
                logging.info('.....点击->【登录】...')
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入用户名密码错误...')
                    exit()
                else:
                    pass
        #获取登录异常信息
        try:
            msg = WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath('//div[@id="ukf-float"]/following-sibling::div[2]/div')).text
            logging.info('.....系统提示/截图：%s' % msg)
            driver.screen_shop(driver)
        except:
            pass
        #判断登录是否成功
        try:
            text = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="softphone-makecall"]/div[2]')).text
            if text == '拨打':
                logging.info('.....客服登录成功！')
            else:
                logging.error('!!!!!客服登录失败...')
        except:
            pass

        return KFhandle

    def KF_HuiFang(driver,OrderNumber,url='http://ekf.51shouhou.cn/main/index#revisitlist/all'):

        #-----------------------------------------------【客服回访】-----------------------------------------------------
        #进入回访页面
        logging.info('<=====>【回访订单】<=====>')
        for i in range(10):
            try:
                driver.get(url)
                time.sleep(2)
                active = driver.find_element_by_xpath('//*[@id="VisitBigList"]/div[1]/ul/li[2]').get_attribute('class')
                if active == 'layui-this':
                    logging.info('.....打开回访网页...')
                    break
            except:
                if i == 9:
                    logging.error('!!!!!进不去回访页面...')
                    exit()
                else:
                    pass
        #搜索待回访订单，进入订单详情页面,默认False
        Search = False
        for i in range(5):
            time.sleep(1)
            try:
                driver.find_element_by_xpath('//input[@name="order"and@type="text"]').clear()
                driver.find_element_by_xpath('//input[@name="order"and@type="text"]').send_keys(OrderNumber)
                logging.info('.....输入搜索单号：%s'%OrderNumber)
                driver.find_element_by_xpath('//button[@class="layui-btn queryBtn"]').click()
                logging.info('.....点击->【查询】')
                Search = True
                break
            except:
                if i == 4:
                    logging.error('!!!!!搜索订单失败...')
                    exit()
                else:
                    pass
        #获取当前浏览器所有窗口的句柄
        oldhandles = driver.window_handles
        #点击搜所订单的单号进入新页面，True已经搜索出订单
        if Search == True:
            logging.info('.....找到回访订单啦！')
            time.sleep(1)
            for i in range(20):
                try:
                    WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//tbody[contains(@id,"view")]/tr/td[1]/span')).click()
                    break
                except:
                    if i == 19:
                        exit()
            logging.info('.....点击->【搜索订单】,...正在进入回访新页面...')
        else:
            logging.error('!!!!!找不到待回访订单...')
            exit()

        #获取最新浏览器所有标签页,切换到最新标签页面
        newhandles = driver.window_handles
        for handle in newhandles:
            if handle not in oldhandles:
                driver.switch_to.window(handle)

        #用户回访信息
        WebDriverWait(driver,2).until(lambda x:x.find_element_by_id('UserVisitFeedBack')).send_keys('用户回访01')
        time.sleep(1)
        #用户回访信息
        logging.info('**********【用户回访】**********')
        #统计大循环次数
        for i in range(10):
            try:
                AllModels = driver.find_element_by_xpath('//div[text()="用户回访"]/../div[2]/form/div')
                Models = AllModels.find_elements_by_tag_name('label')
                ModelNumbers = len(Models)+1
                break
            except:
                if i == 9:
                    logging.error('!!!!!统计所有模块失败！')
                    pass
        #循环大的模块随机选择满意度
        for i in range(1,ModelNumbers):
            try:
                ModelName = Models[i-1].text#选择模块的名字
                #统计满意度种类
                AllWellTypes = AllModels.find_element_by_xpath('.//div['+str(i)+']/div')
                WellTypes = AllWellTypes.find_elements_by_tag_name('span')
                SelectWellTypeNumber = random.randint(1,len(WellTypes))
                SelectWellType = WellTypes[SelectWellTypeNumber-1].text
                for i in range(10):
                    try:
                        time.sleep(1)
                        WellTypes[SelectWellTypeNumber-1].click()#随机匹配列表中满意度的信息点击
                        logging.info('.....%s：%s'%(ModelName,SelectWellType))
                        break
                    except:
                        if i == 9:
                            logging.error('!!!!!选择：%s失败！'%ModelName)
                            pass
            except:
                logging.error('!!!!!选择满意度失败！')
                pass
        logging.info('************【END】************')
        #填写用户反馈内容信息
        tm = time.strftime("%Y-%m-%d", time.localtime(time.time())) + '用户反馈'
        driver.find_element_by_xpath('//textarea[@name="visitfdCon"and@placeholder="填写反馈内容"]').send_keys(tm)
        logging.info('.....用户反馈信息：%s'%tm)
        #点击反馈信息
        time.sleep(1)
        for i in range(10):
            try:
                driver.execute_script('window.scrollBy(0,500)')
                driver.find_element_by_xpath('//*[@id="SubmitFeedback"]').click()
                logging.info('.....点击->【记录反馈】')
                break
            except:
                if i == 9:
                    logging.error('!!!!!记录反馈失败')
                    pass
        #获取记录反馈系统提示信息
        try:
            msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@type="dialog"]/div')).text
            logging.info('.....反馈提交提示：%s' % msg)
        except:
            pass
        #点击->回访
        for i in range(20):
            time.sleep(5)
            try:
                driver.find_element_by_xpath('//button[@class="layui-btn layui-btn-normal visitEndBtn"]').click()
                logging.info('....点击->【完成回访】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击回访失败...')
                    exit()
                else:
                    pass
        #获取回访完系统提示信息
        time.sleep(10)#默认等待回访完成
        try:
            msg = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//div[@type="dialog"]')).text
            logging.info(".....完成回访系统提示：%s"%msg)
        except:
            pass

    def KF_CheckHF(driver,OrderNumber,url='http://ekf.51shouhou.cn/main/index#revisitlist/all'):

        #-----------------------------------------------【验证回访】------------------------------------------------------
        #进入已回访页面
        logging.info('<=====>【回访校验】<=====>')
        driver.get(url)
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="VisitBigList"]/div[1]/ul/li[4]').click()
                logging.info('.....点击->【已回访】')
                break
            except:
                if i == 9:
                    logging.error('!!!!!进不去已回访页面...')
                    exit()
                else:
                    pass
        #搜索订单验证师傅已回访
        Search = False
        for i in range(5):
            try:
                driver.find_element_by_xpath('//input[@name="order"and@type="text"]').clear()
                driver.find_element_by_xpath('//input[@name="order"and@type="text"]').send_keys(OrderNumber)
                logging.info('.....输入搜索单号：%s'%OrderNumber)
                driver.find_element_by_xpath('//button[@class="layui-btn queryBtn"]').click()
                logging.info('.....点击->【查询】')
                Search = True
                break
            except:
                if i == 4:
                    logging.error('!!!!!搜索订单失败...')
                    exit()
                else:
                    pass
        #判断是否有已回访订单
        if Search:
            for i in range(10):
                try:
                    time.sleep(2)
                    Orders = driver.find_element_by_xpath('//tbody[contains(@id,"view")]/tr/td[1]').get_attribute('title')
                    if Orders == OrderNumber:
                        logging.info('.....订单回访成功啦！...')
                        break
                except:
                    if i == 9:
                        logging.error('!!!!!回访失败！')
                        pass
        else:
            logging.error('!!!!!已回访中搜索订单失败啦...')
            exit()

# if __name__ == '__main__':
#
#     from Common import Driver
#     driver = Driver.PC_Brower()
#     AA = KeFu.kf_login(driver,KFHandle='new')
#     KeFu.KF_HuiFang(driver,OrderNumber='AZ19030800000102')
#     driver.switch_to.window(AA)
#     KeFu.KF_CheckHF(driver,OrderNumber='AZ19030800000102')