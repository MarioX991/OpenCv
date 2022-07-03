import cv2 as cv

#----------------   READ IMAGE -----------------#
#read image
#img = cv.imread('./Photos/3.jpg')

#dispaly image
#cv.imshow("3",img)

# waitKey(delay)
#cv.waitKey(0)
#print(pwd)

# NOTICE(large image):
# the images that are bigger than your monitor screen resolution create a problem.
# This mean cv is gonna show back a part of image which correspond to the resolution of our monitor.


#----------------   READ VIDEOS -----------------#

capture = cv.VideoCapture('./Videos/VIDEO1.mp4')
# this is point where reading video is different thatn reading imags. For a video we using while loop
# and read frame by frame
while True:
    # this return the frame and the boolean (give us a response if it current frame is successfully read or not)
    isTrue, frame = capture.read()
    #display frame
    cv.imshow("Video", frame)
    # to break the loop 
    if cv.waitKey(20) & 0xFF==ord("d"): #if the key "D" is pressed than break out from the loop
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
# ERROR -215:Asseartion failed -> wrong path or for the video usualy mean that we were left without any frame