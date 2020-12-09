# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/6 2:24

"""
项目中所有文件夹路径配置
"""

import os

# 项目相对跟目录路径
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 输出日志保存文件夹路径
LOG_SAVE_PATH = os.path.join(PROJECT_PATH, "result", "log")
# 项目配置文件路径
PROJECT_CONFIG_PATH = os.path.join(PROJECT_PATH, "config", "projectConfig.ini")
# 测试用例保存文件路径
TEST_CASE_EXCEL_PATH = os.path.join(PROJECT_PATH, "case", "case.xls")


if __name__ == '__main__':
    # 测试代码
    print(LOG_SAVE_PATH)
