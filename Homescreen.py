from tkinter import *
from PIL import Image,ImageTk

class home():
    def __init__(self,root) :
        self.root = root
        self.root.title("Home Screen - Student Management System")
        self.root.geometry("1350x700+0+0")
        
        self.img = Image.open("images/home.jpg")
        self.resize_image1 = self.img.resize((1350,700))
        self.btnimg = ImageTk.PhotoImage( self.resize_image1)
        btn = Button(self.root, cursor="hand2",image=self.btnimg,command=self.reg_window).place(relwidth=1,relheight=1)
    
    def reg_window(self):
        self.root.destroy()
        from register import Register
        root = Tk()
        obj = Register(root)
        root.mainloop()
        
root=Tk()
obj = home(root)
root.mainloop()