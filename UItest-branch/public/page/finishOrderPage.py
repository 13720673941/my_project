# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/5 17:08

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()

'''
网点完成工单页面
'''
class FinishOrder(BasePage):

    '''网点完成工单页面'''
    finish_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/servicing?tabType=全部工单'
    finishOrderBtn = (By.XPATH,'//a[text()="完成服务"]')
    inputBreakType = (By.XPATH,'//input[@placeholder="请输入故障类型"]')
    masterOrderTime = (By.XPATH,'//input[@placeholder="请选择师傅预约日期"]')
    masterDoorTime = (By.XPATH,'//input[@placeholder="请选择师傅上门时间"]')
    masterFinishTime = (By.XPATH,'//input[@placeholder="请选择师傅完成时间"]')
    inputRemark = (By.XPATH,'//label[text()="服务反馈："]/following-sibling::textarea')
    upLoadingPicture = (By.XPATH,'//input[@type="file"]')
    submitBtn = (By.XPATH,'//button[text()="提交"]')
    parentUpPicture = (By.XPATH,'//label[text()="服务照片："]/../div')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_finish_order_page(self):
        '''进入完成工单列表页'''
        self.open_url(self.finish_order_url)

    def click_finish_btn(self):
        '''点击完成工单按钮'''
        self.click_button(self.finishOrderBtn)
        #log.info('{0}点击->完成服务'.format(self.success))

    def input_break_type(self):
        '''输入故障类型'''
        self.input_message(self.inputBreakType,self.get_now_time(Time=True))
        #log.info('{0}输入故障类型：{1}'.format(self.success,self.get_now_time(Time=True)))

    def input_master_orderTime(self,orderTime):
        '''输入师傅预约时间'''
        self.input_message(self.masterOrderTime,orderTime)
        #log.info('{0}输入师傅预约时间：{1}'.format(self.success,orderTime))

    def input_master_doorTime(self,doorTime):
        '''输入师傅上门时间'''
        self.input_message(self.masterDoorTime,doorTime)
        #log.info('{0}输入师傅上门时间：{1}'.format(self.success,doorTime))

    def input_master_finishTime(self,finishTime):
        '''输入师傅完成时间'''
        self.input_message(self.masterFinishTime,finishTime)
        #log.info('{0}输入师傅完成时间：{1}'.format(self.success,finishTime))

    def input_remark(self):
        '''输入备注'''
        self.input_message(self.inputRemark,self.get_now_time(Time=True))
        #log.info('{0}输入备注：{1}'.format(self.success,self.get_now_time(Time=True)))

    def up_finish_picture(self,upLoading='True'):
        '''上传图片'''
        if upLoading == 'True':
            #获取上传图片个数
            PictureNum = self.get_element_count(parentEl=self.parentUpPicture,childEl='dl')
            #上传图片
            self.up_loading_picture(PictureNum,self.upLoadingPicture)

    def click_submit_btn(self):
        '''点击提交按钮'''
        self.click_button(self.submitBtn)
        #log.info('{0}点击->提交'.format(self.success))

    def finish_order_main(self,ordernumber,url='http://www.51shouhou.cn/singleBranch/#/order/search/servicing?tabType=全部工单'):
        '''
        :param OrderTime:   师傅预约时间
        :param DoorTime:    上门时间
        :param FinishTime:  完工时间
        :param UpLoading:   是否上传图片
        :return:
        '''
        #'''网点完成服务'''
        #log.info('-=【网点完成服务】=-')
        #进入完工订单列表页面
        self.open_url(url)
        #选择工单
        self.select_new_order(ordernumber)
        #点击订单列表完成服务按钮
        self.click_finish_btn()
        #输入故障类型
        self.input_break_type()
        #输入师傅预约时间
        self.input_master_orderTime(self.get_now_time())
        #输入师傅上门时间
        self.input_master_doorTime(self.get_now_time())
        self.sleep(1)
        #输入师傅完成服务时间
        self.input_master_finishTime(self.get_now_time())
        #输入备注
        self.input_remark()
        #上传图片
        self.up_finish_picture()
        #点击提交
        self.click_submit_btn()
        #判断
        if self.get_system_msg() == '操作成功':
            log.info('{0} *Finish order is success！'.format(self.success))
        else:
            log.error('{0} *Finish order is fail, system msg: {1}.'.format(self.fail,self.get_system_msg()))



# from Common import getData
#
# jsonData = getData.GetJsonData()["FinishOrder"]
# dict1 = jsonData[0]
# for k,v in dict1.items():
#     if v == '当前时间':
#         dict1[k] = '2019-06-06'
#
# print(dict1)