from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql.cursors import Cursor

class Courses():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1100x600+200+100")
        self.root.config(bg="cornsilk2")

        #=====All Variables=====
        
        self.Name_var=StringVar()
        self.Duration_var=StringVar()
        self.Charges_var=StringVar()
        self.Search_By = StringVar()
        self.search_txt = StringVar()
      

    #===Manage Frame=====
    
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="springgreen4")
        Manage_Frame.place(x=20,y=30,width=370,height=560)

        m_title=Label(Manage_Frame,text="Manage Courses",fg="white",bg="springgreen4",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        lbl_name=Label(Manage_Frame,text="Course Name",bg="springgreen4",fg="white",font=("times new roman",15,"bold"))
        lbl_name.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        
        lbl_duration=Label(Manage_Frame,text="Duration",bg="springgreen4",fg="white",font=("times new roman",15,"bold"))
        lbl_duration.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        
        txt_duration=Entry(Manage_Frame,textvariable=self.Duration_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_duration.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
        lbl_charges=Label(Manage_Frame,text="Charges",bg="springgreen4",fg="white",font=("times new roman",15,"bold"))
        lbl_charges.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        txt_charges=Entry(Manage_Frame,textvariable=self.Charges_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_charges.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        lbl_description=Label(Manage_Frame,text="Description",bg="springgreen4",fg="white",font=("times new roman",15,"bold"))
        lbl_description.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        
        self.txt_descp=Text(Manage_Frame,width=20,height=3,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        self.txt_descp.grid(row=4,column=1,pady=10,padx=10,sticky="w")

    #===Button Frame=====

        btn_Frame=Frame(Manage_Frame,relief=RIDGE,bg="springgreen4")
        btn_Frame.place(x=0,y=490,width=400)

        Addbtn=Button(btn_Frame,text="Add", font=("goudyoldstyle 8 bold"), bg="cyan4", cursor="hand2", fg="white", height=2,width=10,command=self.add_courses)
        Addbtn.grid(row=0,column=0,padx=5,pady=11)        
        Updatebtn=Button(btn_Frame,text="Update", font=("goudyoldstyle 8 bold"),cursor="hand2", bg="crimson", fg="white", height=2, width=10,command=self.Update_data)
        Updatebtn.grid(row=0,column=1,padx=5,pady=11)        
        Deletebtn=Button(btn_Frame,text="Delete", font=("goudyoldstyle 8 bold"), cursor="hand2", bg="red", fg="white", height=2, width=10,command=self.delete_data)
        Deletebtn.grid(row=0,column=2,padx=5,pady=11)        
        Clearbtn=Button(btn_Frame,text="Clear", font=("goudyoldstyle 8 bold"), cursor="hand2", bg="black", fg="white", height=2, width=10,command=self.clear)
        Clearbtn.grid(row=0,column=3,padx=5,pady=11)        

    #===Detail Frame=====

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="springgreen4")
        Detail_Frame.place(x=405,y=30,width=680,height=550)
        
        lbl_search=Label(Detail_Frame,text="Search By",bg="springgreen4",fg="white",font=("times new roman",17,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")
     
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.Search_By,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Name")
        combo_search.grid(row=0,column=1,pady=10,padx=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search", font=("goudyoldstyle 8 bold"), bg="yellow", cursor="hand2",width=10,pady=5,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=6,pady=10)        
        showallbtn=Button(Detail_Frame,text="Show All", font=("goudyoldstyle 8 bold"), cursor="hand2",width=10,pady=5,command=self.fetch_data)
        showallbtn.grid(row=0,column=4,padx=6,pady=10)        

    #========Table Frame=====

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="springgreen4")
        Table_Frame.place(x=10,y=60,width=650,height=475)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Course_Table = ttk.Treeview(Table_Frame,columns=("cid", "name", "duration", "charges", "description"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Course_Table.xview)
        scroll_y.config(command=self.Course_Table.yview)
        
        self.Course_Table.heading("cid",text="Course ID")
        self.Course_Table.heading("name",text="Name")
        self.Course_Table.heading("duration",text="Duration")
        self.Course_Table.heading("charges",text="Charges")
        self.Course_Table.heading("description",text="Descripion")   
        self.Course_Table['show']='headings'
        self.Course_Table.column('cid',width=60)
        self.Course_Table.column('name',width=120)
        self.Course_Table.column('duration',width=70)
        self.Course_Table.column('charges',width=70)
        self.Course_Table.column('description',width=150)   
        self.Course_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Course_Table.bind("<ButtonRelease-1>",self.get_cursor )
        
    def add_courses(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        try:
            if self.Name_var.get() == "" or self.Charges_var.get() == "" or self.Duration_var.get() == "":
                messagebox.showerror("Error", "All fields are required!")
            else:
                cur.execute("SELECT * FROM courses WHERE name = %s", (self.Name_var.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course name already exists!")
                else:
                    cur.execute("INSERT INTO courses (name, duration, charges, description) VALUES (%s, %s, %s, %s)",
                                (self.Name_var.get(), self.Duration_var.get(), self.Charges_var.get(),
                                self.txt_descp.get('1.0', END)))
                con.commit()
                self.clear()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Course added successfully!")
        except Exception as e:
            messagebox.showerror("Error", "An error occurred: " + str(e))

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from courses")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Course_Table.delete(*self.Course_Table.get_children())
            for row in rows:
                self.Course_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):  
        self.Name_var.set("")  
        self.Duration_var.set("")   
        self.Charges_var.set("")  
        self.txt_descp.delete("1.0",END)    

    def get_cursor(self,ev):
        cursor_row=self.Course_Table.focus()
        contents=self.Course_Table.item(cursor_row)
        row=contents['values']  
        self.Name_var.set(row[0])  
        self.Duration_var.set(row[1])  
        self.Charges_var.set(row[2])   
        self.txt_descp.delete("1.0",END)
        self.txt_descp.insert(END,row[3])
        
    def Update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("Update courses set Duration=%s,Charges=%s,Description=%s where name=%s",(self.Duration_var.get(),self.Gender_var.get(),self.Charges_var.get(),self.course_var.get(),self.txt_descp.get('1.0',END),self.Name_var.get() ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from courses where name = %s",self.Name_var.get())
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
            query = "SELECT * FROM courses WHERE {} LIKE %s".format(search_column)
            cur.execute(query, ("%" + search_text + "%",))
            rows = cur.fetchall()
            
            if len(rows) != 0:
                self.Course_Table.delete(*self.Course_Table.get_children())
                for row in rows:
                    self.Course_Table.insert('', END, values=row)
                con.commit()

        con.close()

if __name__ == "__main__":   
    root = Tk()
    obj = Courses(root)
    root.mainloop()    
