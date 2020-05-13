# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/14 15:24

from public.common.basePage import BasePage
from public.page.groupSearchPage import GroupSearchPage
from config.urlConfig import *

class VisitMemberPage(BasePage):

    """ 邀请圈子接单/派单成员页面 """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search = GroupSearchPage(driver)

    def get_elements(self,option):
        """获取页面元素配置文件"""
        return read_config_data("visit_group_member_page",option,elementDataPath)

    def click_visit_send_member(self,groupName):
        """点击邀请派单成员"""

        # 按名称搜索圈子
        self.search.search_by_name_main(groupName)
        # 点击邀请按钮
        self.click_button(self.get_elements("visit_send_member_btn"))

    def click_visit_take_member(self,groupName):
        """点击邀请接单成员"""

        # 按名称搜索圈子
        self.search.search_by_name_main(groupName)
        # 点击邀请按钮
        self.click_button(self.get_elements("visit_take_member_btn"))

    def input_member_search(self,memberName):
        """输入邀请成员名称搜索"""
        self.input_message(self.get_elements("friend_branch_input"),memberName)

    def click_search_member_btn(self):
        """点击搜索按钮搜索邀请成员"""
        self.click_button(self.get_elements("friend_branch_search_btn"))

    def get_search_member_info(self):
        """获取搜索后的派单成员的信息"""
        try:
            return self.get_text(self.get_elements("after_search_member_info"))
        except:
            return "Not find visit group member in list !"

    def select_visit_member(self,visitMemberList):
        """
        选择所要邀请的成员名称
        :param visitMemberList 字段类型必须是列表，可以选择多个成员邀请
        """

        # 判断参数类型
        if type(visitMemberList).__name__ != "list":
            raise TypeError(" 必须传入列表数据类型参数，例如：['xxx','xxx']")
        # 获取所有成员合计元素位置
        self.sleep(2)
        memberCount,memberList = self.get_element_count(parentEl=self.get_elements("all_friends_parent_element"))
        # 遍历成员列表
        clickCount = 0
        for i in range(1,memberCount+1):
            try:
                # 获取每个子元素的文本
                everyMemberInfo = self.get_text(self.get_elements("every_member_info_element").replace("+num+",str(i)))
                if everyMemberInfo in visitMemberList:
                    # 如果获取的成员名称再列表中点击选择框
                    self.click_button(self.get_elements("select_visit_member_input").replace("+num+",str(i)))
                    clickCount+=1
            except:
                raise TimeoutError(" 获取成员名称错误 ！")
            finally:
                if i == memberCount:
                    if clickCount != len(visitMemberList):
                        raise Exception(" 邀请列表中没有找到所要邀请的成员 !")
                else:
                    pass

    def click_prompt_visit_btn(self):
        """点击确认邀请按钮"""
        self.click_button(self.get_elements("confirm_visit_btn"))

    def input_send_count_of_month(self,sendCountMonth):
        """输入月派单量"""
        self.input_message(self.get_elements("month_send_count_input"),sendCountMonth)

    def select_settle_way(self,settleWay):
        """
        选择结算方式
        :param settleWay: 传入固定字段类型：按单结算、按周结算、按月结算
        """
        self.operate_select(self.get_elements("settle_way_parent_select"),settleWay)

    def click_confirm_visit_btn(self):
        """点击确认邀请按钮"""
        for i in range(1,3):
            try:
                self.click_button(self.get_elements("apply_for_confirm_btn").replace("+num+",str(i)))
                break
            except:
                if i == 2:
                    raise TimeoutError("没有找到确认申请的按钮 ！")
                else:
                    continue

    def input_take_count_of_day(self,takeCountDay):
        """输入日接单量"""
        self.input_message(self.get_elements("take_count_of_day_input"),takeCountDay)

    def select_service_brand(self,brandName):
        """
        选择服务品牌
        :param brandName 传入参数必须是列表，可以选择多个服务品牌信息
        """
        # 判断参数类型
        if type(brandName).__name__ != "list":
            raise TypeError(" 必须传入列表数据类型参数，例如：['xxx','xxx']")
        # 循环选择
        for brand in brandName:
            try:
                self.click_button(self.get_elements("select_take_service_brand").replace("+brand+",brand))
            except:
                raise TypeError(" 服务品牌中没有找到：{} ".format(brandName))

    def select_service_area(self,serviceArea):
        """
        选择服务区域，城市只能选择一个，区县可以选择多个
        :param serviceArea 默认数据类型为字典 如：{"城市":"西安市","区县":["未央区","莲湖区"]}
        """
        # 判断参数类型
        if type(serviceArea).__name__ != "dict":
            raise TypeError(' 必须传入字典数据类型参数，例如：{"城市":"西安市","区县":["未央区","莲湖区"]}')
        # 统计页面城市信息
        cityCount,cityList = self.get_element_count(parentEl=self.get_elements("service_city_parent"))
        # 遍历列表
        for i in range(cityCount):
            try:
                # 判断城市字段
                if cityList[i].text == serviceArea["城市"]:
                    if serviceArea["区县"] == "":
                        # 区县为空则为选择全部市区为服务区域
                        self.click_button(self.get_elements("service_city_input").replace("+num+",str(i+1)))
                    else:
                        # 否则点击城市名称显示出全部的区县列表信息
                        self.click_button(self.get_elements("service_city_for_area").replace("+num+",str(i+1)))
                    break
            except:
                if i == cityCount-1:
                    raise TimeoutError(" 圈子服务城市列表中没有找到选择的城市：{}".format(serviceArea["城市"]))
                else:
                    continue
        # 区县为空默认选择全部城市跳过
        if serviceArea["区县"] != "":
            # 统计页面区县信息
            self.sleep(2)
            areaCount,areaList = self.get_element_count(parentEl=self.get_elements("service_area_parent"))
            # 遍历列表
            for i in range(areaCount):
                try:
                    # 判断城市字段
                    if areaList[i].text in serviceArea["区县"]:
                        # 选择该城市
                        self.click_button(self.get_elements("service_area_input").replace("+num+",str(i+1)))
                except:
                    if i == areaCount-1:
                        raise TimeoutError(" 圈子服务城市列表中没有找到选择的区县：{}".format(serviceArea["区县"]))
                    else:
                        continue

    def enter_group_details(self,groupName):
        """进入圈子详情页"""
        self.click_button(self.get_elements("open_group_detail").replace("+groupName+",groupName))

    def get_send_member_list_names(self,groupName):
        """获取圈子详情页全部派单成员的名称返回一个列表：需要先搜索出圈子"""

        # 进入圈子详情页
        self.click_button(self.get_elements("open_group_detail").replace("+groupName+",groupName))
        # 点击派单方table
        self.click_button(self.get_elements("send_member_table_btn"))
        # 初始化成员列表
        senderMembers = []
        # 统计列表成员信息
        memberCount,memberLists = self.get_element_count(parentEl=self.get_elements("send_member_list_parent"),childEl="i")
        # 循环获取成员名称
        for i in range(memberCount):
            try:
                # 获取每个成员名称
                memberName = self.get_text(self.get_elements("send_member_name_element").replace("+num+",str(i+1)))
                # 添加到列表中
                senderMembers.append(memberName)
            except:
                if i == memberCount-1:
                    raise TimeoutError(" 获取派单方列表成员名称失败！")
                else:
                    continue
        return senderMembers

    def get_take_member_list_names(self,groupName):
        """获取圈子详情页全部接单成员的名称返回一个列表：需要先搜索出圈子"""

        # 进入圈子详情页
        self.click_button(self.get_elements("open_group_detail").replace("+groupName+",groupName))
        # 点击派单方table
        self.click_button(self.get_elements("take_member_table_btn"))
        self.sleep(2)
        # 初始化成员列表
        takerMembers = []
        # 统计列表成员信息
        memberCount,memberLists = self.get_element_count(parentEl=self.get_elements("take_member_list_parent"))
        # 循环获取成员名称
        for i in range(memberCount):
            try:
                # 获取每个成员名称
                memberName = self.get_text(self.get_elements("take_member_name_element").replace("+num+",str(i+1)))
                # 添加到列表中
                takerMembers.append(memberName)
            except:
                if i == memberCount-1:
                    raise TimeoutError(" 获取接单方列表成员名称失败！")
                else:
                    continue
        return takerMembers

    def visit_taker_member_main(self,groupName,member,takeCountDay,brandName,serviceArea):
        """邀请接单方主程序"""

        # 点击接单邀请
        self.click_visit_take_member(groupName)
        # 选择接单成员
        self.select_visit_member(member)
        # 点击立即邀请
        self.click_prompt_visit_btn()
        # 输入日接单量
        self.input_take_count_of_day(takeCountDay)
        # 选择服务品牌
        self.select_service_brand(brandName)
        # 选择服务区域
        self.select_service_area(serviceArea)
        self.sleep(1)
        # 点击确定邀请
        self.click_confirm_visit_btn()
        self.sleep(1)
        self.refresh_page()
        # # 获取详情页中派单方列表
        # takerMemberList = self.get_take_member_list_names(groupName)