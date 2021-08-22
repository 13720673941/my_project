# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 0:10

"""
项目全局变量控制文件
"""

import sys


class VariableConfig:
    # 系统平台名称
    SYSTEM_PLATFORM = sys.platform
    # 谷歌浏览器本地注册表路径
    CHROME_REG = r"Software\Google\Chrome\BLBeacon"
    # 淘宝谷歌驱动下载页面链接
    DOWN_DRIVER_URL = "https://npm.taobao.org/mirrors/chromedriver/"


if __name__ == '__main__':
    var = VariableConfig().SYSTEM_PLATFORM
    print(var)
