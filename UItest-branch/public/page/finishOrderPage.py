#  -*- coding: utf-8 -*-

#  @Author  : Mr.Deng
#  @Time    : 2019/6/5 17:08

from public.common.basePage import BasePage
from public.page.loginPage import LoginPage
from public.page.searchOrderPage import SearchOrderPage
from public.page.createOrderPage import CreateOrderPage
from config.urlConfig import *
from config.pathConfig import *

class FinishOrder(BasePage):
    """
        【网点完成工单页面】
    """

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.login = LoginPage(driver)
        self.create_order = CreateOrderPage(driver)
        self.search_order = SearchOrderPage(driver)

    def get_elements(self,option):
        """获取element_data文件中完成工单服务页面的元素信息"""
        return read_config_data("finish_order_page",option,elementDataPath)

    def enter_serving_order_page(self):
        """进入完成工单列表页"""
        self.open_url(servicing_order_list_url,self.get_elements("finish_order_btn"))

    def enter_finish_order_page(self):
        """进入完成服务工单列表页面"""
        self.open_url(wait_visit_order_url)

    def click_finish_btn(self):
        """点击完成工单按钮"""
        self.click_button(self.get_elements("finish_order_btn"))

    def input_break_type(self):
        """输入故障类型"""
        self.input_message(self.get_elements("break_type_input"),self.get_now_time(Time=True))

    def input_master_orderTime(self,orderTime):
        """输入师傅预约时间"""
        self.input_message(self.get_elements("master_order_time_input"),orderTime)

    def input_master_doorTime(self,doorTime):
        """输入师傅上门时间"""
        self.input_message(self.get_elements("master_door_time_input"),doorTime)

    def input_master_finishTime(self,finishTime):
        """输入师傅完成时间"""
        self.input_message(self.get_elements("master_finish_time_input"),finishTime)

    def input_remark(self):
        """输入备注"""
        self.input_message(self.get_elements("remark_input"),self.get_now_time(Time=True))

    def up_finish_picture(self,upLoading='True'):
        """上传图片"""

        if upLoading == 'True':
            self.sleep(2)
            # 获取上传图片个数
            PictureNum,PictureList = self.get_element_count(
                parentEl=self.get_elements("parent_up_picture"),childEl='dl')
            # 上传图片
            # 加载图片列表
            Plist = os.listdir(picturePath)
            # 循环上传
            for i in range(1,PictureNum+1):
                try:
                    Picture = picturePath + Plist[i]
                    # 上传图片的元素位置
                    element = self.get_elements("update_picture_input").replace("+i+",str(i))
                    self.sleep(1)
                    self.input_message(element,message=Picture)
                    self.log.info(' * Uploading picture: {0} . '.format(Picture))
                except:
                    raise Exception(' Uploading is anomaly ! ')

    def click_submit_btn(self):
        """点击提交按钮"""
        self.click_button(self.get_elements("finish_order_confirm_btn"))

    def get_finish_order_text(self):
        """获取订单状态字段"""
        return self.get_text(self.get_elements("finish_order_status"))

    def finish_order_main(self,ordernumber):
        """
        :param OrderTime:   师傅预约时间
        :param DoorTime:    上门时间
        :param FinishTime:  完工时间
        :param UpLoading:   是否上传图片
        :return:
        """

        self.log.info('-=【网点完成服务】=-')
        # 进入完工订单列表页面
        self.enter_serving_order_page()
        # 刷新页面清除数据
        self.refresh_page()
        self.sleep(2)
        # 搜索订单
        self.search_order.search_order_by_number(ordernumber)
        # 选择工单
        self.create_order.select_operate_order(ordernumber)
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
        self.sleep(4)
        # 点击提交
        self.click_submit_btn()
        self.sleep(1)
        # 判断是否完成服务
        if self.login.get_system_msg() == "操作成功":
            self.log.info(' ** Finish order is success ！')
        else:
            raise TimeoutError(' ** Finish order is fail ! ')

