import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/3.jpg")
#cv.imshow("Cat",img)

# convert image in the gray format

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)



# Simple thresholding
# look each pixel on the iamge and comper if that pixel is above 150 in this case change this pixel to 255 
# on the other case pixel stay the same

# thresh - binorized image
# threshold -  the same values that we pased 150
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # change parameters in the fucntion to figurout what happens with it

#cv.imshow("threshold",thresh)

# invers thrashold
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("threshold_invers",thresh_inv)


# Adapted thrashold - We give the oportunity to pc to specify the optimal threshold value by own.

adaptiv_thresold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 3) # 7 is used fot kernel size, and 3 is for  fine tunning 
cv.imshow("adaptive Threshold", adaptiv_thresold)















cv.waitKey(0)