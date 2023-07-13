from tkinter import *
from tkinter import ttk,messagebox
import pymysql
from PIL import Image,ImageTk
from pymysql import cursors

class Register():
    def __init__(self,root):
        self.root = root
        self.root.title("Registration - Student Management System")
        self.root.geometry("1310x690+0+0")
        self.root.config(bg="lightgray")

        # BG Image
        self.image1 = Image.open("images/image.jpg")
        self.resize_image1 = self.image1.resize((1300,1000))
        img1 = ImageTk.PhotoImage(self.resize_image1)
        # create label and add resize image
        label1 = Label(image=img1)
        label1.image = img1
        label1.place(x=00,y=0,relwidth=1,relheight=1)

        # side IMAGE 
        self.image2 = Image.open("images/kuLogo.jpeg")
        # Reszie the image using resize() method
        self.resize_image2 = self.image2.resize((280, 420))
        img2 = ImageTk.PhotoImage(self.resize_image2)

        # create label and add resize image
        label2 = Label(image=img2)
        label2.image = img2
        label2.place(x=110,y=90)

        framebtn = Frame(self.root, bg = "white")
        framebtn.place(x=110,y=510,width=290,height=60)
        
        # Frames
        frame1 = Frame(self.root, bg = "white")
        frame1.place(x=391,y=90,width=700,height=480)
        

        title = Label(frame1,text="Register Here",font=("timesnewroman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
        f_name = Label(frame1,text="First Name",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("timesnewroman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)


        l_name = Label(frame1,text="Last Name",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=("timesnewroman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        # =======row2

        f_contact = Label(frame1,text="Contact No.",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact = Entry(frame1,font=("timesnewroman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame1,text="Email",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email = Entry(frame1,font=("timesnewroman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)


        # =====row3
        f_security = Label(frame1,text="Security Question",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.combo_security = ttk.Combobox(frame1,font=("timesnewroman",13),state="readonly",justify=CENTER)
        self.combo_security['values'] = ("Select","You best friend name","Your favourite colour","Your birth place")
        self.combo_security.place(x=50,y=270,width=250)
        self.combo_security.current(0)


        answer = Label(frame1,text="Answer",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer = Entry(frame1,font=("timesnewroman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
        # =======row4

        f_pass = Label(frame1,text="Password",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_pass = Entry(frame1,font=("timesnewroman",15), show="*",bg="lightgray")
        self.txt_pass.place(x=50,y=340,width=250)

        txt_cpass = Label(frame1,text="Confirm Password",font=("timesnewroman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpass = Entry(frame1,font=("timesnewroman",15), show="*",bg="lightgray")
        self.txt_cpass.place(x=370,y=340,width=250)

        # Terms 

        self.var_chk = IntVar()
        chk = Checkbutton(frame1,text="I Agree The Terms and Conditions",variable=self.var_chk , offvalue=0 , onvalue=1 ,font=("times new roman", 12),bg="white").place(x=50,y=376)

        
        # Buttons
        forget_btn = Button(frame1,text="Forget Password?",cursor="hand2",bg="white",fg="green",font=("timesnewroman 12 ")).place(x=370 ,y=410,width=250,height=26  )
        
        register_btn = Button(frame1,cursor="hand2",text="Register", command=self.register_data, bg="green",fg="white",font=("timesnewroman 19 ")).place(x=50 ,y=410,width=200,height=30  )
        
        login_btn = Button(framebtn,cursor="hand2",text="Sign In",command=self.signin_window,bg="brown",fg="white",font=("timesnewroman 19 ")).place(x=80 ,y=5,width=120,height=30  )

    def signin_window(self):
        self.new_window = self.root
        self.new_obj = self.lazy_import_login_window(self.new_window)

    def lazy_import_login_window(self, root):
        from logIN import Login_window
        return Login_window(root)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_cpass.delete(0,END)
        self.combo_security.current(0)

    def register_data(self):

        if   self.txt_fname.get()==""  or self.txt_contact.get()=="" or self.txt_email.get()==""  or self.combo_security.get()=="Select"  or self.txt_answer.get()==""or self.txt_pass.get()=="" or self.txt_cpass.get()=="":
           messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same ", parent=self.root)

        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree our terms & conditions", parent=self.root)
            
        
        else:
           
            try:
                con = pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur = con.cursor()
                cur.execute("Select * from registration where email=%s",self.txt_email.get())
                row = cur.fetchone()
                # print(row)
                if row != None:
                     messagebox.showerror("Error", "User Already Exist, Please try with another email", parent=self.root)
            

                else:

                    cur.execute("insert into registration (f_name,l_name,contact,email,question,answer,password ) values( %s,%s,%s,%s,%s,%s,%s )",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.combo_security.get(),
                                self.txt_answer.get(),
                                self.txt_pass.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successful, You can now Signin", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
       

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
