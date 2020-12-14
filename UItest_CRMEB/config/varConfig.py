# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/10 21:48

"""
框架公共参数配置文件
"""


class SysConfig:
    """框架公共变量配置文件"""

    # win谷歌浏览器注册表路径
    CHROME_REG = r"Software\Google\Chrome\BLBeacon"
    # 淘宝谷歌驱动下载页面链接
    DOWN_DRIVER_URL = "https://npm.taobao.org/mirrors/chromedriver/"
    # 启动浏览器类型
    BROWSER_TYPE = "chrome"


class FilePathConfig:
    """框架文件夹路径配置文件"""

    import os

    # 项目相对跟目录路径
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 输出日志保存文件夹路径
    LOG_SAVE_PATH = os.path.join(PROJECT_PATH, "result", "log")
    # 项目配置文件路径
    PROJECT_CONFIG_PATH = os.path.join(PROJECT_PATH, "config", "projectConfig.ini")
    # 测试用例保存文件路径
    TEST_CASE_EXCEL_PATH = os.path.join(PROJECT_PATH, "case", "case.xls")
    # 浏览器驱动存放文件夹路径
    CHROME_DRIVER_PATH = os.path.join(PROJECT_PATH, "config", "driver")
    # 依赖文件保存路径
    REQUIREMENTS_PATH = os.path.join(PROJECT_PATH, "requirements.txt")


if __name__ == '__main__':
    print(FilePathConfig.CHROME_DRIVER_PATH)
