
# A Histogram allows us to visualit the distribution of pixel intensity in an image. 
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/3.jpg")
cv.imshow("Cat",img)



# Computing hist for a grayscal image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Mask

#blank = np.zeros(img.shape[:2],dtype="uint8")
#circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2 ),100,255,-1)
#mask = cv.bitwise_and(gray, gray, mask =circle)
#cv.imshow("mask",mask)

#gray_hist = cv.calcHist([gray],[0],None, [256],[0,256]) #histSize = number of bins
##plt.figure()
#plt.title("GrayScallHistogram")
#plt.xlabel("Bins")
#plt.ylabel("Num of pixels")
#plt.plot(gray_hist)
#plt.xlim([0,256]) # if the most of pixels on the image are white the jumps on the histogram will be on the right area, near to 265 pixel 
#plt.show()

#-------------------- Create mask and calculate the histogram to specific area of the image
# gray_hist_mask = cv.calcHist([gray],[0],mask, [256],[0,256]) #histSize = number of bins
# plt.figure()
# plt.title("GrayScallHistogram_mask")
# plt.xlabel("Bins_")
# plt.ylabel("Num of pixels")
# plt.plot(gray_hist_mask)
# plt.xlim([0,256]) # if the most of pixels on the image are white the jumps on the histogram will be on the right area, near to 265 pixel 
# plt.show()

#------------------- Compute histogram of color image---------------------


# plt.figure()
# plt.title("GrayScallHistogram_color")
# plt.xlabel("Bins_")
# plt.ylabel("Num of pixels")

# colors = ("b","g","r")
# for i, col in enumerate(colors):
#     hist = cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist, color =col)
#     plt.xlim([0,256])

# plt.show()


#------------------- Compute histogram of color image and mask --------------------- 2:15:00

#Change mask property preventing thr error of different dimesions
blank = np.zeros(img.shape[:2],dtype="uint8")
maskt = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2 ),100,255,-1)
masked = cv.bitwise_and(img, img, mask =maskt)
cv.imshow("mask",masked)




plt.figure()
plt.title("ColorHistogram_color_mask")
plt.xlabel("Bins_")
plt.ylabel("Num of pixels")

colors = ("b","g","r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],maskt,[256],[0,256])
    plt.plot(hist, color =col)
    plt.xlim([0,256])

plt.show()








cv.waitKey(0)