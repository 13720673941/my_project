# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/12/10 13:58

"""
检查本地电脑是否安装谷歌浏览器，根据浏览器版本自动匹配下载对应的驱动
"""

import sys
import winreg
import os
import requests
import re
import zipfile


from config.pathConfig import *
from public.common import logConfig
from public.common.rwFile import RWFile

Log = logConfig.Log()

downUrl = "https://npm.taobao.org/mirrors/chromedriver/"


class Chrome:

    @classmethod
    def set_chrome(cls):
        """获取浏览器版本"""
        if sys.platform[:3] == "win":
            try:
                # 查询系统谷歌浏览器注册表中的key
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
                # 获取谷歌浏览器版本号
                chrome_ver = winreg.QueryValueEx(key, "version")[0]
                Log.info("系统检测您的系统是：windows，谷歌浏览器版本号是：{} ".format(chrome_ver))
            except Exception:
                raise Exception(
                    "谷歌浏览器注册表信息查询失败，请检查 config->varConfig.py文件中注册表路径是否正确！")
        else:
            raise Exception("本框架当前只支持windows系统谷歌浏览器驱动自动下载！")
        isFind, filePath = cls.search_local_ver(chrome_ver)
        if isFind:
            findDriverPath = filePath
        else:
            fileVer = cls.search_online_ver(chrome_ver)
            findDriverPath = cls.down_driver(fileVer)

            # 检测正确的浏览器驱动保存到connectParam.ini配置文件中, 驱动直接读取文件路径
            rwParams = RWFile()
            rwParams.write_config_file(CONFIG_DATA_PATH, "DRIVER_PATH", "PATH", findDriverPath)

        return findDriverPath

    @classmethod
    def search_local_ver(cls, chromeVer):
        """搜索本地驱动版本"""
        # 先检查本地驱动文件夹是否存在当前浏览器版本的驱动
        localDriverList = os.listdir(CHROME_DRIVER_PATH)
        for driverName in localDriverList:
            if chromeVer.split(".")[0] == driverName.split("_")[0]:
                Log.info("本地找到对应浏览器版本的驱动文件，浏览器版本：{}，驱动版本：{}".format(chromeVer, driverName))
                return True, "{}\\{}".format(CHROME_DRIVER_PATH, driverName)
        else:
            Log.info("本地浏览器驱动文件夹中没有找对对应版本，正在在线搜索对应版本...")
            return False, None

    @classmethod
    def search_online_ver(cls, chromeVer):
        """搜索谷歌浏览器对应驱动"""
        try:
            # 获取全部驱动名称列表信息，查找对应版本
            downPageText = requests.get(url=downUrl).text
            print(downPageText)
        except Exception:
            raise Exception("淘宝下载接口可能挂了 😭~~~~")
        # 正则匹配所有浏览器版本号信息
        searchVerList = re.compile('/mirrors/chromedriver/(.*?)/">').findall(downPageText)
        if chromeVer in searchVerList:
            fileVer = chromeVer
        else:
            for verName in searchVerList:
                # 默认查找第一个大版本对应驱动就行
                if chromeVer.split(".")[0] == verName[:2]:
                    fileVer = verName
                    break
            else:
                raise Exception("在线查找没有找到对应驱动版本，当前浏览器版本：{}".format(chromeVer))
        return fileVer

    @classmethod
    def down_driver(cls, fileVer):
        """下载谷歌浏览器对应驱动"""
        if sys.platform[:3] == "win":
            file = "chromedriver_win32.zip"
        else:
            raise Exception("本框架当前只支持windows系统谷歌浏览器驱动自动下载！")
        # 组合下载路径
        try:
            res = requests.get(url="{}{}/{}".format(downUrl, fileVer, file))
            Log.info("正在下载谷歌浏览器版本对应驱动文件，请稍后...")
        except Exception:
            raise Exception("淘宝下载接口可能挂了 😭~~~~")
        # 下载文件保存路径
        downPath = "{}\\{}_ver_{}".format(CHROME_DRIVER_PATH, fileVer.split(".")[0], file)
        # 下载文件已二进制格式写入保存.zip类型
        with open(downPath, "wb") as f:
            f.write(res.content)
        Log.info("驱动下载成功保存路径：{}".format(downPath))
        fileName = cls.unzip_file(downPath)
        newFileName = cls.rename_file(fileName, fileVer)
        cls.del_zip_file(downPath)

        return newFileName

    @classmethod
    def unzip_file(cls, filePath):
        """解压下载的驱动zip文件"""
        file = None
        if zipfile.is_zipfile(filePath):
            zipFile = zipfile.ZipFile(filePath)
            fileList = zipFile.namelist()
            for file in fileList:
                zipFile.extract(file, CHROME_DRIVER_PATH)
                Log.info("正在解压驱动.zip文件...")
            zipFile.close()
        else:
            raise Exception("压缩文件是个无效的文件！{}".format(filePath))

        return file

    @classmethod
    def rename_file(cls, filePath, fileVer):
        """重命名解压过的驱动文件"""

        oldFileName = "{}\\{}".format(CHROME_DRIVER_PATH, filePath)
        newFileName = "{}\\{}_ver_{}".format(CHROME_DRIVER_PATH, fileVer.split(".")[0], filePath)
        try:
            os.rename(oldFileName, newFileName)
            Log.info("修改解压文件名称：{} -> {}".format(filePath, fileVer.split(".")[0]+filePath))
        except Exception:
            raise Exception("文件重新命名异常，原文件不存在或者新文件保存路径异常！")

        return newFileName

    @classmethod
    def del_zip_file(cls, filePath):
        """删除下载的压缩文件"""
        try:
            os.remove(filePath)
            Log.info("正在删除下载的.zip驱动文件...")
        except Exception:
            raise Exception("请检查所删除的文件路径是否正确！{}".format(filePath))


if __name__ == '__main__':
    from selenium import webdriver
    driverPath = Chrome.set_chrome()
    driver = webdriver.Chrome(executable_path=driverPath)
    driver.get("https://www.baidu.com")
