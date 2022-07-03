import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


blank = np.zeros((400,400), dtype= "uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)



# bitwise AND 


bitwise_and=cv.bitwise_and(rectangle,circle)
# bitwise OR

bitwise_or=cv.bitwise_or(rectangle, circle)


#bitwise Xor = OR - AND

xor = cv.bitwise_xor(rectangle, circle)

#bitwise not (inverting a picture)

nots = cv.bitwise_not(rectangle)

cv.imshow("rectangle_not",nots)






cv.imshow("Rectangel",rectangle)
cv.imshow("Circle", circle)
#cv.imshow("Botwise_and", bitwise_and)
#cv.imshow("Botwise_or", bitwise_or)
cv.imshow("Xor", xor)
cv.waitKey(0)