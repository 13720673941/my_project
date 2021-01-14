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

    # 操作关键字对应方法字符串
    OPERATE_DB = {
        "打开浏览器": "open_browser",
        "打开网页": "open_url",
        "输入": "input_value",
        "点击": "click_btn",

    }