# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 17:36


"""
正则表达式中符号的表示意思
"""

"""

1、\d    表示数字字符，即任何一位 0-9 的数字
2、()    表示在正则表达式中创建分组，一个括号表示一个分组使用group方法传入参数 1 即第一个分组
3、|     正则表达式中称：“管道” 表示 或 的意思，即查找任意一个字段找到结束代码
4、()?   表示括号里面的字段可有可无，无论括号里面的字段是否存在只要前后一致都会返回
5、()*   表示匹配零次或者多次，括号里面重复出现且前后匹配一致的都可以返回
6、()+   表示括号里面的字段至少出现一次或者多次，不存在的话返回None
7、{}    正则中传入数字表示重复几次可以传入范围，(){,3}表示0-3次实例，(){3,}表示3-无限次实例，(){3,8}表示3-8次实例
8、{}?   表示{}中传递的字符长度取最短字符，(){3,5}? 表示匹配出来的取 3 个字符长度
9、\D    表示除0-9数字以外的任何字符
10、\w   小写表示任何字母、数字或下划线字符可以认为是匹配单词字符
11、\W   大写表示除字母、数字和下划线以外的任何字符
12、\s   小写表示空格、制表符和换行符
13、\S   大写表示除空格、制表符和换行符以外的字符
14、[]   里面匹配自己的字符分类规则例如：[0-9] 匹配 0-9 数字 [^]匹配非字符类，例如：[^a-z] 匹配除a-z小写以外的所有字符
15、^    表达式中加上 ^ 表示以什么开头的字符串例如：\d+^ 以数字开始的字符串
16、$    表示以什么结束的字符串，例如：\d+$ 表示以数字结束的字符串


"""


# 1、. 匹配任意除换行符“\n”外的字符；
# 2、*表示匹配前一个字符0次或无限次；
# 3、+或*后跟？表示非贪婪匹配，即尽可能少的匹配，如*？重复任意次，但尽可能少重复；
# 4、 .*? 表示匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
# 如：a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，它会匹配aab和ab。

