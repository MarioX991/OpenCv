import cv2 as cv
import numpy as np


#Crate blank(dommy image)
blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow("Blank",blank)



#. 1.Paint the image a certain colour

#blank[:] = 0,0,255
#cv.imshow("green",blank)

# 2. color cetain part of image by slicing the matrix

#blank[200:300,300:400] =0,255,0

#cv.imshow("green",blank)

#. 3 Draw a Ractangle
#rectangle_empty = cv.rectangle(img = blank, pt1=(0,0),pt2=(250,250),color=(0,255,0),thickness=3) 
# to fill the inner area of the rectangle insted the number for thickness we put cv.FILLED or just stecify whit the -1
#rectangle = cv.rectangle(img = blank, pt1=(0,0),pt2=(250,250),color=(0,255,0),thickness=cv.FILLED) 
#cv.imshow("Rectangle",rectangle)

# 4. Draw a Circle 

#circle = cv.circle(blank,(225,225),150,(255,0,0), thickness=cv.FILLED)
#cv.imshow("Circle",circle)

#- 5. Draw a Line

#line = cv.line(blank, (0,255),(255,255), color=(0,0,255), thickness=4)
#cv.imshow("Line",line)

#. Write text 

text = cv.putText(blank, "Hello",(255,255),cv.FONT_HERSHEY_COMPLEX_SMALL, 2.0, (0,0,255),thickness=3)
cv.imshow("text",blank)






cv.waitKey(0)