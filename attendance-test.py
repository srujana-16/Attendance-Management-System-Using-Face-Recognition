# Importing libraries
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Importing images
path = 'sample pictures'
images = []                                                                     # list of all the images that are imported
studentNames = []                                                               # list of all names that are imported
myList = os.listdir(path)
print(myList)
for cl in myList:
    currentImage = cv2.imread(f'{path}/{cl}')                                   # reading the current image
    images.append(currentImage)                                                 # appending the current image
    studentNames.append(os.path.splitext(cl)[0])                                # appending student names(excluding .jpg)
print(studentNames)


# Function that computes the encodings of all the images
def FindEncodings(images):
    encode_list = []                                                            # empty list that will store all the encodings
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                              # converting into RGB
        encoded_image = face_recognition.face_encodings(img)[0]                 # finding the encodings
        encode_list.append(encoded_image)                                       # appending it to our encoding list
    return encode_list

# Function to mark attendance for list of students present
def MarkAttendance(name):
    with open('Attendance.csv', 'r+') as f:                                     # opening the file to store the data
        MyDataList = f.readlines()                                              # reading the file to ensure the names are not repeated
        # print(myDataList)
        StudentList = []                                                        # empty list that will store all the names
        for line in MyDataList:
            entry = line.split(',')
            StudentList.append(entry[0])                                        # appending only the name in the list
        if name not in StudentList:                                             # checking if the current name is present or not
            now = datetime.now()                                                # storing the time of entry
            dtString = now.strftime('%H:%M')
            f.writelines(f'\n{name},{dtString}')

# Calling the function to find all the encodings of known faces
EncodeList_known = FindEncodings(images)
classStrength = len(EncodeList_known)                                           # total strength of the class
# print(classStrength)
print('Encoding Complete')

cap = cv2.VideoCapture(0)                                                       # initialising the webcam

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)                                       # reducing size of the image to speed up the process
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)                                           # converting into RGB

    facesCurFrame = face_recognition.face_locations(imgS)                                  # finding the locations in current frame
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):                        # iterating and comparing with encodings
        match = face_recognition.compare_faces(EncodeList_known, encodeFace)
        faceDistance = face_recognition.face_distance(EncodeList_known, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDistance)                                               # finding the lowest distance to get the best match

        if faceDistance[matchIndex] < 0.50:                                                # once the face matches, displaying the name
            name = studentNames[matchIndex].upper()
            MarkAttendance(name)
        else:
            name = 'Unknown'                                                               # display 'unknown' if face is not recognised
        # print(name)
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4                                    # scaling the image back to original size
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)                             # drawing a box around the face recognised
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Video cam', img)
    cv2.waitKey(1)
