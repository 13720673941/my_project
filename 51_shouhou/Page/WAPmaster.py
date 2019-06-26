# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from selenium.webdriver.support.wait import WebDriverWait
import time,random,logging,configparser,os
from Common import Pubilc

class Master(object):

    def SF_login(driver,section,username,password,MasterHandle='table',url='http://www.51shouhou.cn/appmaster/main.html#!/my/my.html'):

        #获取品牌商登陆配置
        Data_Path = Pubilc.data_dir(filename='Login.ini')
        data = configparser.ConfigParser()
        data.read(Data_Path, encoding='utf-8')
        use = data.get(section, username)
        pwd = data.get(section, password)

        #----------------------------------------------【WAP师傅登陆】----------------------------------------------------
        #打开师傅登陆页面
        logging.info('<=====>【WAP师傅登录】<=====>')
        driver.implicitly_wait(20)
        #切换窗口，js打开句柄还在原来的窗口
        if MasterHandle == 'new':
            driver.get(url)
            logging.info('....正在进入师傅登录页面...')
        elif MasterHandle == 'table':
            Pubilc.table_handle(driver=driver,url=url)
        sf_handle = driver.current_window_handle

        #点击登陆/注册按钮
        time.sleep(1)
        for i in range(20):
            try:
                driver.find_element_by_xpath('//*[@class="user-name my-username"]').click()
                logging.info('.....点击->【登陆/注册】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击“登陆”失败')
                    exit()
        #输入用户名密码点击登陆按钮
        for i in range(5):
            try:
                driver.find_element_by_id('txtPhone').clear()
                driver.find_element_by_id('txtPhone').send_keys(use)
                logging.info('.....输入用户名：%s'%use)
                driver.find_element_by_id('txtPwd').clear()
                driver.find_element_by_id('txtPwd').send_keys(pwd)
                logging.info('.....输入密码：%s'%pwd)
                driver.find_element_by_xpath('//a[text()="登录"]').click()
                logging.info('.....点击->【登陆】')
                break
            except:
                if i == 4:
                    logging.error('!!!!!登陆失败...')
                    exit()
                else:
                    pass
        #获取师傅登陆系统异常提示信息
        try:
            login_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....系统提示：%s'%login_msg)
        except:
            pass
        #判断师傅登陆是否成功
        time.sleep(2)
        for i in range(5):
            try:
                #点击我的
                driver.find_element_by_xpath('//div[@class="toolbar-inner"]/a[5]').click()
                time.sleep(1)
                title = driver.find_element_by_xpath('//div[@class="user-name my-username"]').text
                if title != '登录/注册':
                    logging.info('.....师傅登陆成功！')
                else:
                    logging.error('!!!!!师傅登陆失败...')
                    exit()
                break
            except:
                pass

        return sf_handle

    def SF_Order(driver,OrderNumber):

        #-------------------------------------------------【师傅预约订单】------------------------------------------------
        #进入预约订单页面进行订单预约
        logging.info('<=====>【师傅预约订单】<=====>')
        #初始化
        for i in range(10):
            try:
                driver.get('http://www.51shouhou.cn/appmaster/main.html#!/order/index.html?id=1')
                driver.refresh()
                time.sleep(1)
                active = driver.find_element_by_xpath('//*[@id="navtab"]/div/div/a[1]').get_attribute('class')
                if 'active' in active:
                    logging.info('.....正在进入带预约页面...')
                    break
            except:
                if i == 9:
                    logging.error('!!!!!进入带预约失败')
                    exit()
                else:
                    pass
        #遍历所有带预约订单，找到下单订单，
        time.sleep(1)
        for i in range(10):
            try:
                AllCardLists = driver.find_element_by_xpath('//*[@id="navtab"]/following-sibling::div/div[2]/ul')
                CardLists = AllCardLists.find_elements_by_tag_name('li')
                CardNumber = len(CardLists)
                break
            except:
                if i == 9:
                    logging.error('!!!!!获取待预约订单数量失败')
                    exit()
                else:
                    pass
        #匹配给个订单下的按钮文本 点击->【预约上门】
        for i in range(1,CardNumber):
            try:
                FindOrderNumber = AllCardLists.find_element_by_xpath('.//li['+str(i)+']/div[1]/div[1]/span').text
                if FindOrderNumber == OrderNumber:
                    logging.info('.....找到预约订单啦！')
                    AllButtons = AllCardLists.find_element_by_xpath('.//li['+str(i)+']/div[3]/div')
                    Buttons = AllButtons.find_elements_by_tag_name('a')
                    for Button in Buttons:
                        if Button.text == '预约上门':
                            Button.click()
                            logging.info('.....点击->【预约上门】')
                            break
                break
            except:
                if i == CardNumber-1:
                    logging.error('!!!!!找不到【预约上门】按钮')
                    exit()
                else:
                    pass
        #输入预约时间
        tm = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        time.sleep(1)
        for i in range(10):
            try:
                WebDriverWait(driver,5).until(lambda x:x.find_element_by_id("ChangeTime")).click()
                time.sleep(1)
                driver.find_element_by_xpath('//div[@class="date_btn lcalendar_finish"]').click()
                logging.info('.....预约时间：%s'%tm)
                break
            except:
                if i == 9:
                    logging.error('!!!!!预约时间失败...')
                    exit()
                else:
                    pass
        #随机选择预约时间段信息
        for i in range(10):
            try:
                AllTimes = driver.find_element_by_xpath('//h3[text()="预约时段上门"]/../../div[2]/ul')
                Times = AllTimes.find_elements_by_tag_name('li')
                SelectTime = random.randint(1,len(Times))
                Time = AllTimes.find_element_by_xpath('.//li['+str(SelectTime)+']/a')
                Time.click()
                logging.info('.....选择预约时间段：%s'%Time.text)
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择预约时间段失败...')
                    exit()
                else:
                    pass
        #点击->【确定】
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//a[@class="button button-big button-yellow-h btnordersave"]').click()
            logging.info('.....点击->【确定】')
        except:
            logging.error('!!!!!点击“确定”失败...')
            exit()
        #获取预约时间后的系统提示信息
        try:
            yy_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....预约订单,系统提示：%s'%yy_msg)
        except:
            pass

    def SF_DaKa(driver,OrderNumber):

        #-------------------------------------------------【师傅上门打卡】------------------------------------------------
        #进入师傅待服务页面上门打卡
        logging.info('<=====>【师傅上门打卡】<=====>')
        driver.implicitly_wait(10)
        #初始化确认上门订单页面
        for i in range(20):
            try:
                driver.get('http://www.51shouhou.cn/appmaster/main.html#!/order/index.html?id=1.5')
                driver.refresh()
                time.sleep(1)
                active = driver.find_element_by_xpath('//*[@id="navtab"]/div/div/a[2]').get_attribute('class')
                if 'active' in active:
                    logging.info('.....正在进入确认上门页面...')
                    break
            except:
                if i == 19:
                    logging.error('!!!!!进入确认上门失败')
                    exit()
                else:
                    pass
        #统计订单数量信息
        time.sleep(1)
        for i in range(10):
            try:
                AllCardLists = driver.find_element_by_xpath('//div[@id="navtab"]/following-sibling::div[1]/div[2]/ul')
                CardLists = AllCardLists.find_elements_by_tag_name('li')
                CardListNumbers = len(CardLists)
                break
            except:
                if i == 9:
                    logging.error('!!!!!统计订单失败')
                    exit()
                else:
                    pass
        #便利所有订单单号找到订单点击确认上门按钮
        for i in range(1,CardListNumbers):
            try:
                FindOrderNumber = AllCardLists.find_element_by_xpath('.//li['+str(i)+']/div[1]/div[1]/span').text
                if FindOrderNumber == OrderNumber:
                    logging.info('.....找到待上门订单啦！')
                    AllButtons = driver.find_element_by_xpath('.//li['+str(i)+']/div[3]/div')
                    Buttons = AllButtons.find_elements_by_tag_name('a')
                    for Button in Buttons:
                        if Button.text == '确认上门':
                            Button.click()
                            logging.info('.....点击->【确认上门】')
                            break
                break
            except:
                if i == CardListNumbers-1:
                    logging.error('!!!!!点击“确认上门”失败')
                    exit()
                else:
                    pass
        #点击->【确认上门】输出打卡时间
        time.sleep(1)
        for i in range(20):
            try:
                driver.find_element_by_xpath('//div[@id="dayNoclockPage"]/div[2]/div[2]/div').click()
                logging.info('.....点击->【确认上门打卡】')
                Punchtime = driver.find_element_by_xpath('//p[@class="punch-time"]').text
                logging.info('.....打卡时间：%s'%Punchtime)
                break
            except:
                if i == 19:
                    logging.error('!!!!!上门打卡失败...')
                    exit()
                else:
                    pass
        #获取打卡系统提示信息
        try:
            DK_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....预约订单,系统提示：%s'%DK_msg)
        except:
            pass

    def SF_Sheet(driver,OrderNumber):

        #---------------------------------------------【师傅处理工单】----------------------------------------------------
        #上传图片路径
        ParentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DataPath = ParentPath + '\\Config\\Picture\\'
        lists = os.listdir(DataPath)

        #进入服务中地址进行填写工单
        logging.info('<=====>【师傅填写工单】<=====>')
        driver.implicitly_wait(20)
        for i in range(10):
            try:
                driver.get('http://www.51shouhou.cn/appmaster/main.html#!/order/index.html?id=2')
                driver.refresh()
                logging.info('.....打开填写工单地址...')
                time.sleep(1)
                active = driver.find_element_by_xpath('//*[@id="navtab"]/div/div/a[3]').get_attribute("class")
                if "active" in active:
                    break
                else:
                    logging.warning("!!!!!打开工单页面失败")
            except:
                if i == 9:
                    logging.error('!!!!!进入工单页面失败...')
                    exit()
                else:
                    pass
        #统计遍历服务中订单
        time.sleep(1)
        for i in range(10):
            try:
                AllCardLists = driver.find_element_by_xpath('//div[@id="navtab"]/following-sibling::div[1]/div[2]/ul')
                CardLists = AllCardLists.find_elements_by_tag_name('li')
                CardListNumbers = len(CardLists)
                break
            except:
                if i == 9:
                    logging.error('!!!!!统计订单失败')
                    exit()
                else:
                    pass
        #便利所有订单单号找到订单点击确认上门按钮
        for i in range(1,CardListNumbers):
            try:
                FindOrderNumber = AllCardLists.find_element_by_xpath('.//li['+str(i)+']/div[1]/div[1]/span').text
                if FindOrderNumber == OrderNumber:
                    logging.info('.....找到处理工单订单啦！')
                    AllButtons = driver.find_element_by_xpath('.//li['+str(i)+']/div[3]/div')
                    Buttons = AllButtons.find_elements_by_tag_name('a')
                    for Button in Buttons:
                        if Button.text == '处理工单':
                            Button.click()
                            logging.info('.....点击->【处理工单】')
                            break
                break
            except:
                if i == CardListNumbers-1:
                    logging.error('!!!!!点击“处理工单”失败')
                    exit()
                else:
                    pass
        #填写工单页面处理工单
        logging.info('.....开始处理工单...')
        #网点订单需要选择产品规格做个判断
        time.sleep(5)
        GGText = driver.find_element_by_xpath('//div[text()="产品规格"]/following-sibling::div').text
        if GGText == '':
            logging.info('.....选择规格')
            for i in range(10):
                try:
                    driver.find_element_by_xpath('//div[text()="产品规格"]').click()
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[@id="dayDealorderPage"]/div[5]/div/ul/li[2]').click()
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!选择规格失败！')
                        exit()
                    else:
                        pass
        #选择服务措施信息
        for i in range(20):
            try:
                AllLists = driver.find_element_by_xpath('//*[@id="tab1"]/div[1]/div[1]/div[2]')
                AllLists.find_element_by_xpath('.//ul/li[6]/div').click()
                logging.info('.....点击->【服务措施】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!进入“服务措施”页面失败')
                    exit()
        #选择服务措施
        for i in range(5):
            try:
                all_cuoshi = driver.find_element_by_xpath('//*[@id="servicechushi"]/div[2]')
                cuoshi = all_cuoshi.find_elements_by_tag_name('h4')
                sel_cuoshi = random.randint(1,len(cuoshi))
                #随机匹配出选择的服务措施信息选择
                select_cuoshi = driver.find_element_by_xpath('//div[@class="lump-card"][' +str(sel_cuoshi)+ ']')
                time.sleep(2)
                servercuoshi = select_cuoshi.text
                logging.info('.....选择服务措施：%s'%servercuoshi)
                select_cuoshi.click()
                break
            except:
                if i == 4:
                    logging.error('!!!!!选择服务措施失败...')
                    exit()
                else:
                    pass
        #str转换字符串类型
        JSTM = 'JSTM' + str(int(time.time()))
        #输入机身条码信息
        try:
            driver.find_element_by_id('SerialNumber').send_keys(JSTM)
            logging.info('.....机身条码：%s' % JSTM)
        except:
            logging.error('!!!!!输入机身条码失败...')
            exit()
        #上传图片一张
        for i in range(len(lists)):
            try:
                data = DataPath + lists[i]
                file = driver.find_element_by_id('fileservicePhoto')
                driver.execute_script("arguments[0].scrollIntoView();",file)
                time.sleep(1)
                file.send_keys(data)
                logging.info('.....正在上传图片：%s...'%data)
            except:
                logging.error('!!!!!上传图片失败...')
                exit()
        #填写服务描述信息
        ServerInfo = '服务描述：' + time.strftime('%Y-%m-%d', time.localtime(time.time()))
        driver.find_element_by_xpath('.//textarea').send_keys(ServerInfo)
        logging.info('.....服务描述：%s' % ServerInfo)
        #点击->【保存工单】
        for i in range(10):
            try:
                WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="tab1"]/div[2]/a')).click()
                logging.info('.....点击->【保存工单】')
                break
            except:
                if i == 9:
                    logging.error('!!!!!点击保存工单失败"...')
                    exit()
                else:
                    pass
        #获取系统提示信息
        try:
            msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....系统提示：%s'%msg)
        except:
            pass

    def SF_UseBJ(driver,BJname=None,Use_BJNumber=1):

        #------------------------------------------【师傅完成服务使用备件】------------------------------------------------
        #订单使用备件
        logging.info('<=====>【师傅完成服务使用备件】<=====>')
        time.sleep(5) #不使用备件时，保存工单后，提示信息展示慢，加固定时间等待
        try:
            title = driver.find_element_by_xpath('//a[@href="#tab2"]').get_attribute('class')
            if 'active' in title:
                logging.info('.....开始使用备件...')
            else:
                driver.find_element_by_xpath('//a[@href="#tab2"]').click()
                logging.info('.....点击->【使用备件】')
        except:
            pass
        #默认不使用备件
        if BJname == None:
            logging.info('.....不使用备件')
            pass
        else:
            #统计备件，搜索要使用的备件
            time.sleep(1)
            for i in range(10):
                try:
                    All_BJList =  driver.find_element_by_xpath('//*[@id="tab2"]/div[1]/div[2]/div/ul')
                    BJ_List = All_BJList.find_elements_by_tag_name('li')
                    BJ_Numbers = len(BJ_List)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!统计备件种类数量失败')
                        exit()
            #备件种类为0，不适用备件
            if BJ_Numbers > 0:
                #遍历备件信息选择备件
                for i in range(1,BJ_Numbers+1):
                    try:
                        BJ_Name = All_BJList.find_element_by_xpath('.//li['+str(i)+']/div[1]').text
                        BJ_Message = All_BJList.find_element_by_xpath('.//li['+str(i)+']/span').text
                        #备件信息中 库存： 100 用split函数分割输出备件数量信息
                        BJ_Count = BJ_Message.split('：')[1]
                        if BJ_Name == BJname and BJ_Count != 0:
                            logging.info('.....找到要使用的备件了！备件：%s'%BJ_Name)
                            for j in range(Use_BJNumber):
                                try:
                                    time.sleep(2)
                                    All_BJList.find_element_by_xpath('.//li['+str(i)+']/div[3]/span[2]/i').click()
                                    logging.info('.....使用备件：%s个'%Use_BJNumber)
                                except:
                                    logging.error('!!!!!使用备件数量失败')
                                    exit()
                            break
                        elif BJ_Name == BJname and BJ_Count == 0:
                            logging.info('.....使用备件：%s,数量为：0,请申请备件！')
                            break
                    except:
                        logging.error('!!!!!使用备件失败！')
                        exit()
            elif BJ_Numbers == 0:
                logging.info('.....没有可以使用的备件！请手动申请！')
        #点击->【立即结算】
        for i in range(20):
            try:
                driver.find_element_by_xpath('//a[contains(text(),"下一步，提交服务报价")]').click()
                logging.info('.....点击->【下一步，提交服务报价】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!提交报价失败')
                    exit()

    def SF_SubmitPay(driver,OtherPrice=1):

        #---------------------------------------------【师傅提交服务报价】------------------------------------------------
        #判断是否到提交服务报价页面
        logging.info('<=====>【师傅提交服务报价】<=====>')
        try:
            title = driver.find_element_by_id('serverPlace').get_attribute('class')
            if 'active' in title:
                logging.info('.....开始提交服务报价...')
            else:
                driver.find_element_by_id('serverPlace').click()
                logging.info('.....点击->【提交服务报价】')
        except:
            pass
        #输入用户付费价格，因为结算价格为0
        for i in range(5):
            try:
                driver.find_element_by_xpath('//input[@class="txtOtherDealPrice otherExpenses"]').clear()
                driver.find_element_by_xpath('//input[@class="txtOtherDealPrice otherExpenses"]').send_keys(OtherPrice)
                logging.info('.....用户付费：%s元'%OtherPrice)
                break
            except:
                if i == 4:
                    logging.error('!!!!!用户付费失败...')
                    exit()
                else:
                    pass
        #填写备注信息
        tm = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        driver.find_element_by_xpath('//textarea[@class="textarea txtdealremark label-load"]').send_keys(tm)
        logging.info('.....备注：%s'%tm)
        #点击->【提交服务报价】
        time.sleep(1)
        for i in range(20):
            try:
                driver.find_element_by_xpath('//a[text()="提交服务报价"]').click()
                logging.info('.....点击->【提交服务报价】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!提交服务报价失败！')
                    exit()
        #获取系统提示信息
        try:
            msg = WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....系统提示：%s'%msg)
        except:
            pass


    def SF_ShouKuan(driver,OrderNumber):

        #------------------------------------------【师傅现金收款】------------------------------------------------
        #进入待收款页面
        logging.info('<=====>【师傅现金收款】<=====>')
        for i in range(10):
            try:
                driver.get('http://www.51shouhou.cn/appmaster/main.html#!/order/index.html?id=4')
                driver.refresh()
                logging.info('.....打开待收款地址...')
                time.sleep(1)
                active = driver.find_element_by_xpath('//*[@id="navtab"]/div/div/a[5]').get_attribute("class")
                if "active" in active:
                    break
                else:
                    logging.warning("!!!!!打开待收款页面失败")
            except:
                if i == 9:
                    logging.error('!!!!!进入待收款页面失败...')
                    exit()
                else:
                    pass
        #统计代收款订单数量
        time.sleep(1)
        for i in range(10):
            try:
                AllCardLists = driver.find_element_by_xpath('//*[@id="navtab"]/following-sibling::div[1]/div[2]/ul')
                CardList = AllCardLists.find_elements_by_tag_name('li')
                CardNumbers = len(CardList)
                break
            except:
                if i == 9:
                    logging.error('!!!!!代收款订单统计失败')
                    exit()
                else:
                    pass
        #遍历订单单号匹配订单点击立即收款
        for i in range(1,CardNumbers):
            try:
                FindOrderNumber = AllCardLists.find_element_by_xpath('.//li['+str(i)+']/div[1]/div[1]/span[1]').text
                if FindOrderNumber == OrderNumber:
                    logging.info('.....找到代收款订单啦！')
                    AllButtons = driver.find_element_by_xpath('.//li['+str(i)+']/div[3]/div')
                    Buttons = AllButtons.find_elements_by_tag_name('a')
                    for Button in Buttons:
                        if Button.text == '立即收款':
                            Button.click()
                            logging.info('.....点击->【立即收款】')
                            break
                break
            except:
                if i == CardNumbers-1:
                    logging.error('!!!!!找不到待收款订单！')
                    exit()
                else:
                    pass
        #选择现金收款，点击确认收款
        time.sleep(1)
        for i in range(10):
            try:
                AllPayModel = driver.find_element_by_xpath('//div[@class="list-block media-list paymain-list"]/ul')
                PayModels = AllPayModel.find_elements_by_tag_name('li')
                for PayModel in PayModels:
                    Attribute = PayModel.get_attribute('val')
                    if Attribute == '现金支付':
                        PayModel.click()
                        logging.info('.....选择现金支付')
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择现金支付失败...')
                    exit()
                else:
                    pass
        #点击->【确认收款】
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//a[text()="确认收款"]')).click()
        logging.info('.....点击->【确认收款】')
        #获取系统提示信息
        try:
            msg = WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath('//div[@class="modal-text"]')).text
            logging.info('.....系统提示：%s' % msg)
        except:
            pass

    def SF_CheckOrderStatus(driver,CheckOrderNumber,CheckOrderStatus):

        #----------------------------------------------【师傅订单状态校验】----------------------------------------------
        #初始化URL
        logging.info('<=====>【师傅端订单状态校验】<=====>')
        #订单查询地址拼接
        if CheckOrderStatus == '等待师傅预约':
            IDNumber = '1'
        elif CheckOrderStatus == '等待师傅服务':
            IDNumber = '1.5'
        elif CheckOrderStatus == '师傅服务中':
            IDNumber = '2'
        elif CheckOrderStatus == '待件中':
            IDNumber = '3'
        elif CheckOrderStatus == '等待收款':
            IDNumber = '4'
        elif CheckOrderStatus == '等待结算':
            IDNumber = '5'
        #打开地址查询订单状态
        for i in range(20):
            try:
                driver.get('http://www.51shouhou.cn/appmaster/main.html#!/order/index.html?id='+IDNumber+'')
                driver.refresh()
                time.sleep(1)
                titleText = driver.find_element_by_xpath('//div[@class="center"]').text
                if titleText == '工单列表':
                    logging.info('.....正在进入订单状态验证页面...')
                    break
            except:
                if i == 19:
                    logging.error('!!!!!进入师傅状态验证页面失败！')
                    exit()
                else:
                    pass
        #统计订单数量
        for i in range(10):
            time.sleep(2)
            try:
                AllListCard = driver.find_element_by_xpath('//*[@id="navtab"]/following-sibling::div[1]/div[2]/ul')
                Orders = AllListCard.find_elements_by_tag_name('label')
                OrderNumbers = len(Orders)
                break
            except:
                if i == 9:
                    logging.error('!!!!!统计订单失败')
                    exit()
                else:
                    pass
        #查找订单单号校验订单状态
        for i in range(1,OrderNumbers):
            try:
                FindOrderNumber = driver.find_element_by_xpath('//div[@class="list-block worklist"]/ul/li['+str(i)+']/div[1]/div[1]/span[1]').text
                if FindOrderNumber == CheckOrderNumber:
                    logging.info('.....找到订单了！订单单号：%s'%FindOrderNumber)
                    FindOrderStatus = driver.find_element_by_xpath('//div[@class="list-block worklist"]/ul/li['+str(i)+']/div[1]/div[2]').text
                    if FindOrderStatus == CheckOrderStatus:
                        logging.info('.....订单状态验证成功！校验订单状态：%s'%FindOrderStatus)
                    else:
                        logging.error('!!!!!订单状态校验失败！校验订单状态：%s,当前订单状态：%s'%(CheckOrderStatus,FindOrderStatus))
                    break
            except:
                if i == OrderNumbers-1:
                    logging.error('!!!!!找不到校验状态的订单')
                    exit()
                else:
                    pass

# if __name__ == '__main__':
#
#
#      from Common import Driver
#      d = Driver.WAP_Brower()
#      Master.SF_login(d,'SF_Login','sf_username1','sf_password1',MasterHandle='new')
#      Master.SF_Sheet(d,OrderNumber='AZ19031100000214')
