import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# switching between color spaces 

img = cv.imread("./Photos/3.jpg")
#cv.imshow("Image",img)
#plt.imshow(img)
#plt.show()


# BRG -> GrayScale
# grayscale image representation can be used to determine the pixel intensity of an image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# BGR -> HSV("hue saturation value"-> basically, it's a kind of based on how humans think and conceive of colors)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HLS)
#cv.imshow("hsv",hsv)

#BGR -> L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow("lab",lab)


# BGR -> RBG

rbg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow("RBG", rbg)

# ------ now we can do inverse------
# GrayScale  -> BRG
# HSV -> BGR
# lab -> BGR
# RGB -> BGR
# Downsides:  we can't convert Grayscale -> HSV directly. The proper way to do this is: Grayscale->BGR->HSV
#Let's try this: 
HVS_BGR = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow("LAB->BGR", LAB_BGR)
LAB_BGR = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
#cv.imshow("HVS->BGR", HVS_BGR)
GrayBGR = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
cv.imshow("GRAY->BGR",GrayBGR)



cv.waitKey(0)