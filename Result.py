import pymysql
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class Results:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Result - Student Management System")
        self.root.geometry("900x500+200+100")
        self.root.config(bg="white")

        #Side Image
        self.sd_img = Image.open("images/result1.png")
        self.resize_image = self.sd_img.resize((400, 300))
        self.SDimg = ImageTk.PhotoImage( self.resize_image)
        labelimg1 = Label(self.root, image=self.SDimg)
        labelimg1.image = self.SDimg
        labelimg1.place(x=460, y=150, width=400, height=250)

        Manage_Frame = Frame(self.root, bd=4, bg="turquoise4")
        Manage_Frame.place(x=0, y=10, width=900, height=60)

        m_title=Label(Manage_Frame, text="Add Results",fg="white",bg="turquoise4",font=("times new roman",30,"bold"))
        m_title.place(x=320, y=2)

        footerFrame = Frame(self.root, bd=4, bg="turquoise4")
        footerFrame.place(x=0, y=468, width=900, height=30)

        f_title=Label(footerFrame, text="Designed and Developed by Amir Aijaz",fg="white",bg="turquoise4",font=("times new roman", 15))
        f_title.place(x=250, y=0)

        student_label = Label(self.root, text="", bg="turquoise4", font=("goudy old style", 15, "bold"))
        student_label.grid(row=0, columnspan=2, pady=40, padx=10, sticky="w")

        # Create the student selection section
        student_label = Label(self.root, text="Select Student:", bg="white", font=("goudy old style", 15, "bold"))
        student_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.student_combobox = ttk.Combobox(self.root, values=self.fetch_student_roll_numbers())
        self.student_combobox.bind("<<ComboboxSelected>>", self.handle_student_selection)
        self.student_combobox.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        # Create the student name entry
        name_label = Label(self.root, text="Name:", bg="white", font=("goudy old style", 15, "bold"))
        name_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.name_entry = Entry(self.root, bg="cornsilk2", fg="black", font=("goudy old style", 15, "bold"))
        self.name_entry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        # Create the course selection section
        course_label = Label(self.root, text="Course:", bg="white", font=("goudy old style", 15, "bold"))
        course_label.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.course_combobox = ttk.Combobox(self.root, values=self.fetch_course_names())
        self.course_combobox.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # Create the marks obtained entry
        marks_obtained_label = Label(self.root, text="Marks Obtained:", bg="white", font=("goudy old style", 15, "bold"))
        marks_obtained_label.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.marks_obtained_entry = Entry(self.root, bg="cornsilk2", fg="black", font=("goudy old style", 15, "bold"))
        self.marks_obtained_entry.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        # Create the total marks entry
        total_marks_label = Label(self.root, text="Total Marks:", bg="white", font=("goudy old style", 15, "bold"))
        total_marks_label.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.total_marks_entry = Entry(self.root, bg="cornsilk2", fg="black", font=("goudy old style", 15, "bold"))
        self.total_marks_entry.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        # Create the save button
         # Button Frame
        btn_Frame = Frame(self.root, bg="white")
        btn_Frame.place(x=50, y=370, width=200)

        save_button = Button(btn_Frame, text="Add", font=("timesnewroman 10 bold"), bg="#3399ff", cursor="hand2", fg="white", height=2, width=10, command=self.save_result)
        save_button.grid(row=0, column=0, padx=10, pady=5)  

        Clearbtn = Button(btn_Frame, text="Clear", font=("timesnewroman 10 bold"), cursor="hand2", bg="red", fg="white", height=2, width=10, command=self.clear)
        Clearbtn.grid(row=0, column=1, padx=10, pady=5) 

    # Function to fetch the student names from the database
    def fetch_student_roll_numbers(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT roll_no FROM students")
        students = cur.fetchall()
        student_roll_numbers = [student[0] for student in students]
        con.close()
        return student_roll_numbers

    #fetch course names
    def fetch_course_names(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT name FROM courses")
        courses = cur.fetchall()
        course_names = [course[0] for course in courses]
        con.close()
        return course_names

    def handle_student_selection(self, event):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        selected_roll_no = self.student_combobox.get()
        cur.execute("SELECT name, course FROM students WHERE roll_no = %s", (selected_roll_no,))
        student_data = cur.fetchone()
        if student_data:
            self.name_entry.delete(0, END)
            self.course_combobox.set("")
            self.name_entry.insert(END, student_data[0])
            self.course_combobox.set(student_data[1])
        else:
            messagebox.showerror("Error", "No student found with the selected roll number.")

        # Auto-fill the roll number field if a student is selected
        if selected_roll_no:
            cur.execute("SELECT roll_no FROM students WHERE roll_no = %s", (selected_roll_no,))
            student_roll_no = cur.fetchone()
            if student_roll_no:
                self.student_combobox.set(student_roll_no[0])
        con.close()
    # Function to handle saving the result
    def save_result(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        roll_no = self.student_combobox.get()
        name = self.name_entry.get()
        course = self.course_combobox.get()
        marks_obtained = self.marks_obtained_entry.get()
        total_marks = self.total_marks_entry.get()

        # Check if all the fields are filled
        if roll_no and name and course and marks_obtained and total_marks:
            cur.execute("INSERT INTO results (roll_no, name, course, marks_obtained, total_marks) VALUES (%s, %s, %s, %s, %s)",
                        (roll_no, name, course, marks_obtained, total_marks))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Result saved successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def clear(self):
        self.student_combobox.set("")
        self.name_entry.delete(0, END)
        self.course_combobox.set("")
        self.marks_obtained_entry.delete(0, END)
        self.total_marks_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = Results(root)
    root.mainloop()
