# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/4 11:57

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
搜索订单页面信息
'''
class SearchOrderPage(BasePage):

    '''搜索页面元素信息'''
    search_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/allorder?tabType=全部工单'
    inputOrderNum = (By.XPATH,'//label[text()="工单编号"]/following-sibling::input[1]')
    inputUserName = (By.XPATH,'//label[text()="用户姓名"]/following-sibling::input[1]')
    inputUserPhone = (By.XPATH,'//label[text()="用户电话"]/following-sibling::input[1]')
    openServerType = (By.XPATH,'//label[text()="服务类型"]/following-sibling::div/div')
    selectServerType = (By.XPATH,'//label[text()="服务类型"]/../div/div[2]/ul[2]')
    openOrderStatus = (By.XPATH,'//label[text()="工单状态"]/following-sibling::div/div')
    selectOrderStatus = (By.XPATH,'//label[text()="工单状态"]/../div[2]/div[2]/ul[2]')
    openMaster = (By.XPATH,'//label[text()="服务师傅"]/following-sibling::div/div')
    selectMaster = (By.XPATH,'//label[text()="服务师傅"]/../div[3]/div[2]/ul[2]')
    searchBtn = (By.XPATH,'//a[text()="搜索"]')
    moreSearchBtn = (By.XPATH,'//a[text()="更多"]')
    firstOrderInfo = (By.XPATH,'//div/div[2]/table/tbody/tr[1]')
    firstOrderInfo1 = (By.XPATH, '//div/div[2]/table/tbody/tr[1]')
    #########多条件搜索
    selectBrand = (By.XPATH,'//label[text()="家电品牌"]/../select')
    selectKind = (By.XPATH,'//label[text()="家电品类"]/../select')
    inputProductNum = (By.XPATH,'//input[@placeholder="输入产品型号"]')
    inputInPheNum = (By.XPATH,'//input[@placeholder="输入内机条码"]')
    orderForm = (By.XPATH,'//span[text()="请选择工单来源"]')
    parentOrderFrom = (By.XPATH,'//label[text()="工单来源"]/../div/div[2]/ul[2]')
    buyPlace = (By.XPATH,'//label[text()="购买渠道"]/../div/div')
    parentBuyPlace = (By.XPATH,'//span[text()="全部购买渠道"]/../../div[2]/ul[2]')
    addOrderDate = (By.XPATH,'//label[text()="下单日期"]/../div/div/div/input')
    addOrderEndDate = (By.XPATH,'//label[text()="下单日期"]/../div[2]/div/div/input')
    finishOrderDate = (By.XPATH,'//label[text()="完成日期"]/../div/div/div/input')
    finishOrderEndDate = (By.XPATH,'//label[text()="完成日期"]/../div[2]/div/div/input')
    searchBtn1 = (By.XPATH,'//label[text()="工单编号"]/../../../div[2]/div[9]/a')
    searchIsNull = (By.XPATH,'//img[@src="./a5cc0717653f1ec5d188d2a6a1470b03.png"]')
    orderCount = (By.XPATH,'//span[@class="ivu-page-total"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_search_order_page(self):
        self.open_url(self.search_order_url)

    def input_order_Nnumber(self,orderNum):
        '''输入工单编号'''
        self.input_message(self.inputOrderNum,orderNum)
        #log.info('{0}输入工单编号：{1}'.format(self.success,orderNum))

    def input_username(self,username):
        '''输入用户名字'''
        self.input_message(self.inputUserName,username)
        #log.info('{0}输入用户姓名：{1}'.format(self.success,username))

    def input_user_phone(self,phoneNum):
        '''输入用户手机号'''
        self.input_message(self.inputUserPhone,phoneNum)
        #log.info('{0}输入用户手机号：{1}'.format(self.success,phoneNum))

    def select_server_type(self,value):
        '''选择服务类型'''
        if value != '':
            self.operate_not_select(self.openServerType,self.selectServerType,value)
            #log.info('{0}选择服务类型：{1}'.format(self.success,value))

    def select_order_status(self,value):
        '''选择工单状态'''
        if value != '':
            self.operate_not_select(self.openOrderStatus,self.selectOrderStatus,value)
            #log.info('{0}选择工单状态：{1}'.format(self.success,value))

    def select_master(self,value):
        '''选择服务师傅'''
        if value != '':
            self.operate_not_select(self.openMaster,self.selectMaster,value)
            #log.info('{0}选择师傅名称：{1}'.format(self.success,value))

    def click_search_btn(self):
        '''点击搜索按钮'''
        self.click_button(self.searchBtn)
        #log.info('{0}点击->搜索'.format(self.success))

    def click_search_more(self):
        '''点击搜索更多'''
        self.click_button(self.moreSearchBtn)
        #log.info('{0}点击->搜索更多'.format(self.success))

    def select_product_brand(self,value):
        '''选择家电品牌'''
        if value != '':
            self.operate_select(self.selectBrand,value)
            #log.info('{0}选择品牌：{1}'.format(self.success,value))

    def select_product_kinds(self,value):
        '''选择家电品类'''
        if value != '':
            self.operate_select(self.selectKind,value)
            #log.info('{0}选择品类：{1}'.format(self.success,value))

    def input_product_number(self,productNum):
        '''输入产品型号'''
        self.input_message(self.inputProductNum,productNum)
        #log.info('{0}输入产品型号：{1}'.format(self.success,productNum))

    def input_in_pheNum(self,in_pheNum):
        '''输入内机条码'''
        self.input_message(self.inputInPheNum,in_pheNum)
        #log.info('{0}输入内机条码：{1}'.format(self.success,in_pheNum))

    def select_order_from(self,value):
        '''选择工单来源'''
        if value != '':
            self.operate_not_select(self.orderForm,self.parentOrderFrom,value)
            #log.info('{0}选择工单来源：{1}'.format(self.success,value))

    def select_buy_place(self,value):
        '''选择购买渠道'''
        if value != '':
            self.operate_not_select(self.buyPlace,self.parentBuyPlace,value)
            #log.info('{0}选择购买渠道：{1}'.format(self.success,value))

    def input_create_start_date(self,date):
        '''输入订单创建开始日期'''
        self.input_message(self.addOrderDate,date)
        #log.info('{0}输入订单创建开始时间：{1}'.format(self.success,date))

    def input_create_end_date(self,date):
        '''输入订单创建结束日期'''
        self.input_message(self.addOrderEndDate,date)
        #log.info('{0}输入订单创建开始时间：{1}'.format(self.success,date))

    def input_finish_start_date(self,date):
        '''输入完成订单开始日期'''
        self.input_message(self.finishOrderDate,date)
        #log.info('{0}输入订单完成开始时间：{1}'.format(self.success,date))

    def input_finish_end_date(self,date):
        '''输入完成订单结束日期'''
        self.input_message(self.finishOrderEndDate,date)
        #log.info('{0}输入订单完成开始时间：{1}'.format(self.success,date))

    def click_more_search_btn(self):
        '''点击更多订单搜索的搜索按钮'''
        self.click_button(self.searchBtn1)
        #log.info('{0}点击->搜索'.format(self.success))

    def search_order_count(self):
        '''获取搜索订单数量'''
        orderNumStr = self.get_text(self.orderCount)
        #拆分获取订单总数
        OrderCount = orderNumStr.split(' ')[1]
        #log.info('{0}搜索出订单：{1}'.format(self.success,orderNumStr))
        return OrderCount

    def get_first_order_info(self):
        '''获取订单列表第一行订单的所有信息'''
        #分为两个层面的信息
        try:
            orderInfo = self.get_text(self.firstOrderInfo) + self.get_text(self.firstOrderInfo1)
            return orderInfo
        except:
            #判断是否为空
            if self.is_display(self.searchIsNull):
                log.info('{0}搜索订单列表为空！'.format(self.success))
            pass





