import cv2
import numpy as np
# Reading the Image
image = cv2.imread("IMG_20201122_001937.jpg")
# Finding the Edges of Image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 7)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
# Making a Cartoon of the image
color = cv2.bilateralFilter(image, 12, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
#Visualize the cartoon image
# cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)  # "0" is Used to close the image window
cv2.destroyAllWindows()


#convert to gray scale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# #apply gaussian blur
grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
# #detect edges
edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
edgeImage = 255 - edgeImage
#threshold image
ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)
#blur images heavily using edgePreservingFilter
edgePreservingImage = cv2.edgePreservingFilter(image, flags=2, sigma_s=50, sigma_r=0.4)
#create output matrix
output =np.zeros(grayImage.shape)
# #combine cartoon image and edges image
output = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)
#Visualize the cartoon image
# cv2.imshow("Cartoon", output)
cv2.waitKey(0) # "0" is Used to close the image window
cv2.destroyAllWindows()


cartoon_image = cv2.stylization(image, sigma_s=150, sigma_r=0.25)
# cv2.imshow('cartoon', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cartoon_image1, cartoon_image2  = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
# cv2.imshow('pencil', cartoon_image1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('pencil', cartoon_image2)
cv2.waitKey()
cv2.imwrite('./1.jpg', cartoon_image2)
cv2.destroyAllWindows()

