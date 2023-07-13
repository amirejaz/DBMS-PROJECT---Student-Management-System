from tkinter import *
from PIL import ImageTk,Image
from datetime import *
# import time 
from math import *
import pymysql
from tkinter import messagebox
from register import Register
from dashboard import *

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login - Student Management System")
        self.root.geometry("1100x600+80+50")
        self.root.config(bg="thistle4")
       
       
         # BG Image
        self.image1 = Image.open("images/image.jpg")
        self.resize_image1 = self.image1.resize((1200,900))
        img1 = ImageTk.PhotoImage(self.resize_image1)
        label1 = Label(image=img1)
        label1.image = img1
        label1.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame

        login_frame = Frame(self.root,bg="white")
        login_frame.place(x=200,y=60,width=700,height=450)

        title_frame = Label(login_frame,text="LOGIN HERE",font="KinoMT 35 bold",fg="green",bg="white")
        title_frame.place(x=320,y=30)

        lbl_user = Label(login_frame,text="Email Address:",font="timesnewroman 28 bold",fg="violetred3",bg="white")
        lbl_user.place(x=340,y=140)
        
        self.txt_email = Entry(login_frame,font="timesnewroman 20 ",fg="black",bg="lightgray")
        self.txt_email .place(x=340,y=200,width=300,height=30) 
        
        lbl_pass = Label(login_frame,text="Password:",font="timesnewroman 28 bold",fg="violetred3",bg="white")
        lbl_pass.place(x=310,y=250,width=250,height=80)
        
        self.txt_pass = Entry(login_frame,font="timesnewroman 20 ", show="*",fg="black",bg="lightgray")
        self.txt_pass.place(x=340,y=320,width=300,height=30) 
        
        # #Button
        signin_btn = Button(login_frame,text="Login",command=self.login,cursor="hand2",bg="darkgreen",fg="white",font=("timesnewroman 14 bold")).place(x=350 ,y=390,width=140,height=37 )

        register_btn = Button(login_frame,text="Register New Account",command=self.register_window,cursor="hand2",bd=0,bg="white",fg="violetred4",font=("timesnewroman 12 ")).place(x=340 ,y=350,height=20 )

        # side image 
        self.image2 = Image.open("images/login.jpg")
        # Reszie the image using resize() method
        self.resize_image2 = self.image2.resize((280, 360))
        img2 = ImageTk.PhotoImage(self.resize_image2)
        # create label and add resize image
        label2 = Label(image=img2)
        label2.image = img2
        label2.place(x=220,y=140)        

    def register_window(self):
        self.root.destroy()
        root = Tk()
        obj = Register(root)
        root.mainloop()

    def login(self):
        if self.txt_email.get() =="" or self.txt_pass.get() =="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur = con.cursor()
                cur.execute("Select * from registration where email=%s and password=%s",(self.txt_email.get(),self.txt_pass.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                     messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
            
                else:
                    messagebox.showinfo("Success",f"WELCOME {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    root = Tk()
                    obj = STMS(root)
                    root.mainloop()
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

if __name__ == "__main__":        
    root = Tk()
    obj =  Login_window(root)
    root.mainloop()
