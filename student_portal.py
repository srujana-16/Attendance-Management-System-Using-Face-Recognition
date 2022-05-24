# Importing libraries
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Portal")
        self.root.geometry("1350x700+0+0")

        # ====Image and Title====
        # Set background
        bg = Image.open(r"C:\Users\flexuser\PycharmProjects\Attendance System\login\student_bg.jpg")
        bg = bg.resize((1600, 900), Image.ANTIALIAS)
        self.student_bg=ImageTk.PhotoImage(bg)
        bg_label = Label(self.root, image=self.student_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        # Title
        title = Label(self.root, text="Student Portal", font=("times new roman", 40, "bold"),bg="black", fg="white", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        # =====Variables=====
        self.name = StringVar()
        self.roll_num = StringVar()
        self.department = StringVar()
        self.year = StringVar()
        self.course = StringVar()


        # ======Main frame======
        main_frame = Frame(bg_label, bd=2)
        main_frame.place(x=150, y=130, width=1230, height=590)

        # =====Left frame======
        left_frame = LabelFrame(main_frame, bd=2, relief=GROOVE, text="Student Details", font=("times new roman",18, "bold"))                 # Title
        left_frame.place(x=20, y=10, width=445, height=560)

        # Student name
        name_label = Label(left_frame, text="Full name:", font=("times new roman", 15, "bold"))
        name_label.grid(row=0, column=0, padx=2, pady=10)
        name_entry = Entry(left_frame, textvariable=self.name, width=20, bd=5, relief=GROOVE, font=("", 15)).grid(row=0, column=1, padx=20, sticky=W)

        # Roll number
        roll_label = Label(left_frame, text="Roll number:", font=("times new roman", 15, "bold"))
        roll_label.grid(row=1, column=0, padx=2, pady=10)
        roll_entry = Entry(left_frame, textvariable= self.roll_num, width=20, bd=5, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20, sticky=W)

        # Year
        year_label = Label(left_frame, text="Year:", font=("times new roman", 15, "bold"))
        year_label.grid(row=2, column=0, padx=2, pady=10)
        year_entry = Entry(left_frame, textvariable= self.year, width=20, bd=5, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20,sticky=W)

        # Department name
        dep_label = Label(left_frame, text="Department:", font=("times new roman", 15, "bold"))
        dep_label.grid(row=3, column=0, padx=2,pady=10)
        dep_entry = Entry(left_frame, textvariable= self.department, width=20, bd=5, relief=GROOVE, font=("", 15)).grid(row=3,column=1,padx=20,sticky=W)

        # Course name
        course_label = Label(left_frame, text="Course name:", font=("times new roman", 15, "bold"))
        course_label.grid(row=4, column=0, padx=2, pady=10)
        dep_entry = Entry(left_frame, textvariable=self.course, width=20, bd=5, relief=GROOVE, font=("", 15)).grid(row=4, column=1, padx=20, sticky=W)

        # Radio buttons
        self.radio_Button1=StringVar()
        radioButton1 = ttk.Radiobutton(left_frame, variable=self.radio_Button1, text="Take Photo", value="Yes")
        radioButton1.grid(row=5, column=0)
        radioButton2 = ttk.Radiobutton(left_frame, variable=self.radio_Button1, text="No photo sample", value="No")
        radioButton2.grid(row=5, column=1)

        # Buttons frame
        button_frame = Frame(left_frame, bd=2, relief=GROOVE)
        button_frame.place(x=10,y=280,width=420, height=218)

        save_button =Button(button_frame, text="Save",command=self.AddData, width=20, height=3, font=("times new roman", 13, "bold"),  bg="darkblue", fg="white")          # Save button
        save_button.grid(row=0, column=0)

        update_button = Button(button_frame, text="Update", command=self.UpdateDetails, width=20, height=3, font=("times new roman", 13, "bold"), bg="darkblue",fg="white")           # Update button
        update_button.grid(row=0, column=1)

        delete_button = Button(button_frame, text="Delete", command=self.DeleteInfo, width=20, height=3, font=("times new roman", 13, "bold"), bg="darkblue",fg="white")           # Delete button
        delete_button.grid(row=1, column=0)

        reset_button = Button(button_frame, text="Reset", command=self.Reset, width=20, height=3, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")          # Reset button
        reset_button.grid(row=1, column=1)

        take_pic_button = Button(button_frame, text="Take photo", width=20, height=3, font=("times new roman", 13, "bold"), bg="darkblue",fg="white")          # Take photo button
        take_pic_button.grid(row=2, column=0)

        update_pic_button = Button(button_frame, text="Update photo", width=20, height=3, font=("times new roman", 13, "bold"), bg="darkblue",fg="white")  # Update photo button
        update_pic_button.grid(row=2, column=1)

        # =====Right frame=====
        right_frame = LabelFrame(main_frame, bd=2, relief=GROOVE, text="View student details", font=("times new roman", 18, "bold"))
        right_frame.place(x=500, y=10, width=705, height=560)

        # Table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=GROOVE)
        table_frame.place(x=12, y=14, width=675, height=490)

        # Scrollbar
        scrollX = ttk.Scrollbar(table_frame, orient=HORIZONTAL)                                              # X-Axis scrollbar
        scrollY = ttk.Scrollbar(table_frame, orient=VERTICAL)                                                # Y-Axis scrollbar

        self.details_table= ttk.Treeview(table_frame, column=("name", "roll", "year", "dep", "course"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.details_table.xview)
        scrollY.config(command=self.details_table.yview)

        self.details_table.heading("name", text="Name")
        self.details_table.heading("roll", text="Roll number")
        self.details_table.heading("year", text="Year")
        self.details_table.heading("dep", text="Department")
        self.details_table.heading("course", text="Course")
        self.details_table["show"]="headings"

        self.details_table.column("name", width=180)
        self.details_table.column("roll", width=190)
        self.details_table.column("year", width=120)
        self.details_table.column("dep", width=250)
        self.details_table.column("course", width=200)

        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease>", self.GetCursor)
        self.DisplayData()

    # ==========FUNCTIONS===========
    # Store the data in database
    def AddData(self):
        if self.name.get()=="" or  self.roll_num.get()=="" or  self.department.get()=="" or  self.year.get()=="" or self.course.get()=="":                      # If given info is not adequate, show error
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", user="root", password="Mysqlpass@1", database="sys")                                     # Creating the connection
                cursor1=connection.cursor()
                cursor1.execute("insert into student_details values(%s, %s, %s, %s, %s)", (self.name.get(), self.roll_num.get(), self.year.get(), self.department.get(), self.course.get()))

                connection.commit()
                self.DisplayData()
                connection.close()
                messagebox.showinfo("Success", "Successfully stored all details!", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    # Display the data stored
    def DisplayData(self):
        connection = mysql.connector.connect(host="localhost", user="root", password="Mysqlpass@1", database="sys")         # Creating the connection
        cursor1 = connection.cursor()
        cursor1.execute("select * from student_details")                                                                    # Selecting all the data from the dataset
        database = cursor1.fetchall()                                                                                       # Fetching all the data

        if len(database) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for j in database:
                self.details_table.insert("", END, values=j)  # Displaying all the data
            connection.commit()
        connection.close()

    # Get cursor to get all contents from the table to update the student details
    def GetCursor(self, event=""):
        Cursor_focus = self.details_table.focus()                                                                           # Focus the cursor at the table
        content = self.details_table.item(Cursor_focus)                                                                     # Obtain the contents of the table
        data = content["values"]

        self.name.set(data[0]),                                                                                             # Setting all the variables and indexing them
        self.roll_num.set(data[1]),
        self.year.set(data[2]),
        self.department.set(data[3]),
        self.course.set(data[4]),
        self.radio_Button1.set(data[5])

    # Update function
    def UpdateDetails(self):
        if self.name.get()=="" or  self.roll_num.get()=="" or  self.department.get()=="" or  self.year.get()=="" or self.course.get()=="":                      # If given info is not adequate, show error
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                UpdateInfo = messagebox.askokcancel("Update details", "Do you want to update the details?", parent=self.root)
                if UpdateInfo>0:
                    connection = mysql.connector.connect(host="localhost", user="root", password="Mysqlpass@1",database="sys")  # Creating the connection
                    cursor1 = connection.cursor()
                    cursor1.execute("update student_details set name=%s, roll=%s, year=%s, dep=%s, course=%s", (self.name.get(), self.roll_num.get(),self.year.get(),self.department.get(),self.course.get()))

                else:
                    if not UpdateInfo:
                        return
                messagebox.showinfo("Success", "Student details updated successfully!", parent=self.root)
                connection.commit()
                self.DisplayData()
                connection.close()
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


    # Delete function
    def DeleteInfo(self):
        if self.roll_num.get()=="":
            messagebox.showerror("Error", "Roll number is required", parent=self.root)
        else:
            try:
                delete = messagebox.askokcancel("Delete details", "Do you want to delete the data?", parent=self.root)
                if delete>0:
                    connection = mysql.connector.connect(host="localhost", user="root", password="Mysqlpass@1",database="sys")            # Creating the connection
                    cursor1 = connection.cursor()
                    sql = "delete from student_details where roll=%s"
                    val = (self.roll_num.get(),)
                    cursor1.execute(sql, val)

                else:
                    if not delete:
                        return

                connection.commit()
                self.DisplayData()
                connection.close()
                messagebox.showinfo("Success", "Successfully deleted student details!", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    # Reset function
    def Reset(self):
        self.name.set(""),                                                                                             # Setting all the variables to initial conditions
        self.roll_num.set(""),
        self.year.set(""),
        self.department.set(""),
        self.course.set(""),
        self.radio_Button1.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()