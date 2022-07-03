import cv2 as cv

img = cv.imread("./Photos/3.jpg")
cv.imshow("Cat",img)

# 1. Convert an image into the grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)

#2. How to blur an image using the Gaussian blur

#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow("Blur",blur)

# 3. Egde Cascade (this function help us to find edges that are present on the image)
# to reduce the number of edges we should blur the image 
#cany = cv.Canny(img,125,175)
#cv.imshow("Cany",cany)


# 4. Dilating the images

#dilated = cv.dilate(cany, (7,7), iterations=1)
#cv.imshow("Dilated",dilated)


# 5. Eroding

#eroded = cv.erode(dilated,(3,3), iterations=1)
#cv.imshow("Eroded",eroded)

# 5. Resize and crop an image
# if we are shrinking the image, the recommendation is to put one more argument interpolation = cv.INTERNAL AREA
# or in case to upper scale an image use cv.INTER_CUBIC or INTER_LINEAR for the better quality of result
resize = cv.resize(img, (300,300))
cv.imshow("Resize",resize)

# Cropping

cropped = img[50:200,140:340]
cv.imshow("Cropped",cropped)












cv.waitKey(0)