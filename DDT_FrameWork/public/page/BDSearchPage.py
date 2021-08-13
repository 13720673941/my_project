# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/7 21:30

from public.common import basePages
from config.urlConfig import *

"""
    百度搜索页面操作封装
"""

class BaiDuSearch(basePages.Page):

    searchInput = "id->kw"
    searchButton = "id->su"

    def open_baidu_url(self):
        self.driver.open_url(BAI_DU_SEARCH,self.searchInput)

    def input_text(self,value):
        self.driver.input(self.searchInput,value)

    def click_search(self):
        """点击搜索按钮"""
        self.driver.click(self.searchButton)

    def get_title(self):
        """获取页面title"""
        self.driver.time_sleep(5)
        return self.driver.get_title()