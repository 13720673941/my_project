# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/12 9:13


from selenium.webdriver.common.by import By


class KeywordDB:

    # 定位元素方式对应by方法
    BY_DB = {
        "id": By.ID,
        "name": By.NAME,
        "class": By.CLASS_NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "text": By.LINK_TEXT,
        "tag_name": By.TAG_NAME
    }