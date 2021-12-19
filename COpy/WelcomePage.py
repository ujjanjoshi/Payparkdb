from tkinter import *
from PIL import ImageTk
from LoginPage import Login

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Page")
        self.root.geometry("1199x600+100+50")
        #disable resize
        self.root.resizable(False,False)
        # background Image
        # self.bg=ImageTK.PhotoImage(file="")
        # self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)
        Frame_Welcome = Frame(self.root, bg="#F1D9D9")
        Frame_Welcome.place(x=0, y=0, width=1199, height=600)
        title=Label(Frame_Welcome, text="WELCOME TO PAYPARK...", font=("Goudy old Style",45),fg="black",bg="#F1D9D9")
        title.place(x=210,y=200)
        Button(Frame_Welcome,command=self.login_fuction,text="Get Started", bd=0, font=("Goudy old Style", 15,"bold"), fg="white", bg="#CF2F2F").place(
            x=500, y=350, width=200, height=50)

    def login_fuction(self):
        self.close_window()
        Login(Tk())

    def close_window(self):
        welcome_root.destroy()

welcome_root = Tk()
obj = Welcome(welcome_root)
welcome_root.mainloop()
