# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

from Common import GetCode
from Common import Pubilc
import time,configparser,random,logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class HDServer(object):

    def __init__(self):
        pass

    def User_login(driver,HT_driver,HDHandle='table',url='http://rc.51shouhou.cn/wapuser/#/my'):

        #获取配置文件信息
        DataPath = Pubilc.data_dir(filename='Login.ini')
        cf = configparser.ConfigParser()
        cf.read(DataPath,encoding='utf-8')
        user = cf.get('HD_Server','hd_username')

        #--------------------------------------------------【用户登录】---------------------------------------------------
        #打开好滴服务登录地址
        logging.info('<=====>【WAP用户登录】<=====>')
        driver.implicitly_wait(20)
        #默认直接打开进入
        if HDHandle == 'new':
            driver.get(url)
        elif HDHandle == 'table':#切换窗口
            Pubilc.table_handle(driver=driver,url=url)
        HaodiHandle = driver.current_window_handle
        logging.info('.....正在进入好滴服务登录地址')

        #点击进入登录页面
        isOk=False
        for i in range(20):
            try:
                driver.find_element_by_xpath('//a[@class="user-login-btn"]').click()
                logging.info('.....点击->【立即登录】')
                isOk=True
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击立即登录失败"...')
                    exit()
                else:
                    pass
        #输入用户名点击获取验证码
        if isOk:
            for i in range(10):
                try:
                    driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号码"]').clear()
                    driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入手机号码"]').send_keys(user)
                    logging.info('.....输入用户名：%s'%user)
                    driver.find_element_by_xpath('//a[text()="获取验证码"]').click()
                    logging.info('.....点击->【获取验证码】')
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!填写用户名失败...')
                        exit()
                    else:
                        pass
        else:
            logging.error('!!!!!没有探测到登录页面')
            exit()
        #调用后台获取验证码信息
        code = GetCode.FindCheckNum(HT_driver,Phonenum=user)
        #输入验证码
        try:
            driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入验证码"]').clear()
            driver.find_element_by_xpath('//input[@type="text"and@placeholder="输入验证码"]').send_keys(code)
            logging.info('.....输入验证码：%s'%code)
        except:
            logging.error('!!!!!输入验证码失败...')
            exit()
        #点击登录
        WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//a[text()="登录"]/..')).click()
        logging.info('.....点击->【登录】')
        #有时候登录后一直转圈加个判断等待
        Button = WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('//*[@class="user-login-btn"]')).is_displayed()
        if Button:
            #判断登录
            for i in range(5):
                time.sleep(2)
                try:
                    attribute = driver.find_element_by_xpath('//*[@class="user-login-btn"]').get_attribute('style')
                    if attribute == 'display: none;':
                        logging.info('.....登录成功！')
                    else:
                        logging.error('!!!!!登录失败...')
                    break
                except:
                    pass
        else:
            logging.error('!!!!!登录转圈进不去！')
            exit()

        return HaodiHandle

    def User_AddOrder(driver,WDName,PPName,serverType,product,XHInfo,JSTM,buyTime,NewAddress,NewUser,NewPhe,use,phe,BeiZhu,OrderType='品牌商'):
        '''
        :param driver: 驱动
        :param WDName: 购买服务的网点名称
        :param PPName: 订单品牌商名称
        :param serverType: 服务类型
        :param prodect: 产品信息
        :param XHInfo: 产品型号
        :param JSTM: 机身条码
        :param buyTime: 购买时间
        :param NewAddress: 新增加的地址信息
        :param NewUser: 新增加的用户信息
        :param NewPhe: 新增加的手机号
        :param use: 用户名
        :param phe: 联系方式
        :param BeiZhu: 订单备注
        :param OrderType: 订单类型，网点订单 or 品牌商订单
        '''
        #---------------------------------------------------【用户WAP添加订单】--------------------------------------------
        #进入用户收藏的网点列表
        logging.info('<=====>【WAP用户添加订单】<=====>')
        driver.get('http://rc.51shouhou.cn/wapuser/#/my/collect')
        #遍历所有收藏网点信息，制定下单网点点击进入网点主页
        for i in range(10):
            time.sleep(2)
            try:
                #统计网点个数便于遍历次数
                all_wd = driver.find_element_by_xpath('//div[@class="container-pro-list"]/div/ul')
                wds = all_wd.find_elements_by_tag_name('h3')
                for wdname in wds:
                    name = wdname.text
                    if name == WDName:
                        wdname.click()
                        logging.info('.....点击->【网点名称】')
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!查找网点进入网点主页失败...')
                    exit()
                else:
                    pass
        #点击立即下单按钮
        for i in range(20):
            try:
                driver.find_element_by_xpath('//a[@class="btn btn-info btn-big btn-round"]').click()
                logging.info('.....点击->【立即下单】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击"立即下单"失败...')
                    exit()
                else:
                    pass
        #开始下单默认下网点单，如果类型为品牌商就下品牌商【测试公司01】单子
        if OrderType == '品牌商':
            logging.info('//**********【品牌商订单信息】**********//')
            #选择网点合作品牌商信息
            for i in range(30):
                try:
                    driver.refresh()#有时候会定位不上元素
                    time.sleep(2)
                    brands = Select(driver.find_element_by_xpath('//span[text()="授权品牌"]/following-sibling::div/select'))
                    brands.select_by_visible_text(PPName)
                    logging.info('.....选择品牌商：%s'%PPName)
                    break
                except:
                    if i ==29:
                        logging.error('!!!!!选择品牌商失败')
                        exit()
                    else:
                        pass
        elif OrderType != '品牌商':
            logging.info('//**********【网点订单信息】**********//')
        #选择预约服务类型默认选择安装
        AZ,WX = serverType.split(",")
        sel_server = random.randint(1,2)
        for i in range(20):
            try:
                if sel_server == 2:
                    driver.find_element_by_xpath('//a[contains(text(),"'+AZ+'")]').click()
                    logging.info('.....点击->【%s】'%AZ)
                elif sel_server == 1:
                    driver.find_element_by_xpath('//a[contains(text(),"'+WX+'")]').click()
                    logging.info('.....点击->【%s】'%WX)
                break
            except:
                if i == 19:
                    logging.error('!!!!!选择服务失败')
                    exit()
                else:
                    pass
        #点击选择产品信息进入产品信息选择页面
        isClick = False
        for i in range(20):
            try:
                WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath('//p[text()="请选择产品信息"]')).click()
                logging.info('.....点击->【请选择产品信息】')
                isClick = True
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击“选择产品信息失败”')
                    exit()
                else:
                    pass
        #获取所有的产品信息
        LeiBie,PinXian,PinLei = product.split("-")
        #判断是否进入页面
        if isClick:
            #如果是网点订单要选择品牌
            if OrderType != '品牌商':
                time.sleep(1)
                brand = PPName.split('---')[0]
                #统计所有的品牌
                for i in range(10):
                    try:
                        All_PP = driver.find_element_by_xpath('//h3[text()="品牌"]/following-sibling::div')
                        PPs = All_PP.find_elements_by_tag_name("a")
                        for pp in PPs:
                            if pp.text == brand:
                                pp.click()
                                logging.info('.....选择品牌名称：%s'%brand)
                                break
                        break
                    except:
                        if i == 9:
                            logging.error('!!!!!选择品牌失败！')
                            exit()
            #选择产品类别
            time.sleep(1)
            for i in range(10):
                try:
                    #获取所有类别
                    all_LB = driver.find_element_by_xpath('//h3[text()="产品类别"]/following-sibling::div')
                    LBs = all_LB.find_elements_by_tag_name("a")
                    for a in LBs:
                        if a.text == LeiBie:
                            a.click()
                            logging.info('.....产品类别：%s'%LeiBie)
                            break
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!选择产品类别失败')
                        exit()
                    else:
                        pass
            #选择产品线信息
            time.sleep(2)
            for i in range(20):
                try:
                    #获取所有产品线信息
                    all_LB = driver.find_element_by_xpath('//h3[text()="产品线"]/following-sibling::div')
                    LBs = all_LB.find_elements_by_tag_name("a")
                    for a in LBs:
                        if a.text == PinXian:
                            a.click()
                            logging.info('.....产品线：%s'%PinXian)
                            break
                    break
                except:
                    if i == 19:
                        logging.error('!!!!!选择产品线失败')
                        exit()
                    else:
                        pass
            #选择产品品类
            time.sleep(2)
            for i in range(20):
                try:
                    #获取所有品类
                    all_LB = driver.find_element_by_xpath('//h3[text()="品类"]/following-sibling::div')
                    LBs = all_LB.find_elements_by_tag_name("a")
                    for a in LBs:
                        if a.text == PinLei:
                            a.click()
                            logging.info('.....产品品类：%s'%PinLei)
                            break
                    break
                except:
                    if i == 19:
                        logging.error('!!!!!选择产品品类失败')
                        exit()
                    else:
                        pass
            #随机选择产品规格信息
            time.sleep(2)
            all_GG = driver.find_element_by_xpath('//h3[text()="规格"]/following-sibling::div')
            GG = all_GG.find_elements_by_tag_name("a")
            #随机数字选择规格信息
            select_num = random.randint(1,len(GG))
            try:
                select_GG = all_GG.find_element_by_xpath('//h3[text()="规格"]/following-sibling::div/a['+str(select_num)+']')
                select_GG.click()
                logging.info('.....产品规格：%s'%select_GG.text)
            except:
                logging.error('!!!!!选择产品规格失败')
                exit()
            #点击确定提交产品信息
            button = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('.//div[6]/a'))
            driver.execute_script("arguments[0].scrollIntoView();",button)
            button.click()
            logging.info('.....点击->【确定】')
        else:
            logging.error('!!!!!进入选择产品信息失败')
            exit()
        #按照随机选择的数字选择产品型号信息
        for i in range(20):
            try:
                #输入产品型号信息
                driver.find_element_by_xpath('//input[@placeholder="请输入或选择产品型号"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入或选择产品型号"]').send_keys(XHInfo)
                logging.info('.....产品型号：%s'%XHInfo)
                break
            except:
                if i == 19:
                    logging.error('!!!!!选择产品型号失败')
                    exit()
                else:
                    pass
        #获取机身条码信息
        tm = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        jstm = JSTM.split("+")[0] + tm
        #输入机身条码信息
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请输入机身条码"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入机身条码"]').send_keys(jstm)
                logging.info('.....机身条码：%s'%jstm)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入机身条码失败')
                    exit()
                else:
                    pass
        #选择故障类型信息 维修订单要选择故障类型
        if sel_server == 1:
            time.sleep(2)
            for i in range(20):
                try:
                    #统计故障类型随机选择
                    all_type = driver.find_element_by_xpath("//span[text()='故障类型']/following-sibling::div/select")
                    types = all_type.find_elements_by_tag_name('option')
                    select_type_num = random.randint(1,len(types)+1)
                    GZ_Type = driver.find_element_by_xpath("//span[text()='故障类型']/following-sibling::div/select/option["+str(select_type_num)+"]").text
                    select_GZ_Type = Select(driver.find_element_by_xpath("//span[text()='故障类型']/following-sibling::div/select"))
                    select_GZ_Type.select_by_index(select_type_num-1)
                    logging.info('.....故障类型：%s'%GZ_Type)
                    break
                except:
                    if i == 19:
                        logging.error('!!!!!获取故障类型失败')
                        exit()
                    else:
                        pass
        #选择购买时间固定时间
        year,month,day = buyTime.split("-")
        driver.find_element_by_xpath('//span[text()="请选择购买时间"]').click()
        logging.info('.....点击->【请选择购买时间】')
        #选择匹配年、月、日时间信息三级联动
        for i in range(1,4):
            try:
                time.sleep(2)
                All_Years = driver.find_element_by_xpath('//div[6]/div/div[2]/div['+str(i)+']/ul')
                years = All_Years.find_elements_by_tag_name('li')
                for li in years:
                    li.click()
                    if li.text == year or li.text == month:
                        break
                    if li.text == day and i == 3:
                        break
            except:
                if i == 9:
                    logging.error('!!!!!选择购买时间失败')
                    exit()

        #点击确定购买日期
        try:
            driver.find_element_by_xpath('//div[6]/div/div[1]/div[2]').click()
            logging.info('.....点击->【完成】')
            logging.info('.....购买日期：%s'%buyTime)
        except:
            logging.error('!!!!!点击确定失败')
            exit()
        #选择服务地址信息
        for i in range(20):
            try:
                driver.find_element_by_xpath('//span[text()="服务地址"]/following-sibling::div/a/p[1]').click()
                logging.info('.....点击->【选择地址信息】')
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击“选择地址失败”')
                    exit()
                else:
                    pass
        #判断地址信息是否为空，为空新添加地址信息
        time.sleep(2)
        try:
            all_address = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[5]/div/div')
            address = all_address.find_elements_by_tag_name('input')
            if len(address) > 0:#如果大于2说明有地址信息可选
                if len(address) > 1:
                    selectAddressNum = random.randint(2,len(address)+1)
                    addressInfo = driver.find_element_by_xpath('//div[@class="address-list"]['+str(selectAddressNum)+']/div[1]/div[1]')
                elif len(address) == 1:
                    addressInfo = driver.find_element_by_xpath('//div[@class="address-list"][2]/div[1]/div[1]')
                addressMsg = addressInfo.text
                addressInfo.click()
                logging.info('.....服务地址：%s'%addressMsg)
            elif len(address) == 0:#服务地址信息为空情况下重新添加地址
                logging.info('.....重新添加地址信息：')
                driver.find_element_by_xpath('//a[@href="#/my/addAddress"]').click()
                logging.info('.....点击->【新增地址】')
                #进入新地址的选择地址页面
                time.sleep(2)
                try:
                    driver.find_element_by_xpath('//span[text()="地址"]/following-sibling::div/a/p[1]').click()
                    WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="address-position"]/following-sibling::div[2]/div[2]/a')).click()
                    logging.info('.....点击->【选择地址信息】')
                except:
                    logging.error('!!!!!进入选择新地址失败')
                    exit()
                #选择匹配信息地址信息
                pro,city,area = NewAddress.split("-")
                time.sleep(2)
                FindCity = driver.find_element_by_xpath('//*[@class="opt-address"]/span')
                #如果本来就是西安市就不用再次选择，不是的话再次选择省市信息
                if FindCity.text == city:
                    pass
                else:
                    FindCity.click()
                    #循环选择省市信息
                    for j in range(1,3):
                        time.sleep(2)
                        try:
                            all_pro = driver.find_element_by_xpath('//*[@class="van-picker van-area"]/div[2]/div['+str(j)+']/ul')
                            proes = all_pro.find_elements_by_tag_name('li')
                            for li in proes:
                                time.sleep(0.5)
                                li.click()
                                if li.text == pro or li.text == city:
                                    break
                        except:
                            logging.error('!!!!!选择省市失败')
                            exit()
                    #点击完成选择
                    WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@class="van-picker__confirm"]')).click()
                    logging.info('.....点击->【完成】')
                #随机选择一个匹配的地址信息
                for k in range(10):
                    try:
                        all_area = driver.find_element_by_xpath('//div[@class="search-address-list"]/ul')
                        areas = all_area.find_elements_by_tag_name('li')
                        selectArea = random.randint(1,len(areas))
                        driver.find_element_by_xpath('//div[@class="search-address-list"]/ul/li['+str(selectArea)+']').click()
                        break
                    except:
                        if k == 9:
                            logging.error('!!!!!选择区地址失败')
                            exit()
                        else:
                            pass
                #输入门牌号等详细信息
                for a in range(10):
                    try:
                        driver.find_element_by_xpath('//input[@placeholder="请输入具体楼号、门牌号码"]').send_keys(area)
                        driver.find_element_by_xpath('//*[@class="locat-deter"]/a').click()
                        logging.info('.....点击->【确定】')
                        break
                    except:
                        logging.error('!!!!!输入详细信息失败')
                        exit()
                #保存新增地址信息
                for b in range(10):
                    try:
                        driver.find_element_by_xpath('//input[@placeholder="请输入联系人姓名"]').send_keys(NewUser)
                        logging.info('.....联系人：%s'%NewUser)
                        driver.find_element_by_xpath('//input[@placeholder="手机号码"]').send_keys(NewPhe)
                        logging.info('.....手机号：%s'%NewPhe)
                        logging.info('.....地址：%s'%NewAddress)
                        driver.find_element_by_xpath('//a[@class="btn btn-big btn-info"]').click()
                        logging.info('.....点击->【确定】')
                        break
                    except:
                        if b == 9:
                            logging.error('!!!!!保存新增地址失败')
                            exit()
                        else:
                            pass
        except:
            logging.error('!!!!!选择服务地址失败')
            exit()
        #输入联系人和电话信息
        user = use.split('+')[0] + tm
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请输入联系人姓名"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入联系人姓名"]').send_keys(user)
                logging.info('.....联系人：%s'%use)
                driver.find_element_by_xpath('//span[text()="联系电话"]/following-sibling::div/input').clear()
                driver.find_element_by_xpath('//span[text()="联系电话"]/following-sibling::div/input').send_keys(phe)
                logging.info('.....电话：%s'%phe)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入联系人电话失败')
                    exit()
                else:
                    pass
        #选择服务时间
        for i in range(10):
            try:
                driver.find_element_by_xpath('//span[text()="请选择服务时间"]').click()
                logging.info('.....点击->【服务时间】')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@class="item-after"]').click()
                logging.info('.....点击->【预约时间】')
                break
            except:
                if i == 9:
                    logging.error('!!!!!点击“预约时间”失败')
                    exit()
                else:
                    pass
        #填写服务时间相关信息，选择当前时间
        for i in range(10):
            try:
                WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath('//div[@class="van-picker__confirm"]')).click()
                logging.info('.....点击->【完成】')
                YY_Time = driver.find_element_by_xpath('//*[@class="item-after"]').text
                logging.info('.....预约时间：%s'%YY_Time)
                #随机选择预约时间段信息
                selectTime = random.randint(1,3)
                timeDay = driver.find_element_by_xpath('//*[@class="slot-list"]/ul/li['+str(selectTime)+']')
                timeDay.click()
                logging.info('.....时间段：%s'%timeDay.text)
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择时间失败')
                    exit()
                else:
                    pass
        #确定信息
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//a[@class="btn btn-big btn-info"]')).click()
        logging.info('.....点击->【完成】')
        #输入备注
        orderBei = BeiZhu.split('+')[0] + tm
        try:
            driver.find_element_by_xpath('//textarea').send_keys(orderBei)
            logging.info('.....备注：%s'%orderBei)
        except:
            logging.error('!!!!!输入备注失败')
            exit()
        #提交订单信息
        WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//a[text()="立即下单"]')).click()
        logging.info('.....点击->【立即下单】')
        #获取提交订单的系统提示信息
        for i in range(10):
            try:
                AddOrderMsg = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_xpath('//*[@class="van-toast-wrapper"]/div/div')).text
                logging.info('.....系统提示：%s'%AddOrderMsg)
                break
            except:
                if i == 9:
                    logging.error('!!!!!获取系统提示失败')
                    exit()
                else:
                    pass

    def User_CheckOrderStatus(driver,CheckOrderNumber,CheckOrderStatus):

        #-------------------------------------------【用户端订单状态校验】------------------------------------------------
        #进入用户端订单查询页面
        logging.info('<=====>【用户端订单状态校验】<=====>')
        driver.get('http://rc.51shouhou.cn/wapuser/#/my/order?type=%E5%85%A8%E9%83%A8')
        driver.refresh()
        #统计所有订单列表里面订单的数量
        time.sleep(2)
        for i in range(10):
            try:
                All_OrderList = driver.find_element_by_xpath('//div[@class="van-pull-refresh__track"]/div[2]')
                Orders = All_OrderList.find_elements_by_tag_name('h2')
                OrdersNumber = len(Orders)
                break
            except:
                if i == 9:
                    logging.error('!!!!!订单统计失败')
                    exit()
                else:
                    pass
        #查找订单验证订单状态
        for i in range(1,OrdersNumber):
            try:
                FindOrderNumber = driver.find_element_by_xpath('//div[@class="card-ordernumber"]['+str(i)+']').text
                if CheckOrderNumber in FindOrderNumber:
                    #找到订单单号验证订单状态
                    logging.info('.....找到要验证订单了！单号：%s'%CheckOrderNumber)
                    FindOrderStatus = driver.find_element_by_xpath('//div[@class="card-order-state"]['+str(i)+']').text
                    if FindOrderStatus == CheckOrderStatus:
                        logging.info('.....订单状态验证成功！订单状态为：%s'%CheckOrderStatus)
                    else:
                        logging.error('!!!!!订单状态验证失败！当前订单状态为：%s,验证订单状态为：%s'%(FindOrderStatus,CheckOrderStatus))
                    break
            except:
                if i == OrdersNumber-1:
                    logging.error('!!!!!找不到验证订单单号')
                    exit()
                else:
                    pass














#
#
# if __name__ == '__main__':
#
#     from Common import Driver
#     driver = Driver.PC_Brower()
#     dr = Driver.WAP_Brower()
#
#     HDServer.User_login(dr,HT_driver=driver)

