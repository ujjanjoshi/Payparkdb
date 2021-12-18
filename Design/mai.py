from tkinter import *
from PIL import Image, ImageTk
import datetime
from datetime import date
import calendar
import pandas as p
class ParkingAvailable:
    def __init__(self,root):
        global photo,image
        self.root = root
        self.root.title("Profile")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        Frame_prk = Frame(self.root, bg="#F1D9D9")
        Frame_prk.place(x=0, y=0, width=1199, height=600)
        Frame_title = Frame(Frame_prk, bg="#CF2F2F")
        Frame_title.place(x=0, y=0, width=1199, height=60)
        title = Label(Frame_title, text="paYpark", font=("Goudy old Style", 15,"italic"), fg="white",
                      bg="#CF2F2F")
        title.place(x=45, y=15)
        Button(Frame_title, text="Log Out", bd=0,font=("Goudy old Style", 10, "bold"), fg="black", bg="#F1D9D9").place(
               x=1090, y=15, width=60, height=30)
        self.Frame_datetime=Frame(self.root, bg="white",highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.Frame_datetime.place(x=100, y=100, width=180, height=60)
        Frame_img = Frame(self.root,bg="white",highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        Frame_img.place(x=100, y=200, width=180, height=280)
        image = Image.open("../Photo/paypark_001.png")
        resize_image = image.resize((140, 140))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(Frame_img,image=img)
        label1.place(x=16,y=20)
        label1.image = img
        day = Label(Frame_img, text=f"Ram Shrestha ",
                    font=("Goudy old Style", 14, "bold"), fg="black", bg="white")
        day.place(x=20, y=170)
        day = Label(Frame_img, text=f"paypark_1001 ",
                    font=("Goudy old Style", 10, "italic"), fg="black", bg="white")
        day.place(x=50, y=205)
        Frame_login = Frame(self.root, bg="#CF2F2F")
        Frame_login.place(x=410, y=100, width=350, height=380)
        on_off = Button(Frame_login, text="Incoming cam", bd=0, font=("Goudy old style", 15),
                        bg="white",
                        fg="black").place(x=50, y=80, width=250, height=60)
        on_off = Button(Frame_login, text="Outgoing cam", bd=0, font=("Goudy old style", 15),
                        bg="white",
                        fg="black").place(x=50, y=180, width=250, height=60)
        show_details = Button(Frame_login, text="Show Details", bd=0, font=("Goudy old style", 15),
                              bg="white",
                              fg="black").place(x=50, y=280, width=250, height=60)
        self.Frame_park = Frame(self.root, bg="white",highlightcolor="#EA7676",
                              highlightbackground="#EA7676", highlightthickness=1)
        self.Frame_park.place(x=900, y=100, width=200, height=200)
        self.Frame_parktitle = Frame(self.Frame_park, bg="#CF2F2F")
        self.Frame_parktitle.place(x=0, y=0, width=200, height=40)
        title = Label(self.Frame_parktitle, text="Available Spaces", font=("Goudy old Style", 13), fg="white",
                      bg="#CF2F2F")
        title.place(x=35,y=5)
        self.timerefresher()


    def timerefresher(self):
        data = p.read_csv("../Record/parkingno.csv")
        self.parking = data["parking"][0]
        rd = p.read_csv("../Record/record.csv")
        self.datalgth = len(rd)
        print(self.datalgth)
        self.res = self.parking - self.datalgth
        print(self.parking)
        num = Label(self.Frame_park, text=self.res, font=("Impact", 40), fg="black", bg="white")
        num.place(x=70, y=80)
        self.now = datetime.datetime.now()
        self.current_time = self.now.strftime("%H:%M %p")
        curr_date = date.today()
        day = Label(self.Frame_datetime, text=f"{calendar.day_name[curr_date.weekday()]}",
                         font=("Goudy old Style", 10,"italic","bold"), fg="black", bg="white")
        day.place(x=20, y=15)
        day = Label(self.Frame_datetime, text=f"{self.current_time} ",
                    font=("Goudy old Style", 10, "italic", "bold"), fg="black", bg="white")
        day.place(x=95, y=15)

        self.root.after(1000, self.timerefresher)

parkingwindow=Tk()
ParkingAvailable(parkingwindow)
parkingwindow.mainloop()