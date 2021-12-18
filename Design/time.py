from tkinter import *
import pandas as p
import datetime
from datetime import date
import calendar

class ParkingAvailable:
    def __init__(self,root):
        self.root = root
        self.root.title("Parking Available")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        self.Frame_prk = Frame(self.root, bg="white")
        self.Frame_prk.place(x=0, y=0, width=1199, height=600)
        self.refresher()
    def refresher(self):
        self.now = datetime.datetime.now()
        self.current_time = self.now.strftime("%H:%M %p")
        curr_date = date.today()
        time = Label(self.Frame_prk, text=f"{calendar.day_name[curr_date.weekday()]}{self.current_time}", font=("Impact", 50), fg="black", bg="white")
        time.place(x=80, y=280)

        self.root.after(1000, self.refresher)


parkingwindow=Tk()
ParkingAvailable(parkingwindow)
parkingwindow.mainloop()