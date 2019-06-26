# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/5/24 17:13

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from public.common.logconfig import Log
from config.pathconfig import *
import time,random
log = Log()
'''
获取元素等工共操作的二次封装
'''
class BasePage(object):
    '''
    所有的Page类都继承该基础类
    '''
    def __init__(self,driver):
        self.driver = driver
        self.success = "SUCCESS "
        self.fail = "FAIL "
        
    def get_element(self,element):
        """
        定位页面元素位置
        eg：driver.get_element(element=(By.XPATH,'//div[@id="kw"]'))
        """
        t1 = time.time()
        try:
            el = WebDriverWait(self.driver,20,1).until(EC.presence_of_element_located(element))
            log.info('{0} Find element <{1}>, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
            return el
        except TimeoutException:
            # log.error('{0} Unable find element <{1}>, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
            raise TimeoutException('{0} Unable find element <{1}> timeout, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
        finally:
            pass

    def open_url(self,url):
        """
        打开Url地址
        eg：driver.open_url('http://www.baidu.com')
        """
        t1 = time.time()
        try:
            self.driver.get(url)
            log.info('{0} Open url <{1}>, Spend {2} seconds.'.format(self.success,url,time.time()-t1))
        except Exception:
            log.error('{0} Unable to open url <{1}>, Spend {2} seconds.'.format(self.fail,url,time.time()-t1))
            raise

    def window_max(self):
        """
        页面最大化
        """
        t1 = time.time()
        self.driver.maximize_window()
        log.info('{0} Set window size max, Spend {1} seconds.'.format(self.success,time.time()-t1))

    def sleep(self,seconds):
        """
        强制等待
        eg: driver.sleep(1)
        """
        time.sleep(seconds)
        log.info('{0} Webdriver sleep {1} seconds.'.format(self.success,seconds))

    def wait(self):
        """
        隐性等待
        eg: driver.wait()
        """
        t1 = time.time()
        self.driver.implicitly_wait(20)
        log.info('{0} Wait page load... , Spend {1} seconds.'.format(self.success,time.time()-t1))

    def is_display(self,element):
        '''
        元素是否可见
        eg: driver.is_display(element=(By.XPATH,'//div[@id="kw"]'))
        '''
        t1 = time.time()
        flag=False
        try:
            self.get_element(element).is_displayed()
            log.info('{0} Find element <{1}> is true, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
            flag=True
        except Exception:
            log.info('{0} Find element <{1}> is false, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
            raise
        finally:
            return flag

    def clear_input(self,element):
        '''
        清除输入框
        eg: driver.clear_input(xxx)
        '''
        t1 = time.time()
        self.get_element(element).clear()
        log.info('{0} Clear element <{1}> input message, Spend {2} seconds.'.format(self.success,element,time.time()-t1))

    def input_message(self,element,message):
        '''
        输入字段信息
        eg: driver.input_message('xpath','input_message')
        '''
        t1 = time.time()
        try:
            self.get_element(element).send_keys(message)
            log.info('{0} Input message: {1}, Spend {2} seconds'.format(self.success,message,time.time()-t1))
        except Exception:
            log.error('{0} Unable input message: {1}, Spend {2} seconds'.format(self.fail,message,time.time()-t1))
            pass

    def click_button(self,element):
        '''
        点击页面按钮
        eg: driver.click_button(element=(By.XPATH,'//*[@id='kw]'))
        '''
        t1 = time.time()
        button = self.get_element(element)
        try:
            button.click()
            log.info('{0} Click button -> <{1}>, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
        except Exception:
            #报错再次判断页面元素是否存在
            if self.is_display(element):
                #等待两秒再次点击
                self.sleep(2)
                button.click()
                log.info('{0} Second time click button -> <{1}>, Spend {2} seconds.'.format(self.success, element, time.time()-t1))
            else:
                log.error('{0} Unable click button -> <{1}>, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
                pass

    def get_text(self,element):
        '''
        获取元素文本信息
        eg: driver.get_text('xxx')
        '''
        t1 = time.time()
        try:
            element_text = self.get_element(element).text
            log.info('{0} Get element <{1}> text, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
            return element_text
        except Exception:
            log.error('{0} Unable get element <{1}> text, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
            pass

    def get_att(self,element,attribute):
        '''
        获取元素属性
        eg: driver.get_att('xpath','attribute key')
        '''
        t1 = time.time()
        try:
            att =  self.get_element(element).get_attribute(attribute)
            log.info('{0} Get element <{1}> , attribute by {2}, Spend {3} seconds.'.format(self.success,element,attribute,time.time()-t1))
            return att
        except Exception:
            log.error('{0} Unable get element <{1}> , attribute by {2} Spend {3} seconds.'.format(self.fail,element,attribute,time.time()-t1))
            pass

    def use_js(self,js):
        '''
        适用js脚本
        eg: driver.use_js('window.open('http://www.baidu.com')')
        '''
        t1 = time.time()
        try:
            self.driver.execute_script(js)
            log.info('{0} Execute js {1}, Spend {2} seconds.'.format(self.success,js,time.time()-t1))
        except Exception:
            log.error('{0} Unable execute js {1}, Spend {2} seconds'.format(self.fail,js,time.time()-t1))
            raise

    def get_title(self):
        '''
        获取网页标题信息
        eg: driver.get_title()
        '''
        t1 = time.time()
        try:
            title = self.driver.title
            log.info('{0} Get window page title text, Spend {1} seconds.'.format(self.success,time.time()-t1))
            return title
        except Exception:
            log.error('{0} Unable get window page title text, Spend {1} seconds.'.format(self.fail,time.time()-t1))
            raise

    def quit_browser(self):
        '''
        退出浏览器
        eg: driver.quit_browser()
        '''
        t1 = time.time()
        self.driver.quit()
        log.info('{0} Quit browser, Spend {1} seconds.'.format(self.success,time.time()-t1))

    def close_page(self):
        """
        关闭页面
        eg: driver.close_page()
        """
        t1 = time.time()
        self.driver.close()
        log.info('{0} Close current window page, Spend {1} seconds.'.format(self.success,time.time()-t1))

    def refresh_page(self):
        '''
        刷新页面
        eg: driver.refresh_page()
        '''
        t1 = time.time()
        self.driver.refresh()
        log.info('{0} Refresh current page, Spend {1} seconds.'.format(self.success,time.time()-t1))

    def click_and_hold_btn(self,element):
        """
        点击并保持长按鼠标左键
        eg: driver.click_and_hold_btn('xpath')
        """
        t1 = time.time()
        try:
            actions = ActionChains(self.driver)
            actions.click_and_hold(element).perform()
            log.info('{0} Click element <{1}> and hold on, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
            return actions
        except Exception:
            log.error('{0} Unable click element <{1}> and hold on, Spend {2} seconds.'.format(self.fail,element,time.time()-t1))
            raise

    def get_all_handles(self):
        """
        获取所有的窗口handle
        eg: driver.get_all_handles()
        """
        t1 = time.time()
        handles = self.driver.window_handles
        log.info('{0} Get all window handles in a list, Spend {1} seconds.'.format(self.success,time.time()-t1))
        return handles

    def get_current_handle(self):
        """
        获取当前窗口的handle
        """
        t1 = time.time()
        current_handle = self.driver.current_window_handle
        log.info('{0} Get current window handle, Spend {1} seconds.'.format(self.success,time.time()-t1))
        return current_handle

    def switch_window_handle(self,all_handles,old_handle):
        """
        切换页面新窗口
        :param all_handles 所有的窗口句柄列表
        :param old_handle  当前窗口的句柄
        """
        t1 = time.time()
        try:
            for handle in all_handles:
                if handle != old_handle:
                    #切换新窗口
                    self.driver.switch_to.window(handle)
                    log.info('{0} Switch to window handle <{1}>, Spend {2} seconds.'.format(self.success,handle,time.time()-t1))
        except Exception:
            log.error('{0} Unable switch to window handle, Spend {1} seconds.'.format(self.fail,time.time()-t1))
            raise

    def take_screen_shot(self):
        """
        截图
        """
        t1 = time.time()
        name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + '.png'
        try:
            self.driver.get_screenshot_as_file(errorImagePath + name)
            log.info('{0} Save screen shot to: {1}, Spend {2} seconds.'.format(self.success,errorImagePath + name,time.time()-t1))
        except Exception:
            log.error('{0} Unable screen shot! Spend {1} seconds'.format(self.fail,time.time()-t1))
            raise

    def operate_select(self,element,value=None,is_random=False):
        """
        操作select选择框，按文本选择或者随机选择
        """
        t1 = time.time()
        #因下单页面涉及select模块较多封装调用
        select_method = Select(self.get_element(element))
        try:
            if is_random:
                AllOption = self.get_element(element)
                options = AllOption.find_elements_by_tag_name('option')
                #随机选择一个数字，选择该选项的索引
                chooseNum = random.randint(1,len(options)-1)
                select_method.select_by_index(chooseNum)
                #返回一个该随机选择的文本值
                for select in select_method.all_selected_options:
                    log.info('{0} Select value: {1}, Spend {2} seconds.'.format(self.success,select.text,time.time()-t1))
            else:
                select_method.select_by_visible_text(value)
                log.info('{0} Select value: {1}, Spend {2} seconds.'.format(self.success,value,time.time()-t1))
        except Exception:
            log.error('{0} Unable select value, Spend {1} seconds.'.format(self.fail,time.time()-t1))
            raise

    def get_now_time(self,Time=False):
        '''
        获取当前时间 年-月-日 时：分：秒
        '''
        if Time:
            timeType = '%Y-%m-%d %H:%M:%S'
        else:
            timeType = '%Y-%m-%d'
        return time.strftime(timeType,time.localtime(time.time()))

    def get_now_timenum(self):
        '''
        获取当前时间的时间戳
        '''
        return time.time()

    def get_one_timenum(self,DataTime,Time=False):
        '''
        获取指定时间的时间戳
        '''
        if Time:
            timeType = '%Y-%m-%d %H:%M:%S'
        else:
            timeType = '%Y-%m-%d'
        #返回时间戳
        return time.mktime(time.strptime(DataTime,timeType))

    def drag_button(self,element,txtelement,arrivetxt):
        """
        结算页面固定比例结算按钮左右滑动封装
        :param txtelement 判断所用获取的文本
        :param arrivetxt  索要滑动的位置文本
        """
        t1 = time.time()
        #等待按钮加载
        self.sleep(2)
        dragButton = self.get_element(element)
        #获取滑块y坐标位置
        dragButton_y = dragButton.location['y']
        actions = self.click_and_hold_btn(dragButton)
        #归零0，y
        self.sleep(1)
        while True:
            #获取移动后的文本
            txt1 = self.get_text(txtelement)
            #滑块x坐标归零
            if txt1 == '0':
                break
            else:
                actions.move_by_offset(-1,dragButton_y).perform()
        #清除缓存操作
        actions.reset_actions()
        log.info('{0} Button: <{1}>, remove zero, Spend {2} seconds.'.format(self.success,element,time.time()-t1))
        while True:
            self.sleep(1)
            txt2 = self.get_text(txtelement)
            if txt2 == arrivetxt:
                actions.release(dragButton).perform() #释放左键
                break
            else:
                actions.move_by_offset(1,dragButton_y).perform()
        log.info('{0} Button: {1}, remove right arrive {2}, Spend {3} seconds.'.format(self.success,element,arrivetxt,time.time()-t1))

    def get_element_count(self,parentEl,childEl='li'):
        '''
        获取元素个数信息
        :param parentEl 子元素的父亲元素位置
        :param childEl  子元素
        '''
        t1 = time.time()
        try:
            ParentPath = self.get_element(parentEl)
            ChildElList = ParentPath.find_elements_by_tag_name(childEl)
            count = len(ChildElList)
            log.info('{0} Get children element <{1}> count are {2}, Spend {3} seconds.'.format(self.success,childEl,count,time.time()-t1))
            return count
        except Exception:
            log.error('{0} Get element <{1}> count is anomaly, Spend {2} seconds.'.format(self.fail,childEl,time.time()-t1))
            raise

    def operate_not_select(self,open_el,parent_el,value=None,child_el='li',is_random=False):
        """
        操作不是select的选择框封装
        :param OpenEl   点击打开选择框的元素位置
        :param ParentEl 总计子元素的父元素位置
        :param value    要选择的文本值
        :param ChildEl  选择项子元素
        :param Random   是否随机选择
        """
        t1 = time.time()
        #点击打开选择框
        self.click_button(open_el)
        self.sleep(1)
        try:
            ParentPath = self.get_element(parent_el)
            ChildList = ParentPath.find_elements_by_tag_name(child_el)
            SelectNum = random.randint(1,len(ChildList))
            if is_random:
                ChildList[SelectNum].click()
                log.info('{0} Select value: {1} by random choose, Spend {2} seconds.'.format(self.success,ChildList[SelectNum].text,time.time()-t1))
            else:
                for child in ChildList:
                    self.sleep(1)
                    if child.text == value:
                        child.click()
                        break
                log.info('{0} Select value: {1}, Spend {2} seconds.'.format(self.success,value,time.time()-t1))
        except Exception:
            log.error('{0} Select value is anomaly, Spend {1} seconds.'.format(self.fail,time.time()-t1))
            raise

    def up_loading_picture(self,num,element):
        '''
        上传图片
        :param num      上传图片的个数
        :param element  上传图片元素位置
        '''
        #加载图片列表
        Plist = os.listdir(picturePath)
        #循环上传
        for i in range(num):
            t1 = time.time()
            try:
                Picture = picturePath+Plist[i]
                self.sleep(1)
                self.input_message(element,message=Picture)
                log.info('{0} Uploading picture: {1}, Spend {2} seconds.'.format(self.success,Picture,time.time()-t1))
            except Exception:
                log.error('{0} Uploading is anomaly, Spend {1} seconds.'.format(self.fail,time.time()-t1))
                raise

    def print_case_name(self,CaseName):
        """
        打印用例名称
        """
        log.info('{0} Load case name: {1}'.format(self.success,CaseName))

    def select_new_order(self,OrderNumber):
        """
        订单列表中勾选所要处理的订单单号
        :param OrderNumber:
        :return:
        """
        time.sleep(2)
        for i in range(1,10):
            try:
                OrderNum = self.get_text((By.XPATH,'//div/div[2]/table/tbody/tr['+str(i)+']/td[3]/div/a'))
                if OrderNum == OrderNumber:
                    self.click_button((By.XPATH,'//div/div[2]/table/tbody/tr['+str(i)+']/td[2]/div/label/span/input'))
                    log.info('{0} Select order: {1}.'.format(self.success,OrderNumber))
                    break
            except Exception:
                if i == 9:
                    log.error('{0} Select order: {1} anomaly.'.format(self.fail,OrderNumber))
                    raise

    def get_order_number(self,insteadOrder=False):
        '''
        获取最新工单单号
        '''
        #仅报单 到待报单页面获取
        if insteadOrder:
            self.open_url('http://www.51shouhou.cn/singleBranch/#/order/search/instead')
        #等待页面加载
        self.sleep(2)
        self.refresh_page()
        newOrderNum=''
        #获取工单单号
        for i in range(10):
            try:
                #获取第一个订单的创建时间
                if insteadOrder: #代报单获取创建时间不一样
                    addOrderTime = self.get_text(element=(By.XPATH,'//div/div[2]/*/*/tr[1]/td[6]/*/span'))
                else:
                    addOrderTime = self.get_text(element=(By.XPATH,'//div/div[2]/*/*/tr[1]/td[5]/*/span'))
                #把时间转化为时间戳小于30秒就是新订单
                oldTimeNumber = self.get_one_timenum(DataTime=addOrderTime,Time=True)
                newTime = self.get_now_timenum()
                if newTime - oldTimeNumber < 60:
                    newOrderNum = self.get_text(element=(By.XPATH,'//div/div[2]/table/tbody/tr[1]/td[3]/div/a'))
                    log.info('{0} Get order number: {1}.'.format(self.success,newOrderNum))
                    #有时候获取不到订单单号，判断单号的长度，否则刷新页面
                    if len(newOrderNum) == 18:
                        break
                    else:
                        self.refresh_page()
            except Exception:
                if i == 9:
                    log.error('{0} Unable get order number.'.format(self.fail))
                    raise
        return newOrderNum
    
    def get_system_msg(self,element=(By.XPATH,'//*[@class="ivu-message-notice-content"]/div/div/span')):
        '''
        获取系统提示信息
        '''
        return self.get_text(element)

    def open_order_message(self,OrderNumber):
        '''
        点击订单号进入详情页
        '''
        time.sleep(2)
        for i in range(1,10):
            try:
                OrderNum = self.get_text((By.XPATH,'//div/div[2]/table/tbody/tr['+str(i)+']/td[3]/div/a'))
                if OrderNum == OrderNumber:
                    self.click_button((By.XPATH,'//div/div[2]/table/tbody/tr['+str(i)+']/td[3]/div/a'))
                    log.info('{0} Into order: {1} message page.'.format(self.success,OrderNumber))
                    break
            except Exception:
                if i == 9:
                    log.error('{0} Unable into order: {1} message page.'.format(self.fail,OrderNumber))
                    raise

