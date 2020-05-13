# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/16 17:00

from public.common.basePage import BasePage
from public.page.groupSearchPage import GroupSearchPage
from public.page.visitMemberPage import VisitMemberPage
from config.urlConfig import *
import re

class EditGroupPage(BasePage):

    """
    编辑圈子页面操作：
    设置起收单数、收费规则-免费/金额/比例、派单方式、接单优先级、日接单数量、结算方式、删除派单/接单方、解散圈子
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search_group = GroupSearchPage(driver)
        self.visit_member = VisitMemberPage(driver)

    def get_elements(self,option):
        """获取编辑圈子页面的元素"""
        return read_config_data("edit_my_group_page",option,elementDataPath)

    def enter_my_group_list_page(self):
        """进入我创建的圈子列表页面"""
        self.search_group.enter_my_group_list_page()

    def enter_join_group_list_page(self):
        """进入我加入的圈子列表页"""
        self.open_url(group_list_my_join)

    def click_edit_group_btn(self,groupName):
        """
        点击圈子编辑按钮-> 只能再搜索之后使用
        :param groupName:  圈子名称
        """
        # 输入圈子名称搜索圈子
        self.search_group.input_group_name_search(groupName)
        self.search_group.click_search_btn()
        self.sleep(2)
        # 点击编辑按钮
        self.click_button(self.get_elements("edit_group_btn"))

    def get_wait_for_charge(self):
        """获取圈子详情页待收款金额数量"""
        try:
            return float(self.get_text(self.get_elements("will_take_service_charge")))
        except:
            return 0

    def get_already_take_charge(self):
        """获取圈子详情页实际收取的服务费金额"""
        try:
            return float(self.get_text(self.get_elements("already_take_service_charge")))
        except:
            return 0

    def click_process_node_table(self):
        """点击过程节点table"""
        for i in range(1,4):
            try:
                self.click_button(self.get_elements("process_node_table").replace("+num+",str(i)))
                break
            except:
                if i == 3:
                    raise TimeoutError("没有找到过程节点按钮")
                else:
                    continue

    def get_new_process_node_info(self):
        """过去最新过程节点信息->解析文本获取网点名称和手机号"""

        # 获取最新过程节点信息
        nodeInfo = None
        self.sleep(1)
        for i in range(1,4):
            try:
                nodeInfo = self.get_text(self.get_elements("new_node_info").replace("+num+",str(i)))
                break
            except:
                if i == 3:
                    raise TimeoutError("没有找到过程节点按钮")
                else:
                    continue
        return nodeInfo
        # # 创建正则表达式
        # regex = re.compile(r"指派给 (.*?)\）")
        # try:
        #     # 解析字段
        #     response = regex.findall(nodeInfo)[0].split("（")
        #     if len(response) != 0:
        #         return {"网点名称":response[0],"手机号码":response[1]}
        #     else:
        #         raise Exception(" 获取文本正则提取数据为空：{}".format(nodeInfo))
        # except:
        #     raise Exception( "字符串: {} 分割异常".format(regex.findall(nodeInfo)))

    def enter_group_order_market_page(self):
        """进入圈子抢单市场页面"""
        self.open_url(group_order_of_market_url,self.get_elements("group_grad_page_table"))

    def set_take_count_of_day(self,memberName,takeCount):
        """
        设置日接单量
        :param memberName: 需设置接单量成员的名称
        """
        # 获取全部接单成员信息
        memberCount,memberList = self.get_element_count(
            parentEl=self.get_elements("priority_list_parent"),childEl="tr")
        # 日接单输入框
        takeInput = self.get_elements("take_order_of_day_input")
        # 遍历列表
        for i in range(memberCount):
            try:
                # 判断所设置的成员名称在哪一行
                if memberName in memberList[i].text:
                    try:
                        # 清空接单数据重新输入
                        self.clear_input(takeInput.replace("+num+",str(i+1)))
                        self.input_message(takeInput.replace("+num+",str(i+1)),takeCount)
                    except:
                        raise TimeoutError(" 输入日结单量失败，获取输入框超时 ！")
                    break
            except:
                if i == memberCount-1:
                    raise TimeoutError(" 接单列表中没有找到成员：{}".format(memberName))
                else:
                    continue

    def set_take_order_priority(self,memberName):
        """
        设置接单成员的优先级->默认设置成员第一优先级
        :param memberName: 接单成员名称
        """
        # 获取全部接单成员信息
        memberCount,memberList = self.get_element_count(
            parentEl=self.get_elements("priority_list_parent"),childEl="tr")
        # 遍历列表判断第一个是否为所要设置的成员否则点击上移
        for i in range(memberCount):
            try:
                # 获取第一个成员信息
                firstMemberInfo = self.get_text(self.get_elements("first_take_member_info"))
                if memberName not in firstMemberInfo:
                    # 判断当前成员在第几行
                    number = None
                    for info in memberList:
                        if memberName in info.text:
                            number = memberList.index(info)
                            break
                    # 判断不是第一个点击移动
                    self.click_button(self.get_elements("set_sequence_btn").replace("+num+",str(number+1)))
                else:
                    break
            except:
                if i == memberCount-1:
                    raise TimeoutError(" 设置接单成员: {} 优先级失败 ！".format(memberName))
                else:
                    continue

    def del_send_order_member(self,memberName):
        """
        删除派单方 默认删除一个
        :param memberName: 派单方名称
        """
        # 获取派单方列表所有成员信息
        count,eList = self.get_element_count(parentEl=self.get_elements("send_order_member_parent"),childEl="tr")
        # 遍历列表判断在第几行
        for i in range(count):
            try:
                everyRowInfo = self.get_text(self.get_elements("send_order_member_row_info").replace("+num+",str(i+1)))
                if memberName in everyRowInfo:
                    # 找到行数点击删除
                    self.click_button(self.get_elements("del_send_member_btn").replace("+num+",str(i+1)))
                    # 点击确认删除
                    self.click_button(self.get_elements("confirm_del_btn"))
                    break
            except:
                if i == count-1:
                    raise TimeoutError(" 列表中没有找到所要删除的派单成员：{}".format(memberName))
                else:
                    continue

    def del_take_order_member(self,memberName):
        """
        删除接单方 默认删除一个
        :param memberName: 接单方名称
        """
        # 获取接单方列表所有成员信息
        count,eList = self.get_element_count(parentEl=self.get_elements("take_order_member_parent"),childEl="tr")
        # 遍历列表判断在第几行
        for i in range(count):
            try:
                everyRowInfo = self.get_text(self.get_elements("take_order_member_row_info").replace("+num+",str(i+1)))
                if memberName in everyRowInfo:
                    # 找到行数点击删除
                    self.click_button(self.get_elements("del_take_member_btn").replace("+num+",str(i+1)))
                    # 点击确认删除
                    self.click_button(self.get_elements("confirm_del_btn"))
                    break
            except:
                if i == count-1:
                    raise TimeoutError(" 列表中没有找到所要删除的接单成员：{}".format(memberName))
                else:
                    continue

    # def get_all_send_order_member(self):
    #     """获取派单成员列表中的全部数据->用来判断是否删除成功"""
    #
    #     sendMemberList = []
    #     # 获取派单方列表所有成员信息
    #     try:
    #         count,eList = self.get_element_count(
    #             parentEl=self.get_elements("send_order_member_parent"),childEl="tr")
    #         # 遍历列表添加数据到列表中
    #         for member in eList:
    #             sendMemberList.append(member.text)
    #     except:
    #         sendMemberList = None
    #     finally:
    #         return sendMemberList

    # def get_all_take_order_member(self):
    #     """获取接单成员列表中的全部数据->用来判断是否删除成功"""
    #
    #     takeMemberList = []
    #     # 获取接单方列表所有成员信息
    #     try:
    #         count,eList = self.get_element_count(
    #             parentEl=self.get_elements("take_order_member_parent"),childEl="tr")
    #         # 遍历列表添加数据到列表中
    #         for member in eList:
    #             takeMemberList.append(member.text)
    #     except:
    #         takeMemberList = None
    #     finally:
    #         return takeMemberList

    def open_group_details(self,groupName):
        """进入圈子详情页"""
        self.click_button(self.get_elements("open_group_details").replace("+groupName+",groupName))

    def click_group_transfer(self):
        """点击圈子转移"""
        self.click_button(self.get_elements("transfer_group_manager_btn"))

    def select_member_for_leader(self,MemberName):
        """选择转移圈主的名称"""
        self.click_button(self.get_elements("select_member_for_leader").replace("+MemberName+",MemberName))

    def click_confirm_transfer(self):
        """点击确认转移圈主"""
        self.click_button(self.get_elements("confirm_transfer_btn"))

    def click_quit_group_btn(self):
        """点击退出圈子按钮"""
        self.click_button(self.get_elements("quit_group_btn"))
        self.sleep(1)
        # 点击确认
        self.click_button(self.get_elements("confirm_del_btn"))

    def click_break_up_group(self):
        """点击解散圈子"""
        self.click_button(self.get_elements("break_up_group_btn"))
        # 确认解散
        self.click_button(self.get_elements("confirm_del_btn"))

    def click_save_edit_btn(self):
        """点击保存按钮"""
        self.click_button(self.get_elements("save_group_set_btn"))