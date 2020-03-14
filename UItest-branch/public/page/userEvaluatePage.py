# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/3/13 9:50

from public.common.basePage import BasePage
from config.urlConfig import *
import hashlib

class UserEvaluatePage(BasePage):

    """用户评价页面：关联市场单好评返现"""

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        # 满意度全部字段信息
        self.satisfactionList = ["非常不满意", "不满意", "一般", "满意", "非常满意"]

    def get_elements(self,option):
        """获取页面元素配置文件中用户评价页面的元素信息"""
        return read_config_data("user_evaluate_page",option,elementDataPath)

    def enter_user_evaluate_page(self,orderNumber):
        """进入用户评价页面"""

        # 对评价订单的单号进行MD5加密
        strPkId = hashlib.md5(orderNumber.encode("utf-8")).hexdigest()
        # 对加密后的字符串进行拼装链接->订单PkId格式：F0E789F9-93BD-26CE-9611-4B9EA7D44EA3
        orderPkId = strPkId[:8]+"-"+strPkId[8:12]+"-"+strPkId[12:16]+"-"+strPkId[16:20]+"-"+strPkId[20:]
        # 读取用户评价基础地址替换订单PkId
        url = user_evaluate_url.replace("+orderPkId+",orderPkId)
        # 打开用户评价页面
        self.use_js(js='window.open("'+url+'")')
        # 切换新页面
        self.switch_to_new_handle()
        # 校验当前页面
        self.open_url(url,self.get_elements("title_text"))

    def select_comprehensive_evaluate_star(self,userSatisfaction):
        """
        选择综合评价的星级
        :param userSatisfaction 对应 5档 非常不满意、不满意、一般、满意、非常满意
        """
        # 判断传入参数是否正确
        if userSatisfaction not in self.satisfactionList:
            raise TypeError("参数：userSatisfaction 传入的字段错误，字段类型包含：{}".format(self.satisfactionList))
        # 获取传入的字段在列表中的索引
        satisfactionIndex = self.satisfactionList.index(userSatisfaction)
        # 选择用户满意度的星级别
        self.click_button(self.get_elements("comprehensive_evaluate_btn").replace("+num+",str(satisfactionIndex+1)))

    def select_service_attitude_star(self,serviceAttitude):
        """
        选择服务态度的星级
        :param serviceAttitude 对应 5档 非常不满意、不满意、一般、满意、非常满意
        """
        # 判断传入参数是否正确
        if serviceAttitude not in self.satisfactionList:
            raise TypeError("参数：serviceAttitude 传入的字段错误，字段类型包含：{}".format(self.satisfactionList))
        # 获取传入的字段在列表中的索引
        satisfactionIndex = self.satisfactionList.index(serviceAttitude)
        # 选择用户满意度的星级别
        self.click_button(self.get_elements("service_attitude_btn").replace("+num+",str(satisfactionIndex+1)))

    def select_service_skills_star(self,serviceSkills):
        """
        选择服务技能的星级
        :param serviceSkills 对应 5档 非常不满意、不满意、一般、满意、非常满意
        """
        # 判断传入参数是否正确
        if serviceSkills not in self.satisfactionList:
            raise TypeError("参数：serviceSkills 传入的字段错误，字段类型包含：{}".format(self.satisfactionList))
        # 获取传入的字段在列表中的索引
        satisfactionIndex = self.satisfactionList.index(serviceSkills)
        # 选择用户满意度的星级别
        self.click_button(self.get_elements("service_skills_btn").replace("+num+",str(satisfactionIndex+1)))

    def select_door_speed_star(self,doorSpeed):
        """
        选择上门速度的星级
        :param doorSpeed 对应 5档 非常不满意、不满意、一般、满意、非常满意
        """
        # 判断传入参数是否正确
        if doorSpeed not in self.satisfactionList:
            raise TypeError("参数：doorSpeed 传入的字段错误，字段类型包含：{}".format(self.satisfactionList))
        # 获取传入的字段在列表中的索引
        satisfactionIndex = self.satisfactionList.index(doorSpeed)
        # 选择用户满意度的星级别
        self.click_button(self.get_elements("door_speed_btn").replace("+num+",str(satisfactionIndex+1)))

    def input_user_suggestions(self,userSuggestion):
        """输入用户建议描述"""
        self.input_message(self.get_elements("user_suggestion_input"),userSuggestion)

    def click_submit_evaluate_btn(self):
        """点击提交评价按钮"""
        self.click_button(self.get_elements("submit_evaluate_btn"))

    def estimate_submit_success_text(self):
        """判断是否提交成功"""
        return self.is_display(self.get_elements("evaluate_success_text"))

    def user_evaluate_main(self,orderNumber,userSatisfaction="非常满意",serviceAttitude="非常满意",
                           serviceSkills="非常满意",doorSpeed="非常满意",userSuggestion="非常满意"):
        """
        用户评价主程序->默认好评
        :param orderNumber          订单编号
        :param userSatisfaction     用户综合
        :param serviceAttitude      服务态度
        :param serviceSkills        服务技能
        :param doorSpeed            上门速度
        :param userSuggestion       用户建议评价
        """

        self.log.info("-=【用户评价】=-")
        self.enter_user_evaluate_page(orderNumber)
        self.select_comprehensive_evaluate_star(userSatisfaction)
        self.select_service_attitude_star(serviceAttitude)
        self.select_service_skills_star(serviceSkills)
        self.select_door_speed_star(doorSpeed)
        self.input_user_suggestions(userSuggestion)
        self.sleep(1)
        self.click_submit_evaluate_btn()
        # 判断提交评价成功
        if self.estimate_submit_success_text():
            self.log.info(" ** User evaluate success !")
        else:
            raise TimeoutError(" ** User evaluate fail !")