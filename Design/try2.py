from tkinter import *
class Try2:
    def __init__(self,root):
        print("Hello")
        self.root = root
        self.root.title("Login")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        Button(self.root, command=self.rs, text="Forget Password?", bd=0, font=("Goudy old style", 12),
               fg="black",
               bg="#F9F1F1").place(x=130, y=310)
    def rs(self):
        import try1
        try1.Try1(Tk())
