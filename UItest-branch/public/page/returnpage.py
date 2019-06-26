# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/12 16:07

from public.common.basepage import BasePage
from selenium.webdriver.common.by import By
from public.common.logconfig import Log
log=Log()
'''
返单页面操作
'''
class ReturnOrderPage(BasePage):

    '''返单页面元素操作'''
    return_order_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'
    finish_return_url = 'http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=已返单&page=1'
    returnOrderBtn = (By.XPATH,'//a[text()="返单"]')
    alterReturnBranch = (By.XPATH,'//a[text()="修改返单服务商"]')
    confirmBtn = (By.XPATH,'//div[text()="服务商列表"]/../following-sibling::div[2]/button[2]')
    addBranch = (By.XPATH,'//a[text()="添加代结单服务商"]')
    delReturnOrder = (By.XPATH,'//a[text()="撤销返单"]')
    turnTitle = (By.XPATH,'//a[text()="添加经销商"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def enter_return_order_page(self):
        self.open_url(self.return_order_url)

    def enter_finish_return_page(self):
        self.open_url(self.finish_return_url)

    def click_return_btn(self):
        '''点击返单按钮'''
        self.click_button(self.returnOrderBtn)
        #log.info('{0}点击->返单'.format(self.success))

    def click_alter_return_branch(self):
        '''点击修改返单服务商'''
        self.click_button(self.alterReturnBranch)
        #log.info('{0}点击->修改返单服务商'.format(self.success))

    def select_branch_name(self,branchName):
        '''选择返单服务商名称'''
        if branchName != '':
            self.click_button(element=(By.XPATH,'//label[text()=" '+branchName+'"]'))
            #log.info('{0}选择修改返单服务商：{1}'.format(self.success,branchName))

    def click_confirm_btn(self):
        '''点击确定'''
        self.click_button(self.confirmBtn)
        #log.info('{0}点击->确定'.format(self.success))

    def click_add_branch(self):
        '''点击添加待接单服务商'''
        self.click_button(self.addBranch)
        #log.info('{0}点击->添加代结单服务商'.format(self.success))

    def click_del_return(self):
        '''点击撤销返单'''
        self.click_button(self.delReturnOrder)
        #log.info('{0}点击->撤销返单'.format(self.success))

    def turn_title_isDisplayed(self):
        '''判断页面是否跳转添加服务商页面'''
        return self.is_display(self.turnTitle)

    def return_order_main(self,orderNumber,alterReturnBranch=False,branchName=None,
                        url='http://www.51shouhou.cn/singleBranch/#/order/search/waitvisit?tabType=待返单&page=1'):
        '''返单主程序'''
        #log.info('-=【返单】=-')
        #进入返单页面
        self.open_url(url)
        self.wait()
        #选择订单
        self.select_new_order(orderNumber)
        #返单是否修改返单服务商
        if alterReturnBranch:
            #点击修改返单服务商
            self.click_alter_return_branch()
            #选择服务商名称
            self.select_branch_name(branchName)
        #点击返单按钮
        self.click_return_btn()
        self.sleep(1)
        #断言
        if '操作成功' in self.get_system_msg():
            log.info('{0} *Return order: {1} success！'.format(self.success,orderNumber))
        else:
            log.error('{0} *Return order: {1} fail, system msg: {2}.'.format(self.fail,orderNumber,self.get_system_msg()))