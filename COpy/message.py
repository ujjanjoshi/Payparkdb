from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
class Message:
    def __init__(self,root):
        # global image
        self.root = root
        self.root.title("Qrcode")
        self.root.geometry("0x0+600+350")
        # self.root.resizable(False, False)
        Label(self.root,text=messagebox.showinfo("sucess","PaymentSucessful"))
        self.root.destory()