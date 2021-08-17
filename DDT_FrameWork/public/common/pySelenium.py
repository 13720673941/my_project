# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 19:18

from selenium import webdriver
from config.pathConfig import *
from public.common.rwFile import RWFile
from public.common.logConfig import Log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time,datetime

"""
    webdriver 中方法的二次封装
"""
rwConfigData = RWFile()
log = Log()
browser = rwConfigData.read_config_file(CONFIG_DATA_PATH, "BROWSER", "BROWSER_TYPE")
driverPath = rwConfigData.read_config_file(CONFIG_DATA_PATH, "DRIVER_PATH", "path")

class PySelenium:

    def __init__(self,browserType=browser):
        """
        :param browserType: 浏览器驱动类型在configData文件夹中配置,默认谷歌浏览器
        :return:
        """
        # 初始化参数
        self.success = "SUCCESS "
        self.fail = "FAIL "
        # 判断浏览器类型
        if browserType.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path=driverPath)
        elif browserType.lower() == "firefox":
            self.driver = webdriver.Firefox()
        elif browserType.lower() == "internet explorer":
            self.driver = webdriver.Ie()
        else:
            raise NameError(
                "配置文件 config->configData.ini 中 browser->browserType 下参数写入有误！允许参数类型：chrome、firefox、internet explorer")
        # 浏览器最大化
        self.driver.maximize_window()
        log.info("{}打开浏览器：{}".format(self.success,browserType))

    def wait_element(self,elementPath,seconds=10):
        """
        :param elementPath: 页面元素路径表达式
        :param seconds:     等待元素加载时间
        Usage:
            xxx.wait_element("id->kw")
        """
        if "->" not in elementPath:
            raise TypeError("元素路径字段：{}类型传入有误！允许格式例如：id->kw".format(elementPath))
        # 分割元素路径字符串
        typeName = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        message = " {}秒内在页面中没有找到元素：{}".format(seconds,elementPath)
        # 等待页面加载元素，每1秒检查一次
        if typeName == "id":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.ID,path)),message)
        elif typeName == "name":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.NAME,path)),message)
        elif typeName == "class":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CLASS_NAME,path)),message)
        elif typeName == "xpath":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.XPATH,path)),message)
        elif typeName == "text":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.LINK_TEXT,path)),message)
        elif typeName == "css":
            WebDriverWait(self.driver,seconds,1).until(EC.presence_of_element_located((By.CSS_SELECTOR,path)),message)
        else:
            raise TypeError("路径类型：{}有误！允许传入类型：id、name、class、xpath、text、css ".format(typeName))

    def find_element(self,elementPath):

        if "->" not in elementPath:
            raise TypeError("元素路径字段：{}类型传入有误！允许格式例如：id->kw".format(elementPath))
        # 切割字符串获取 定位方式和元素路径
        typeName = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        # 获取页面元素
        if typeName == "id":
            element = self.driver.find_element_by_id(path)
        elif typeName == "name":
            element = self.driver.find_element_by_name(path)
        elif typeName == "class":
            element = self.driver.find_element_by_class_name(path)
        elif typeName == "xpath":
            element = self.driver.find_element_by_xpath(path)
        elif typeName == "text":
            element = self.driver.find_element_by_link_text(path)
        elif typeName == "css":
            element = self.driver.find_element_by_css_selector(path)
        else:
            raise TypeError("路径类型：{}有误！允许传入类型：id、name、class、xpath、text、css ".format(typeName))
        return element

    def open_url(self,url,path=None):
        """
        打开url地址
        :param url:  url地址参数
        :param path: 需要校验页面的元素
        :return:
        """
        # 判断是否需要校验页面元素是否存在
        if path != None:
            for i in range(5):
                try:
                    self.driver.get(url)
                    log.info("{}打开url地址：{}".format(self.success,url))
                    if self.find_element(path).is_displayed():
                        break
                except:
                    if i == 4:
                        log.error("{}Url：{}地址打开失败！".format(self.fail,url))
                    else:
                        self.driver.refresh()
        else:
            self.driver.get(url)
            log.info("{}打开url地址：{}".format(self.success,url))

    def set_window_max(self):
        """设置窗口最大化"""
        self.driver.maximize_window()
        log.info("{}设置浏览器窗口最大化".format(self.success))

    def set_window_size(self,width,height):
        """
        设置浏览器大小
        :param width:  宽度尺寸
        :param height: 高度尺寸
        """
        self.driver.set_window_size(width,height)
        log.info("{}设置浏览器尺寸：{}x{}".format(self.success,width,height))

    def refresh_page(self):
        """刷新页面"""
        self.driver.refresh()
        log.info("{}刷新当前页面".format(self.success))

    def back(self):
        """返回上一个页面"""
        self.driver.back()
        log.info("{}返回上一个页面".format(self.success))

    def implicitly_wait(self,seconds=10):
        """隐式等待"""
        self.driver.implicitly_wait(seconds)
        log.info("{}隐式等待 {}s ".format(self.success,seconds))

    def time_sleep(self,seconds):
        """显性等待死等"""
        time.sleep(seconds)
        log.info("{}等待 {}s ".format(self.success,seconds))

    def close(self):
        """关闭当前页面"""
        self.driver.close()
        log.info("{}关闭当前页面".format(self.success))

    def quit(self):
        """退出浏览器"""
        self.driver.quit()
        log.info("{}退出浏览器".format(self.success))

    def clear_input(self,path):
        """清除输入框"""
        try:
            self.wait_element(path)
            self.find_element(path).clear()
            log.info("{}清除输入框：<{}> 字段".format(self.success,path))
        except:
            log.error("{}清除输入框：<{}> 失败！！！".format(self.fail,path))
            raise

    def input(self,path,value):
        """
        输入一个字段信息
        :param path: 输入框元素路径
        :param value: 所要输入的参数信息
        Usage:
            xxx.input("id->kw","python")
        """
        try:
            self.wait_element(path)
            self.find_element(path).send_keys(value)
            log.info("{}输入字段：{}".format(self.success,value))
        except:
            log.error("{}输入字段：{}失败！！！".format(self.fail,value))
            raise

    def click(self,path):
        """
        点击页面按钮
        :param path: 按钮元素路径
        Usage:
            xxx.click("id->su")
        """
        try:
            self.wait_element(path)
            self.find_element(path).click()
            log.info("{}点击按钮：<{}> ".format(self.success,path))
        except:
            log.error("{}点击按钮：<{}> 失败！！！".format(self.fail,path))
            raise

    def right_click(self,path):
        """右键点击"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            # 使用ActionChains类中的context_click方法实现右键点击
            ActionChains(self.driver).context_click(el).perform()
            log.info("{}右键点击按钮：<{}>".format(self.success,path))
        except:
            log.error("{}右键点击按钮：<{}> 失败！！！".format(self.fail,path))
            raise

    def double_click(self,path):
        """左键双击按钮"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            # 使用ActionChains类中的double_click方法实现左键双击
            ActionChains(self.driver).double_click(el).perform()
            log.info("{}双击按钮：<{}> ".format(self.success,path))
        except:
            log.error("{}双击按钮：<{}> 失败！！！".format(self.fail,path))
            raise

    def drag_and_drop(self,path,target):
        """
        长按拖拽按钮从某元素到另一个元素
        :param path: 需要长安的按钮
        :param target: 拖拽到的元素
        Usage:
            xxx.drag_and_drop("id->kw","id->su")
        """
        try:
            self.wait_element(path)
            element = self.find_element(path)
            self.wait_element(target)
            ta_element = self.find_element(target)
            ActionChains(self.driver).drag_and_drop(element,ta_element).perform()
            log.info("{}长按拖拽按钮：<{}> 移动到按钮：<{}> ".format(self.success,path,target))
        except:
            log.error("{}长按拖拽按钮：<{}> 移动到按钮：<{}> 失败！！！".format(self.fail,path,target))
            raise

    def click_hold_on(self,path):
        """点击长按按钮"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            ActionChains(self.driver).click_and_hold(el).perform()
            log.info("{}长按按钮：<{}> ".format(self.success,path))
        except:
            log.error("{}长按按钮：<{}> 失败！！！".format(self.fail,path))
            raise

    def move_and_click(self,path):
        """移动到某元素上并点击"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            ActionChains(self.driver).move_to_element(el).click().perform()
            log.info("{}鼠标移动到按钮：<{}> 上并点击 ".format(self.success,path))
        except:
            log.error("{}鼠标移动到按钮：<{}> 上并点击失败！！！".format(self.fail,path))
            raise

    def submit(self,path):
        """提交"""
        try:
            self.wait_element(path)
            self.find_element(path).submit()
            log.info("{}提交".format(self.success))
        except:
            log.error("{}提交失败！！！".format(self.fail))
            raise

    def get_title(self):
        """获取页面title"""
        try:
            title = self.driver.title
            log.info("{}获取页面title：{}".format(self.success,title))
            return title
        except:
            log.error("{}获取页面title失败！！！".format(self.fail))
            raise

    def get_text(self,path):
        """获取页面元素的文本信息"""
        try:
            self.wait_element(path)
            text = self.find_element(path).text
            log.info("{}获取元素<{}>文本：{}".format(self.success,path,text))
            return text
        except:
            log.error("{}获取元素<{}>文本失败！！！".format(self.fail,path))
            raise

    def get_attribute(self,path,attName):
        """获取元素标签的属性"""
        try:
            self.wait_element(path)
            att = self.find_element(path).get_attribute(attName)
            log.info("{}获取元素<{}> “{}” 属性：{}".format(self.success,path,attName,att))
            return att
        except:
            log.error("{}获取元素<{}> “{}” 属性失败！！！".format(self.fail,path,attName))
            raise

    def get_current_url(self):
        """获取当前页面的url"""
        url = self.driver.current_url
        log.info("{}获取当前页面url：{}".format(self.success,url))
        return url

    def accept_alert(self):
        """接受页面警告弹窗"""
        self.driver.switch_to.alert.accept()
        log.info("{}接受警告弹窗".format(self.success))

    def dismiss_alert(self):
        """取消弹窗"""
        self.driver.switch_to.alert.dismiss()
        log.info("{}取消警告弹窗".format(self.success))

    def switch_to_frame(self,path):
        """切换到 iframe 框"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            self.driver.switch_to.frame(el)
            log.info("{}切换到frame：<{}>层".format(self.success,path))
        except:
            log.error("{}切换到frame层失败！！！".format(self.fail))
            raise

    def switch_out_frame(self):
        """切换出iframe"""
        self.driver.switch_to.default_content()
        log.info("{}切换出frame层".format(self.success))

    def execute_js(self,script):
        """执行 js 脚本"""
        self.driver.execute_script(script)
        log.info("{}执行js脚本：{}".format(self.success,script))

    def switch_new_page(self,path):
        """点击按钮打开信页面且切换到新页面"""

        current_handle = self.driver.current_window_handle
        self.click(path)
        for handle in self.driver.window_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                log.info("{}切换到新打开页面".format(self.success))
        pass

    def use_of_key(self,path,keyName):
        """
        键盘的使用,其他所想使用的键盘操作需添加到keyDict中
        :param path:  元素路径
        :param keyName: keyDict中键盘键的名称字段
        :return:
        """
        keyDict = {
            "enter":Keys.ENTER,"back_space":Keys.BACK_SPACE,
            "space":Keys.SPACE,"":Keys.F5
        }
        if keyName not in keyDict.keys():
            raise NameError("键盘对应字典中没有找到所要点击的键字段，请在'keyDict'中添加后在使用...")
        try:
            self.wait_element(path)
            self.find_element(path).send_keys(keyDict[keyName])
            log.info("{}使用键盘：{}键操作".format(self.success,keyName))
        except:
            log.error("{}使用键盘：{}键操作失败！！！".format(self.fail,keyName))
            raise

    def screen_shot(self):
        """截图功能"""
        imgName = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".png"
        self.driver.get_screenshot_as_file(filename=ERROR_IMG_PATH+imgName)
        log.info("{}错误截图：{}".format(self.success,ERROR_IMG_PATH+imgName))

    def operate_select_by_text(self,path,text):
        """select下拉框文本选择"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            Select(el).select_by_visible_text(text)
            log.info("{}下拉选择文本：{}".format(self.success,text))
        except:
            log.error("{}下拉选择文本：“{}” 失败！！！".format(self.fail,text))
            raise

    def operate_select_by_index(self,path,index):
        """select下拉框索引选择"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            Select(el).select_by_index(index)
            log.info("{}下拉选择索引：{}".format(self.success,index))
        except:
            log.error("{}下拉选择索引：“{}” 失败！！！".format(self.fail,index))
            raise

    def operate_select_by_option(self,path,value):
        """select 下拉框value值选择"""
        try:
            self.wait_element(path)
            el = self.find_element(path)
            Select(el).select_by_value(value)
            log.info("{}下拉选择value：{}".format(self.success,value))
        except:
            log.error("{}下拉选择value：“{}” 失败！！！".format(self.fail,value))
            raise

    @property
    def origin_driver(self):
        """返回原生driver"""
        return self.driver


if __name__ == '__main__':

    py = PySelenium()
    py.open_url("https://www.baidu.com")

