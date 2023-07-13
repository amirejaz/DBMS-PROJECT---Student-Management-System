from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Students:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Student - Student Management System")
        self.root.geometry("1130x650+90+30")
        self.root.config(bg="cornsilk2")

        # All Variables
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Age_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_No_var = StringVar()
        self.course_var = StringVar()
        self.Search_By = StringVar()
        self.search_txt = StringVar()
        self.selected_courses = []

        # Manage Frame
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="springgreen4")
        Manage_Frame.place(x=10, y=30, width=400, height=600)

        m_title = Label(Manage_Frame, text="Manage Students", fg="white", bg="springgreen4",
                        font=("times new roman", 25, "bold"))
        m_title.grid(row=0, columnspan=2, pady=6)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="springgreen4", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=5, padx=5, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="springgreen4", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=5, padx=5, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        lbl_age = Label(Manage_Frame, text="Age", bg="springgreen4", fg="white", font=("times new roman", 15, "bold"))
        lbl_age.grid(row=3, column=0, pady=5, padx=5, sticky="w")

        txt_age = Entry(Manage_Frame, textvariable=self.Age_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_age.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="springgreen4", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=5, padx=5, sticky="w")

        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.Gender_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_Gender['values'] = ("male", "female", "other")
        combo_Gender.grid(row=4, column=1, pady=5, padx=5)

        lbl_cont = Label(Manage_Frame, text="Contact No.", bg="springgreen4", fg="white",
                         font=("times new roman", 15, "bold"))
        lbl_cont.grid(row=5, column=0, pady=5, padx=5, sticky="w")

        txt_cont = Entry(Manage_Frame, textvariable=self.Contact_No_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_cont.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        lbl_course = Label(Manage_Frame, text="Courses", bg="springgreen4", fg="white",
                           font=("times new roman", 15, "bold"))
        lbl_course.grid(row=6, column=0, pady=5, padx=5, sticky="w")

        self.course_combobox = ttk.Combobox(Manage_Frame, textvariable=self.course_var,
                                            font=("times new roman", 13, "bold"), state='readonly')
        self.course_combobox.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        btn_add_course = Button(Manage_Frame, text="Add Course", font=("timesnewroman 9 bold"), bg="crimson",
                                cursor="hand2", fg="white", height=2, width=15, command=self.add_course)
        btn_add_course.grid(row=7, column=0, pady=2)

        lbl_selected_courses = Label(Manage_Frame, text="Selected Courses", bg="springgreen4", fg="white",
                                      font=("times new roman", 10, "bold"))
        lbl_selected_courses.grid(row=8, column=0, pady=5, padx=5, sticky="w")

        self.selected_courses_listbox = Listbox(Manage_Frame, height=3, font=("times new roman", 8), bd=2, relief=GROOVE)
        self.selected_courses_listbox.grid(row=8, column=1, pady=5, padx=5, sticky="w", rowspan=2)

        btn_remove_course = Button(Manage_Frame, text="Remove Course", font=("timesnewroman 9 bold"), bg="red",
                                   cursor="hand2", fg="white", height=2, width=15, command=self.remove_course)
        btn_remove_course.grid(row=7, column=1, pady=1)

        lbl_add = Label(Manage_Frame, text="Address", bg="springgreen4", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_add.grid(row=10, column=0, pady=5, padx=5, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=15, height=2, font=("times new roman", 10, "bold"), bd=5,
                                relief=GROOVE)
        self.txt_Address.grid(row=10, column=1, pady=5, padx=5, sticky="w")

        # Button Frame
        btn_Frame = Frame(Manage_Frame, relief=RIDGE, bg="springgreen4")
        btn_Frame.place(x=0, y=490, width=400)

        Addbtn = Button(btn_Frame, text="Add", font=("goudyoldstyle 8 bold"), bg="turquoise4", cursor="hand2", fg="white",
                        height=2, width=10, command=self.add_students)
        Addbtn.grid(row=0, column=0, padx=5, pady=8)
        Updatebtn = Button(btn_Frame, text="Update", font=("goudyoldstyle 8 bold"), cursor="hand2", bg="turquoise3",
                           fg="white", height=2, width=10, command=self.update_data)
        Updatebtn.grid(row=0, column=1, padx=5, pady=8)
        Deletebtn = Button(btn_Frame, text="Delete", font=("goudyoldstyle 8 bold"), cursor="hand2", bg="brown",
                           fg="white", height=2, width=10, command=self.delete_data)
        Deletebtn.grid(row=0, column=2, padx=5, pady=8)
        Clearbtn = Button(btn_Frame, text="Clear", font=("goudyoldstyle 8 bold"), cursor="hand2", bg="black",
                          fg="white", height=2, width=10, command=self.clear)
        Clearbtn.grid(row=0, column=3, padx=5, pady=8)

        # Detail Frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="springgreen4")
        Detail_Frame.place(x=425, y=30, width=680, height=600)

        lbl_search = Label(Detail_Frame, text="Search By", bg="springgreen4", fg="white",
                           font=("times new roman", 17, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.Search_By, width=10,
                                    font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll No.", "Name", "Age")
        combo_search.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"),
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", font=("times new roman", 10), cursor="hand2", bg="yellow",
                           fg="black", width=10, pady=5, command=self.search_data)
        searchbtn.grid(row=0, column=3, padx=6, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", cursor="hand2", width=10, pady=5, command=self.fetch_data)
        showallbtn.grid(row=0, column=4, padx=6, pady=10)

        # Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="springgreen4")
        Table_Frame.place(x=10, y=60, width=650, height=475)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame,
                                          columns=("Roll No.", 'Name', 'Age', 'Gender', 'Contact', 'Courses',
                                                   'Address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Roll No.", text="Roll No.")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Age", text="Age")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("Courses", text="Courses")
        self.Student_Table.heading("Address", text="Address")
        self.Student_Table['show'] = 'headings'
        self.Student_Table.column('Roll No.', width=80)
        self.Student_Table.column('Name', width=140)
        self.Student_Table.column('Age', width=100)
        self.Student_Table.column('Contact', width=140)
        self.Student_Table.column('Courses', width=120)
        self.Student_Table.column('Address', width=150)
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Load courses from the database and populate the course combobox
        self.load_courses()

    def load_courses(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT name FROM courses")
        courses = cur.fetchall()
        con.close()

        self.course_combobox['values'] = courses

    def add_course(self):
        selected_course = self.course_combobox.get()
        if selected_course not in self.selected_courses:
            self.selected_courses.append(selected_course)
            self.selected_courses_listbox.insert(END, selected_course)

    def remove_course(self):
        selected_index = self.selected_courses_listbox.curselection()
        if selected_index:
            self.selected_courses_listbox.delete(selected_index)
            del self.selected_courses[selected_index[0]]

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or len(self.selected_courses) == 0:
            messagebox.showerror("Error", "Roll No, Name, and Courses fields are required!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()

            cur.execute("INSERT INTO students VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (self.Roll_No_var.get(), self.Name_var.get(), self.Age_var.get(), self.Gender_var.get(),
                         self.Contact_No_var.get(), ", ".join(self.selected_courses),
                         self.txt_Address.get('1.0', END)))
            con.commit()
            con.close()
            self.clear()
            self.fetch_data()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Age_var.set("")
        self.Gender_var.set("")
        self.Contact_No_var.set("")
        self.course_var.set("")
        self.selected_courses.clear()
        self.selected_courses_listbox.delete(0, END)
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Student_Table.focus()
        contents = self.Student_Table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Age_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_No_var.set(row[4])
        self.selected_courses = [course.strip() for course in row[5].split(',')]
        self.selected_courses_listbox.delete(0, END)
        for course in self.selected_courses:
            self.selected_courses_listbox.insert(END, course)
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        cur.execute("UPDATE students SET name=%s, age=%s, gender=%s, contact=%s, course=%s, address=%s WHERE roll_no=%s",
                    (self.Name_var.get(), self.Age_var.get(), self.Gender_var.get(), self.Contact_No_var.get(),
                     ", ".join(self.selected_courses), self.txt_Address.get('1.0', END), self.Roll_No_var.get()))
        con.commit()
        messagebox.showinfo("Success", "Record has been updated")
        con.close()
        self.fetch_data()
        self.clear()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE roll_no = %s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()

        search_column = self.Search_By.get()
        search_text = self.search_txt.get()

        if search_column and search_text:
            query = "SELECT * FROM students WHERE {} LIKE %s".format(search_column)
            cur.execute(query, ("%" + search_text + "%",))
            rows = cur.fetchall()

            if len(rows) != 0:
                self.Student_Table.delete(*self.Student_Table.get_children())
                for row in rows:
                    self.Student_Table.insert('', END, values=row)
                con.commit()

        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()
