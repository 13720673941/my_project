# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:36

"""
webdriver类中操作浏览器方法二次封装
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from util.browserDriver import BrowserDriver


class PageAction(BrowserDriver):

    def find_element(self, elementPath, seconds=10):
        """查找页面元素"""
        if "=" not in elementPath:
            raise Exception("元素路径传入参数格式不正确：{} ！允许传入参数格式：id=kw ".format(elementPath))
        typeName = elementPath.split("=")[0]
        path = elementPath.split("=")[1]
        message = "{} 秒内在页面中没有找到该元素：{}".format(seconds, elementPath)
        wait = WebDriverWait(self.driver, seconds, 1)
        if typeName == "id":
            element = wait.until(EC.presence_of_element_located((By.ID, path)), message)
        elif typeName == "name":
            element = wait.until(EC.presence_of_element_located((By.NAME, path)), message)
        elif typeName == "class":
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, path)), message)
        elif typeName == "text":
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, path)), message)
        elif typeName == "css":
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, path)), message)
        elif typeName == "xpath":
            element = wait.until(EC.presence_of_element_located((By.XPATH, path)), message)
        else:
            raise Exception("传入的参数中定位方式字段不正确：{} ！允许传入字段：id, name, class, text, css, xpath".format(typeName))

        return element

    def open_url(self, url):
        """打开网页地址"""
        self.driver.get(url)

    def input_value(self, path, value):
        """输入一个值"""
        self.find_element(path).send_keys(value)

    def click_btn(self, path):
        """点击按钮"""
        self.find_element(path).click()

    def get_title(self):
        """获取网页title"""
        return self.driver.title


if __name__ == '__main__':

    import inspect

    caseDB = {
        "open_url": ["http://www.baidu.com"],
        "input_value": ["id=kw", "python"],
        "click_btn": ["id=su"]
    }

    def add():
        ls = inspect.stack()
        for i in ls[1]:
            print(i)

    add()
