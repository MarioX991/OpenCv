import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize

# Contours and Edges are two different things in the mathematical .

img = cv.imread("./Photos/3.jpg")
cv.imshow("Original",img)


# create a blank image to show contours that have been found on the image

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank",blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# bluer the image before we go for te contours

blue = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)



#cv.imshow("Gray",gray)
# edges
canny = cv.Canny(blue,125,175)
#cv.imshow("canny",canny)

# countoures 

# MODE:
# cv.RETR_TREE -  if we want all hierarchical countours 
# cv.RETR_EXTERNASL - all external countours
# cv. RERT_LIST - list od all countours on the img

# METHODS:
#cv.CHAIN_APPROX_NONE - how we want to approximating contours
# cv.CHAIN_APPROX_SIMPLE : ex: if we have the line on the image with this we get just two points that basicaly represent this line

# the function "cv.findContours" return two values: the country which is the array of all coordinates of the contours find on the image
# hierachies : hierarchical representaion of the contours, based od the composition operation

#contours, hierarchies = cv.findContours(canny, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
#print(f"Number of contoues found on the image: {len(contours)}")



# -------------------------Another way to find the contors in the image is cv.thresh

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY) # what this do is bipolariz the image every pixel under the 125 it's going to set zero or oposit it's going to set in the white
cv.imshow("TRESH",thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(f"Number of contoues found on the image: {len(contours)}")

# Drawing the countours on the black image 
contors_draw = cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow("Contors", blank)























cv.waitKey(0)