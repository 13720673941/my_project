#coding=utf-8
#品牌商服务配置

from selenium import webdriver
from Common.Logger import logFormat
import logging,configparser,time,random,unittest
from selenium.webdriver.support.wait import WebDriverWait

def Set_Server(driver,url,PPname,Server,PinXian,PinLei):

    #-------------------------------------------【品牌商配置服务】-------------------------------------------
    #进入配置服务页面
    for i in range(10):
        try:
            driver.find_element_by_xpath('//div[@class="content-block"][3]/div/ul/li[2]').click()
            logging.info('.....点击->【服务配置】')
            break
        except:
            if i == 9:
                driver.get(url)
                logging.info('.....正在打开服务配置地址...')
                headerInfo = driver.find_element_by_xpath('//div[@class="header-center"]').text
                if headerInfo == '服务配置':
                    logging.info('.....进入服务配置页面...')
                else:
                    logging.error('!!!!!进入服务配置页面失败')
                    exit()
            else:
                pass
    #读取品牌名称信息添加品牌信息
    tm = time.strftime('%M%S',time.localtime(time.time()))
    PP = PPname.split('+')[0] + tm
    for i in range(10):
        try:
            driver.find_element_by_xpath('//a[@href="#/my/servSet/editBrand"]').click()
            logging.info('.....点击->【添加】')
            AddPP = driver.find_element_by_xpa5th('//a[@class="t50-add"]')
            driver.execute_script("arguments[0].scrollIntoView();",AddPP)
            AddPP.click()
            logging.info('.....点击->【+添加品牌名称】')
            break
        except:
            if i == 9:
                logging.error('!!!!!进入添加品牌商输入框失败')
                exit()
            else:
                pass
    #输入品牌名称信息确定
    for i in range(10):
        try:
            logging.info('**************【品牌商服务配置信息】**************')
            driver.find_element_by_xpath('//input[@type="text"and@placeholder="请输入品牌名称"]').send_keys(PP)
            logging.info('品牌名称：%s'%PP)
            driver.find_element_by_xpath('//a[text()="确定"]').click()
            logging.info('点击->【确定】')
        except:
            if i == 9:
                logging.error('!!!!!输入品牌名称失败')
                exit()
            else:
                pass
    #获取系统提示信息
    try:
        system_msg = WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_xpath('//*[@id="app"]/following-sibling::div/div')).text
        logging.info('系统提示：%s'%system_msg)
    except:
        logging.error('!!!!!获取系统消息失败')
        pass
    #选择添加的品牌名称待添加品类
    for i in range(10):
        try:
            #获取所有的品牌名称标签选择刚才添加的品牌
            all_lis = driver.find_element_by_xpath('//*[@class="t50-list"]/ul')
            lis = all_lis.find_elements_by_tag_name('li')
            for li in lis:
                addPP = li.text
                attribute = li.get_attribute('class')
                #标签属性不等于active就是没有选中可以选取
                if addPP == PP and attribute != 'active':
                    li.click()
                    logging.info('点击->【%s】'%PP)
                    try:
                        driver.find_element_by_xpath('//a[text()="确定"]').click()
                        logging.info('点击->确定')
                    except:
                        logging.error('!!!!!点击确定失败')
                    break
            break
        except:
            if i == 9:
                logging.error('!!!!!选择品牌失败')
                exit()
            else:
                pass
    #获取系统提示信息,保存添加的品牌名称的提示信息
    try:
        system_msg = WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath('//*[@id="app"]/following-sibling::div/div')).text
        logging.info('系统提示：%s' % system_msg)
    except:
        logging.error('!!!!!获取系统消息失败')
        pass
    #随机选择服务类型进行待添加品线
    sel_num = random.randint(0,1)
    selServer = Server.split(',')[str(sel_num)]
    for i in range(10):
        try:
            driver.find_element_by_xpath('//a[text()="' +selServer+ '"]').click()
            logging.info('服务类型：%s'%selServer)
            break
        except:
            if i == 9:
                logging.error('!!!!!选择服务类型失败')
                exit()
            else:
                pass
    #添加产品线信息



