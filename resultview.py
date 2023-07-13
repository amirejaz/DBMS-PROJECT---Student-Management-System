import pymysql
from tkinter import *
from tkinter import messagebox, ttk

class ResultView:
    def __init__(self, root):
        self.root = root
        self.root.title("View Result - Student Management System")
        self.root.geometry("1100x500+140+100")
        self.root.config(bg="white")

        Manage_Frame = Frame(self.root, bd=4, bg="darkorange")
        Manage_Frame.place(x=0, y=10, width=1100, height=60)

        m_title = Label(Manage_Frame, text="View Student Results", fg="white", bg="darkorange", font=("times new roman", 30, "bold"))
        m_title.place(x=380, y=2)

        footerFrame = Frame(self.root, bd=4, bg="turquoise4")
        footerFrame.place(x=0, y=468, width=1100, height=30)

        f_title = Label(footerFrame, text="Designed and Developed by Amir Aijaz", fg="white", bg="turquoise4", font=("times new roman", 15))
        f_title.place(x=390, y=0)

        self.searchBy_label = Label(self.root, text="Search By:", bg="white", font=("times new roman", 15))
        self.searchBy_label.place(x=180, y=100)

        self.roll_no_label = Label(self.root, text="Roll No:", bg="white", font=("times new roman", 15))
        self.roll_no_label.place(x=310, y=100)

        self.roll_no_entry = Entry(self.root, font=("goudy old style", 15), bg="cornsilk2")
        self.roll_no_entry.place(x=390, y=100)

        self.search_button = Button(self.root, text="Search", font=("times new roman", 15, "bold"), bg="deepskyblue2", cursor="hand2", width=13, fg="white", command=self.search_result)
        self.search_button.place(x=630, y=95)

        roll_no_lbl = Label(self.root, text="Roll No.", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        roll_no_lbl.place(x=110, y=250, width=150, height=50)
        name_lbl = Label(self.root, text="Name", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        name_lbl.place(x=260, y=250, width=150, height=50)
        course_lbl = Label(self.root, text="Course", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        course_lbl.place(x=410, y=250, width=150, height=50)
        marks_obtained_lbl = Label(self.root, text="Marks Obtained", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        marks_obtained_lbl.place(x=560, y=250, width=150, height=50)
        total_marks_lbl = Label(self.root, text="Total Marks", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        total_marks_lbl.place(x=710, y=250, width=150, height=50)
        percentage_lbl = Label(self.root, text="Percentage", font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        percentage_lbl.place(x=860, y=250, width=150, height=50)

        self.roll_no = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.roll_no.place(x=110, y=300, width=150, height=50)
        self.name = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.name.place(x=260, y=300, width=150, height=50)
        self.course = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.course.place(x=410, y=300, width=150, height=50)
        self.marks_obtained = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.marks_obtained.place(x=560, y=300, width=150, height=50)
        self.total_marks = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.total_marks.place(x=710, y=300, width=150, height=50)
        self.percentage = Entry(self.root, font=("times new roman", 12), bg="white", fg="black", bd=2, relief=RIDGE)
        self.percentage.place(x=860, y=300, width=150, height=50)

        self.delete_button = Button(self.root, text="Delete", font=("times new roman", 12, "bold"), bg="red2", fg="white", cursor="hand2", width=12, command=self.delete_result)
        self.delete_button.place(x=400, y=380)

        self.clear_button = Button(self.root, text="Clear", font=("times new roman", 12, "bold"), bg="gray11", fg="white", cursor="hand2", width=12, command=self.clear_result)
        self.clear_button.place(x=530, y=380)

    def search_result(self):
        roll_no = self.roll_no_entry.get()

        if roll_no:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("SELECT * FROM results WHERE roll_no = %s", (roll_no,))
            result = cur.fetchone()
            if result:
                self.roll_no.delete(0, END)
                self.roll_no.insert(END, result[0])
                self.name.delete(0, END)
                self.name.insert(END, result[1])
                self.course.delete(0, END)
                self.course.insert(END, result[2])
                self.marks_obtained.delete(0, END)
                self.marks_obtained.insert(END, result[3])
                self.total_marks.delete(0, END)
                self.total_marks.insert(END, result[4])
                percentage = (result[3] / result[4]) * 100
                self.percentage.delete(0, END)
                self.percentage.insert(END, percentage)
            else:
                messagebox.showinfo("Information", "No result found for the specified Roll No.")

            con.close()
        else:
            messagebox.showerror("Error", "Please enter a Roll No.")

    def delete_result(self):
        roll_no = self.roll_no.get()

        if roll_no:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("DELETE FROM results WHERE roll_no = %s", (roll_no,))
            con.commit()
            con.close()
            messagebox.showinfo("Information", "Result for Roll No. {} has been deleted.".format(roll_no))
            self.clear_result()
        else:
            messagebox.showerror("Error", "Please enter a Roll No.")

    def clear_result(self):
        self.roll_no.delete(0, END)
        self.name.delete(0, END)
        self.course.delete(0, END)
        self.marks_obtained.delete(0, END)
        self.total_marks.delete(0, END)
        self.percentage.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    obj = ResultView(root)
    root.mainloop()
