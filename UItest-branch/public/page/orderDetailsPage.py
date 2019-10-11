#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/7/5 14:11

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime

class OrderDetailsPage(BasePage):
    """
    订单详情页面
    """

    # 预约订单按钮
    appoint_order_btn = (By.XPATH,'//button[contains(.,"预约")]')
    # 改约订单按钮
    alter_appoint_time_btn = (By.XPATH,'//button[contains(.,"改约")]')
    # 清除预约日期
    appoint_date_clear = (By.XPATH,'//label[text()="预约日期："]/../div/div/div/i')
    # 预约日期输入框
    appoint_time_input = (By.XPATH,'//input[@placeholder="选择起始日期"]')
    # 预约时间打开下拉按钮
    open_appoint_select = (By.XPATH,'//label[contains(.,"预约时间：")]/../div/div/span[1]')
    # 下拉时间段的统计父目录
    parent_for_select = (By.XPATH,'//div[contains(text(),"预约时间")]/../../../../../preceding-sibling::div[1]/ul[2]')
    # 确定预约按钮
    confirm_appoint_btn = (By.XPATH,'//div[contains(text(),"预约时间")]/../../div[3]/button[2]')
    # 预约后详情页有预约字段
    appoint_time_text = (By.XPATH,'//label[text()="预约上门时间："]/../div')
    # 修改工单按钮
    alter_order_btn = (By.XPATH,'//button[contains(.,"修改工单")]')
    # 订单详情页修改订单手机号的字段
    order_info_of_pheNum = (By.XPATH,'//label[text()="联系方式："]/../div')
    # 催单按钮
    cui_order_btn = (By.XPATH,'//button[contains(.,"催单")]')
    # 催单反馈输入框
    cui_reason_input = (By.XPATH,'//label[text()="催单内容："]/.././/textarea')
    # 催单确定按钮
    confirm_cui_button = (By.XPATH,'//div[contains(text(),"催单内容")]/../../div[3]/button[2]')
    # 催单校验字
    order_info_of_cui = (By.XPATH,'//label[text()="服务反馈："]/../div')
    # 详情页新建工单
    new_create_order_btn = (By.XPATH,'//button[contains(.,"新建工单")]')
    # 打印工单按钮
    print_order_btn = (By.XPATH,'//button[contains(.,"打印工单")]')
    # 点击空白关闭日期框
    white_place = (By.XPATH,'(//label[contains(.,"预约日期：")])[3]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_appoint_btn(self):
        """点击预约按钮"""
        self.click_button(self.appoint_order_btn)

    def click_alter_appoint_btn(self):
        """点击修改预约按钮"""
        self.click_button(self.alter_appoint_time_btn)

    def clear_appoint_date(self):
        """清除预约日期"""
        self.mouse_move_and_click(self.appoint_date_clear)

    def input_appoint_date(self,alter=False):
        """输入预约日期"""
        if alter:
            appoint_date = str(datetime.datetime.now().date() + datetime.timedelta(1))
        else:
            appoint_date = self.get_now_time()
        self.input_message(self.appoint_time_input,appoint_date)

    def select_appoint_time(self,appoint_time):
        """随机选择预约时间段"""
        if appoint_time != '':
            self.operate_not_select(self.open_appoint_select,self.parent_for_select,is_random=True)

    def click_confirm_appoint_btn(self):
        """点击确定预约按钮"""
        self.click_button(self.confirm_appoint_btn)

    def get_appoint_text(self):
        """获取订单详情的预约字段，判断预约成功"""
        return self.get_text(self.appoint_time_text)

    def click_alter_order_btn(self):
        """点击修改订单按钮"""
        self.click_button(self.alter_order_btn)

    def get_alter_text_of_order(self):
        """获取修改订单的字段验证"""
        return self.get_text(self.order_info_of_pheNum)

    def click_cui_order_btn(self):
        """点击催单按钮"""
        self.click_button(self.cui_order_btn)

    def input_cui_of_reason(self,cui):
        """输入催单原因"""
        if cui != '':
            self.clear_input(self.cui_reason_input)
            self.input_message(self.cui_reason_input,"cui {0}".format(self.get_now_time(Time=True)))

    def click_confirm_cui_order(self):
        """点击确定催单"""
        self.click_button(self.confirm_cui_button)

    def get_cui_text_of_order(self):
        """获取订单详情页催单验证字段"""
        return self.get_text(self.order_info_of_cui)

    def click_new_create_btn(self):
        """点击新建工单"""
        self.click_button(self.new_create_order_btn)

    def click_print_order_btn(self):
        """点击打印工单按钮"""
        self.click_button(self.print_order_btn)

    def click_white_place(self):
        """点击空白区域"""
        self.click_button(self.white_place)