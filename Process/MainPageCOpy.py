from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from NumberPlateDetect import NumDetect


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("600x650+450+30")
        self.root.resizable(False, False)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=0, y=0, width=600, height=650)
        on_off = Button(Frame_login, command=self.numrec,text="Incoming cam", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=50, y=50, width=500, height=100)
        on_off = Button(Frame_login, command=self.numrec, text="Outgoing cam", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=50, y=200, width=500, height=100)
        show_details = Button(Frame_login, text="Show Details", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=50, y=350, width=500, height=100)
        parking_information = Button(Frame_login, text="Parking Information", bd=0, font=("Goudy old style", 15),
                        bg="#6162FF",
                        fg="white").place(x=50, y=500, width=500, height=100)

    def numrec(self):
        NumDetect(True)

main=Tk()
MainPage(main)
main.mainloop()