import numpy as np
import cv2 as cv

people = ["Ben Affleck", "Elton JOhn","Madonna","Zika Pavlovic"]

harr_casscade = cv.CascadeClassifier("harr.xml")
# Load the files previosuly created by the Face_tain.py
# if we don't comment this will bring a error if we want to use this we need to pass in allow_pickele=TRUE
#feature = np.load("features.npy")
#labels = np.load("labels.npy")


# Load the yml file 
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")
# insert the test(Validation) image and convert it in the grayscal image
img = cv.imread(r"C:\Users\marinko\Desktop\openCV\Faces\validation\ben.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



cv.imshow("Persion", gray)


# Detect the face in the image

face_rec = harr_casscade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rec:
     face_roi = gray[y:y+h, x:x+w]
     # now we can do prediction of given image 

     label, confidence = face_recognizer.predict(face_roi)

     print(f"Label ={people[label]} with confidence of {confidence}")

     cv.putText(img,  str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
     cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0), thickness=2)


cv.imshow("Detected image", img)
cv.waitKey(0)








