import cv2 as cv

#------------- RESIZE AN IMAGE-------------#

# import image
img = cv.imread("./Photos/Cat.jpg")



# rescale function
def rescaleFrame(frame, scale = 1.75 ):
    # this method will work on the images, videos and the live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# function to change resolution
def changeRes(width, height):
    # work just on the live video
    capture.set(3,width) # 3 reference to the width 
    capture.set(4,height) # 4 reference to the higth




# read our old video and applay the rescaleFamame function
capture = cv.VideoCapture('./Videos/VIDEO1.mp4')



# display image
cv.imshow("Cat",img)
resize_img = rescaleFrame(img)
cv.imshow("Cat_resieze",resize_img)
#cv.waitKey(0)

while True:
    
    ifTrue, frame = capture.read()

#------------- RESIZE A VIDEO -------------#

    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video_resize", frame_resized)
    if cv.waitKey(20) & 0xFF==ord("d"): 
        break

capture.release()
cv.destroyAllWindows()

