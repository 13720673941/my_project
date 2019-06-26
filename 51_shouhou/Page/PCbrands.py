# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/3/2 15:33

import time,os,logging,random,configparser
from Common import Pubilc,Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class PC_Brands(object):

    def PCbrands_login(driver,section,username,password,url='http://www.51shouhou.cn/nweb/sign/login'):

        '''
        PC品牌商登录参数信息
        :param section: 配置文件中PC品牌商登录账号密码的Section
        :param username: 登录账号
        :param password: 登录密码
        :param url: 地址
        :return:
        '''
        #获取品牌商登陆配置
        Data_Path = Pubilc.data_dir(filename="Login.ini")
        data = configparser.ConfigParser()
        data.read(Data_Path, encoding='utf-8')
        use = data.get(section, username)
        pwd = data.get(section, password)

        #---------------------------------------------【PC品牌商登陆】----------------------------------------------------
        #打开PC品牌商登录页面
        logging.info('<=====>【PC品牌商登录】<=====>')
        for i in range(20):
            try:
                driver.get(url)
                logging.info('.....打开登录页面...')
                break
            except:
                if i == 19:
                    logging.error('!!!!!打开登录页面失败..')
                    exit()
                else:
                    pass
        pp_pchandle = driver.current_window_handle
        #输入账号密码，点击->【登录】
        for i in range(5):
            try:
                driver.find_element_by_xpath('//input[@type="text"]').clear()
                driver.find_element_by_xpath('//input[@type="text"]').send_keys(use)
                logging.info('.....输入用户名：%s'%use)
                driver.find_element_by_xpath('//input[@type="password"]').clear()
                driver.find_element_by_xpath('//input[@type="password"]').send_keys(pwd)
                logging.info('.....输入密码：%s'%pwd)
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
            msg = WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath('//div[@id="ukf-float"]/following-sibling::div[2]/div')).text
            logging.info('.....系统提示/截图：%s'%msg)
            driver.screen_shop(driver)
        except:
            pass
        #判断登录成功
        for i in range(5):
            time.sleep(2)
            try:
                title = driver.title
                if '超级品牌' == title:
                    logging.info('.....PC品牌登录成功！')
                    break
                else:
                    logging.info('.....PC品牌登录失败！')
            except:
                if i == 4:
                    logging.error('!!!!!登录错误...')
                    exit()
                else:
                    pass
        return pp_pchandle

    def PCbrands_SetAddOrder(driver,ddfrom,model):

        '''
        设置派单页面参数信息
        :param ddfrom: 订单来源
        :param model: 派单方式
        :return:
        '''
        #-----------------------------------------【PC品牌设置派单方式】-------------------------------------------
        logging.info('<=====>【PC品牌设置派单方式】<=====>')
        #进入系统设置页面设置派单方式
        if ddfrom == 'PC端':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="pcSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="pcSourceRule"]'
                Youxian_id = 'pcSourceAutoModel'
        if ddfrom == 'WAP端':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="wapSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="wapSourceRule"]'
                Youxian_id = 'wapSourceAutoModel'
        if ddfrom == '微信端':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="wxSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="wxSourceRule"]'
                Youxian_id = 'wxSourceAutoModel'
        #呼叫中心自动派单没有优先级，只有手动自动派单
        if ddfrom == '呼叫中心':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="hjSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="hjSourceRule"]'
        if ddfrom == '网点提交':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="branchSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="branchSourceRule"]'
                Youxian_id = 'branchSourceAutoModel'
        if ddfrom == '品牌商提交':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="brandSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="brandSourceRule"]'
                Youxian_id = 'brandSourceAutoModel'
        if ddfrom == '订单系统对接':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="orderSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="orderSourceRule"]'
                Youxian_id = 'orderSourceAutoModel'
        if ddfrom == '第三方订单平台':
            if model == 'shou':
                xpath = '//input[@class="shou_radio"and@name="otherSourceRule"]'
            elif model == 'zi':
                xpath = '//input[@class="zi_radio"and@name="otherSourceRule"]'
                Youxian_id = 'otherSourceAutoModel'
        #设置派单方式
        if model == 'shou':
            modelName = '手动派单'
        elif model == 'zi':
            modelName = '自动派单'

        driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Admin/Personal/Personal/send_single')
        time.sleep(1)
        for i in range(5):
            try:
                element = driver.find_element_by_xpath(xpath + '/following-sibling::i')
                if model == 'shou':
                    if element.is_selected():
                        pass
                    else:
                        element.click()
                    logging.info('.....设置派单方式：%s'%modelName)
                    break
                elif model == 'zi' and ddfrom != '呼叫中心':
                    driver.find_element_by_xpath(xpath + '/following-sibling::i').click()
                    time.sleep(1)
                    sel = Select(driver.find_element_by_id(Youxian_id))
                    sel.select_by_visible_text('合作网点优先')
                    logging.info('.....%s：派单方式：【%s】-【合作网点优先】'%(ddfrom,modelName))
                    break
                else:
                    pass
            except:
                if i == 4:
                    Driver.screen_shop(driver)
                    logging.error('!!!!!选择派单方式失败')
                    exit()
                else:
                    pass
        #点击保存设置
        time.sleep(2)
        botton = driver.find_element_by_xpath('//*[@class="wrapper-md"]/a')
        driver.execute_script("arguments[0].scrollIntoView();",botton)
        botton.click()
        logging.info('.....点击->【保存设置】')
        #获取保存设置后的系统提示信息
        try:
            system_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@type="dialog"]/div')).text
            logging.info('.....系统提示：%s'%system_msg)
        except:
            logging.warning('!!!!!获取不到系统提示信息')
            pass

    def PCbrands_AddOrder(driver,url,phone,user,address,area,server,BaoNW,ShouH,pro_mag,buytime,massage):

        '''
        下单页面参数信息
        :param url: 品牌商PC端下单页面地址信息
        :param phone: 用户联系方式
        :param user: 用户姓名
        :param address: 服务地址省市区
        :param area: 服务详细地址信息
        :param server: 服务类型
        :param BaoNW: 保内保外订单
        :param ShouH: 售前机售后机
        :param pro_mag: 产品信息 品牌-品线-品类
        :param buytime: 购买时间
        :param massage: 订单下单备注信息
        :return:
        '''
        #------------------------------------【PC品牌商添加系统订单】----------------------------------------
        #进入PC添加订单页面
        logging.info('<=====>【PC品牌提交订单】<=====>')
        for i in range(10):
            try:
                driver.get(url)
                time.sleep(1)
                active = driver.find_element_by_xpath('//h2[text()="订单"]/../div/ul/li[1]').get_attribute('class')
                if 'active' in active:
                    logging.info('.....正在进入添加订单页面...')
                    break
            except:
                if i == 9:
                    logging.info('.....直接登录添加订单网址失败..')
                    exit()
                else:
                    pass
        #获取联系人和联系方式
        tm = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        username = user.split('+')[0] + tm
        #输入联系方式联系人
        logging.info('************ Order Massage ************')
        for i in range(5):
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//input[@type="text"and@name="userMobile"]').send_keys(phone)
                logging.info('联系方式：%s'%phone)
                driver.find_element_by_xpath('//input[@type="text"and@name="userName"]').send_keys(username)
                logging.info('联系人：%s'%username)
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入手机号联系人失败...')
                    exit()
                else:
                    pass
        #随机选取用户性别 1、先生/2、女士
        select_num = random.randint(1,2)
        for i in range(5):
            try:
                sex = driver.find_element_by_xpath('//label[text()="性别"]/../div/label['+str(select_num)+']')
                sex_info = sex.text
                sex.click()
                logging.info('性别：%s'%sex_info)
                break
            except:
                if i == 4:
                    logging.error('!!!!!性别选择失败...')
                    exit()
                else:
                    pass
        #所在地区选择省市区
        province, city, collage = address.split('-')
        #选择省份市区 改版之后可以手输入/选择
        for i in range(5):
            try:
                driver.find_element_by_id("block").clear()
                driver.find_element_by_id('block').send_keys(collage)
                time.sleep(2)
                all_block = driver.find_element_by_xpath('//div[@class="div_select_a"]')
                blocks = all_block.find_elements_by_tag_name('div')
                #模糊匹配省市 判断省市 和 配置文件一样不
                for block in blocks:
                    block_info = block.text
                    if province and city in block_info:
                        block.click()
                        logging.info('所在地区：%s-%s-%s'%(province,city,collage))
                        break
                break
            except:
                if i == 4:
                    logging.error('!!!!!输入省市区失败')
                    exit()
                else:
                    pass
        #输入详细地址
        try:
            driver.find_element_by_xpath('//input[@name="areaDetail"]').send_keys(area)
            logging.info('详细地址：%s'%area)
        except:
            pass
        #固定选取安装、保内、售后机
        for i in range(10):
            try:
                AllServerType = driver.find_element_by_xpath('//label[text()="预约服务类型"]/../div')
                ServerTypes = AllServerType.find_elements_by_tag_name('input')
                for ServerType in ServerTypes:
                    attribute = ServerType.get_attribute('t_name')
                    if  attribute == server:
                        ServerType.find_element_by_xpath('./..').click()
                        logging.info('服务类型：%s'%server)
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!固定类型选择失败...')
                    exit()
                else:
                    pass
        #报内外选择
        for i in range(10):
            try:
                AllServerType = driver.find_element_by_xpath('//label[text()="保内保外"]/../div')
                ServerTypes = AllServerType.find_elements_by_tag_name('input')
                for ServerType in ServerTypes:
                    attribute = ServerType.get_attribute('nt')
                    if  attribute == BaoNW:
                        ServerType.find_element_by_xpath('./..').click()
                        logging.info('服务类型：%s'%BaoNW)
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!固定类型包内外选择失败...')
                    exit()
                else:
                    pass
        #选择售后类型
        for i in range(10):
            try:
                AllServerType = driver.find_element_by_xpath('//label[text()="售后类型"]/../div')
                ServerTypes = AllServerType.find_elements_by_tag_name('input')
                for ServerType in ServerTypes:
                    attribute = ServerType.get_attribute('value')
                    if  attribute == ShouH:
                        ServerType.find_element_by_xpath('./..').click()
                        logging.info('服务类型：%s'%ShouH)
                        break
                break
            except:
                if i == 9:
                    logging.error('!!!!!固定类型售后机制选择失败...')
                    exit()
                else:
                    pass
        #选择产品品牌、品类、品线
        brand,product,bigpro = pro_mag.split('-')
        for i in range(5):
            try:
                select_brand = Select(driver.find_element_by_id('brand'))
                select_brand.select_by_visible_text(brand)
                logging.info('产品品牌：%s'%brand)
                time.sleep(2)
                select_brand = Select(driver.find_element_by_id('product'))
                select_brand.select_by_visible_text(product)
                logging.info('产品线：%s'%product)
                time.sleep(2)
                select_brand = Select(driver.find_element_by_id('bigpro'))
                select_brand.select_by_visible_text(bigpro)
                logging.info('产品品类：%s'%bigpro)
                break
            except:
                if i == 4:
                    logging.error('!!!!!选择产品信息失败...')
                    exit()
                else:
                    pass
        #点击->【产品型号】
        time.sleep(2)
        try:
            driver.find_element_by_id('model').click()
        except:
            pass
        #随机选择产品型号
        for i in range(5):
            try:
                all_model = driver.find_element_by_id('selmodel')
                models = all_model.find_elements_by_tag_name('div')
                #随机产品型号数
                select_model = random.randint(1,(len(models)))
                try:
                    model = driver.find_element_by_xpath('//*[@id="selmodel"]/div[' +str(select_model)+ ']')
                    modelname = model.text
                    logging.info('产品型号：%s'%modelname)
                    guige = model.get_attribute('specificationname')    #获取关联规格
                    logging.info('产品规格：%s'%guige)
                    model.click()
                except:
                    pass
                break
            except:
                if i == 4:
                    logging.error('!!!!!选择产品型号/规格失败...')
                    pass
        #获取全部购买其渠道综合随机数
        try:
            all_buy = driver.find_element_by_id('channelPkId')
            buys = all_buy.find_elements_by_tag_name('option')
            selbuy = random.randint(1,len(buys)-1) #第一个非选取项所以从1开始
        except:
            pass
        #随机购买渠道选取
        for i in range(5):
            try:
                sel = Select(driver.find_element_by_id('channelPkId'))
                sel.select_by_index(selbuy)
                channelPkId = driver.find_element_by_xpath('//select[@id="channelPkId"]/option[' +str(selbuy+1)+ ']').text
                logging.info('购买渠道：%s'%channelPkId)
                break
            except:
                if i == 4:
                    logging.error('!!!!!选择购买渠道失败...')
                    exit()
                else:
                    pass
        #解除禁止输入，输入购买时间
        try:
            time.sleep(2)
            js = "$('input[name=buyTime]').attr('readonly',false)"
            driver.execute_script(js)
            driver.find_element_by_xpath('//input[@placeholder="选择购买时间"and@name="buyTime"]').send_keys(buytime)
            logging.info('购买日期：%s'%tm)
            #driver.find_element_by_xpath('//*[@id="form"]/div[16]/label').click() #点击日期弹屏外面地方去除日期弹屏
        except:
            logging.error('!!!!!输入购买日期失败...')
            pass
        #选择预约时间段
        for j in range(5):
            try:
                day_nums = random.randint(0,2)
                day = Select(driver.find_element_by_id('ReserveNoon'))
                day.select_by_index(day_nums)
                day_text = driver.find_element_by_xpath('//*[@id="ReserveNoon"]/option[' + str(day_nums + 1) + ']').text
                logging.info('预约时间段：%s'% day_text)
                break
            except:
                if j == 4:
                    logging.error('!!!!!选择时间段错误...')
                    exit()
                else:
                    pass
        #解除禁止属性，输入预约服务时间
        try:
            js1 = "$('input[name=orderAppointTime]').attr('readonly',false)"
            driver.execute_script(js1)
            driver.find_element_by_xpath('//input[@name="orderAppointTime"and@placeholder="选择预约服务时间"]').send_keys(tm)
            logging.info('预约时间：%s'%tm)
            driver.find_element_by_xpath('//*[@id="form"]/div[8]').click()  #点击日期弹屏外面地方去除日期弹屏
        except:
            logging.error('!!!!!输入预约日期失败...')
            pass
        #填写订单申请备注信息
        BeiZ = massage.split('+')[0] + tm
        driver.find_element_by_xpath('//label[text()="反馈情况"]/following-sibling::div/div/textarea').send_keys(BeiZ)
        logging.info('备注：%s' % BeiZ)
        #点击->【计算交通费】,获取异常信息
        # try:
        #     driver.find_element_by_xpath('//*[@class="btn btn-warning btnQuelist"]').click()
        #     logging.info('点击->【计算交通费】')
        #     #获取异常信息提示
        #     JiaoT = WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath('//div[@type="dialog"]/div')).text
        #     if JiaoT:
        #         logging.info('.....计算交通费异常：%s'%JiaoT)
        #     else:
        #         pass
        # except:
        #     pass
        #统计匹配网点信息
        # try:
        #
        #     all_wd = driver.find_element_by_xpath('//div[@class="table-container"]/table/tbody')
        #     wds = all_wd.find_elements_by_tag_name('tr')
        #     count_wd = len(wds)
        #     logging.info('匹配网点到：%s个网点'%count_wd)
        #     for j in range(1,count_wd+1):
        #         try:
        #             wdname = WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath(
        #                 '//div[@class="table-container"]/table/tbody/tr[' +str(j)+ ']')).text
        #             logging.info('|-----------------------|')
        #             logging.info('%s'%wdname)
        #         except:
        #             logging.error('!!!!!打印匹配网点信息失败...')
        #             pass
        # except:
        #     pass
        #点击提交品牌商订单
        try:
            driver.find_element_by_xpath('//button[@ng-click="save()"and@type="button"]').click()
            logging.info('点击->【提交】')
        except:
            logging.error('!!!!!点击提交失败...')
            exit()
        #获取提交订单信息提示
        try:
            form_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//div[@type="dialog"]')).text
            logging.info('*******************************')
            logging.info('提交信息：%s'%form_msg)
        except:
            pass

    def PCbrands_FindOrdernum(driver,DD_Status=None,OrderModel='shou'):

        '''
        查找品牌商下单订单的订单号",校验待审核订单状态
        :param DD_Status: 订单状态
        :param OrderModel 派单方式，自动派单要在订单查询里面寻找订单单号信息
        :return:
        '''
        #...................................-【获取订单号】........................................-
        logging.info('<=====>【获取订单单号】<=====>')
        #进入订单审核页面
        if OrderModel == 'shou':
            driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Admin/Order/Order/index')
            driver.refresh()
            #默认第一个订单为新件订单,判断时间间隔，小于60秒
            for i in range(5):
                try:
                    addordertm = driver.find_element_by_xpath('//div[@class="order-main"]/div[1]/div[1]/span[1]/font').text
                    #把获取的时间转换成时间戳
                    old_time = time.mktime(time.strptime(addordertm,'%Y-%m-%d %H:%M:%S'))
                    new_time = time.time()
                    cha_time = new_time - old_time
                    if cha_time < 60:
                        FindOrderNumber = driver.find_element_by_xpath('//div[@class="order-main"]/div/div/span[2]/font').text
                        logging.info('.....该订单为新建订单订单号：%s ；下单时间：%s'%(FindOrderNumber,addordertm))
                    else:
                        logging.warning('!!!!!获取订单信息超时,刷新重试....')
                    if i == 1:
                        driver.refresh()
                        logging.info('.....找不到订单刷新重试...')
                    else:
                        pass
                    break
                except:
                    if i == 4:
                        logging.error('.....你把订单添加到哪了？？？')
                        exit()
                    else:
                        pass
            #待审核订单状态校验
            if DD_Status == None:
                pass
            else:
                logging.info('-=【添加订单校验】=-')
                # 订单状态校验
                for i in range(5):
                    try:
                        input = driver.find_element_by_xpath('//input[@type="text"and@placeholder="订单/手机号/地址/原始单号查询"]')
                        input.clear()
                        input.send_keys(FindOrderNumber)
                        driver.find_element_by_xpath('.//form/div[1]/button').click()
                        dd_status = driver.find_element_by_xpath('//td[@class="td-mod-lborder"][2]/div[1]/p').text
                        if dd_status == DD_Status:
                            logging.info('.....品牌商添加订单校验成功！当前订单状态：%s'%dd_status)
                        else:
                            logging.error('!!!!!品牌商添加订单校验失败...；当前订单状态：%s'%dd_status)
                            exit()
                        break
                    except:
                        pass
        #自动派单单号查询
        elif OrderModel == 'zi':
            driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Admin/Order/Order/query')
            driver.refresh()
            time.sleep(2)
            #默认第一个订单为新件订单,判断时间间隔，小于60秒
            for i in range(5):
                try:
                    addordertm1 = driver.find_element_by_xpath('//div[@class="order-mod-nopay"][1]/span[1]/font').text
                    # 把获取的时间转换成时间戳
                    old_time1 = time.mktime(time.strptime(addordertm1,'%Y-%m-%d %H:%M:%S'))
                    new_time1 = time.time()
                    cha_time1 = new_time1 - old_time1
                    if cha_time1 < 60:
                        FindOrderNumber = driver.find_element_by_xpath('//div[@class="order-mod-nopay"][1]/span[2]/font').text
                        logging.info('.....该订单为新建订单订单号：%s ；下单时间：%s'%(FindOrderNumber,addordertm1))
                    else:
                        logging.warning('!!!!!获取订单信息超时,刷新重试....')
                    if i == 1:
                        driver.refresh()
                        logging.info('.....找不到订单刷新重试...')
                    else:
                        pass
                    break
                except:
                    if i == 4:
                        logging.error('.....你把订单添加到哪了？？？')
                        exit()
                    else:
                        pass
        return FindOrderNumber

    def PCbrands_CheckOrderStatus(driver,OrderNumber,DD_Status,ExceptWD=None,ExceptSF=None):

        '''
        除待审核外的订单状态的校验，以及接受订单的网店和师傅名称的校验
        :param OrderNumber: 所要校验的订单单号
        :param DD_Status: 订单状态
        :param ExceptWD: 接受订单的网店名称
        :param ExceptSF: 接受订单的师傅名称
        :return:
        '''
        #---------------------------------------------【订单状态/收单校验】-----------------------------------------------
        #搜索订单单号
        logging.info('<=====>【订单状态校验】<=====>')
        driver.get('http://www.51shouhou.cn/brands3/haodi3/index.php/Admin/Order/Order/query')
        for i in range(10):
            try:
                input = driver.find_element_by_xpath('//input[@type="text"and@placeholder="订单/手机号/地址/原始单号查询"]')
                input.clear()
                input.send_keys(OrderNumber)
                driver.find_element_by_xpath('.//form/div[1]/button').click()
                break
            except:
                if i == 2:
                    driver.refresh()
                    pass
            finally:
                if i == 9:
                    logging.error('!!!!!搜索订单失败...')
                    exit()
                else:
                    pass
        #输出搜索订单状态
        for i in range(5):
            try:
                dd_status = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@class="text-warning ng-binding"]')).text
                if dd_status == DD_Status:
                    logging.info('.....订单校验成功！当前订单状态：【%s】'%dd_status)
                else:
                    logging.error('!!!!!订单状态校验失败；当前订单状态：【%s】;校验订单状态：【%s】'%(dd_status,DD_Status))
                    exit()
                break
            except:
                pass
        #当前该订单接受网点名称校验
        if ExceptWD == None:
            pass
        else:
            logging.info('-=【派单网点校验】=-')
            for i in range(5):
                try:
                    wd_name = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//t[@class="ng-scope"]/span[1]')).text
                    if ExceptWD in wd_name:
                        logging.info('.....派单网点校验成功！%s'%wd_name)
                    else:
                        logging.error('!!!!!派单网点校验失败...当前%s'%wd_name)
                        exit()
                    break
                except:
                    pass
        #当前该党的接受师傅名称校验
        if ExceptSF == None:
            pass
        else:
            logging.info('-=【派单师傅校验】=-')
            for i in range(5):
                try:
                    sf_name = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('.//tbody/tr/td[4]/div/p[2]')).text
                    if ExceptSF in sf_name:
                        logging.info('.....派单师傅校验成功！接单师傅：%s'%sf_name)
                    else:
                        logging.error('!!!!!师傅接单校验失败...无接单师傅')
                        exit()
                    break
                except:
                    pass


# if __name__ == '__main__':
#
#     from Common import Driver
#     A = Driver.PC_Brower()
#     PC_Brands.PCbrands_login(A,'PPS_Login','pps_username','pps_password')
#     PC_Brands.PCbrands_SetAddOrder(A,ddfrom='品牌商提交',model='zi')