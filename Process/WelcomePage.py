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
        Frame_Welcome = Frame(self.root, bg="white")
        Frame_Welcome.place(x=0, y=0, width=1199, height=600)
        title=Label(Frame_Welcome, text="Welcome to ABC Parking Lot", font=("Impact",50,"bold"),fg="black",bg="white")
        title.place(x=210,y=200)
        Button(Frame_Welcome,command=self.login_fuction,text="Continue", bd=0, font=("Goudy old Style", 15), fg="white", bg="#6162FF").place(
            x=500, y=350, width=180, height=80)

    def login_fuction(self):
        self.close_window()
        Login(Tk())

    def close_window(self):
        welcome_root.destroy()

welcome_root = Tk()
obj = Welcome(welcome_root)
welcome_root.mainloop()
