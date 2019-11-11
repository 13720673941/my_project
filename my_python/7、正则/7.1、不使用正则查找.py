# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2019/11/10 0:52


"""
[1]: 不用正则表达式查找文本,电话格式为 444-555-7890
"""

def phone_number(text):

    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():# 如果字符串只包含数字字符且非空 返回True
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


print(phone_number(text="444-555-7890")) # 格式相同返回 True
print(phone_number(text="aaa111222333")) # 格式不同返回 False

"""
[2]: 调用上面封装的非正则遍历函数，查找字符串中的电话
"""

# 在一串字符中查找上面的格式电话

message = "This is my phone number: 444-555-7890,my email is: 888-999-0000"

for i in range(0,len(message)):

    # 定义查找的字段范围 12 位
    check_text = message[i:i+12]

    # 调用上面的函数如果返回真就是找到了
    if phone_number(check_text):

        print("check number are: %s"%(check_text))

print("Finish!")
