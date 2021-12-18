from tkinter import *
import pandas as p
import datetime

class ParkingAvailable:
    def __init__(self,root):
        self.root = root
        self.root.title("Parking Available")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        data=p.read_csv("../Record/parkingno.csv")
        self.parking=data["parking"][0]
        # print()
        rd=p.read_csv("../Record/record.csv")
        self.datalgth=len(rd)
        print(self.datalgth)
        self.res=self.parking-self.datalgth
        print(self.parking)
        Frame_prk = Frame(self.root, bg="white")
        Frame_prk.place(x=0, y=0, width=1199, height=600)
        title=Label(Frame_prk, text="Parking Available", font=("Impact", 30), fg="black", bg="white")
        title.place(x=8, y=20)
        num=Label(Frame_prk, text=self.res, font=("Impact", 100), fg="black", bg="white")
        num.place(x=80, y=100)
        num = Label(Frame_prk, text="hello", font=("Impact", 100), fg="black", bg="white")
        num.place(x=80, y=280)
        self.now = datetime.datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")
        # print("Current Time =", current_time)
        time = Label(Frame_prk, text=self.current_time, font=("Impact", 100), fg="black", bg="white")
        time.place(x=80, y=280)
        self.root.after(1000,self.refresher)
    def refresher(self):
        rd = p.read_csv("../Record/record.csv")
        self.datalgth = len(rd)
        self.res = self.parking - self.datalgth
        print(self.res)
        self.now = datetime.datetime.now()
        self.current_time = self.now.strftime("%H:%M:%S")
        print("Current Time =", self.current_time)
        Frame_prk = Frame(self.root, bg="white")
        Frame_prk.place(x=0, y=0, width=300, height=300)
        title = Label(Frame_prk, text="Parking Available", font=("Impact", 30), fg="black", bg="white")
        title.place(x=8, y=20)
        num = Label(Frame_prk, text=self.res, font=("Impact", 100), fg="black", bg="white")
        num.place(x=80, y=100)
        time = Label(Frame_prk, text=self.current_time, font=("Impact", 100), fg="black", bg="white")
        time.place(x=80, y=280)

        self.root.after(1000, self.refresher)


parkingwindow=Tk()
ParkingAvailable(parkingwindow)
parkingwindow.mainloop()