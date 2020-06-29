# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/6/17 16:39

"""
    数据库操作封装 默认mysql
"""

from config.configVar import *
from common.logConfig import Log
import pymysql
log = Log()

# 获取配置文件中数据库信息
NAME = DataBaseConfig.DB_NAME
HOST = DataBaseConfig.DB_HOST
USER = DataBaseConfig.DB_USERNAME
PASSWORD = DataBaseConfig.DB_PASSWORD
PORT = DataBaseConfig.DB_PORT

class DataBaseVerify():

    def __init__(self):
        try:
            # 连接数据库
            self.db = pymysql.connect(
                database=NAME,host=HOST,user=USER,password=PASSWORD,port=int(PORT))
            log.info("连接数据库：{} ".format(NAME))
        except:
            log.error("数据库：{} 连接失败！！！".format(NAME))
            raise
        # 创建一个实例游标输出字典格式
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def _select(self,sql):
        """执行sql语句返回查询结果"""
        try:
            # 创建sql语句
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            log.info("执行SQL语句：{} ".format(sql))
            return res
        except:
            log.error("SQL语句执行失败！！！")
            raise

    def _other(self,sql):
        """执行其他sql语句需要进行commit提交"""
        try:
            # 创建sql语句
            self.cursor.execute(sql)
            self.cursor.fetchall()
            self.db.commit()
            log.info("执行SQL语句：{} ".format(sql))
        except:
            log.error("SQL语句执行失败！！！")
            raise

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    
    d = DataBaseVerify()

    a = d._select('SELECT department.departmentid FROM department')

    print(a)