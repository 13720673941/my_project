# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/14 10:01

from public.common.basePage import BasePage
from config.urlConfig import *

class GroupSearchPage(BasePage):

    """ 我创建的圈子页面列表：搜索功能页面元素 """

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def get_elements(self,option):
        """获取页面元素配置文件"""
        return read_config_data("my_group_search_page",option,elementDataPath)

    def enter_my_group_list_page(self):
        """进入我创建的圈子列表页面"""
        self.open_url(my_create_group_list,self.get_elements("search_by_name_input"))

    def input_group_name_search(self,groupName):
        """输入圈子名称搜索"""
        self.input_message(self.get_elements("search_by_name_input"),groupName)

    def select_service_area_search(self,serviceArea):
        """
        选择服务区域搜索
        :param serviceArea 传入参数必须是固定格式类型如： {"省份":"陕西省","城市":"西安市"}
        """

        # 解析字段格式
        if type(serviceArea).__name__ != "dict":
            raise TypeError('传入字段类型错误，必须是字典格式，如：{"省份":"xxx","城市":"xxx"} ')
        # 选择省份和城市
        if serviceArea["省份"] != "":
            self.operate_select(self.get_elements("search_by_province_select"),serviceArea["省份"])
            self.sleep(1)
            if serviceArea["城市"] != "":
                self.operate_select(self.get_elements("search_by_city_select"),serviceArea["城市"])

    def select_service_type_search(self,serviceType):
        """
        选择服务类型
        :param serviceType 固定系统默认的几个服务类型选择
        """
        if serviceType != "":
            self.operate_select(self.get_elements("search_by_type_select"),serviceType)

    def select_service_brand_search(self,serviceBrand):
        """
        选择服务品牌
        :param serviceBrand 固定选择系统服务品牌字段
        """
        if serviceBrand != "":
            self.operate_select(self.get_elements("search_by_brands_select"),serviceBrand)

    def select_service_kind_search(self,serviceKind):
        """
        选择服务品类
        :param serviceKind: 固定选择系统服务品类字段
        """
        if serviceKind != "":
            self.operate_select(self.get_elements("search_by_kinds_select"),serviceKind)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_button(self.get_elements("search_btn"))

    def get_after_search_info(self):
        """获取搜索后的第一条信息"""
        try:
            return self.get_text(self.get_elements("after_search_group_info"))
        except:
            return "Not find group in page !"

    def search_by_name_main(self,groupName):
        """搜索主程序 使用圈子名称搜索"""

        self.log.info("-=【搜索圈子】=-")
        # 进入圈子列表页面
        self.enter_my_group_list_page()
        # 输入圈子名称
        self.input_group_name_search(groupName)
        self.click_search_btn()
        self.sleep(1)
        if groupName in self.get_after_search_info():
            self.log.info(" ** Search group: {} success !".format(groupName))
        else:
            raise TimeoutError(" ** Not find group: {} in list !".format(groupName))