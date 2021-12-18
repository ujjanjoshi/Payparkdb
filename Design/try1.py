from tkinter import *


class Try1:
    def __init__(self,root):
        print("Hello1")

        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        Button(self.root, command=self.rst, text="Forget Password?", bd=0, font=("Goudy old style", 12),
               fg="black",
               bg="#F9F1F1").place(x=130, y=310)
    def rst(self):
        import try2
        try2.Try2(Tk())

w=Tk()
Try1(w)
w.mainloop()