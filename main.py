# Importing libraries
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

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

        # Buttons
        # Student portal
        img1 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\student_portal.jpg")                                                                      # Path for the image
        img1 = img1.resize((240,240), Image.ANTIALIAS)                                                                                                                          # Resizing
        self.student_img = ImageTk.PhotoImage(img1)
        StudentButton = Button(bg_1abel, image=self.student_img, cursor="hand2")                                                                                                # Converting the image into a button
        StudentButton.place(x=300, y=140, width=240, height=240)                                                                                                                # Giving appropriate coordinates
        b1 = Button(bg_1abel, text="Student Portal", cursor="hand2", font=("times new roman",15, "bold"), bg="darkblue", fg="white")
        b1.place(x=300, y=340, width=240, height=40)

        # Face detection
        img2 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\face_recog.jpg")
        img2 = img2.resize((240, 240), Image.ANTIALIAS)
        self.face_img = ImageTk.PhotoImage(img2)
        face_img = Button(bg_1abel, image=self.face_img, cursor="hand2")
        face_img.place(x=640, y=140, width=240, height=240)
        b2 = Button(bg_1abel, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2.place(x=640, y=340, width=240, height=40)

        # Mark attendance
        img3 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\attendance.png")
        img3 = img3.resize((240, 240), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(img3)
        attendance_img = Button(bg_1abel, image=self.attendance_img, cursor="hand2")
        attendance_img.place(x=980, y=140, width=240, height=240)
        b3 = Button(bg_1abel, text="Attendance Portal", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3.place(x=980, y=340, width=240, height=40)

        # Train data
        img4 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\train.jpg")
        img4 = img4.resize((240, 240), Image.ANTIALIAS)
        self.train_img = ImageTk.PhotoImage(img4)
        train_img = Button(bg_1abel, image=self.train_img, cursor="hand2")
        train_img.place(x=300, y=480, width=240, height=240)
        b4 = Button(bg_1abel, text="Train Dataset", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b4.place(x=300, y=680, width=240, height=40)

        # Access photos
        img5 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\photos.jpg")
        img5 = img5.resize((240, 240), Image.ANTIALIAS)
        self.photos_img = ImageTk.PhotoImage(img5)
        photos_img = Button(bg_1abel, image=self.photos_img, cursor="hand2")
        photos_img.place(x=640, y=480, width=240, height=240)
        b5 = Button(bg_1abel, text="Access Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b5.place(x=640, y=680, width=240, height=40)

        # Exit
        img6 = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\exit.jpg")
        img6 = img6.resize((240, 240), Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(img6)
        exit_img = Button(bg_1abel, image=self.exit_img, cursor="hand2")
        exit_img.place(x=980, y=480, width=240, height=240)
        b6 = Button(bg_1abel, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6.place(x=980, y=680, width=240, height=40)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
