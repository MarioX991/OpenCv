# https://www.classicgame.com/game/Whack+a+Mole


import cv2 as cv
import numpy as np
import pyautogui as auto
from time import sleep
from re import template


# No Cooldown time 

auto.PAUSE = 0


# Get tamplates

template = cv.imread("./Images/nose.png")
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
width, height = template_gray.shape[::-1] # when we work with images we get (high, weight) when we apply same function in the OpenCV we get different order
#cv.imshow("img1", template_gray)



# game windows dimension

x,y,w,h, = 523, 247, 875, 679

# wait 
sleep(2)

# main 

while True:


    #screemshot
    auto.screenshot("Images/image.png",(x,y,w,h))
    image = cv.imread("Images/image.png")

    while True: 
            #show what the computer sees
        image_mini = cv.resize(
            src = image,
            dsize = (450,350) #must be integer, not float
        )
        cv.imshow("vision", image_mini)
        cv.waitKey(10)


        Image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

        result = cv.matchTemplate(
            image=Image_gray,
            templ=template_gray,
            method=cv.TM_CCOEFF_NORMED
            )

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        # to be sure that we are going to get the best results we set the thrashold
        if max_val >= 0.8: #if we match 80percent or higher we are good to go
            auto.click(
                x = max_loc[0] + x,
                y = max_loc[1] + y
            )

        #make rectangle aroung the noice
            image = cv.rectangle(
            img = image,
            pt1 = max_loc,
            pt2  = (max_loc[0] + width, max_loc[1] + height),
            color = (0,0,255),
            thickness=-1 #fill the rectange
            )
        else :
            #if we dont have matches break
            break





















