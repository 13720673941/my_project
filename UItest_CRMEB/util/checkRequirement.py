# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/13 22:02

"""
检查安装本地电脑脚本执行依赖文件并下载安装
"""

import os
import sys

from util.logConfig import Logger
from config.varConfig import *

Log = Logger().logger


class CheckRequired:

    @classmethod
    def check_required_libraries(cls):
        """检查本地依赖库并自动下载安装"""
        cls.check_python_version()
        # 获取本地安装的依赖所有库
        resLb = cls.run_pip(cmd="list").split("\n")
        newResLb = [rl.rstrip(" ").split(" ") for rl in resLb]
        # 获取框架依赖库版本信息
        with open(FilePathConfig.REQUIREMENTS_PATH, "r") as f:
            requirements = f.readlines()
        newRequirementLs = [req.strip("\n") for req in requirements]
        for rb in newRequirementLs:
            for lb in newResLb:
                if rb.split("==")[0] == lb[0]:
                    if rb.split("==")[1] == lb[-1]:
                        Log.info("{} 依赖库版本检测成功！".format(rb))
                    else:
                        Log.warning("{} 依赖库版本检测失败！".format(rb))
                        cls.install_required_library(rb)
                    break
            else:
                Log.warning("本地没有检测到：{} 依赖文件".format(rb))
                cls.install_required_library(rb)
        pass

    @classmethod
    def run_pip(cls, cmd, runType=1):
        """运行pip命令"""
        if sys.platform[:3] == "win":
            pip = "pip"
        # """可以加入其他系统的命令判断"""
        else:
            raise Exception("当前框架不支持该电脑系统：{}".format(sys.platform))
        # 检查本地安装依赖版本
        try:
            if runType == 1:
                res = os.popen("{} {}".format(pip, cmd)).read()
            else:
                res = os.system("{} {}".format(pip, cmd))
            # Log.info("执行pip命令：{} {}".format(pip, cmd))
        except Exception:
            raise Exception("pip 命令运行出错，请检查是否配置pip环境变量！")

        return res

    @classmethod
    def install_required_library(cls, library):
        """安装所依赖的库文件"""
        Log.info("本地依赖库：{} 正在安装...".format(library))
        status = cls.run_pip(cmd="install {}".format(library), runType=2)
        if status == 0:
            Log.info("{} 安装成功！".format(library))
        else:
            raise Exception("{} 安装失败！请手动安装！".format(library))

    @classmethod
    def check_python_version(cls):
        """检查本地python版本"""
        try:
            res = os.popen("python --version").read().strip("\n")
        except Exception:
            raise Exception("没有安装python，或没有配置环境变量！")
        # 判断python版本，python 3以上版本
        pyVer = res.split(" ")[1].split(".")
        if int(pyVer[0]) > 2:
            Log.info("本地安装python版本检测成功：{} ".format(res))
        else:
            raise Exception("本框架执行脚本python 3版本！当前版本：{}".format(res))


if __name__ == '__main__':
    CheckRequired.check_required_libraries()
