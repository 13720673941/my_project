# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/31 19:18

from public.common.logConfig import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

"""
    webdriver 中操作的二次封装
"""

class BasePage():

    def __init__(self,driver):
        self.log = logger()
        self.driver = driver

    def wait_element(self,elementPath,seconds=10):
        """
        :param elementPath: 页面元素路径表达式
        :param seconds:     等待元素加载时间
        :return:
        Usage: wait_element("id->kw")
        """
        if "->" not in elementPath:
            raise TypeError("元素路径字段：{} 类型传入有误！允许格式例如：id->kw".format(elementPath))
        # 分割元素路径字符串
        typeName = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        message = " {} 秒内在页面中没有找到元素：{}".format(seconds,elementPath)
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
            raise TypeError("路径类型：{} 有误！允许传入类型：id、name、class、xpath、text、css ".format(typeName))

    def get_element(self,elementPath):

        if "->" not in elementPath:
            raise TypeError("元素路径字段：{} 类型传入有误！允许格式例如：id->kw".format(elementPath))
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
            raise TypeError("路径类型：{} 有误！允许传入类型：id、name、class、xpath、text、css ".format(typeName))
        return element

    




if __name__ == '__main__':

    from selenium import webdriver

    d = webdriver.Chrome()
    d.get("https://www.baidu.com")
    b = BasePage(d)

    searchInput = "id-ks"
    b.wait_element(elementPath=searchInput)


