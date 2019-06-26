# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/2/24 16:41

from Common import GetCode
from Common import Pubilc
import time,configparser,random,logging,os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class PPMenHu():

    def MenHu_login(driver,PCdriver,MHHandle="table",url="http://www.51shouhou.cn/brands3/haodi3/index.php/Home/Reserve/index?mercode=ebed6635-99e9-4d74-935b-1fbd6e486ef6"):

        #---------------------------------------------【WAP端门户登陆】---------------------------------------------------
        #获取门户登陆配置文件
        DataPath = Pubilc.data_dir(filename="Login.ini")
        cf = configparser.ConfigParser()
        cf.read(DataPath,encoding="utf-8")
        use = cf.get("MH_Login","mh_username")

        #打开登陆页面
        logging.info('<=====>【门户登录】<=====>')
        if MHHandle == "table":
            Pubilc.table_handle(driver=driver,url=url)
        elif MHHandle == "new":
            driver.get(url)
        MHhandle = driver.current_window_handle

        driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Home/My/center')
        #点击进入登录页面
        isOk = False
        for i in range(20):
            try:
                driver.find_element_by_xpath("//p[contains(text(),'请登录')]").click()
                logging.info('.....点击->【请登录】')
                isOk = True
                break
            except:
                if i == 19:
                    logging.error('!!!!!点击“登录失败”')
                    exit()
                else:
                    pass
        #输入用户名点击发送验证码
        if isOk:
            for i in range(10):
                try:
                    driver.find_element_by_xpath('//input[@type="text"and@ng-model="username"]').clear()
                    driver.find_element_by_xpath('//input[@type="text"and@ng-model="username"]').send_keys(use)
                    logging.info('.....输入用户名：%s'%use)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!输入用户名失败')
                        exit()
                    else:
                        pass
            #点击发送验证码
            for i in range(10):
                try:
                    driver.find_element_by_id('va').click()
                    logging.info('.....点击->【发送验证码】')
                    Msg = driver.find_element_by_xpath('//*[@class="layui-m-layercont"]').text
                    logging.info('.....系统提示：%s'%Msg)
                    break
                except:
                    pass
            #获取验证码
            code = GetCode.FindCheckNum(driver=PCdriver,Phonenum=use)
            #输入验证码点击登陆
            for i in range(10):
                try:
                    driver.find_element_by_id("vainput").clear()
                    driver.find_element_by_id("vainput").send_keys(code)
                    logging.info('.....输入验证码：%s'%code)
                    break
                except:
                    if i == 9:
                        logging.info('.....输入验证码失败')
                        exit()
                    else:
                        pass
            #点击登陆
            driver.find_element_by_id("en").click()
            logging.info('.....点击->【登录】')
            #有时候登录一直转圈进不去加时间等待
            Button = WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('//*[@class="sign-out"]/a')).is_displayed()
            if Button:
                pass
            else:
                logging.error('!!!!!登录超时！')
                exec()
            #验证登陆是否成功
            try:
                msg = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@class="sign-out"]/a')).text
                if msg == "退出":
                    logging.info('.....门户登陆成功！')
                else:
                    logging.error('!!!!!门户登陆失败')
            except:
                pass
        return MHhandle

    def MenHu_AddOrder(driver,url,serverType,product,JSTM,buyPlace,txtRemark,serverAddress,addInfo,use,phe):
        '''
        :param url:             门户下单地址
        :param serverType:      服务类型
        :param product:         产品信息
        :param JSTM:            机身条码
        :param buyPlace:        购买渠道
        :param txtRemark:       订单备注
        :param serverAddress:   服务区域信息
        :param addInfo:         地址详细信息
        :param use:             用户姓名
        :param phe:             用户手机号
        '''
        #---------------------------------------------【WAP门户添加订单】-------------------------------------------------
        #进入下单页面
        logging.info('<=====>【WAP门户下单】<=====>')
        driver.get(url)
        logging.info('.....正在进入下单页面')

        driver.implicitly_wait(20)
        #选择服务类型
        for i in range(10):
            try:
                all_server = driver.find_element_by_xpath('//*[@class="index-list"]/ul')
                servers = all_server.find_elements_by_tag_name('li')
                for li in servers:
                    if serverType in li.text:
                        li.click()
                        logging.info('.....服务类型：%s'%serverType)
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择服务类型失败')
                    exit()
                else:
                    pass
        #获取产品信息配置文件
        PinPai,PinXian,PinLei = product.split("-")
        #选择产品品牌-品线-品类
        for i in range(20):
            try:
                select_PP = Select(driver.find_element_by_xpath('//*[@id="faulttype"]/preceding-sibling::li[7]/div[2]/select'))
                select_PP.select_by_visible_text(PinPai)
                logging.info('.....产品品牌：%s'%PinPai)
                select_PX = Select(driver.find_element_by_xpath('//*[@id="faulttype"]/preceding-sibling::li[6]/div[2]/select'))
                select_PX.select_by_visible_text(PinXian)
                logging.info('.....产品品线：%s'%PinXian)
                select_PL = Select(driver.find_element_by_xpath('//*[@id="faulttype"]/preceding-sibling::li[5]/div[2]/select'))
                select_PL.select_by_visible_text(PinLei)
                logging.info('.....产品品类：%s'%PinLei)
                break
            except:
                if i == 19:
                    logging.error('!!!!!选择产品信息失败')
                    exit()
                else:
                    pass
        #选择产品型号信息
        time.sleep(1)
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@class="icon-xuanqu"]').click()
                logging.info('.....点击->【选择型号】')
                break
            except:
                if i == 9:
                    logging.info('.....点击“选择型号失败”')
                    exit()
                else:
                    pass
        #随机选择产品型号信息
        for i in range(10):
            try:
                #获取所有型号数
                all_xh = driver.find_element_by_xpath('//p[text()="已有型号"]/following-sibling::div')
                xh = all_xh.find_elements_by_tag_name("a")
                select_XH = random.randint(1,len(xh))
                XH_Info = driver.find_element_by_xpath('//p[text()="已有型号"]/following-sibling::div/a['+str(select_XH)+']')
                XH = XH_Info.text
                XH_Info.click()
                logging.info('.....产品型号：%s'%XH)
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择产品型号失败')
                    exit()
                else:
                    pass
        #输入机身条码信息
        tm = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        jstm_Info = JSTM.split("+")[0] + tm
        try:
            driver.find_element_by_id("SerialNumber").clear()
            driver.find_element_by_id("SerialNumber").send_keys(jstm_Info)
            logging.info('.....机身条码：%s'%jstm_Info)
        except:
            logging.error('!!!!!输入机身条码失败')
            exit()
        #输入购买时间
        buy_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        driver.execute_script("$('input[id=BuyTime]').attr('readonly',false)")#执行JS取消input狂禁止输入属性
        driver.find_element_by_id('BuyTime').clear()
        driver.find_element_by_id('BuyTime').send_keys(buy_time)
        logging.info('.....购买时间：%s'%buy_time)
        #选择购买渠道
        for i in range(10):
            try:
                all_place = Select(driver.find_element_by_xpath('//*[@id="faulttype"]/preceding-sibling::li[1]/div[2]/select'))
                all_place.select_by_visible_text(buyPlace)
                logging.info('.....购买渠道：%s'%buyPlace)
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择购买渠道失败')
                    exit()
                else:
                    pass
        #维修单的时需要选择故障类型
        if serverType == "维修":
            for i in range(10):
                try:
                    all_ggType = driver.find_element_by_xpath('//*[@id="faulttype"]/div[2]/select')
                    ggTypes = all_ggType.find_elements_by_tag_name('option')
                    select_ggType = random.randint(0,len(ggTypes)-1)
                    ggTypeInfo = all_ggType.find_element_by_xpath('//option['+str(select_ggType)+']').text
                    GZ_Type = Select(driver.find_element_by_xpath('//*[@id="faulttype"]/div[2]/select'))
                    GZ_Type.select_by_index(select_ggType)
                    logging.info('.....故障类型：%s'%ggTypeInfo)
                    break
                except:
                    if i == 9:
                        logging.error('!!!!!选择故障类型失败')
                        exit()
                    else:
                        pass
            #上传图片文件路径
            ParentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            DataPath = ParentPath + '\\Config\\Picture\\'
            lists = os.listdir(DataPath)
            #循环上传图片
            for i in range(len(lists)):
                try:
                    WebDriverWait(driver,2).until(lambda x:x.find_element_by_id('imgOne')).send_keys(lists[i])
                    picture = DataPath + lists[i]
                    logging.info('.....正在上传图片：%s'%picture)
                except:
                    logging.error('!!!!!上传图片失败')
                    exit()
        #输入订单备注信息
        txtRemarks = txtRemark.split('+')[0] + tm
        input = driver.find_element_by_id('txtRemarks')
        driver.execute_script("arguments[0].scrollIntoView();",input)
        input.send_keys(txtRemarks)
        logging.info('.....订单备注：%s'%txtRemarks)
        #选择服务地址信息
        try:
            driver.find_element_by_xpath('//*[@class="item-lab select_address"]').click()
            logging.info('.....点击->【选择服务地址】')
            driver.find_element_by_xpath('//*[@class="locat-main"]/div[1]/a').click()
            time.sleep(2)
        except:
            logging.error('!!!!!进入地址信息填写页面失败')
            exit()
        #选择服务地址三级联动
        WebDriverWait(driver,2).until(lambda x:x.find_element_by_xpath('//*[@class="opt-address"]')).click()
        #选择省市区
        pro,city,area = serverAddress.split("-")
        for i in range(1,4):
            try:
                time.sleep(2)
                all_address = driver.find_element_by_xpath('//*[@class="wheel-wrapper wheel-wrapper-hook"]/div['+str(i)+']/ul')
                address = all_address.find_elements_by_tag_name("li")
                for li in address:
                    time.sleep(1)
                    li.click()
                    if li.text == pro or li.text == city or li.text == area:
                        break
            except:
                pass
        #点击确定
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@class="confirm confirm-hook"]')).click()
        logging.info('.....服务地区：%s-%s-%s'%(pro,city,area))
        logging.info('.....点击->【确定】')
        #随机选择筛选列表信息
        try:
            time.sleep(2)
            all_lis = driver.find_element_by_xpath('//*[@class="search-address-list ng-scope"]/ul')
            lis = all_lis.find_elements_by_tag_name('li')
            select_list = random.randint(1,len(lis))
            #随机的选择列表地址
            driver.find_element_by_xpath('//*[@class="search-address-list ng-scope"]/ul/li['+str(select_list)+']').click()
            logging.info('.....选择列表地址')
        except:
            logging.error('!!!!!选择列表地址失败')
            exit()
        #输入订单服务信息
        user = use.split('+')[0] + buy_time
        for i in range(10):
            try:
                driver.find_element_by_xpath('//input[@placeholder="请输入具体楼号、门牌号码"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="请输入具体楼号、门牌号码"]').send_keys(addInfo)
                logging.info('.....详细地址：%s'%addInfo)
                driver.find_element_by_xpath('//input[@placeholder="姓名"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="姓名"]').send_keys(user)
                logging.info('.....用户姓名：%s'%user)
                driver.find_element_by_xpath('//input[@placeholder="联系电话"]').clear()
                driver.find_element_by_xpath('//input[@placeholder="联系电话"]').send_keys(phe)
                logging.info('.....联系电话：%s'%phe)
                break
            except:
                if i == 9:
                    logging.error('!!!!!输入用户信息失败')
                    exit()
                else:
                    pass
        #点击确定提交用户信息
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@class="locat-deter"]')).click()
        logging.info('.....点击->【确定】')
        #输入服务时间，当前时间
        driver.execute_script("$('input[id=ServiceTime]').attr('readonly',false)")
        driver.find_element_by_id('ServiceTime').clear()
        driver.find_element_by_id('ServiceTime').send_keys(buy_time)
        logging.info('.....服务时间：%s'%buy_time)
        #随机选择服务时间段
        for i in range(10):
            try:
                all_day =Select(driver.find_element_by_id('ReserveNoon'))
                select_number = random.randint(0,2)
                select_day = driver.find_element_by_xpath('//*[@id="ReserveNoon"]/option['+str(select_number+1)+']').text
                all_day.select_by_index(select_number)
                logging.info('.....服务时间段：%s'%select_day)
                break
            except:
                if i == 9:
                    logging.error('!!!!!选择时间段失败')
                    exit()
                else:
                    pass
        #点击立即预约提交订单
        WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//a[@class="btn btn-info"]')).click()
        logging.info('.....提交订单')
        #获取提交订单的系统提示信息
        for i in range(10):
            try:
                AddOrderMsg = driver.find_element_by_xpath('//*[@class="layui-m-layercont"]').text
                logging.info('.....系统提示：%s'%AddOrderMsg)
                break
            except:
                if i == 9:
                    logging.error('!!!!!获取系统提示失败')
                    exit()
                else:
                    pass

    def MenHu_CheckOrderStatus(driver,CheckOrderNumber,CheckOrderStatus):

        '''
        :param CheckOrderNumber: 索要验证的订单单号
        :param CheckOrderStatus: 索要验证的订单状态
        '''

        #----------------------------------------------【订单状态校验】---------------------------------------------------
        #进入订单查询页面
        logging.info('<=====>【门户订单状态校验】<=====>')
        driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Home/My/myorder')
        driver.refresh()
        #统计订单数量获取订单状态和订单编号
        for i in range(20):
            time.sleep(2)
            try:
                All_orderCard = driver.find_element_by_xpath('//*[@class="wrap ng-scope"]/div[2]')
                OrderCards = All_orderCard.find_elements_by_tag_name('a')
                OrderNumbers = len(OrderCards)
                break
            except:
                if i == 19:
                    logging.error('!!!!!统计订单数失败')
                    exit()
                else:
                    pass
        #查找订单单号校验订单状态信息
        for i in range(1,OrderNumbers):
            try:
                FindOrderNumber = driver.find_element_by_xpath('//div[@class="card-list-header"]['+str(i)+']/span[1]').text
                if FindOrderNumber == CheckOrderNumber:
                    #找到订单核对订单状态信息
                    logging.info('.....找到校验订单了！单号：%s'%FindOrderNumber)
                    FindOrderStatus = driver.find_element_by_xpath('//div[@class="card-list-header"]['+str(i)+']/span[2]').text
                    if FindOrderStatus == CheckOrderStatus:
                        logging.info('.....订单状态校验成功！订单状态为：%s'%FindOrderStatus)
                    else:
                        logging.error('!!!!!订单状态校验失败！当前订单状态：%s,校验订单状态：%s'%(FindOrderStatus,CheckOrderStatus))
                    break
            except:
                if i == OrderNumbers-1:
                    logging.error('!!!!!找不到订单单号')
                    exit()
                else:
                    pass












if __name__ == '__main__':
    a = PPMenHu()
    print(a.MenHu_login())