import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread("./Photos/3.jpg")
cv.imshow("Image",img)

# Bluer by averaging

average = cv.blur(img, (7,7))
cv.imshow("Avaeraging Bluer", average)

# Gaussian blur

gauss = cv.GaussianBlur(img,(7,7), sigmaX= 0 ) #sigmaX standard deviation in the x direction
cv.imshow("Gaussian_blue", gauss)

# Median blue

median = cv.medianBlur(img, 7) # kernel size is here just a number 

cv.imshow("median", median)


# Bilateral blur 
# sigmaSpace - corresponding to the distance of the pixel on the image that will affect the "middle" (main) one.
bilateral = cv.bilateralFilter(img, d=5,sigmaColor=15, sigmaSpace=50)
cv.imshow("Bilateeral", bilateral)

cv.waitKey(0)