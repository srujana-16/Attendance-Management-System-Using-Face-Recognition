# Importing libraries
from tkinter import *
from PIL import Image, ImageTk
import os
import face_recognition
import numpy as np
from datetime import datetime
import cv2


class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("1350x700+0+0")

        # ====Image and Title====
        # Set background
        bg = Image.open(r"login\faceRec.jpeg")
        bg = bg.resize((1580, 750), Image.ANTIALIAS)
        self.student_bg = ImageTk.PhotoImage(bg)
        bg_label = Label(self.root, image=self.student_bg)
        bg_label.place(x=0, y=60, width=1580, height=750)

        # Title
        title = Label(self.root, text="Face Recognition", font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # Train dataset button
        face_button = Button(self.root, text="Start", command= self.face_recognition, width=20, height=3, font=("times new roman", 18, "bold"), bg="black", fg="white", relief=GROOVE)
        face_button.place(x=430, y=475)

    # =======Face Recognition function=======
    def face_recognition(self):
        path = 'Dataset'
        images = []                                                                    # List of all the images that are in the database
        student_id = []                                                                # list of all the student IDs in the database
        my_list = os.listdir(path)
        # print(my_list)

        for cl in my_list:
            current_img = cv2.imread(f'{path}/{cl}')                                   # Reading the current image
            ids = int(os.path.split(cl)[1].split('.')[1])                              # Obtaining the ID
            images.append(current_img)                                                 # Appending the current image
            student_id.append(ids)                                                     # appending the IDs
        # print(classNames)

        # Function that computes the encodings of all the images
        def findEncodings(faces):
            encode_list = []                                                           # Empty list that will store all the encodings
            for img in faces:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                             # Converting into RGB
                encode = face_recognition.face_encodings(img)[0]                       # Finding the encodings
                encode_list.append(encode)                                             # Appending it to our encoding list
                return encode_list

        # Calling the function to find all the encodings of known faces
        EncodeListKnown = findEncodings(images)
        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)                                                                          # Reducing size of the image to speed up the process
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)                                                                              # Converting into RGB

            faces_cur_frame = face_recognition.face_locations(imgS)                                                                   # Finding the locations in current frame
            encodes_cur_frame = face_recognition.face_encodings(imgS, faces_cur_frame)

            for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):                                                       # Iterating and comparing with encodings
                match = face_recognition.compare_faces(EncodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(EncodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)                                                                                       # Finding the lowest distance to get the best match

                if faceDis[matchIndex] < 0.50:                                                                                        # If face recognized from database, then print Student ID
                    name = student_id[matchIndex]
                    self.MarkAttendance(name)


                else:
                    name = 'Unknown'                                                                                                   # If face not recorded in database, print "unknown"
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4                                                                        # Saving the image back to original size
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)                                                                 # Drawing a rectangle around face
                cv2.rectangle(img, (x1, y2 - 32), (x2, y2), (0, 255, 0), cv2.FILLED)                                                   # Rectangle for text
                cv2.putText(img, "Student ID:" + str(name), (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)       # Text



            cv2.imshow('Webcam', img)
            cv2.waitKey(1)

    # ======Mark Attendance function=======
    # Function to mark attendance for list of students recognised
    def MarkAttendance(self, name):
        with open('Attendance.csv', 'r+', newline="\n") as f:                        # Opening the file to store the data
            MyDataList = f.readlines()                                               # Reading the file to ensure that attendance is not already marked
            print(MyDataList)
            StudentList = []                                                         # Empty list that will store all the IDs
            for line in MyDataList:
                entry = line.split(',')
                StudentList.append(entry[1])                                         # Appending only the name in the list
            if name not in StudentList:                                              # Checking if the current name is present or not
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")                                      # Storing the date
                time = now.strftime('%H:%M')                                         # Storing the time of entry
                f.writelines(f'\n{name}, {date}, {time}, Present')



if __name__ == "__main__":
    root = Tk()
    obj = Recognition(root)
    root.mainloop()
