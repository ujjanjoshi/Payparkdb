from tkinter import *
import pandas as p
from MainPage import MainPage
from ParkingDisplay import ParkingAvailable
from LoginPage import Login
class LoginConfrim:
    def __init__(self, root,usrname):
        self.root = root
        self.root.title("Login")
        self.username=usrname
        self.root.geometry("1199x600+100+50")
        #disable resize
        self.root.resizable(False,False)
        data = p.read_csv("../Data/Useralldetails.csv")
        print(data.loc[0]["username"])
        for r in range(len(data)):
            if (data.loc[r]["username"] == self.username):
                self.name=(data.loc[r]["Name"])
        Frame_Login = Frame(self.root, bg="#F1D9D9")
        Frame_Login.place(x=0, y=0, width=1199, height=600)
        Frame_Confrim = Frame(self.root, bg="#F9F1F1")
        Frame_Confrim.place(x=400, y=150, width=400, height=230)
        title=Label(Frame_Confrim,text=f"Welcome {self.name}!!",font=("Goudy old Style",20,"bold"),fg="black",bg="#F9F1F1")
        title.place(x=29,y=40)
        sub = Label(Frame_Confrim, text=f"You have logged in as {self.username}", font=("Goudy old Style", 15), fg="black", bg="#F9F1F1")
        sub.place(x=29, y=100)
        Button(Frame_Confrim,command=self.nxt,text="Next", bd=0,
        font=("Goudy old Style", 15), fg="white", bg="#CF2F2F").place(x=40, y=160, width=80, height=35)
        Button(Frame_Confrim,command=self.logout ,text="Logout", bd=0,
               font=("Goudy old Style", 15), fg="white", bg="#CF2F2F").place(x=250, y=160, width=80, height=35)
    def close_window(self):
        self.root.destroy()
    def logout(self):
        self.close_window()
        Login(Tk())
    def nxt(self):
        self.close_window()
        MainPage(Tk())
        ParkingAvailable(Tk())
