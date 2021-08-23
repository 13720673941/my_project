# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 23:39

"""
检测本地python版本，及项目相关依赖文件，并下载安装
"""

from config.filePathConfig import requirementsPath
from public.common.checkDriverVersion import SYSTEM_PLATFORM
from public.common.logConfig import Logger

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
            raise Exception("该项目程序不支持本地电脑系统平台：{} ！！！".format(SYSTEM_PLATFORM))
        # 判断python3版本，低于 3的不支持运行该测试项目
        pythonBigVersionNum = pythonVersionNumber.split(".")[0]
        if int(pythonBigVersionNum) >= 3:
            Log.info("检测本地python版本为：{}，可以运行该测试项目".format(pythonVersionNumber))
        else:
            raise Exception("本地安装python版本：{}不符合项目运行要求，请手动升级！！！".format(pythonVersionNumber))

    @classmethod
    def pip_install(cls, library):
        """
        pip命令在线安装依赖
        :return:
        """
        try:
            installResult = os.system("pip install {}".format(library))
            Log.info("系统正在安装项目依赖库：{}，请稍后...".format(library))
        except:
            raise Exception("项目依赖库：{} 安装超时请手动安装！！！".format(library))
        # os.system 返回状态 0，及安装成功
        if installResult == 0:
            Log.info("项目依赖库：{} 安装成功！".format(library))
        else:
            raise Exception("项目依赖库：{} 安装失败请手动安装！！！".format(library))

    @classmethod
    def check_install_requirements(cls):
        """
        检测本地需要安装的依赖文件项目
        :return: 本地索要安装依赖列表
        """
        # 先获取项目所需依赖列表
        with open(requirementsPath, "r", encoding="utf-8") as f:
            # 数据处理，去掉换行符
            needInstallReqList = [lineData.strip("\n") for lineData in f.readlines()]
        # 获取本地安装相关依赖列表
        alreadyInstallReqResult = os.popen("pip list").read().split("\n")
        # 数据处理去掉列表中字符右边最后的空格
        alreadyInstallReqResultLs = [req.rstrip(" ") for req in alreadyInstallReqResult]
        # 循环两个列表判断所需安装依赖是否在列表中
        for needInstallReq in needInstallReqList:
            for alreadyInstallReq in alreadyInstallReqResultLs:
                # 判断名称
                if needInstallReq.split("==")[0] in alreadyInstallReq:
                    # 判断版本
                    if needInstallReq.split("==")[1] == alreadyInstallReq.split(" ")[-1]:
                        Log.info("检测项目所需依赖版本：{} 已安装，可正常运行".format(needInstallReq))
                    else:
                        # 已安装但是版本不一致，直接安装对应版本的项目依赖
                        cls.pip_install(library=needInstallReq)
                    break
            else:
                # 已经安装的项目中没有检索到对应依赖直接安装
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
