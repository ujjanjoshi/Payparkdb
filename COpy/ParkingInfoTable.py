from tkinter import *
from tkinter import ttk
import pandas as p

class ParkingInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1300x600+25+50")
        self.root.resizable(False, False)
        # background Image
        # self.bg =ImageTk.P#hotoImage(file="..")
        # self.bg_imge=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.root['bg'] = 'white'
        Frame_detail= Frame(self.root,bg="white")
        Frame_detail.place(x=0, y=0, width=1199 + 100, height=600 + 50)
        Label(Frame_detail, text="Details of User", font=("Goudy old style", 20, "bold"),justify="center", fg="black",
                        bg="white").place(x=500, y=40)
        Frame_table=Frame(self.root,bg="white")
        Frame_table.pack()
        Frame_table.place(x=0, y=100, width=1199 + 100, height=600 + 50)
        frame_sc=Scrollbar(Frame_table)
        frame_sc.pack(side=RIGHT, fill=Y)
        frame_sc = Scrollbar(Frame_table, orient='horizontal')
        frame_sc.pack(side=BOTTOM, fill=X)
        my_frame = ttk.Treeview(Frame_table,yscrollcommand=frame_sc.set, xscrollcommand=frame_sc.set)
        my_frame.pack()
        frame_sc.config(command=my_frame.yview)
        frame_sc.config(command=my_frame.xview)
        my_frame['columns'] = ('Token_no', 'NumberPlate', 'ParkingNo', 'Incoming', 'Outgoing','Hrs','Rate','Button')

        # format our column
        my_frame.column("#0", width=0)
        my_frame.column("Token_no", anchor=CENTER, width=140)
        my_frame.column("NumberPlate", anchor=CENTER, width=240)
        my_frame.column("ParkingNo", anchor=CENTER, width=100)
        my_frame.column("Incoming", anchor=CENTER, width=180)
        my_frame.column("Outgoing", anchor=CENTER, width=180)
        my_frame.column("Hrs", anchor=CENTER, width=100)
        my_frame.column("Rate", anchor=CENTER, width=100)
        my_frame.column("Button", anchor=CENTER, width=240)


        # Create Headings
        my_frame.heading("#0", text="", anchor=CENTER)
        my_frame.heading("Token_no", text="N_id", anchor=CENTER)
        my_frame.heading("NumberPlate", text="NumberPlate", anchor=CENTER)
        my_frame.heading("ParkingNo", text="Pk_no", anchor=CENTER)
        my_frame.heading("Incoming", text="IncomingTime", anchor=CENTER)
        my_frame.heading("Outgoing", text="OutgoingTime", anchor=CENTER)
        my_frame.heading("Hrs", text="Hrs", anchor=CENTER)
        my_frame.heading("Rate", text="Rate", anchor=CENTER)
        my_frame.heading("Button", text="Total", anchor=CENTER)

        data=p.read_csv('../Record/try.csv')
        print(data.loc[0][0])
        # add data
        data1 = p.read_csv('../Record/count.csv')
        count=0
        print(data1.loc[0][0])
        for rg in range(len(data)):
            for gr in range(len(data)):
                 print(data.loc[rg][gr],data.loc[rg][gr+1],data.loc[rg][gr+2],data.loc[rg][gr+3],data.loc[rg][gr+4],data.loc[rg][gr+5],data.loc[rg][gr+6],data.loc[rg][gr+7])
                 my_frame.insert(parent='', index='end', iid=count, text='',values=(data.loc[rg][gr],data.loc[rg][gr+1],data.loc[rg][gr+2],data.loc[rg][gr+3],data.loc[rg][gr+4],data.loc[rg][gr+5],data.loc[rg][gr+6],data.loc[rg][gr+7]))
                 count=count+1
                 finalco=count
                 break
        print(finalco)
        with open('../Record/count.csv', 'w') as fi:
            fi.writelines('Count\n')
            fi.writelines(f'{finalco}')
            fi.close()
        # my_frame.insert(parent='', index='end', iid=0, text='',
        #                values=('1', 'Ninja', '101', 'Oklahoma', 'Moore','1hr','30',
        #                 Button(Frame_table,text="check", bd=0, font=("Goudy old style", 12), fg="#6162FF",
        #                   bg="white")))
        # my_frame.insert(parent='', index='end', iid=1, text='',
        #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', '1hr', '30', 'btn'))
        # my_frame.insert(parent='', index='end', iid=2, text='',
        #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', '1hr', '30', 'btn'))
        # my_frame.insert(parent='', index='end', iid=3, text='',
        #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', '1hr', '30', 'btn'))
        # my_frame.insert(parent='', index='end', iid=4, text='',
        #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', '1hr', '30', 'btn'))
        # my_frame.insert(parent='', index='end', iid=5, text='',
        #                 values=('1', 'Ninja', '101', 'Oklahoma', 'Moore', '1hr', '30', 'btn'))
        my_frame.pack()
#
# parking = Tk()
# ParkingInfo(parking)
# parking.mainloop()
