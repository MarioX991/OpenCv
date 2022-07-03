import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize

img = cv.imread("./Photos/3.jpg")
cv.imshow("Cat",img)

# Translation

def translate(img, x,y):
    """
(x,y): numbers of pixel that we want to shift along the x and the y axes respectively.
Property for picking different numbers "x" and "y": 

-x : Shifts the image on the Left
-y : Shifts the image Up
x: Shifts the image on the Right
y: shifts the image Down 

    """
    transMAt  = np.array([[1,0,x],[0,1,y]],dtype=float)
    dimensions = (img.shape[1], img.shape[0]) # (width, height)

    return cv.warpAffine(img, transMAt, dimensions)


#translate_image = translate(img, 100,100)
#cv.imshow("Translate",translate_image)

# Rotation

def rotation(img, angle, RotPoint=None):
    (height, width ) = img.shape[:2]
    if RotPoint is None:
        RotPoint = (width//2,height//2)

    RotMat  = cv.getRotationMatrix2D(RotPoint,angle,1.0)    
    dimension = (width, height)

    return cv.warpAffine(img, RotMat, dimension)


rotate_image = rotation(img, 180,None)
#cv.imshow("Rotated_image",rotate_image)

# Resizing
#resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#cv.imshow("Resized", resize)

# Flip an image

flip = cv.flip(img, 1) # 0 - basically implies flip over the x axis and 1- over the y axis respectly
#cv.imshow("Flip", flip)

#Crop image
crp = img[200:400,100:300]
cv.imshow("Crop",crp)


cv.waitKey(0)