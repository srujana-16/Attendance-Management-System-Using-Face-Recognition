# Attendance Management System Using Face Recognition
This project entails developing an attendance system that uses facial recognition to record students' presence and time-in. It includes facial detection, alignment, and recognition, as well as the creation of a web application to support the system's many use cases, such as registration, photo addition to the dataset, reading attendance reports, and so on.

The goal of this project is to automate the traditional attendance method, which involves manually marking attendance. The system's digitalization would help to improve data visualisation by employing graphs to show the number of students present today, total classes attended, in-time, and other metrics, as well as decrease manual process errors. Its enhanced features make it a viable upgrade and replacement for older attendance systems.

### Following functionalities can be performed by the admin:
- Register new students to the system
- Add students photos to the training data set
- Train the model
- View attendance report of all students

### Following functionalities can be performed by the student:
- Register themselves
- Mark his/her time-in by scanning their face
- View attendance report of self

## Methodology
The first step in our pipeline is collecting the photo samples, that is generating the database. This involves detecting the face. Facial detection is implemented using OpenCV's haarcascade classifer. 100 samples are collected each time a new student registers.
  
Once the database is generated, the next step is training the dataset to find the encodings for each image. The network learns to reliably generate 128 measurements for each person. Any ten different pictures of the same person should give roughly the same measurements. The measurements here are the face distances. MySQL is used for storing all the databbase.
  
The final step is facial recognition. This face recognition application has been developed using Python OpenCV's Face Recognition library. The unique encodings of these faces which are generated are used to map to the right face. Once the face is recognised, the data is stored and the student's attendance is marked in attendance.csv. 
  
Tkinter is used to generate the graphical user interface.

## How to run?
- Clone it on your computer
- Install the following dependencies:
    - MySQL 
    - dlib 19.24
    - face_recognition 1.3
    - opencv-python 4.5.5.64
    - pillow 8.1.0
    - numpy 1.22.3
    - cmake 3.22.4
- Compile and run main.py inside \Attendance-Management-System-Using-Face-Recognition
