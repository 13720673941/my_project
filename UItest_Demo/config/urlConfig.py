# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/15 9:53

from public.common.rwFile import RWFile
from config.pathConfig import *

rw = RWFile()
# 获取配置文件中环境切换的值
environmentNum = rw.read_config_file(CONFIG_DATA_PATH,"ENVIRONMENT","EN_TYPE_NUMBER")
if environmentNum == "1":
    Host = rw.read_config_file(CONFIG_DATA_PATH,"ENVIRONMENT","OFFICIAL_EN")
elif environmentNum == "2":
    Host = rw.read_config_file(CONFIG_DATA_PATH,"ENVIRONMENT","TEST_EN")
else:
    raise NameError("HOST 地址参数传入有误！允许字段：正式环境 1 ，测试环境 2 ")

# web 页面路由拼接
# 例如：百度更多模块展示页面
BAI_DU_SEARCH = Host+"/more/"
