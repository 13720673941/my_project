#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/5 17:08

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
from public.page.searchOrderPage import SearchOrderPage
from config.urlconfig import *
log=Log()

class FinishOrder(BasePage):
    """
    网点完成工单页面
    """
    
    # 完成工单按钮
    finish_order_btn = (By.XPATH,'//a[text()="完成服务"]')
    # 故障类型输入框
    break_type_input = (By.XPATH,'//input[@placeholder="请输入故障类型"]')
    # 师傅预约时间输入框
    master_order_time_input = (By.XPATH,'//input[@placeholder="请选择师傅预约日期"]')
    # 师傅上门时间输入框
    master_door_time_input = (By.XPATH,'//input[@placeholder="请选择师傅上门时间"]')
    # 师傅完成时间输入框
    master_finish_time_input = (By.XPATH,'//input[@placeholder="请选择师傅完成时间"]')
    # 完成服务备注
    remark_input = (By.XPATH,'//label[text()="服务反馈："]/following-sibling::textarea')
    # 上传图片输入框
    update_picture_input = (By.XPATH,'//input[@type="file"]')
    # 完成服务提交按钮
    finish_order_confirm_btn = (By.XPATH,'//button[text()="提交"]')
    # 上传图片父路(判断上传图片的个数)
    parent_up_picture = (By.XPATH,'//label[text()="服务照片："]/../div')

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.search_page = SearchOrderPage(driver)

    def enter_finish_order_page(self):
        """进入完成工单列表页"""
        self.open_url(servicing_order_list_url)

    def click_finish_btn(self):
        """点击完成工单按钮"""
        self.click_button(self.finish_order_btn)

    def input_break_type(self):
        """输入故障类型"""
        self.input_message(self.break_type_input,self.get_now_time(Time=True))

    def input_master_orderTime(self,orderTime):
        """输入师傅预约时间"""
        self.input_message(self.master_order_time_input,orderTime)

    def input_master_doorTime(self,doorTime):
        """输入师傅上门时间"""
        self.input_message(self.master_door_time_input,doorTime)

    def input_master_finishTime(self,finishTime):
        """输入师傅完成时间"""
        self.input_message(self.master_finish_time_input,finishTime)

    def input_remark(self):
        """输入备注"""
        self.input_message(self.remark_input,self.get_now_time(Time=True))

    def up_finish_picture(self,upLoading='True'):
        """上传图片"""
        if upLoading == 'True':
            # 获取上传图片个数
            PictureNum,PictureList = self.get_element_count(parentEl=self.parent_up_picture,childEl='dl')
            # 上传图片
            self.up_loading_picture(PictureNum,self.update_picture_input)

    def click_submit_btn(self):
        """点击提交按钮"""
        self.click_button(self.finish_order_confirm_btn)

    def finish_order_main(self,ordernumber):
        """
        :param OrderTime:   师傅预约时间
        :param DoorTime:    上门时间
        :param FinishTime:  完工时间
        :param UpLoading:   是否上传图片
        :return:
        """
        # """网点完成服务"""
        log.info('-=【网点完成服务】=-')
        # 进入完工订单列表页面
        self.enter_finish_order_page()
        # 刷新页面
        self.refresh_page()
        self.sleep(2)
        # 搜索订单
        self.search_page.search_order_by_number(ordernumber)
        # 选择工单
        self.select_new_order(ordernumber)
        # 点击订单列表完成服务按钮
        self.click_finish_btn()
        self.sleep(1)
        # 输入故障类型
        self.input_break_type()
        # 输入师傅预约时间
        self.input_master_orderTime(self.get_now_time())
        # 输入师傅上门时间
        self.input_master_doorTime(self.get_now_time())
        self.sleep(1)
        # 输入师傅完成服务时间
        self.input_master_finishTime(self.get_now_time())
        # 输入备注
        self.input_remark()
        # 上传图片
        self.up_finish_picture()
        self.sleep(2)
        # 点击提交
        self.click_submit_btn()
        # 判断
        if self.get_system_msg() == '操作成功':
            log.info('{0} ** Finish order is success！'.format(self.success))
        else:
            log.error('{0} ** Finish order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))