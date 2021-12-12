from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pandas as p
from MainPage import MainPage
from FaceRecong import FaceReco
from datetime import datetime
from forgetpass import ForgetPass
from ParkingDisplay import ParkingAvailable

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # background Image
        # self.bg =ImageTk.P#hotoImage(file="..")
        # self.bg_imge=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)
        # title and subtitle
        Label(Frame_login, text="Login here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90,
                                                                                                           y=30)
        Label(Frame_login, text="Members Area Login", font=("Goudy old style", 15, "bold"), fg="#1d1d1d",
              bg="white").place(x=90, y=100)
        # username
        Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",
              bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)
        Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",
              bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        # button
        Button(Frame_login, command=self.checkpass,text="Forget Password?", bd=0, font=("Goudy old style", 12), fg="#6162FF",
               bg="white").place(x=90, y=280)
        Button(Frame_login, command=self.check_function, text="Login", bd=0, font=("Goudy old style", 15),
               bg="#6162FF",
               fg="white").place(x=90, y=320, width=180, height=40)
        Button(Frame_login, command=self.camera, text="UseCamera", bd=0, font=("Goudy old style", 15),
               bg="#6162FF",
               fg="white").place(x=300, y=320, width=180, height=40)

    def check_function(self):
        file = p.read_csv('../Data/login.csv')
        self.usrname = file.username
        self.passwrd = file.password
        self.length = len(file)
        self.flag = 0
        self.user = self.username.get()
        self.pas = self.password.get()
        self.loops()

    def loops(self):
        for i in range(self.length):
            print(self.usrname[i],self.passwrd[i])
            # ans=self.user == self.usrname[i] or self.pas == self.passwrd[i]
            # print (ans)
            if self.user == self.usrname[i] and self.pas == self.passwrd[i]:
                self.flag = 1
            if self.user == "" or self.pas == "":
                self.flag = 2
        print(self.flag)
        print(self.user, self.pas)
        self.check()

    def check(self):
        print(self.flag)
        if self.flag==2:
            messagebox.showerror("Error", "All field are required", parent=self.root)
            Login(self.root)
        if self.flag==0:
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
            Login(self.root)
        if self.flag==1:
            self.close_window()
            self.markAttendence(self.user)
            # messagebox.showinfo("Welcome","Welcome to Main Page!!")
            MainPage(Tk())
            ParkingAvailable(Tk())

    def markAttendence(self, name):
        with open('../Record/Attendence.csv', 'r+') as f:
            mydataList = f.readlines()
            namelist = []
            print(mydataList)
            for line in mydataList:
                entry = line.split(',')
                namelist.append(entry[0])
            if name not in namelist:
                now = datetime.now()
                dtString = now.strftime('%H:%M%S')
                f.writelines(f'\n{name},{dtString}')

    def close_window(self):
        self.root.destroy()

    def camera(self):
        FaceReco(True)
        self.close_window()

    def checkpass(self):
        # self.close_window()
        ForgetPass(True)