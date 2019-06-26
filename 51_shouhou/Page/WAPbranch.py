# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

import logging,time,random,configparser,os
from Common import GetCode
from Common import Pubilc
from selenium.webdriver.support.wait import WebDriverWait

class Branch(object):

    def WD_login(driver,section,username,HTdriver,WDHandle='table',url='http://www.51shouhou.cn/wapbranch/#/my'):

        '''
        WAP网店登录
        :param section:配置文件WAP网店登录section
        :param username:用户名
        :param HTdriver:后台浏览器driver
        :param WDHandle:网店登录是否切换窗口
        :param url:地址
        :return:
        '''
        #获取品牌商登陆配置
        Data_Path = Pubilc.data_dir(filename='Login.ini')
        data = configparser.ConfigParser()
        data.read(Data_Path, encoding='utf-8')
        use = data.get(section,username)
        #pwd = data.get(section, password)

        #----------------------------------------------【WAP网点登陆】----------------------------------------------------
        #打开WAP网点登陆网址信息
        logging.info('<=====>【WAP网点登陆】<=====>')
        if WDHandle == 'table':
            Pubilc.table_handle(driver=driver,url=url)
        elif WDHandle == 'new':
            driver.get(url)
        wd_handle = driver.current_window_handle
        #点击登陆进入登陆页面
        for i in range(20):
            try:
                time.sleep(1)
                driver.find_element_by_xpath('//*[@class="wrap"]/div[2]/div/div[2]/h2').click()
                logging.info('......点击->【登陆/注册】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击“登陆/注册”失败')
                    exit()
        #输入手机号发送验证码
        time.sleep(1)
        for i in range(5):
            try:
                element = driver.find_element_by_xpath('//*[@id="footer"]/following-sibling::div[2]/div/form[3]')
                element.find_element_by_xpath('.//input[@placeholder="请输入手机号"]').clear()
                element.find_element_by_xpath('.//input[@placeholder="请输入手机号"]').send_keys(use)
                logging.info('.....输入用户名：%s'%use)
                element.find_element_by_xpath('.//a[text()="发送验证码"]').click()
                logging.info('.....点击->【发送验证码】')
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入手机号报错')
                    exit()
                else:
                    pass
        #登陆后台查询验证码信息
        checkNum = GetCode.FindCheckNum(HTdriver,Phonenum=use)
        #输入查询的验证码登陆
        for i in range(5):
            try:
                element.find_element_by_xpath('.//input[@placeholder="验证码"]').clear()
                element.find_element_by_xpath('.//input[@placeholder="验证码"]').send_keys(checkNum)
                logging.info('.....输入验证码：%s'%checkNum)
                element.find_element_by_xpath('.//a[@class="pop-login-btn mtrop"]').click()
                logging.info('.....点击->【登陆】')
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入验证码失败...')
                    exit()
                else:
                    pass
        #获取登陆异常
        try:
            login_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="qb-sougou-search"]/following-sibling::div/div')).text
            logging.info('.....系统提示：%s'%login_msg)
        except:
            pass
        #判断网点登陆
        for i in range(5):
            try:
                check_info = driver.find_element_by_xpath('//div[@class="user-store-code"]/p').text
                if check_info == '店铺码':
                    logging.info('.....WAP网点登陆成功！')
                else:
                    logging.error('!!!!!WAP网点登陆失败')
                    exit()
                break
            except:
                pass
        return wd_handle

    def WD_ShouD(driver,OrderNumber,url="http://www.51shouhou.cn/wapbranch/#/order/index?statusName=%E5%85%A8%E9%83%A8"):

        #-----------------------------------------------【网店收单校验】---------------------------------------------------
        # 进入网点订单管理页面
        logging.info('<=====>【网点接单校验】<=====>')
        for i in range(5):
            try:
                driver.get(url)
                driver.refresh()
                logging.info('.....正在进入订单管理页面...')
                break
            except:
                if i == 4:
                    logging.error('!!!!!进入订单管理页面失败...')
                    exit()
                else:
                    pass
        #搜索订单号，派单师傅
        isPass=False
        for i in range(5):
            try:
                time.sleep(1)
                driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号、订单号"]').clear()
                driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号、订单号"]').send_keys(OrderNumber)
                logging.info('.....输入订单号：%s' % OrderNumber)
                driver.find_element_by_xpath('//a[@class="search-btn"]').click()
                logging.info('.....点击->【搜索】')
                isPass=True
                break
            except:
                if i == 4:
                    logging.error('!!!!!搜索订单失败...')
                    exit()
                else:
                    pass
        #判断搜索出的订单是否是拍单订单
        if isPass:
            for i in range(5):
                try:
                    time.sleep(2)
                    ordernum = driver.find_element_by_xpath('//*[@id="view"]/div/div[1]/div[10]/div')
                    nums = ordernum.find_elements_by_tag_name('h2')
                    if len(nums) > 0:
                        logging.info('.....网点接受订单成功！')
                    else:
                        logging.error('!!!!!网点没有收到订单...')
                    break
                except:
                    if i == 4:
                        logging.error('!!!!!统计搜索订单失败...')
                        exit()
                    else:
                        pass
        elif isPass == False:
            logging.error('!!!!!搜索订单失败...')

    def PleaseOrder(driver,OrderNumber,sfName=None,ButtonText='派给师傅'):

        '''
        WAP网店派单
        :param orderNumber: 派单单号
        :param sfName: 接单师傅名称
        :param url: 拍单地址
        :return:
        '''
        #-----------------------------------------------【网点派单】-----------------------------------------------------
        #进入网点订单管理页面
        driver.implicitly_wait(20)
        logging.info('<=====>【网点派单】<=====>')
        driver.get('http://www.51shouhou.cn/wapbranch/#/order/index?statusName=%E5%85%A8%E9%83%A8')
        driver.refresh()
        logging.info('.....正在进入订单管理页面...')
        #搜索订单号，派单师傅
        isSearch = False
        for i in range(10):
            try:
                time.sleep(2)
                driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号、订单号"]').clear()
                driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号、订单号"]').send_keys(OrderNumber)
                logging.info('.....输入订单号：%s'%OrderNumber)
                driver.find_element_by_xpath('//a[@class="search-btn"]').click()
                logging.info('.....点击->【搜索】')
                isSearch = True
                break
            except:
                if i == 9:
                    logging.error('!!!!!搜索订单失败...')
                    exit()
                else:
                    pass
        #点击派单到师傅
        if isSearch:
            for i in range(10):
                try:
                    time.sleep(1)
                    element = driver.find_element_by_xpath('//a[text()="搜索"]/../../following-sibling::div/div')
                    AllButtons = element.find_element_by_xpath('.//div/./div[@class="card-list-foot"]')
                    ButtonList = AllButtons.find_elements_by_tag_name('a')
                    for Button in ButtonList:
                        if Button.text == ButtonText:
                            Button.click()
                            logging.info('.....点击->【%s】'%ButtonText)
                            break
                    break
                except:
                    if i == 9:
                        logging.info('.....点击”%s“失败'%ButtonText)
                        exit()
                    else:
                        pass
            #指定派单师傅名称，派单
            if sfName == None:
                pass
            else:
                time.sleep(2)
                if driver.find_element_by_xpath('//a[text()="确定派单"]').is_displayed():
                    pass
                else:
                    logging.error('!!!!!没有进入派单页面！')
                    exit()
                #网点派单
                for i in range(5):
                    try:
                        all_sf = driver.find_element_by_xpath('//*[@class="master-list"]/ul')
                        sfNums = all_sf.find_elements_by_tag_name('li')
                        for j in range(1,len(sfNums)+1):
                            try:
                                sf_name = all_sf.find_element_by_xpath('.//li['+str(j)+']/div[2]/div[1]/div[1]').text
                                if sf_name == sfName:
                                    all_sf.find_element_by_xpath('.//li['+str(j)+']/span').click()
                                    logging.info('.....选择派单给师傅：%s'%sf_name)
                                    driver.find_element_by_xpath('//a[text()="确定派单"]').click()
                                    logging.info('.....点击->【确定派单】')
                                    break
                            except:
                                pass
                        break
                    except:
                        if i == 4:
                            logging.error('!!!!!确认派单失败...')
                            exit()
                        else:
                            pass
                #获取拍单给师傅的系统消息
                time.sleep(2)
                try:
                    PD_msg = driver.find_element_by_xpath('//a[@href="#/order/index"and@class="btn btn-big btn-white"]')
                    if PD_msg:
                        PD_msg.click()
                        logging.info('.....网点派单成功！点击->【继续预约派单】')
                    else:
                        logging.error('!!!!!派单失败...')
                except:
                    pass


    def WD_logout(driver,url='http://www.51shouhou.cn/wapbranch/#/my'):

        #-----------------------------------------------【网点退出】-----------------------------------------------------
        #点击我的并退出
        for i in range(20):
            try:
                driver.get(url)
                time.sleep(1)
                button = driver.find_element_by_xpath('//*[@id="MyBranch"]/preceding-sibling::div[1]/div[6]/div')
                driver.execute_script("arguments[0].scrollIntoView();",button)
                button.click()
                break
            except:
                if i == 19:
                    logging.info('!!!!!网点退出失败...')
                    exit()
                else:
                    pass

    def WD_CheckOrderStatus(driver,CheckOrderNumber,CheckOrderStatus):

        #------------------------------------------【网点订单状态校验】--------------------------------------------------
        #进入网点订单查询地址页面
        logging.info('<=====>【WAP网点订单状态校验】<=====>')
        driver.get('http://www.51shouhou.cn/wapbranch/#/order/index?statusName=%E5%85%A8%E9%83%A8')
        driver.refresh()
        logging.info('.....正在进入网点订单管理页面...')
        #搜索订单单号
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="输入手机号、订单号"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="输入手机号、订单号"]').send_keys(CheckOrderNumber)
                driver.find_element_by_xpath('//a[@class="search-btn"]').click()
                break
            except:
                if i == 9:
                    logging.error('!!!!!搜索订单失败')
                    exit()
                else:
                    pass
        #统计订单数量
        try:
            time.sleep(2)
            All_Orders = driver.find_element_by_xpath('//div[@class="order-content"]/div')
            Orders = All_Orders.find_elements_by_tag_name('h2')
            Numbers = len(Orders)
        except:
            logging.error('!!!!!统计订单失败')
            pass
        #判断订单状态信息
        if Numbers > 1:
            logging.info('.....找到订单啦！')
            for i in range(10):
                try:
                    FindOrderStatus = driver.find_element_by_xpath('//div[@class="card-order-state"]').text
                    if FindOrderStatus == CheckOrderStatus:
                        logging.info('.....订单状态校验成功！当前订单状态：%s'%FindOrderStatus)
                    else:
                        logging.error('!!!!!订单状态校验失败！当前订单状态：%s,校验订单状态：%s'%(FindOrderStatus,CheckOrderStatus))
                    break
                except:
                    if i == 9:
                        logging.info('!!!!!获取订单状态失败')
                        exit()
                    else:
                        pass

    def WD_FinishServer(driver,BJName=None,BJ_UseNumber=1,OtherPrices=1):

        #---------------------------------------------【WAP网点完成服务】------------------------------------------------
        #判断是否进入填写工单页面
        logging.info('<=====>【师傅完成服务】<=====>')
        logging.info('-=【填写工单】=-')
        time.sleep(1)
        for i in range(10):
            try:
                active = driver.find_element_by_xpath('//div[@class="wrap"]/div[1]/div/ul/li[1]')
                if active.get_attribute('class') == 'active':
                    logging.info('.....开始填写工单...')
                    break
                else:
                    active.click()
                    break
            except:
                if i == 9:
                    logging.error('!!!!!不是填写工单页面！')
                    exit()
        #输入机身条码
        PhoneNumber = 'JsTm' + str(int(time.time()))
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@class="text-input"]').clear()
                driver.find_element_by_xpath('//input[@class="text-input"]').send_keys(PhoneNumber)
                logging.info('.....输入机身条码:%s'%PhoneNumber)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入机身条码失败')
                    exit()
                else:
                    pass
        #点击选择服务措施信息
        try:
            driver.find_element_by_xpath('//div[text()="服务措施"]/following-sibling::div/div').click()
            logging.info('.....点击->【服务措施】')
        except:
            logging.error('!!!!!点击“服务措施”失败！')
            exit()
        #随机选择服务措施信息
        time.sleep(2)
        for i in range(10):
            try:
                Element = driver.find_element_by_xpath('//a[text()="下一步"]/../../div[8]/div')
                AllServerSteps = Element.find_element_by_xpath('.//div[@class="van-picker-column"]/ul')
                ServerSteps = AllServerSteps.find_elements_by_tag_name('li')
                SelectNumber = random.randint(2,len(ServerSteps))
                time.sleep(1)
                ServerSteps[SelectNumber-1].click()
                logging.info('.....服务措施：%s'%ServerSteps[SelectNumber-1].text)
                #点击确定按钮
                try:
                    Element.find_element_by_xpath('.//div[@class="van-picker__confirm"]').click()
                    logging.info('.....点击->【确定】')
                except:
                    logging.error('!!!!!点击“确定”失败！')
                    exit()
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择服务措施失败！')
                    exit()
                else:
                    pass
        #获取上传图片的路径信息
        ParentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DataPath = ParentPath + '\\Config\\Picture\\'
        PictureList = os.listdir(DataPath)
        PictureNumber = len(PictureList)
        #上传文件父路径信息
        ParentElement = driver.find_element_by_xpath('//a[text()="下一步"]/../preceding-sibling::div[1]/div/div')
        #循环上传图片信息
        for i in range(PictureNumber):
            try:
                Data = DataPath + PictureList[i]
                AddPicture = ParentElement.find_element_by_xpath('.//input[@type="file"and@class="van-uploader__input"]')
                driver.execute_script("arguments[0].scrollIntoView();",AddPicture)
                time.sleep(1)
                AddPicture.send_keys(Data)
                logging.info('.....正在上传图片：%s'%Data)
            except:
                logging.error('!!!!!上传图片失败！')
                exit()
        #填写备注信息
        try:
            driver.find_element_by_xpath('//textarea[@placeholder="服务描述，请留言给商家(限50字)"]').send_keys('网点完成服务')
            logging.info('.....备注：网点完成服务')
        except:
            logging.error('!!!!!输入备注失败！')
            pass
        #点击下一步
        WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//a[text()="下一步"]')).click()
        logging.info('.....点击->【下一步】')
        #判断是否进入使用备件页面
        logging.info('-=【使用备件】=-')
        time.sleep(5)
        for i in range(10):
            try:
                active2 = driver.find_element_by_xpath('//div[@class="wrap"]/div[1]/div/ul/li[2]')
                if active2.get_attribute('class') == 'active':
                    logging.info('.....开始使用备件...')
                    break
                else:
                    active2.click()
                    break
            except:
                if i == 9:
                    logging.error('!!!!!不是使用备件页面！')
                    exit()
        #判断是否使用备件
        if BJName == None:
            logging.info('.....不使用备件！')
        else:
            #统计备件种类
            time.sleep(1)
            for i in range(10):
                try:
                    Element = driver.find_element_by_xpath('//div[@class="row-buttons"]/../div[@class="content-block"]')
                    BJList = Element.find_element_by_xpath('.//div[@class="repair-list"]/ul')
                    BJKindNumber = BJList.find_elements_by_tag_name('li')
                    Kinds = len(BJKindNumber)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!统计备件种类失败！')
                        exit()
            #循环遍历备件名称选择使用的备件
            for i in range(1,Kinds+1):
                try:
                    FindBJName = BJList.find_element_by_xpath('.//li['+str(i)+']/div[1]').text
                    FindBJNumber = BJList.find_element_by_xpath('.//li['+str(i)+']/div[2]/span[1]').get_attribute('class')
                    #属性'sum-input'为库存为零的情况
                    if FindBJName == BJName and FindBJNumber != 'sum-input':
                        logging.info('.....找到备件啦！库存充足！')
                        for j in range(BJ_UseNumber):
                            try:
                                time.sleep(1)
                                BJList.find_element_by_xpath('.//li['+str(i)+']/div[2]/span[2]/i').click()
                            except:
                                logging.info('.....点击使用备件失败！')
                        logging.info('.....使用备件：%s,%s个'%(BJName,BJ_UseNumber))
                        break
                    elif FindBJName == BJName and FindBJNumber == 'sum-input':
                        logging.info('.....找到备件啦！库存不足，请手动申请备件！')
                        break
                except:
                    logging.error('!!!!!找不到备件,使用备件失败！')
                    pass
        #提交服务报价
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//a[text()="下一步，提交服务报价"]')).click()
        logging.info('.....点击->【下一步，提交服务报价】')
        #判断是否进入服务报价页面
        logging.info('-=【提交服务报价】=-')
        time.sleep(5)
        for i in range(10):
            try:
                active3 = driver.find_element_by_xpath('//div[@class="wrap"]/div[1]/div/ul/li[3]')
                if active3.get_attribute('class') == 'active':
                    logging.info('.....开始提交服务报价...')
                    break
                else:
                    active3.click()
                    break
            except:
                if i == 9:
                    logging.error('!!!!!不是提交报价页面！')
                    exit()
        #输入用户其他付费默认1元
        for i in range(10):
            try:
                driver.find_element_by_xpath('//div[contains(text(),"其他")]/following-sibling::div/input').clear()
                driver.find_element_by_xpath('//div[contains(text(),"其他")]/following-sibling::div/input').send_keys(OtherPrices)
                logging.info('.....用户其他付费：1元')
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入其他费用失败！')
                    exit()
                else:
                    pass
        #点击完成服务
        isClick=False
        try:
            time.sleep(1)
            Button = driver.find_element_by_xpath('//a[text()="完成服务"]')
            driver.execute_script("arguments[0].scrollIntoView();",Button)
            Button.click()
            logging.info('.....点击->【完成服务】')
            isClick=True
        except:
            logging.error('!!!!!点击“完成服务失败”')
            exit()
        #点击确认订单完成
        if isClick:
            for i in range(20):
                try:
                    Accept = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//div[text()="订单已完成"]')).is_displayed()
                    if Accept:
                        driver.find_element_by_xpath('//div[@class="van-dialog__message"]/../../div[2]').click()
                        logging.info('.....点击->【确定】,完成服务！')
                        break
                except:
                    if i == 19:
                        logging.error('!!!!!没有弹窗啊！')
                        exit()
                    else:
                        pass















# if __name__ == '__main__':
#
#     from Common import Driver
#     B = Driver.PC_Brower()
#     A = Driver.WAP_Brower()
#     Branch.WD_login(A,'WD_Login','wd_username1',HTdriver=B,WDHandle='new')
#     Branch.PleaseOrder(A,OrderNumber='AZ19031300000068',ButtonText='完成服务')
#     Branch.WD_FinishServer(A,BJName='海尔自动化通用备件02',BJ_UseNumber=5)



    
