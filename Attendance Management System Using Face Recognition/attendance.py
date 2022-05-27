# Importing libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import csv
from tkinter import filedialog
from tkinter import messagebox
import cv2

class attendance_sheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance")
        self.root.geometry("1350x700+0+0")

        # ====Image and Title====
        # Set background
        bg = Image.open(r"pictures\student_bg.jpg")
        bg = bg.resize((1600, 900), Image.ANTIALIAS)
        self.student_bg = ImageTk.PhotoImage(bg)
        bg_label = Label(self.root, image=self.student_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        # Title
        title = Label(self.root, text="Attendance", font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # ====Main frame===
        main_frame = Frame(bg_label, bd=2)
        main_frame.place(x=225, y=130, width=1100, height=590)

        details_frame = LabelFrame(main_frame, bd=2, relief=GROOVE, text="View attendance", font=("times new roman", 18, "bold"))
        details_frame.place(x=5, y=10, width=1050, height=390)

        # Table frame
        table_frame = Frame(details_frame, bd=2, bg="white", relief=GROOVE)
        table_frame.place(x=12, y=14, width=1020, height=330)

        # Scrollbar
        scrollX = ttk.Scrollbar(table_frame, orient=HORIZONTAL)               # X-Axis scrollbar
        scrollY = ttk.Scrollbar(table_frame, orient=VERTICAL)                 # Y-Axis scrollbar

        self.details_table = ttk.Treeview(table_frame, column=("id", "date", "time", "status"), xscrollcommand=scrollX.set , yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.details_table.xview)
        scrollY.config(command=self.details_table.yview)

        self.details_table.heading("id", text="Student ID")
        self.details_table.heading("date", text="Date")
        self.details_table.heading("time", text="Time")
        self.details_table.heading("status", text="Attendance Status")
        self.details_table["show"] = "headings"

        self.details_table.column("id", width=150)
        self.details_table.column("date", width=200)
        self.details_table.column("time", width=200)
        self.details_table.column("status", width=200)

        self.details_table.pack(fill=BOTH, expand=1)

        # Import data button
        import_button = Button(main_frame, text="Import csv", command=self.Import, width=16, height=2, font=("times new roman", 18, "bold"), bg="black", fg="white", relief=GROOVE)
        import_button.place(x=420, y=440)

    # Fetch and display data function
    def FetchData(self, rows):
        self.details_table.delete(*self.details_table.get_children())                                                        # Delete old data present
        for i in rows:
            self.details_table.insert("", END, values=i)                                                                     # Inserting the data in the table
            messagebox.showinfo("Success", "Attendance information has been imported successfully!", parent=self.root)

    def Import(self):
        MyFile = []
        file = filedialog.askopenfilename(initialdir=os.getcwd(), title="OPEN CSV", filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)              # Selecting the csv file to be read
        with open(file) as f:
            FileRead = csv.reader(f, delimiter=",", dialect="excel")                                                                                                       # Reading the file
            for i in FileRead:
                MyFile.append(i)                                                                                                                                           # Store the data read
            self.FetchData(MyFile)                                                                                                                                         # Calling the function to display the data in the table


if __name__ == "__main__":
    root = Tk()
    obj = attendance_sheet(root)
    root.mainloop()