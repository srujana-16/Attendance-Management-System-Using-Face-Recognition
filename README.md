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

Any facial recognition algorithm uses biometrics to map out facial features captured in a video still or a photograph. That information is then compared to a database of faces. 

STEP 1: FACE DETECTION, This step involves collecting the photo samples for generating our database. First, a camera will detect and recognize a human’s face – one that can either be in a crowd or alone. It is most easily detected when the person is looking straight at the camera. Facial detection is implemented using OpenCV Python Haarcascade Classifer. HAAR cascade is a feature-based algorithm for object detection which is used to detect the frontal face and its features like eyes, nose, and mouth. 100 samples are collected each time a new student registers.

STEP 2: FACE ANALYSIS After detection, a photo will capture the face and will then be analyzed. During analysis, the face will be separated into distinguishable landmarks – we can call these nodal points. A human face has eight nodal points. After analysis, each nodal point becomes a number in the application database. Face recognition technology will analyze each of these points – for example, the distance between your eyebrows. The network learns to reliably generate 128 measurements for each person. Any ten different pictures of the same person should give roughly the same measurements. MySQL is used for storing all the databbase.

STEP 3: FACE RECOGNITION The final step of the process is finding a match. Your faceprint is compared to the database that stores all the facial distances. The facial recognition technology then identifies a match for your exact facial features. Once the face is recognised, it returns the user with the found match and other relevant information from the database. The data is stored and the student's attendance is marked in attendance.csv. This face recognition application has been developed using Python OpenCV's Face Recognition library.

#### Video Demo - [https://iiitaphyd-my.sharepoint.com/:f:/g/personal/srujana_vanka_students_iiit_ac_in/EhPiQoArdJZCpXlN_yvhnEIB869iW9QGStpw_SbPd8Miiw?e=JwNRA3]

## Tech Used

- Build With 
    - Python 3.7
  
- Modules used
    - OpenCV - Open Source Computer Vision and Machine Learning software library
    - Dlib - C++ Library containing Machine Learning Algorithms 
    - face_recognition by Adam Geitgey
    - Tkinter - Python framework to create GUI applications
  
- Face recognition algorithms
    - Haar Cascade - Face detection algorithm
    - Dlib's HOG - To find face locations and encodings 
    - face_recognition - Extraction of Facial Embeddings
  
- Software used
    - Pycharm 2022.1.1
    - MySQL - Database management system

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
- Compile and run python3 main.py inside \Attendance-Management-System-Using-Face-Recognition
