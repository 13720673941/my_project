# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2021/1/17 22:35

import os


class FilePathConfig:
    """框架文件夹路径配置文件"""

    # 项目相对跟目录路径
    PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 输出日志保存文件夹路径
    LOG_SAVE_PATH = os.path.join(PROJECT_PATH, "result", "log")
    # 错误日志保存路径
    ERROR_LOG_PATH = os.path.join(PROJECT_PATH, "traceback.log")
    # 错误截图保存路径
    ERROR_IMG_SAVE_PATH = os.path.join(PROJECT_PATH, "result", "errorImg")
    # 项目配置文件路径
    PROJECT_CONFIG_PATH = os.path.join(PROJECT_PATH, "config", "projectConfig.ini")
    # 测试用例保存文件路径
    TEST_CASE_EXCEL_PATH = os.path.join(PROJECT_PATH, "data", "case.xls")
    # 浏览器驱动存放文件夹路径
    CHROME_DRIVER_PATH = os.path.join(PROJECT_PATH, "config", "driver")
    # 项目关联参数保存文件
    PROJECT_CONNECT_PARAM_PATH = os.path.join(PROJECT_PATH, "config", "connectParam.ini")
    # 依赖文件保存路径
    REQUIREMENTS_PATH = os.path.join(PROJECT_PATH, "requirements.txt")
