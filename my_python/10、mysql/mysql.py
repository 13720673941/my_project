# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/6/28 13:03
import pymysql

#链接数据库  "数据库地址","用户名","密码","数据库名字"
db = pymysql.connect("127.0.0.1","root","","test")

#创建一个实例游标
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)#输出的都是字典格式


#增删改 一定要提交 commit
cursor.execute("INSERT INTO mytest(id,name) values ('2','dpf')")
cursor.fetchall()
db.commit()

cursor.execute("SELECT * FROM mytest") #sql语句

#执行sql
a = cursor.fetchall()

print(a)


cursor.close()
db.close()

