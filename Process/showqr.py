from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
class QrShow:
    def __init__(self,root):
        global image
        self.root = root
        self.root.title("Qrcode")
        self.root.geometry("420x420+500+150")
        self.root.resizable(False, False)
        image = Image.open(f"Qr.png")
        # resize_image = image.resize((140, 140))
        img = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image=img)
        label1.place(x=0, y=0)
        label1.image = img
        # .place(x=20+210,y=30+30)
        Label(self.root,text=messagebox.showinfo("sucess","PaymentSucessful"))
        self.root.destory()
# main=Tk()
# QrShow(main)
# main.mainloop()