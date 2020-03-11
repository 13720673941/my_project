#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/5/24 17:13

from config.pathConfig import *
from public.common.logConfig import Log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time,random

class BasePage(object):
    """
        对 webdriver 中的基本方法进行二次封装，所有的Page类都继承该基础类
    """
    def __init__(self,driver):
        self.driver = driver
        self.log = Log()

    def wait_element(self,path,sec=20):
        """
        固定时间内检测元素是否在页面显示,没有显示直接抛出错误messages,默认 5s 可以重新赋值
        Usage:
        driver.wait_element("id->kw")
        """

        if "->" not in path:
            raise NameError("Element path: '{0}' error ! For lack of '->' .".format(path))
        by_name = path.split('->')[0]
        path_name = path.split('->')[1]
        messages = "Element: {0} not find in {1}s .".format(path_name,sec)
        if by_name == "id":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.ID,path_name)),messages)
        elif by_name == "name":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.NAME,path_name)),messages)
        elif by_name == "class":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.CLASS_NAME,path_name)),messages)
        elif by_name == "xpath":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.XPATH,path_name)),messages)
        elif by_name == "link_text":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.LINK_TEXT,path_name)),messages)
        elif by_name == "css":
            WebDriverWait(self.driver,sec,1).until(EC.presence_of_element_located((By.CSS_SELECTOR,path_name)),messages)
        else:
            raise NameError("Please enter right elements, 'id','name','class','xpath','link_text','css'.")

    def get_element(self,path):
        """
        找到页面元素位置,并返回找到的元素
        Usage:
        driver.get_element("id->kw")
        """

        if "->" not in path:
            raise NameError("Element path: '{0}' error ! For lack of '->' .".format(path))
        by_name = path.split('->')[0]
        path_name = path.split('->')[1]

        if by_name == "id":
            element = self.driver.find_element_by_id(path_name)
        elif by_name == "name":
            element = self.driver.find_element_by_name(path_name)
        elif by_name == "class":
            element = self.driver.find_element_by_class_name(path_name)
        elif by_name == "xpath":
            element = self.driver.find_element_by_xpath(path_name)
        elif by_name == "link_text":
            element = self.driver.find_element_by_link_text(path_name)
        elif by_name == "css":
            element = self.driver.find_element_by_css_selector(path_name)
        else:
            raise NameError("Please enter right elements, 'id','name','class','xpath','link_text','css'.")
        return element

    def clear_catch(self):
        """
        selenium 运行加载的网站过多，清除浏览器缓存
        Usage:
        driver.clear_catch()
        """
        self.driver.delete_all_cookies()
        self.log.info(' * Clear browser catch data .')

    def open_url(self,url,element=None):
        """
            打开Url地址,可以传入一个打开页面后的元素路径进行判断,未出现时会刷新页面
        不传入参数就是直接打开网址没有刷新操作
        Usage:
        driver.open_url('http://www.baidu.com')
        """

        if element == None:
            self.driver.get(url)
            self.log.info(' * Open url: {0} .'.format(url))
        else:
            for i in range(5):
                self.driver.get(url)
                # 尝试获取登录页面信息
                if self.is_display(element):
                    self.log.info(' * Open url: {0} .'.format(url))
                    break
                else:
                    if i < 4:
                        self.refresh_page()
                    else:
                        raise TimeoutError('Not Open Url: {0} ! '.format(url))
            pass

    def get_current_url(self):
        """
        获取当前url地址信息
        Usage:
        driver.get_current_url()
        """

        url = self.driver.current_url
        self.log.info(" * Get current url: {0} . ".format(url))
        return url

    def window_max(self):
        """
        浏览器页面最大化
        Usage:
        driver.window_max()
        """

        self.driver.maximize_window()
        self.log.info(' * Set window size max .')

    def sleep(self,sec=1):
        """
        强制等待，默认 1s
        Usage:
        driver.sleep()
        """
        time.sleep(sec)
        # self.log.info(' * Webdriver sleep {0} seconds .'.format(sec))

    def wait(self,sec=20):
        """
        隐性等待,20秒内等待不到抛出错误

        driver.wait()
        """

        self.driver.implicitly_wait(sec)
        self.log.info(' * Wait page load...')

    def is_display(self,element):
        """
        判断页面元素是否可见
        Usage:
        driver.is_display("id->kw")
        """

        flag = False
        try:
            time.sleep(2)
            if self.get_element(element).is_displayed():
                self.log.info(' * Find element: {0} is true .'.format(element))
                flag = True
        except:
            raise Exception(' * Find element: {0} is false .'.format(element))
        finally:
            return flag

    def clear_input(self,element):
        """
        清除输入框
        Usage:
        driver.clear_input("id->kw")
        """

        self.wait_element(element)
        self.get_element(element).clear()
        self.log.info(' * Clear element: {0} .'.format(element))

    def input_message(self,element,message):
        """
        输入字段信息
        Usage:
        driver.input_message("id->kw","message")
        """

        try:
            self.wait_element(element)
            self.get_element(element).send_keys(message)
            self.log.info(' * Input message: {0} '.format(message))
        except Exception:
            self.log.error(' Unable input message: {0} ! '.format(message))
            raise

    def click_button(self,element):
        """
        点击页面按钮
        Usage:
        driver.click_button("id->kw")
        """

        try:
            self.wait_element(element)
            button = self.get_element(element)
            button.click()
            self.log.info(' * Click button: {0} .'.format(element))
        except:
            if self.is_display(self.get_element(element)):
                time.sleep(2)
                self.get_element(element).click()
            else:
                raise Exception(' Unable click button: {0} ! '.format(element))

    def get_text(self,element):
        """
        获取元素文本信息
        Usage:
        driver.get_text("id->kw")
        """

        try:
            self.wait_element(element)
            element_text = self.get_element(element).text
            self.log.info(' * Get element: {0} text: {1} .'.format(element,element_text))
            return element_text
        except:
            raise Exception(' Unable get element: {0} text .'.format(element))

    def get_att(self,element,attribute):
        """
        获取元素属性
        Usage:
        driver.get_att('xpath','attribute key')
        """

        try:
            self.wait_element(element)
            att = self.get_element(element).get_attribute(attribute)
            self.log.info(' * Get element: {0}, value: "{1}" attribute: "{2}" . '.format(element,attribute,att))
            return att
        except:
            raise Exception(' Unable get element: {0}, attribute by {1} .'.format(element,attribute))

    def roll_page_to_element(self,element):
        """
        页面滚动到某元素位置
        """
        element_place = self.get_element(element)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();",element_place)
            self.log.info(" * Execute js roll page to {0}.".format(element))
        except:
            raise Exception(" Unable execute js roll page to element .")

    def get_title(self):
        """
        获取网页标题信息
        Usage:
        driver.get_title()
        """

        try:
            title = self.driver.title
            self.log.info(' * Get window page title text .')
            return title
        except Exception:
            raise Exception(' Unable get window page title text .')

    def quit_browser(self):
        """
        退出浏览器
        Usage:
        driver.quit_browser()
        """

        self.driver.quit()
        self.log.info(' * Quit browser .')

    def close_page(self):
        """
        关闭页面
        Usage:
        driver.close_page()
        """

        self.driver.close()
        self.log.info(' * Close current window page .')

    def refresh_page(self):
        """
        刷新页面
        Usage:
        driver.refresh_page()
        """

        self.driver.refresh()
        self.log.info(' * Refresh current page .')

    def back_page(self):
        """
        返回上一个页面
        :return:
        """
        self.driver.back()

    def mouse_move_to_element(self,element):
        """
        鼠标移动到某元素按钮上
        Usage:
        driver.mouse_move_to_element("id->kw")
        """
        move_element = self.get_element(element)

        try:
            ActionChains(self.driver).move_to_element(move_element).perform()
            self.log.info(' * Move mouse to element: <{0}>  .'.format(element))
        except:
            raise Exception(' Unable move mouse to element: <{0}> and click.'.format(element))

    def mouse_move_and_click(self,element):
        """
        鼠标移动到某元素点击
        Usage:
        driver.mouse_move_and_click("id->kw")
        """
        move_element = self.get_element(element)

        try:
            ActionChains(self.driver).move_to_element(move_element).click().perform()
            self.log.info(' * Move mouse to element: {0} and click .'.format(element))
        except:
            raise Exception(' Unable move mouse to element: {0} and click.'.format(element))

    def mouse_double_click(self,element):
        """
        鼠标双击
        Usage:
        driver.mouse_double_click("id->kw")
        """
        double_click_element = self.get_element(element)

        try:
            ActionChains(self.driver).double_click(double_click_element).perform()
            self.log.info(' * Double click element: {0} .'.format(element))
        except:
            raise Exception(' Unable double click element: {0}.'.format(element))

    def mouse_right_click(self,element):
        """
        鼠标右键点击
        Usage:
        driver.mouse_right_click("id->kw")
        """
        click_element= self.get_element(element)

        try:
            ActionChains(self.driver).context_click(click_element).perform()
            self.log.info(' * Mouse right click element: {0} .'.format(element))
        except:
            raise Exception(' Unable right click element: {0}.'.format(element))

    def click_and_hold_btn(self,element):
        """
        点击并保持长按鼠标左键
        Usage:
        driver.click_and_hold_btn('xpath')
        """

        try:
            actions = ActionChains(self.driver)
            actions.click_and_hold(element).perform()
            self.log.info(' * Click element: {0} and hold on .'.format(element))
            return actions
        except Exception:
            raise Exception(' Unable click element: {0} and hold on .'.format(element))

    def roll_element_by_offset(self,x_offset,y_offset):
        """
        坐标移动按钮一般配合click_and_hold_btn一起使用
        Usage:
        click_and_hold_btn(xxx)->roll_element_by_offset(x,y)
        """

        try:
            # 实例化Actions
            actions = ActionChains(self.driver)
            # 按坐标移动元素
            actions.move_by_offset(x_offset,y_offset).perform()
            # 释放左键
            actions.release().perform()
            self.log.info(' * Move button from now place to [{0} {1}] offset place .'
                     .format(x_offset,y_offset))
        except Exception:
            raise Exception(' Can not move button to offset [{0} {1}].'.format(x_offset,y_offset))

    def get_all_handles(self):
        """
        获取所有的窗口handle
        Usage:
        driver.get_all_handles()
        """

        handles = self.driver.window_handles
        self.log.info(' Get all window handles in a list .')
        return handles

    def get_current_handle(self):
        """
        获取当前窗口的handle
        Usage:
        driver.get_current_handle()
        """

        current_handle = self.driver.current_window_handle
        self.log.info(' Get current window handle .')
        return current_handle

    def switch_to_new_handle(self,all_handles,old_handle):
        """
        切换页面新窗口, 需要先获取旧的窗口句柄和当前所有窗口的句柄列表
        :param all_handles 所有的窗口句柄列表
        :param old_handle  当前窗口的句柄
        Usage:
        driver.switch_to_new_handle()
        """

        try:
            for handle in all_handles:
                if handle != old_handle:
                    # 切换新窗口
                    self.driver.switch_to.window(handle)
                    self.log.info(' * Switch to window new handle: {0} .'.format(handle))
        except:
            raise Exception(' Unable switch to window handle .')

    def up_roll_page(self):
        """
        页面向上滑动
        Usage:
        driver.up_roll_page()
        """

        self.driver.execute_script("window.scrollBy(0,500)")
        self.log.info(' * Roll current page up .')

    def take_screen_shot(self):
        """
        截图
        Usage:
        driver.take_screen_shot()
        """

        name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + '.png'
        try:
            self.driver.get_screenshot_as_file(errorImagePath + name)
            self.log.info(' * Save screen shot to: {0} .'.format(errorImagePath + name))
        except:
            raise Exception(' Unable screen shot ! ')

    def operate_select(self,element,value=None,is_random=False):
        """
        操作select选择框，按文本选择或者随机选择
        :param element: select 元素位置路径
        :param value: option的文本信息
        :param is_random: 是否随机选择True/False关闭
        Usage:
        driver.operate_select()
        """

        # 因下单页面涉及select模块较多封装调用
        self.sleep(2)
        select_method = Select(self.get_element(element))
        try:
            if is_random:
                AllOption = self.get_element(element)
                options = AllOption.find_elements_by_tag_name('option')
                # 随机选择一个数字，选择该选项的索引
                chooseNum = random.randint(1,len(options)-1)
                select_method.select_by_index(chooseNum)
                # 返回一个该随机选择的文本值 all_selected_options 查看我选中的选项
                for select in select_method.all_selected_options:
                    self.log.info(' * Select value: {0} .'.format(select.text))
            else:
                select_method.select_by_visible_text(value)
                self.log.info(' * Select value: {0} .'.format(value))
        except:
            raise Exception(' Unable select value .')

    def get_now_time(self,Time=False):
        """
        获取当前时间 年-月-日 时：分：秒
        Usage:
        xxx.get_now_time()
        """
        if Time:
            timeType = '%Y-%m-%d %H:%M:%S'
        else:
            timeType = '%Y-%m-%d'
        return time.strftime(timeType,time.localtime(time.time()))

    def get_now_timenum(self):
        """
        获取当前时间的时间戳
        """
        return time.time()

    def get_one_timenum(self,DataTime,Time=False):
        """
        获取指定时间的时间戳
        """
        if Time:
            timeType = '%Y-%m-%d %H:%M:%S'
        else:
            timeType = '%Y-%m-%d'
        # 返回时间戳
        return time.mktime(time.strptime(DataTime,timeType))

    def get_element_count(self,parentEl,childEl='li'):
        """
        获取元素个数信息,返回列表包含：子元素合计个数/元素的列表
        :param parentEl 子元素的父亲元素位置
        :param childEl  子元素
        Usage:
        driver.get_element_count()
        """

        try:
            self.wait_element(parentEl)
            ParentPath = self.get_element(parentEl)
            ChildElList = ParentPath.find_elements_by_tag_name(childEl)
            count = len(ChildElList)
            # 定义一个空列表，把子元素的列表文本添加进去
            # text_list = []
            # for i in range(count):
            #     text_list.append(ChildElList[i])
            self.log.info(' * Get children element: {0} count are {1} .'.format(childEl,count))
            return count,ChildElList
        except:
            raise Exception(' Get element: {0} count is anomaly .'.format(childEl))

    def operate_not_select(self,open_el,parent_el,value=None,child_el='li',is_random=False):
        """
        操作不是select的下拉选择框封装
        :param OpenEl   点击打开选择框的元素位置
        :param ParentEl 总计子元素的父元素位置
        :param value    要选择的文本值
        :param ChildEl  选择项子元素
        :param Random   是否随机选择
        Usage:
        driver.operate_not_select()
        """

        # 点击打开选择框
        self.click_button(open_el)
        self.sleep(2)
        try:
            self.wait_element(parent_el)
            ParentPath = self.get_element(parent_el)
            ChildList = ParentPath.find_elements_by_tag_name(child_el)
            SelectNum = random.randint(1,len(ChildList))
            if is_random:
                self.sleep(2)
                ChildList[SelectNum-1].click()
                self.log.info(' * Select value: {0} by random choose .'.format(ChildList[SelectNum-1].text))
            else:
                for child in ChildList:
                    self.sleep(1)
                    if value in child.text:
                        child.click()
                        self.log.info(' * Select value: {0} .'.format(value))
                        break
                else:
                    raise NameError(" * '{0}' not find in select list ! ".format(value))
        except:
            raise Exception(' Select value is anomaly .'.format())

    def print_case_name(self,caseName):
        """
        打印用例名称
        """
        self.log.info("----------------------------- Cut Off Line -----------------------------")
        self.log.info(' * Load case name: 【{0}】'.format(caseName["用例名称"]))