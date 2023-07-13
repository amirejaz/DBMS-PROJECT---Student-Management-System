from tkinter import *
from tkinter import Message, messagebox
from PIL import Image, ImageTk ,ImageDraw
from datetime import *
import os 
from math import *
from Course import Courses
from Student import Students
from Result import Results
from resultview import ResultView
import pymysql
import time

class STMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard - STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
  
        Manage_Frame = Frame(self.root,bg="white")
        Manage_Frame.place(x=0,y=0,relwidth=1,height=110)

        #title
        self.title = Label(Manage_Frame,text="Student Management System",font=("timesnewroman 50 bold "),bg="turquoise4",fg="white")
        self.title.place(x=0,y=10,relwidth=1,height=100)

        self.img = Image.open("images/logo2.jpg")
        self.resize_image1 = self.img.resize((80,80))
        self.logoimg = ImageTk.PhotoImage( self.resize_image1)
        labelimg = Label(Manage_Frame, image=self.logoimg)
        labelimg.image = self.logoimg
        labelimg.place(x=100, y=20)

        #Menu Frame 
        Menu_Frame = LabelFrame(self.root, bg="white")
        Menu_Frame.place(x=0,y=130,relwidth=1,height=100)

        txt_menu = Label(Menu_Frame,text="Menu",font=("timesnewroman 20"),bg="white",fg="black")
        txt_menu.place(x=5,y=10,height=20)

        #buttons inside menu
        course_btn = Button(Menu_Frame, text="Course", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.add_courses).place(x=100,y=40, width=120,height=40)
        std_btn = Button(Menu_Frame, text="Student", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.add_students).place(x=300,y=40, width=120,height=40)
        result_btn = Button(Menu_Frame, text="Result", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.add_results).place(x=500,y=40, width=120,height=40)
        viewR_btn = Button(Menu_Frame, text="View Result", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.view_results).place(x=700,y=40, width=120,height=40)
        logout_btn = Button(Menu_Frame, text="Logout", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.logOut).place(x=900,y=40, width=120,height=40)
        exit_btn = Button(Menu_Frame, text="Exit", font=("timesnewroman 15 "), bd=3, fg="white",bg="turquoise4",cursor="hand2", command=self.exit_).place(x=1100,y=40, width=120,height=40)

        #Background Image
        self.bg_img = Image.open("images/stud2.png")
        self.resize_image2 = self.bg_img.resize((880, 320))
        self.BGimg = ImageTk.PhotoImage( self.resize_image2)
        labelimg1 = Label(self.root, image=self.BGimg)
        labelimg1.image = self.BGimg
        labelimg1.place(x=400, y=240, width=870, height=320)
 
        #Update details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ] ", bd=7, relief=RIDGE, font=("times new roman", 20), bg="orange", fg="white")
        self.lbl_course.place(x=430, y= 570, width = 260, height = 70)
        self.lbl_results = Label(self.root, text="Total Results\n[ 0 ] ", bd=7, relief=RIDGE, font=("times new roman", 20), bg="red", fg="white")
        self.lbl_results.place(x=705, y= 570, width = 260, height = 70)
        self.lbl_students = Label(self.root, text="Total Students\n[ 0 ] ", bd=7, relief=RIDGE, font=("times new roman", 20), bg="green3", fg="white")
        self.lbl_students.place(x=980, y= 570, width = 260, height = 70)

        #footer
        
        footer_Frame = Frame(self.root, bg="turquoise4")
        footer_Frame.place(x=0,y=660,relwidth=1,height=40)
        self.lbl_footer = Label(footer_Frame, text="Designed and Developed by Amir Aijaz", font=("times new roman", 17), bg="turquoise4", fg="white")
        self.lbl_footer.place(x=450, y= 6, height = 20)

        # clock leftside
        self.lbl= Label(self.root,bg="black",bd=0)
        self.lbl.place(x=80,y=250, width=300, height=400)
        self.clock_working()

        #widget update
        self.update_details()

    def clock_image(self,hr,min_,sec_):
        clock = Image.new("RGB",(400,400),(0,0,0))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/clock1.png")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        origin=200,200
        # Hour line image 
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))),fill="red",width=3)
        # Min line image 
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))),fill="red",width=3)
        # Sec line image 
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))),fill="floralwhite",width=3)
        draw.ellipse((195,195,210,210),fill="gray")
        clock.save("images/clock_new.png")    

    def clock_working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(300,self.clock_working)  


    #Functions
    #Courses
    def add_courses(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Courses(self.new_window)
    
    #Students
    def add_students(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Students(self.new_window)
    # add_results
    def add_results(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Results(self.new_window)
    # view_results
    def view_results(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = ResultView(self.new_window)
    # logout
    def logOut(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            self.create_login_window()

    def create_login_window(root):
        from logIN import Login_window
        root = Tk()
        obj = Login_window(root)
        root.mainloop()

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

    def update_details(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor() 
        try:
            cur.execute("select * from courses")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            
            cur.execute("select * from results")
            cr = cur.fetchall()
            self.lbl_results.config(text=f"Total Results\n[{str(len(cr))}]")

            cur.execute("select * from students")
            cr = cur.fetchall()
            self.lbl_students.config(text=f"Total Students\n[{str(len(cr))}]")
            
        except Exception as ex: 
            messagebox.showerror("Error", f"Error due to {str(ex)}")
            
                   

  

                

if __name__ == "__main__":
    root = Tk()
    stms_app=STMS(root)
    root.mainloop()
