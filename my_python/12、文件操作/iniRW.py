# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/5/23 11:23

"""

    .ini 类型配置文件的读写 依赖于 configparser 库

"""

from configparser import ConfigParser

# 文件路径
filePath = "initest.ini"

# 实例化类
cf = ConfigParser()

# 写入配置文件 前提是先要确定 section 和 option 参数
cf.read(filePath,encoding="utf-8")
cf.set(section="test001",option="username",value="111111")
# 写入
with open(filePath,"w",encoding="utf-8") as f:
    cf.write(f)

# 读取文件
value = cf.get(section="test001",option="username")
print(value)

# 添加section option
cf.add_section("test002")
cf.set(section="test002",option="username",value="222222")
# 写入
with open(filePath,"w",encoding="utf-8") as f:
    cf.write(f)