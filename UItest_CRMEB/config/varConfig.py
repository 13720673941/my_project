# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/10 21:48

"""
框架公共参数配置文件
"""

from config.filePathConfig import FilePathConfig


class SysConfig:
    """框架公共变量配置文件"""

    # ===============浏览器配置===============
    # win谷歌浏览器注册表路径
    CHROME_REG = r"Software\Google\Chrome\BLBeacon"
    # 淘宝谷歌驱动下载页面链接
    DOWN_DRIVER_URL = "https://npm.taobao.org/mirrors/chromedriver/"
    # 启动浏览器类型
    BROWSER_TYPE = "chrome"
    # 浏览器打开手机模式型号
    MOBILE_TYPE = "iPhone 8"
    # 查找元素最大时间
    FIND_TIMEOUT = 10

    # ===============日志配置===============
    import logging
    # 日志开关
    LOG_DEBUG = True
    # 日志格式
    LOG_FILE_FORMATTER = "%(asctime)s-[%(filename)s]-line: %(lineno)d %(levelname)s: %(message)s"
    LOG_CONSOLE_FORMATTER = "[%(filename)s]-line: %(lineno)d %(levelname)s: %(message)s"
    # 日志等级
    LOG_LEVEL = logging.INFO
    # 日志保存路径
    LOG_SAVE_PATH = FilePathConfig.LOG_SAVE_PATH
    # 写入方式
    LOG_MODE = "a"
    # 编码
    LOG_ENCODING = "utf-8"


class ExcelVariable:
    """excel数据表格中每列固定字段的索引"""

    # 固定字段行数
    systemNum = 0
    # caseOverView 表格字段列索引值
    testCaseNum = 0
    caseDescription = 1
    isRun = 2
    caseResult = 3
    # 用例步骤表格中列的索引值
    stepNum = 0
    stepDescription = 1
    pageName = 2
    funcName = 3
    elementPath = 4
    params = 5
    stepResult = 6


class BaoTaConfig:
    """项目安装宝塔配置信息"""

    BT_URL = "http://39.96.4.63:8888/site"
    BT_USERNAME = "zhenglu"
    BT_PASSWORD = "zhenglu123"


