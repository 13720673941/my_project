# -*- coding: utf-8 -*-

# @Project : DDT_FrameWork
# @Author  : Mr.Deng
# @Time    : 2021/8/22 0:00

"""
检查本地谷歌浏览器驱动版本，项目中存在匹配版本可直接运行项目，不匹配的驱动进行重新下载匹配驱动
"""

from config.filePathConfig import chromeDriverPath, configDataPath
from config.variableConfig import VariableConfig
from public.common.logConfig import Logger
from public.common.readWriteData import ReadWriteData

import os
import winreg
import requests
import zipfile
import re

# 实例化日志类
Log = Logger().origin_logger


class CheckDriverVersion:

    @classmethod
    def get_chrome_version(cls):
        """
        获取本地chrome浏览器版本号
        :return:
        """
        if VariableConfig.SYSTEM_PLATFORM[:3] == "win":
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, VariableConfig.CHROME_REG)
                localChromeVersion = winreg.QueryValueEx(key, "version")[0]
                Log.info("检测本地谷歌浏览器版本为：{} ".format(localChromeVersion))
            except:
                raise Exception(
                    "浏览器版本检测失败！！！请检查variableConfig.py文件中CHROME_REG注册表路径：{} 是否正确！".format(VariableConfig.CHROME_REG))
        else:
            raise Exception("本地机器系统版本：{} 不支持运行该测试脚本！！！".format(VariableConfig.SYSTEM_PLATFORM))
        # 解析返回浏览器大版本号
        return localChromeVersion

    @classmethod
    def check_local_driver(cls, chromeVersion):
        """
        检测本地浏览器驱动是否匹配
        :param chromeVersion: 浏览器版本号
        :return:
        """
        findDriverPath = None
        # 获取本地config->driver目录下所有驱动文件，过滤驱动文件
        driverFileList = [file for file in os.listdir(chromeDriverPath) if file.endswith(".exe")]
        # 固定驱动名称，谷歌浏览器版本_chromedriver.exe，遍历驱动文件匹配本地浏览器版本
        for driver in driverFileList:
            if chromeVersion.split(".")[0] == driver.split("_")[0]:
                findDriverPath = chromeDriverPath + driver
                Log.info("项目驱动中已匹配到本地chrome浏览器对应驱动版本：{} ".format(findDriverPath))
                return True, findDriverPath
        else:
            return False, findDriverPath

    @classmethod
    def down_chrome_driver(cls, chromeVersion):
        """
        检测本地项目中是否存在匹配的驱动，不存在的话就在线搜索下载
        :param chromeVersion: 浏览器版本号
        :return:
        """
        # 本地没有找到去下载对应版本的谷歌浏览器驱动
        try:
            downListPage = requests.get(url=VariableConfig.DOWN_DRIVER_URL).text
            Log.info("项目中没有匹配到对应本地谷歌浏览器驱动，正在启动在线下载，请稍后...")
        except:
            raise Exception("淘宝下载谷歌浏览器驱动接口链接超时！！！，请手动检查：{}".format(VariableConfig.DOWN_DRIVER_URL))
        # 正则匹配浏览器对应大版本，查找子下载路径
        findChromeVersionList = re.compile('<a href="/mirrors/chromedriver/(.*?)/">').findall(downListPage)
        # 判断本地浏览器版本是否在列表中，不在的话就匹配最大版本第一个
        if chromeVersion in findChromeVersionList:
            downChromeDriverVersion = chromeVersion
        else:
            for findChromeVersion in findChromeVersionList:
                if findChromeVersion.split(".")[0] == chromeVersion.split(".")[0]:
                    downChromeDriverVersion = findChromeVersion
                    break
            else:
                raise Exception("没有找到本地浏览器所对应驱动版本：{} 信息，请手动下载！！！".format(chromeVersion))
        pass
        # 组合驱动下载url下载文件
        findChromeDownUrl = "{}{}/chromedriver_win32.zip".format(VariableConfig.DOWN_DRIVER_URL,
                                                                 downChromeDriverVersion)
        # 写入驱动数据文件路径
        writeChromeDriverFilePath = "{}chromedriver.zip".format(chromeDriverPath)
        # 请求下载url二进制写入本地
        try:
            driverUnzipFile = requests.get(url=findChromeDownUrl)
            with open(writeChromeDriverFilePath, "wb") as fp:
                fp.write(driverUnzipFile.content)
            Log.info("本地谷歌浏览器驱动对应版本下载成功，路径：{}".format(writeChromeDriverFilePath))
        except:
            raise Exception("下载驱动接口链接超时，驱动下载失败，请手动下载！！！")

        return writeChromeDriverFilePath

    @classmethod
    def process_down_zipFile(cls, zipFilePath, chromeVersion):
        """
        解压处理下载文件，解压-》重命名-》删除原文件
        :param zipFilePath: 压缩文件目录
        :param chromeVersion: 浏览器版本号
        :return:
        """
        # 判断文件格式是否为zip压缩文件
        global zipChildFile
        if zipfile.is_zipfile(zipFilePath):
            Log.info("正在解压压缩文件：{}，请稍后...".format(zipFilePath))
            zipFile = zipfile.ZipFile(zipFilePath)
            zipList = zipFile.namelist()
            for zipChildFile in zipList:
                zipFile.extract(zipChildFile, path=chromeDriverPath)
            zipFile.close()
        else:
            raise Exception("解压压缩文件格式非zip，请检查后再试！！！文件目录：{}".format(zipFilePath))

        # 重新命名解压的驱动文件名称
        oldFileName = "{}{}".format(chromeDriverPath, zipChildFile)
        newFileName = "{}{}_chromedriver.exe".format(chromeDriverPath, chromeVersion.split(".")[0])
        os.rename(oldFileName, newFileName)
        Log.info("旧文件：{} 重新命名 -> 新文件：{}_chromedriver.exe".format(zipChildFile, chromeVersion.split(".")[0]))

        # 删除已下载驱动压缩文件
        os.remove(zipFilePath)
        Log.info("删除下载压缩文件：{} ".format(zipFilePath))

        return newFileName

    @classmethod
    def check_driver_version(cls):
        """
        检查本地谷歌浏览器版本，匹配项目驱动，不存在的重新下载解压
        :return:
        """
        localChromeVersion = cls.get_chrome_version()
        isHave, driverPath = cls.check_local_driver(chromeVersion=localChromeVersion)
        if isHave:
            driverConfigPath = driverPath
        else:
            # 在线下载谷歌驱动文件
            downZipFilePath = cls.down_chrome_driver(chromeVersion=localChromeVersion)
            processZipFilePath = cls.process_down_zipFile(zipFilePath=downZipFilePath, chromeVersion=localChromeVersion)
            driverConfigPath = processZipFilePath

        # 项目本地谷歌浏览器驱动路径写入配置文件
        ReadWriteData(configDataPath).write_config_data(section="CHROME_DRIVER_PATH", option="path",
                                                        value=driverConfigPath)


if __name__ == '__main__':
    CheckDriverVersion.check_driver_version()
