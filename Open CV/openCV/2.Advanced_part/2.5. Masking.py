import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./Photos/3.jpg")
cv.imshow("Cat",img)


blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)
print(f"Img shape {img.shape}")

mask = cv.circle(blank, (img.shape[0]//2, img.shape[1]//2),250,255,-1)

cv.imshow("Mask", mask)

mask_img = cv.bitwise_and(img, img, mask = mask)




cv.imshow("Maks_image",mask_img)

cv.waitKey(0)


