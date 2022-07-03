import cv2 as cv
img = cv.imread("./Photos/face3.jpg")

cv.imshow("Face1",img)


# the image need to be in grayscale mode before we do facedetection
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)

# note: The harr_cascade is realy sensitive to the noice on the image,this mean that everything which look like or have the same shape 
# of face will be detect as face. 

haar_cascade = cv.CascadeClassifier('harr.xml')
# now we try to detect faces on the image
# returns the points of a rectangle that surrounding found face 
# the result is an array where each element is an array of length 4
face_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 1)
# we can print the number of detected faces on the image

print(f"Number detected faces ont he image is : {len(face_rect)}")
print(face_rect)

# now wa are going to print rectangel on the image

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0),2)

cv.imshow("Found_faces",img)




cv.waitKey(0)