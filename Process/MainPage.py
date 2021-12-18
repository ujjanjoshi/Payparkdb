from tkinter import *
from PIL import Image, ImageTk
import datetime
from datetime import date
import calendar
import pandas as p
from NumberPlateDetect import NumDetect
from OutgoingNumberPlateDetect import OutgoingNumDetect
from ParkingInfoTable import ParkingInfo
from ShowDetails import ShowDetails
from IncomingTable import IncomingDetails


class MainPage:
    def __init__(self, root,usr):
        global image
        self.root = root
        self.root.title("Profile")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.username=usr
        Frame_prk = Frame(self.root, bg="#F1D9D9")
        Frame_prk.place(x=0, y=0, width=1199, height=600)
        Frame_title = Frame(Frame_prk, bg="#CF2F2F")
        Frame_title.place(x=0, y=0, width=1199, height=60)
        title = Label(Frame_title, text="paYpark", font=("Goudy old Style", 15, "italic"), fg="white",
                      bg="#CF2F2F")
        title.place(x=45, y=15)
        Button(Frame_title,command=self.logout ,text="Log Out", bd=0, font=("Goudy old Style", 10, "bold"), fg="black", bg="#F1D9D9").place(
            x=1090, y=15, width=60, height=30)
        self.Frame_datetime = Frame(self.root, bg="white", highlightcolor="#EA7676",
                                    highlightbackground="#EA7676", highlightthickness=1)
        self.Frame_datetime.place(x=100, y=100, width=180, height=60)
        Frame_img = Frame(self.root, bg="white", highlightcolor="#EA7676",
                          highlightbackground="#EA7676", highlightthickness=1)
        Frame_img.place(x=100, y=200, width=180, height=280)
        image = Image.open(f"../Photo/{self.username}.png")
        resize_image = image.resize((140, 140))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(Frame_img, image=img)
        label1.place(x=16, y=20)
        label1.image = img
        data = p.read_csv("../Data/Useralldetails.csv")
        print(data.loc[0]["username"])
        for r in range(len(data)):
            if (data.loc[r]["username"] == self.username):
                self.name = (data.loc[r]["Name"])
        day = Label(Frame_img, text=f"{self.name} ",
                    font=("Goudy old Style", 14, "bold"), fg="black", bg="white")
        day.place(x=20, y=170)
        day = Label(Frame_img, text=f"{self.username}",
                    font=("Goudy old Style", 10, "italic"), fg="black", bg="white")
        day.place(x=50, y=205)
        Frame_login = Frame(self.root, bg="#CF2F2F")
        Frame_login.place(x=410, y=80, width=350, height=480)
        on_off = Button(Frame_login,command = self.numrec ,text="Incoming cam", bd=0, font=("Goudy old style", 15),
                        bg="white",
                        fg="black").place(x=50, y=50, width=250, height=60)
        on_off = Button(Frame_login, command = self.outnumrec,text="Outgoing cam", bd=0, font=("Goudy old style", 15),
                        bg="white",
                        fg="black").place(x=50, y=150, width=250, height=60)
        show_details = Button(Frame_login, command=self.parl1, text="Parked Vechiles", bd=0, font=("Goudy old style", 15),
                              bg="white",
                              fg="black").place(x=50, y=250, width=250, height=60)
        show_details = Button(Frame_login,command = self.parl, text="Full Details", bd=0, font=("Goudy old style", 15),
                              bg="white",
                              fg="black").place(x=50, y=350, width=250, height=60)
        self.Frame_park = Frame(self.root, bg="white", highlightcolor="#EA7676",
                                highlightbackground="#EA7676", highlightthickness=1)
        self.Frame_park.place(x=900, y=100, width=200, height=200)
        self.Frame_parktitle = Frame(self.Frame_park, bg="#CF2F2F")
        self.Frame_parktitle.place(x=0, y=0, width=200, height=40)
        title = Label(self.Frame_parktitle, text="Available Spaces", font=("Goudy old Style", 13), fg="white",
                      bg="#CF2F2F")
        title.place(x=35, y=5)
        self.qr=Frame(self.root,bg="white",highlightcolor="#EA7676",highlightbackground="#EA7676", highlightthickness=1)
        self.qr.place(x=900, y=350, width=200, height=200)
        self.timerefresher()

    def timerefresher(self):
        global image1
        data = p.read_csv("../Record/parkingno.csv")
        self.parking = data["parking"][0]
        rd = p.read_csv("../Record/allincomingrecord.csv")
        self.datalgth = len(rd)
        print(self.datalgth)
        self.res = self.parking - self.datalgth
        print(self.parking)
        num = Label(self.Frame_park, text=self.res, font=("Impact", 40), fg="black", bg="white")
        num.place(x=70, y=80)
        self.now = datetime.datetime.now()
        self.current_sec = self.now.strftime("%S")
        curr_date = date.today()
        if(int(self.current_sec)%2==0):
            self.now = datetime.datetime.now()
            self.current_time = self.now.strftime("%I:%M %p")
        else:
            self.now = datetime.datetime.now()
            self.current_time = self.now.strftime("%I %M %p")
        day = Label(self.Frame_datetime, text=f"{calendar.day_name[curr_date.weekday()]}",
                    font=("Goudy old Style", 10, "italic", "bold"), fg="black", bg="white")
        day.place(x=20, y=15)
        day = Label(self.Frame_datetime, text=f"{self.current_time} ",
                    font=("Goudy old Style", 10, "italic", "bold"), fg="black", bg="white")
        day.place(x=95, y=15)
        image1 = Image.open(f"Qr.png")
        resize_image = image1.resize((192, 190))
        img1 = ImageTk.PhotoImage(resize_image)
        label1 = Label(self.qr, image=img1)
        label1.place(x=0, y=0)
        label1.image = img1
        self.root.after(1000, self.timerefresher)

    def close_window(self):
        self.root.destroy()

    def numrec(self):
        NumDetect(True)

    def outnumrec(self):
        OutgoingNumDetect(True)

    def parl(self):
        self.close_window()
        ShowDetails(Tk())

    def parl1(self):
        self.close_window()
        IncomingDetails(Tk())

    def logout(self):
        self.close_window()
        import LoginPage
        LoginPage.Login(Tk())

        # LoginPageCopy()

# main=Tk()
# MainPage(main,"paypark_001")
# main.mainloop()
