# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/7 21:30

from public.common import basePages
from public.common.logConfig import logger
log = logger()

class BaiDuSearch(basePages.Page):

    searchInput = "id->kw"
    searchButton = "id->su"

    def open_baidu_url(self,url):
        self.driver.open_url(url,self.searchInput)
        log.info("打开网址：%s"%url)

    def input_text(self,value):
        self.driver.input(self.searchInput,value)
        log.info("输入搜索关键字：%s"%value)

    def click_search(self):
        self.driver.click(self.searchButton)
        log.info("点击 “搜索” 按钮")

    def get_title(self):
        """获取页面title"""
        self.driver.time_sleep(2)
        title = self.driver.get_title()
        log.info("获取页面title: {} ".format(title))
        return title