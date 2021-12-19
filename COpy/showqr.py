from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pandas as p
class QrShow:
    def __init__(self,root):
        global image3
        self.root = root
        self.root.title("Qrcode")
        self.root.geometry("420x420+500+150")
        self.root.resizable(False, False)
        image3 = Image.open(f"Qr.png")
        # resize_image = image.resize((140, 140))
        img1 = ImageTk.PhotoImage(image3)
        label1 = Label(self.root, image=img1)
        label1.place(x=0, y=0)
        label1.image = img1
        # .place(x=20+210,y=30+30)
        Label(self.root,text=messagebox.showinfo("sucess","PaymentSucessful"))
        self.root.destory()
    def main(self):
        from MainPage import MainPage
        data=p.read_csv("../Record/login.csv")
        usr=data.loc[0]["Username"]
        MainPage(Tk,usr)
#
# main=Tk()
# QrShow(main)
# main.mainloop()