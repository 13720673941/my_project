# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/10 21:48

"""
框架公共参数配置文件
"""


class SysConfig:
    """框架系统配置文件信息"""

    # win谷歌浏览器注册表路径
    chrome_reg = r"Software\Google\Chrome\BLBeacon"
    # 淘宝谷歌驱动下载页面链接
    down_driver_url = "https://npm.taobao.org/mirrors/chromedriver/"


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


if __name__ == '__main__':
    print(FilePathConfig.CHROME_DRIVER_PATH)
