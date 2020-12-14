# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/13 22:02

"""
检查安装本地电脑脚本执行依赖文件
"""

import os
import sys

from util.logConfig import Logger
from config.varConfig import *

Log = Logger().logger


class Install:

    def check_local_file(self):
        """检查本地依赖文件是否安装"""

        if sys.platform[:3] == "win":
            pip = "pip"
        else:
            raise Exception("当前框架不支持该电脑系统：{}".format(sys.platform))
        # 检查本地安装依赖版本
        try:
            res = os.popen("{} list".format(pip)).read()
        except Exception:
            raise Exception("pip 命令运行出错，请检查是否配置pip环境变量！")
        # 获取框架依赖库版本信息
        with open(FilePathConfig.REQUIREMENTS_PATH, "r") as f:
            requirements = f.readlines()
        for i in requirements:
            for j in res.split("\n"):
                if i.split(">=")[0] == j.strip(" ").split(" ")[0]:
                    if i.split(">=")[1].strip("\n") == j.rstrip(" ").split(" ")[-1]:
                        Log.info("{} 依赖库版本检测成功！".format(i.strip("\n")))
                    else:
                        Log.info("{} 依赖库版本检测失败！".format(i.strip("\n")))
                        # 卸载已安装版本
                        """"""
            else:
                # 直接安装
                pass


if __name__ == '__main__':
    Install().check_local_file()