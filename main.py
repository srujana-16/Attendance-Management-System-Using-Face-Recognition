# Importing libraries
import tkinter.messagebox
from tkinter import*
import tkinter
from tkinter import ttk
from time import strftime
from datetime import datetime
from PIL import Image,ImageTk
from student_portal import Student
from train_dataset import Train
from recognition import Recognition
from attendance import attendance_sheet
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1350x700+0+0")

        # Set background
        self.bg_icon = ImageTk.PhotoImage(file="login/bg.jpg")
        bg_1abel = Label(self.root, image=self.bg_icon).pack()

        # Title
        title = Label(self.root, text="Face Recognition Attendance System", font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # Display time
        def Time():
            timestring= strftime('%H:%M:%S %p')
            time_label.config(text=timestring)
            time_label.after(1000,Time)

        time_label = Label(title, font=('times new roman', 15, 'bold'), bg="black", fg="blue")
        time_label.place(x=5, y=5, width=110,height=50)
        Time()

        # Buttons
        # Student portal
        img1 = Image.open(r"login\student_portal.jpg")                                                                      # Path for the image
        img1 = img1.resize((240,240), Image.ANTIALIAS)                                                                                                                          # Resizing
        self.student_img = ImageTk.PhotoImage(img1)
        StudentButton = Button(bg_1abel, image=self.student_img, command=self.details_portal, cursor="hand2")                                                                                                # Convertig the image into a button
        StudentButton.place(x=300, y=140, width=240, height=240)                                                                                                                # Giving appropriate coordinates
        b1 = Button(bg_1abel, text="Student Portal", command=self.details_portal, cursor="hand2", font=("times new roman",15, "bold"), bg="darkblue", fg="white")
        b1.place(x=300, y=340, width=240, height=40)

        # Face detection
        img2 = Image.open(r"login\face_recog.jpg")
        img2 = img2.resize((240, 240), Image.ANTIALIAS)
        self.face_img = ImageTk.PhotoImage(img2)
        face_img = Button(bg_1abel, image=self.face_img, command=self.Face_Recog, cursor="hand2")
        face_img.place(x=640, y=140, width=240, height=240)
        b2 = Button(bg_1abel, text="Face Recognition", cursor="hand2", command=self.Face_Recog, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2.place(x=640, y=340, width=240, height=40)

        # View attendance
        img3 = Image.open(r"login\attendance.png")
        img3 = img3.resize((240, 240), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(img3)
        attendance_img = Button(bg_1abel, image=self.attendance_img, command=self.View_Attendance, cursor="hand2")
        attendance_img.place(x=980, y=140, width=240, height=240)
        b3 = Button(bg_1abel, text="Attendance Portal", cursor="hand2", command=self.View_Attendance, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3.place(x=980, y=340, width=240, height=40)

        # Train data
        img4 = Image.open(r"login\train.jpg")
        img4 = img4.resize((240, 240), Image.ANTIALIAS)
        self.train_img = ImageTk.PhotoImage(img4)
        train_img = Button(bg_1abel, image=self.train_img, cursor="hand2", command=self.training_portal)
        train_img.place(x=300, y=480, width=240, height=240)
        b4 = Button(bg_1abel, text="Train Dataset", cursor="hand2", command=self.training_portal, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b4.place(x=300, y=680, width=240, height=40)

        # Access photos
        img5 = Image.open(r"login\photos.jpg")
        img5 = img5.resize((240, 240), Image.ANTIALIAS)
        self.photos_img = ImageTk.PhotoImage(img5)
        photos_img = Button(bg_1abel, image=self.photos_img, cursor="hand2", command=self.Open_Photos)
        photos_img.place(x=640, y=480, width=240, height=240)
        b5 = Button(bg_1abel, text="Access Photos", cursor="hand2", command=self.Open_Photos, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b5.place(x=640, y=680, width=240, height=40)

        # Exit
        img6 = Image.open(r"login\exit.jpg")
        img6 = img6.resize((240, 240), Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(img6)
        exit_img = Button(bg_1abel, image=self.exit_img, command=self.iExit, cursor="hand2")
        exit_img.place(x=980, y=480, width=240, height=240)
        b6 = Button(bg_1abel, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6.place(x=980, y=680, width=240, height=40)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Exit face recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    # ======FUNCTIONS=======
    # Function to link main and student portal
    def details_portal(self):
        self.new_window = Toplevel(self.root)
        self.portal = Student(self.new_window)

    # Function to link main and training portal
    def training_portal(self):
        self.new_window = Toplevel(self.root)
        self.portal = Train(self.new_window)

    # Function to access photos
    def Open_Photos(self):
        os.startfile("Dataset")

    # Function to open face recognition portal
    def Face_Recog(self):
        self.new_window = Toplevel(self.root)
        self.portal = Recognition(self.new_window)

    # Function to open attendance portal
    def View_Attendance(self):
        self.new_window = Toplevel(self.root)
        self.portal = attendance_sheet(self.new_window)

    # # Exit window
    # def Exit(self):



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
