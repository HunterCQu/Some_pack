import cv2


#读取图片


# cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
# cv2.IMREAD_GRAYSCALE：读入灰度图片
# cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
img = cv2.imread('girls_1_1.png',cv2.IMREAD_UNCHANGED)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#显示图像

cv2.imshow('image,',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #保存图像
# cv2.imwrite(file，img，num)保存一个图像。
# 第一个参数是要保存的文件名，第二个参数是要保存的图像。
# 可选的第三个参数，它针对特定的格式：对于JPEG，其表示的是图像的质量，
# 用0 - 100的整数表示，默认95;对于png ,第三个参数表示的是压缩级别。默认为3.

# #图像去噪
# gray = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# medina = cv2.medianBlur(gray, 41)
#
#
# #图像裁剪
# #[左上角x轴坐标:右下角x轴坐标,左上角y轴坐标:右下角y轴坐标]
# show_img_11 = img[50:150,50:150]
# plt.imshow(show_img_11)
# plt.show()
#
#
# #翻转图像，flipcode控制翻转效果。
# cv2.flip(img,flipcode)
# flipcode = 0：沿x轴翻转
# flipcode > 0：沿y轴翻转
# flipcode < 0：x,y轴同时翻转
#
#
# #彩色图像转为灰度图像
#
# img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#
# #灰度图像转为彩色图像
# img3 = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)