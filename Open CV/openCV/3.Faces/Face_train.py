import cv2 as cv
import os
import numpy as np

# Create the list of all names that we want to use for recognition
# This cen be done manually
people = ["Ben Affleck", "Elton JOhn","Madonna","Zika Pavlovic"]
# OR loop over every folder in given location and get the names of them in an array. (Fenomenal stuff) 
# p =[]
# for i in os.listdir(r"C:\Users\marinko\Desktop\openCV\Faces\Train"):
#     p.append(i)
# print(p)

# Create a variable which contain the path to the main folder where we store images

DIR = "C:/Users/marinko/Desktop/openCV/Faces/Train"

haar_cascade = cv.CascadeClassifier('harr.xml')
features = []
labels =[]
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        # this way we minimize the computation complexity for the pc by converting string values in to the numerical 
        label = person.index(person)


        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)


            #now we are going to use harr fot detecting the face on the image

            face_rec = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors = 4)

            for (x,y,w,h) in face_rec:
                #here we are copping the face 
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)



create_train()
# print(f"The Lenght of the featrures is: {len(features)}")
# print(f"The Lenght of the labels is: {len(features)}")
print("--------------  Training done -------------")
features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train the facerecognizer on the feature list and the labels

face_recognizer.train(features,labels)
# top be able to use the tained model whenever and wherevery we want, we use the property of the OpenCv to save in the yml file.

face_recognizer.save("face_trained.yml")


# save the labels and features list 
np.save("features.npy", features)
np.save("labels.npy", labels)
 












