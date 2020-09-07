# -*- coding: utf-8 -*-

# @Author  : Mr.Deng
# @Time    : 2020/9/6 15:14

"""
    识别登录图片验证码，需要使用到的库，pytesseract.py pillow.py
    需要本地安装pytesseract_ocr图片识别客户端，配置环境变量
"""

import time,re
import pytesseract
from PIL import Image, ImageEnhance

def image_recognition(imagePath="C:\\Users\\kk\\Desktop\\123.png"):
    # 获取验证码图片，读取验证码
    image_obj = Image.open(imagePath)
    img = image_obj.convert("L")  # 转灰度
    img.save("C:\\Users\\kk\\Desktop\\aaa.png")
    pixdata = img.load()
    w, h = img.size
    threshold = 160
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255

    image = img
    image.save("C:\\Users\\kk\\Desktop\\bbb.png")
    time.sleep(2)
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
    result = pytesseract.image_to_string(image)  # 图片转文字
    resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
    result_four = resultj[0:4]  # 只获取前4个字符
    # print(resultj)  # 打印识别的验证码
    print(result)


if __name__ == '__main__':
    image_recognition()