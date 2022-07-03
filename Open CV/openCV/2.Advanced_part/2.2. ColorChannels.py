import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#  How to split and merge color channels in CV
# Use a image and split it into the R-B-G channals

img = cv.imread("./Photos/3.jpg")
#cv.imshow("Image",img)
# this function is gonna return three grayscale images, which correspond to the distribution of pixel intensities depending on R,G,B color level
# the region where is darker represent a little or no pixels of the specific channel on the image and opposite for the bright area on the given images
b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2],dtype="uint8")

#cv.imshow("Blue",b)
#cv.imshow("Red",r)
#cv.imshow("Green",g)

# print the shape of images up
print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

# merge with the blank image
merge_blank = cv.merge([b,blank, blank])
cv.imshow("blue_chanal",merge_blank)


# let's merge this three color channal 

merge = cv.merge([b,g,r])
cv.imshow("merge",merge)


cv.waitKey(0)