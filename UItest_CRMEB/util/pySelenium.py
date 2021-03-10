# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/4 19:36

"""
webdriver类中操作浏览器方法二次封装, 提供给页面page类使用，
包括浏览器基本操作打开浏览器、打开网页、点击、输入、下拉框选择，cookie操作，以及窗口、iframe切换等
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from util.logConfig import Logger
from config.keywordDB import KeywordDB as KDB
from config.varConfig import *
from util.rwFile import ReadWriteFile
from util.timeTool import Time
from config.filePathConfig import FilePathConfig

import time
import random

Log = Logger().origin_log
rwParams = ReadWriteFile(FilePathConfig.PROJECT_CONNECT_PARAM_PATH)

# 获取浏览器类型参数
browserType = SysConfig.BROWSER_TYPE.lower()
# 读取驱动保存路径
chromeDriverPath = rwParams.read_ini_file(section="DRIVER_PATH", option="driver_path")


class PySelenium:

    def __init__(self, openType="pc"):
        # 判断打开浏览器模式
        if openType.lower() == "pc":
            # 判断浏览器类型选择驱动
            if browserType == "chrome":
                self.driver = webdriver.Chrome(executable_path=chromeDriverPath)
            elif browserType == "firefox":
                self.driver = webdriver.Firefox()
            elif browserType == "ie":
                self.driver = webdriver.Ie()
            else:
                raise NameError("浏览器类型字段错误，允许字段类型：chrome、firefox、ie ")
            # 浏览器最大化
            self.set_window_max()
            Log.info("正在打开 {} 浏览器PC模式...".format(SysConfig.BROWSER_TYPE))
        elif openType.lower() == "h5":
            # H5 模式打开浏览器必须是chrome浏览器
            if browserType != "chrome":
                raise TypeError("浏览器: {} 不支持切换 H5 模式".format(browserType))
            # 浏览器类型为h5打开浏览器为手机模式，默认iphone8
            mobileEmulation = {'deviceName': SysConfig.MOBILE_TYPE}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobileEmulation)
            self.driver = webdriver.Chrome(options=options, executable_path=chromeDriverPath)
            Log.info("正在打开谷歌浏览器切换: {} 手机模式...".format(SysConfig.MOBILE_TYPE))
        else:
            Log.error("不支持打开 {} 浏览器模式类型！请检查openType字段！".format(openType))

    def wait_element(self, elementPath, seconds=10):
        """
        等待页面元素显示在页面
        :param elementPath: 元素定位方式和路径组合 id->kw
        :param seconds: 等待时间
        :return:
        """
        if "->" not in elementPath:
            raise NameError("元素路径字段：{}类型传入有误！允许格式例如：id->kw".format(elementPath))
        name = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        message = " {}秒内在页面中没有找到元素：{}".format(seconds, elementPath)
        # 判断元素路径类型是否正确
        if name not in KDB.BY_DB.keys():
            raise NameError("元素定位类型：{} 名称不正确！".format(name))
        # 等待页面加载元素，每1秒检查一次
        WebDriverWait(self.driver, seconds, 1).until(EC.visibility_of_element_located((KDB.BY_DB[name], path)), message)

    def _find_element(self, elementPath):
        """
        查找页面元素返回元素定位信息`
        :param elementPath: 元素定位方式和路径组合 id->kw
        :return:
        """
        # 等待页面元素显示
        self.wait_element(elementPath)
        name = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        # 查找并返回页面元素
        return self.driver.find_element(KDB.BY_DB[name], path)

    def _find_elements(self, elementPath) -> list:
        """
        查找一组元素返回页面全部元素列表
        :param elementPath: 元素定位方式和路径组合 id->kw
        :return:
        """
        # 等待页面元素显示
        self.wait_element(elementPath)
        name = elementPath.split("->")[0]
        path = elementPath.split("->")[1]
        # 查找并返回页面元素列表
        return self.driver.find_elements(KDB.BY_DB[name], path)

    def open_url(self, url, element=None, openOnCurrentWin=False):
        """
        打开网页地址，传入页面元素判断页面是否完全加载
        :param url: 地址url
        :param element: 被检测页面元素路径
        :return:
        """
        for i in range(5):
            try:
                if openOnCurrentWin:
                    # 在同一浏览器打开另一个链接
                    self.driver.execute_script("window.open('"+url+"')")
                    Log.info("在当前浏览器重新打开一个页面：{} ".format(url))
                else:
                    self.driver.get(url)
                    Log.info("打开网址：{} ".format(url))
                # 检测页面元素是否显示
                if element is not None:
                    self.wait_element(element)
                break
            except:
                if i == 4:
                    raise Exception("网站地址: {} 打开失败没有检测到页面元素: {}".format(url, element))
                else:
                    pass

    def sleep(self, seconds):
        """死等几秒"""
        time.sleep(seconds)
        Log.info("等待: {}s".format(seconds))

    def set_window_max(self):
        """设置窗口最大化"""
        self.driver.maximize_window()
        Log.info("设置打开浏览器最大尺寸")

    def set_window_size(self, width, height):
        """
        设置浏览器显示尺寸
        :param width: 宽度
        :param height: 高度
        :return:
        """
        self.driver.set_window_size(width, height)
        Log.info("设置打开浏览器尺寸宽: {} 高: {}".format(width, height))

    def back(self):
        """返回上一级页面"""
        self.driver.back()
        Log.info("返回浏览器上一级操作页面")

    def refresh_page(self):
        """刷新页面"""
        self.driver.refresh()
        Log.info("刷新浏览器当前页面")

    def forward_page(self):
        """前进一级页面"""
        self.driver.forward()
        Log.info("前进浏览器下一个操作页面")

    def close_window(self):
        """关闭当前页面窗口"""
        self.driver.close()
        Log.info("关闭浏览器当前所在页面")

    def quit_browser(self):
        """关闭当前浏览器"""
        self.driver.quit()
        Log.info("退出当前打开的浏览器")

    def click_button(self, elementPath):
        """
        点击页面按钮
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            button = self._find_element(elementPath)
            button.click()
            Log.info("点击按钮: <{}>".format(elementPath))
        except:
            raise Exception("点击按钮: {} 失败页面上没有找到该操作按钮！".format(elementPath))

    def right_click(self, elementPath):
        """
        右键点击页面按钮
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).context_click(el).perform()
            Log.info("鼠标右键点击按钮: <{}>".format(elementPath))
        except:
            raise Exception("右键点击页面按钮：{} 失败！".format(elementPath))

    def double_click(self, elementPath):
        """
        左键双击页面按钮
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).double_click(el).perform()
            Log.info("鼠标左键双击按钮: <{}>".format(elementPath))
        except:
            raise Exception("双击页面按钮：{} 失败！".format(elementPath))

    def drag_and_drop(self, elementPath, target):
        """
        长按拖拽按钮从某元素到另一个元素
        :param path: 需要长安的按钮
        :param target: 拖拽到的元素
        """
        try:
            el = self._find_element(elementPath)
            target_el = self._find_element(target)
            ActionChains(self.driver).drag_and_drop(el, target_el).perform()
            Log.info("长按拖拽按钮：<{}> 移动到按钮：<{}> ".format(elementPath, target))
        except:
            raise Exception("长按拖拽按钮：<{}> 移动到按钮：<{}> 失败！！！".format(elementPath, target))

    def move_and_click(self, elementPath):
        """
        移动到某元素上并点击
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).move_to_element(el).click().perform()
            Log.info("鼠标移动到按钮: <{}> 上并点击按钮".format(elementPath))
        except:
            raise Exception("鼠标移动到按钮：<{}> 上并点击失败！！！".format(elementPath))

    def click_hold_on(self, elementPath):
        """
        点击长按按钮
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).click_and_hold(el).perform()
            Log.info("点击并长按按钮：<{}>".format(elementPath))
        except:
            raise Exception("点击并长按按钮：<{}> 失败！！！".format(elementPath))

    def hold_on_release(self, elementPath):
        """
        释放长按按钮操作
        :param elementPath:元素定位方式和路径组合 id->kw
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).release(el)
            Log.info("释放当前长按按钮：<{}>".format(elementPath))
        except:
            raise Exception("释放当前长按按钮：<{}> 失败！！！".format(elementPath))

    def click_drag_and_drop_by_offset(self, elementPath, xOffset, yOffset):
        """
        长按按钮并移动到规定坐标量位置
        :param elementPath: 元素定位方式和路径组合 id->kw
        :param xOffset: 移动到所在位置的 x 坐标
        :param yOffset: 移动到所在位置的 y 坐标
        :return:
        """
        try:
            el = self._find_element(elementPath)
            ActionChains(self.driver).\
                drag_and_drop_by_offset(source=el, xoffset=xOffset, yoffset=yOffset).perform()
            Log.info("长按并拖拽按钮: <{}> 到X坐标: {} ，Y坐标: {}".format(elementPath, xOffset, yOffset))
        except:
            raise Exception("长按并拖拽按钮: <{}> 到X坐标: {} ，Y坐标: {} 失败！！！".format(elementPath, xOffset, yOffset))

    def submit(self, elementPath):
        """
        提交
        :param elementPath:
        :return:
        """
        try:
            self._find_element(elementPath).submit()
            Log.info("点击提交按钮: <{}>".format(elementPath))
        except:
            raise Exception("提交失败！！！")

    def clear_input(self, elementPath):
        """
        清除输入框输入的数据字段
        :param elementPath:
        :return:
        """
        self._find_element(elementPath).clear()
        Log.info("清除输入框所有字段")

    def input_keyword(self, elementPath, keyword):
        """
        输入字符串
        :param elementPath: 输入框页面元素路径
        :param keyword: 输入关键字
        :return:
        """
        self.clear_input(elementPath)
        self._find_element(elementPath).send_keys(keyword)
        Log.info("在输入框: <{}> 输入字段: {}".format(elementPath, keyword))

    def check_element_on_page(self, elementPath) -> bool:
        """
        检查查找元素是否存在页面上
        :param elementPath:
        :return:
        """
        flag = None
        try:
            flag = self._find_element(elementPath).is_displayed()
            Log.info("元素: <{}> 存在于当前页面上 返回->True".format(elementPath))
        except:
            flag = False
            raise Exception("页面上没有找到该元素：{} 返回->False".format(elementPath))
        finally:
            return flag

    def get_title(self) -> str:
        """获取页面标题"""
        title = self.driver.title
        Log.info("获取当前页面title: {}".format(title))

        return title

    def get_current_url(self) -> str:
        """获取当前页面url地址"""
        url = self.driver.current_url
        Log.info("获取当前页面url: {}".format(url))

        return url

    def get_text(self, elementPath) -> str:
        """
        获取页面元素文本
        :param elementPath:
        :return:
        """
        text = self._find_element(elementPath).text
        Log.info("获取当前元素文本信息: {}".format(text))

        return text

    def get_attribute(self, elementPath, attributeName):
        """
        获取页面元素属性
        :param elementPath:
        :return:
        """
        attribute = self.driver.find_element(elementPath).get_attribute(attributeName)
        Log.info("获取当前元素: {} 属性值: {}".format(attributeName, attribute))

        return attribute

    def change_attribute(self, elementPath, attribute, attValue):
        """
        设置标签的属性值
        :param elementPath:
        :param attribute: 属性名称
        :param attValue: 属性值
        :return:
        """
        element = self._find_element(elementPath)
        self.driver.execute_script("arguments[0].{}='{}';".format(attribute, attValue), element)
        Log.info("修改页面元素: <{}> 属性: {}, 值变为: {} ".format(elementPath, attribute, attValue))

    def accept_alert(self):
        """接受页面警告弹窗"""
        self.driver.switch_to.alert.accept()
        Log.info("确认警告弹窗")

    def dismiss_alert(self):
        """取消弹窗"""
        self.driver.switch_to.alert.dismiss()
        Log.info("取消警告弹窗")

    def switch_to_iframe(self, elementPath):
        """
        切换到frame框中
        :param elementPath:
        :return:
        """
        try:
            el = self.driver.find_element(elementPath)
            self.driver.switch_to.frame(el)
            Log.info("切换进入iframe框: {} ".format(elementPath))
        except:
            raise Exception("切换页面iframe：{} 失败！".format(elementPath))

    def switch_out_iframe(self):
        """切换出iframe"""
        self.driver.switch_to.default_content()
        Log.info("切换出iframe框")

    def switch_to_one_window(self):
        """
        切换到当前打开的网页窗口
        :return:
        """
        # 获取全部窗口句柄
        handles = self.driver.window_handles
        # 获取当前窗口句柄
        currentHandle = self.driver.current_window_handle
        for handle in handles:
            if handle != currentHandle:
                # 切换至另一个窗口
                self.driver.switch_to.window(handle)
                Log.info("切换浏览器窗口至: {}".format(handle))
        else:
            raise Exception("当前浏览器只打开了一个窗口无需切换！！！")

    def screen_shot(self):
        """截图功能"""
        imgName = FilePathConfig.ERROR_IMG_SAVE_PATH + "\\" + \
                  Time().get_now_time(timeFormat="%Y%m%d%H%M%S") + ".png"
        try:
            self.driver.get_screenshot_as_file(filename=imgName)
            Log.info("操作异常截图成功，图片保存路径: {}".format(imgName))
        except:
            raise Exception("错误截图保存失败！")

    def select_by_text(self, elementPath, text, tagName=None, isFuzzy=False):
        """
        按页面显示文字选择下拉元素
        :param tagName: 下拉选项标签
        :param isFuzzy: 是否开启模糊匹配
        :param elementPath: 下拉框元素路径地址
        :param text: 被选中的文本信息
        :return:
        """
        # 获取下拉框元素定位
        select = Select(self._find_element(elementPath))
        if isFuzzy:
            # 获取全部下拉选项总数量
            parentElement = self._find_element(elementPath)
            selectList = parentElement.find_elements_by_tag_name(tagName)
            for tag in selectList:
                # 加时间等待下
                self.sleep(1)
                tagText = tag.text
                if text in tagText or tagText in text:
                    select.select_by_visible_text(tagText)
                    break
            else:
                raise NameError("模糊匹配的选项：{} 下拉列表中不存在！".format(text))
        else:
            select.select_by_visible_text(text)
        Log.info("展开下拉框并根据选项文本信息选中: {}".format(text))

    def select_by_index(self, elementPath, tagName=None, index=None, isRandom=False):
        """
        按页面显示索引选择下拉元素
        :param elementPath: 下拉框元素路径地址
        :param text: 被选中的文本索引
        :return:
        """
        global randomSelectNum
        # 获取下拉框元素定位
        select = Select(self._find_element(elementPath))
        if isRandom:
            try:
                # 获取全部下拉选项总数量
                parentElement = self._find_element(elementPath)
                selectCount = parentElement.find_elements_by_tag_name(tagName)
                # 随机选中一个索引
                randomSelectNum = random.randint(0,len(selectCount)-1)
                select.select_by_index(randomSelectNum)
                Log.info("展开下拉框并根据选项索引信息选中: {}".format(randomSelectNum))
            except:
                raise Exception("下拉选项中不存在该索引：{} ".format(randomSelectNum))
        else:
            select.select_by_index(index)
            Log.info("展开下拉框并根据选项索引信息选中: {}".format(index))

    def select_by_value(self, elementPath, value, tagName=None, isFuzzy=False):
        """
        根据下拉列表选项中的标签的value属性值进行选择
        :param elementPath: 下拉框元素路径地址
        :param value: 被选中的标签属性值
        :param tagName: 标签名称
        :param isFuzzy: 是否执行模糊匹配
        :return:
        """
        # 获取下拉框元素定位
        select = Select(self._find_element(elementPath))
        if isFuzzy:
            # 获取全部下拉选项总数量
            parentElement = self._find_element(elementPath)
            selectList = parentElement.find_elements_by_tag_name(tagName)
            for tag in selectList:
                # 加时间等待下
                self.sleep(1)
                attrNameStr = tag.get_attribute("value")
                if value in attrNameStr or attrNameStr in value:
                    select.select_by_value(attrNameStr)
                    break
            else:
                raise NameError(
                    "根据标签：{} 值属性：value 模糊匹配的选项：{} 下拉列表中不存在！".format(tagName, value))
        else:
            select.select_by_value(value)
        Log.info("展开下拉框并根据选项value属性值信息选中: {}".format(value))

    def operate_not_select_box(self, elementPath, tagName, text=None, isRandom=False):
        """
        操作非select下拉选择框操作, 遍历下拉列表中的文本数据匹配关键字
        :param elementPath: 下拉框元素路径地址
        :param tagName: 下拉列表标签名称
        :param text: 所要选中的文本信息
        :param isRandom: 是否开启随机选择模式
        :return:
        """

        # 获取父级元素定位信息
        parentElement = self._find_element(elementPath)
        # 获取子集所有标签列表
        childElementList = parentElement.find_elements_by_tag_name(tagName)
        if isRandom:
            # 开启随机选择模式
            randomSelectNum = random.randint(0, len(childElementList) - 1)
            try:
                self.sleep(1)
                childElementList[randomSelectNum].click()
                Log.info("非select下拉框，根据选项文本信息选中: {}".format(childElementList[randomSelectNum].text))
            except:
                raise Exception("随机选中列表选项：{} 失败！".format(childElementList[randomSelectNum].text))
        else:
            # 按标签文本选中
            for child in childElementList:
                self.sleep(1)
                childText = child.text
                if text in childText or childText in text:
                    try:
                        child.click()
                        Log.info("非select下拉框，根据选项文本信息选中: {}".format(childText))
                    except:
                        raise Exception("点击选中列表选项：{} 失败！".format(text))
                    finally:
                        break
            else:
                raise Exception("下拉列表中没有找到匹配的选项：{} ".format(text))

    def use_keys(self, elementPath, keyName):
        """
        使用键盘操作页面按钮等
        :param elementPath: 操作元素路径
        :param keyName: 使用键盘按键名称
        :return:
        """
        keys_DB = {
            "space": Keys.SPACE, "enter": Keys.ENTER,
            "back_space": Keys.BACK_SPACE, "f5": Keys.F5
        }
        if keyName.lower() not in keys_DB.keys():
            raise NameError("输入键盘按钮名称不正确：{} ，请检查keys_DB库中是否包含该字段！".format(keyName))
        try:
            self._find_element(elementPath).send_keys(keys_DB[keyName])
            Log.info("在页面元素: {} 上使用键盘: {} 操作".format(elementPath, keyName))
        except:
            raise Exception("使用键盘：{} 操作页面按钮：{} 失败！".format(keyName, elementPath))

    def get_cookie(self, option):
        """
        获取登录后的cookie值
        :param option: 配置文件中标题的值
        :param section: 对应key值
        :return:
        """
        # 由于.ini文件中不能写入 % 字符，会报错，替换成 $ 后写入
        cookieValue = str(self.driver.get_cookies()).replace("%", "$")
        Log.info("获取浏览器cookie值: {}...".format(cookieValue[:50]))
        # cookie值保存到配置文件
        rwParams.write_ini_file(section="LOGIN_COOKIE", option=option, value=cookieValue)

    def set_cookie(self, option):
        """
        设置携带cookie访问网页
        :param option: 索要获取的cookie对应key值
        :return:
        """
        cookieStr = rwParams.read_ini_file(section="LOGIN_COOKIE", option=option)
        # 保存的cookie值中需要把 $ 字符替换为 % 字符, 且转化为原格式
        cookieValue = eval(cookieStr.replace("$", "%"))
        # 添加cookie, 原格式是个列表循环添加
        [self.driver.add_cookie(cookie) for cookie in cookieValue]
        Log.info("给浏览器添加cookie值: {}...".format(cookieStr[:50]))

    def del_cookie(self):
        """删除cookie"""
        self.driver.delete_all_cookies()
        Log.info("删除当前添加的所有cookie值")

    @property
    def origin_driver(self):
        """返回原生驱动"""
        return self.driver


if __name__ == '__main__':
    p = PySelenium(openType="pc")
    p.open_url(url="http://mer1.crmeb.net/admin/merchant/list")
    p.sleep(2)
    p.input_keyword('xpath->(//input[@name="username"])[1]',"admin2")
    p.input_keyword('xpath->//input[@name="password"]',"11111111")
    p.input_keyword('xpath->(//input[@name="username"])[2]',"code")
    p.click_button('xpath->//span[contains(text(),"登录")]')