# -*- coding:utf-8 -*-
# 本程序用于显示图片的直方图
import cv2  # 导入opencv模块
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("girls_1_1.png")  # 导入图片，图片放在程序所在目录
cv2.namedWindow("imagshow", 2)  # 创建一个窗口
cv2.imshow('imagshow', img)  # 显示原始图片

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
# plt.hist(gray.ravel(), 256, [0, 256])  # 计算灰度直方图
# plt.show()

# RGB
color = ('b', 'g', 'r')  # 颜色分量
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])  # 计算颜色分量直方图
    plt.plot(histr, color=col)  # 绘制直方图
    plt.xlim([0, 256])

plt.show()  # 显示直方图

cv2.waitKey()