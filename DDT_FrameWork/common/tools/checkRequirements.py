# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 23:39

"""
检测本地python版本，及项目相关依赖文件，并下载安装
"""

from config.filePathConfig import requirementsPath
from common.tools.checkDriverVersion import SYSTEM_PLATFORM
from common.tools.logConfig import Logger
from common.tools.operateTxtData import OperateTxtData

import os

Log = Logger().origin_logger


class CheckRequirements:

    @classmethod
    def check_python_version(cls):
        """
        检测python版本，低于 3的不支持运行该测试项目
        :return:
        """
        if SYSTEM_PLATFORM[:3] == "win":
            pythonVersionNumber = os.popen("python --version").read().split(" ")[1].strip("\n")
        else:
            raise Exception(f"该项目程序不支持本地电脑系统平台：{SYSTEM_PLATFORM} ！！！")
        # 判断python3版本，低于 3的不支持运行该测试项目
        pythonBigVersionNum = pythonVersionNumber.split(".")[0]
        if int(pythonBigVersionNum) >= 3:
            Log.info(f"检测本地python版本为：{pythonVersionNumber}，可以运行该测试项目")
        else:
            raise Exception(f"本地安装python版本：{pythonVersionNumber}不符合项目运行要求，请手动安装！！！")

    @classmethod
    def pip_install(cls, library: str):
        """
        pip命令在线安装依赖
        :return:
        """
        try:
            installResult = os.system(f"pip install {library}")
            Log.info(f"系统正在安装项目依赖库：{library}，请稍后...")
        except:
            raise Exception(f"项目依赖库：{library} 安装超时请手动安装！！！")
        # os.system 返回状态 0，及安装成功
        if installResult == 0:
            Log.info(f"项目依赖库：{library} 安装成功！")
        else:
            raise Exception(f"项目依赖库：{library} 安装失败请手动安装！！！")

    @classmethod
    def check_install_requirements(cls):
        """
        检测本地需要安装的依赖文件项目
        :return:
        """
        # 先获取项目所需依赖列表
        needInstallReqList = OperateTxtData(requirementsPath).read_txt_data()
        # 获取本地安装相关依赖列表
        alreadyInstallReqResult = os.popen("pip list").read().split("\n")
        # 数据处理去掉列表中字符右边最后的空格
        alreadyInstallReqResultLs = [req.rstrip(" ") for req in alreadyInstallReqResult]
        # 循环两个列表判断所需安装依赖是否在列表中
        for needInstallReq in needInstallReqList:
            for alreadyInstallReq in alreadyInstallReqResultLs:
                if needInstallReq.split("==")[0] in alreadyInstallReq:
                    if needInstallReq.split("==")[1] == alreadyInstallReq.split(" ")[-1]:
                        Log.info(f"检测项目所需依赖版本：{needInstallReq} 已安装，可正常运行")
                    else:
                        cls.pip_install(library=needInstallReq)
                    break
            else:
                cls.pip_install(library=needInstallReq)
        pass

    @classmethod
    def check_requirements(cls):
        """
        检查python版本，检测项目依赖对应版本安装
        :return:
        """
        cls.check_python_version()
        cls.check_install_requirements()


if __name__ == '__main__':
    CheckRequirements().check_requirements()
