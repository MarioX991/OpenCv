import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import _64Bit

img = cv.imread("./Photos/3.jpg")
#cv.imshow("Cat",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Laplasian method for edge detection

lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.abs(lap))

#cv.imshow("Laplasin",lap)


# Sobel

sobel_x = cv.Sobel(gray, cv.CV_64F, 1,0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0,1)

combined_sobel = cv.bitwise_and(sobel_x, sobel_y)


# Canny

canny = cv.Canny(gray, 150,175)
cv.imshow("Canny", canny)

cv.imshow("SOBEL_X",sobel_x)
cv.imshow("SOBEL_y",sobel_y)
cv.imshow("Combine_sobel", combined_sobel)








cv.waitKey(0)