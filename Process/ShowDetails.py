from tkinter import *
from tkinter import ttk
import pandas as p


class ShowDetails:
    def __init__(self, root):
        global image
        self.root = root
        self.root.title("Details")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        Frame_prk = Frame(self.root, bg="#F1D9D9")
        Frame_prk.place(x=0, y=0, width=1199, height=600)
        Frame_title = Frame(Frame_prk, bg="#CF2F2F")
        Frame_title.place(x=0, y=0, width=1199, height=60)
        title = Button(Frame_title,command=self.back ,text="Back", font=("Goudy old Style", 15, "italic","underline"),bd=0 ,fg="white",
                      bg="#CF2F2F")
        title.place(x=45, y=13)
        title = Label(Frame_title, text="Details", font=("Goudy old Style", 20, "bold"), fg="white",
                      bg="#CF2F2F")
        title.place(x=555, y=15)
        Frame_tbl = Frame(Frame_prk, bg="white")
        Frame_tbl.place(x=25, y=80, width=1150, height=500)
        Frame_in =Frame(Frame_tbl,bg="#CF2F2F")
        Frame_in.place(x=0,y=0,width=1150,height=500)
        title = Label(Frame_in, text="Full Details", font=("Goudy old Style", 20, "bold"), fg="white",
                      bg="#CF2F2F")
        title.place(x=500, y=15)
        Frame_table = Frame(Frame_in, bg="white",bd=0)
        Frame_table.pack()
        Frame_table.place(x=0, y=70, width=1150, height=430)
        frame_sc = Scrollbar(Frame_table)
        frame_sc.pack(side=RIGHT, fill=Y)
        # frame_sc = Scrollbar(Frame_table, orient='horizontal')
        # frame_sc.pack(side=BOTTOM, fill=X)
        my_frame = ttk.Treeview(Frame_table, yscrollcommand=frame_sc.set)
        my_frame.pack()
        frame_sc.config(command=my_frame.yview)
        # frame_sc.config(command=my_frame.xview)
        my_frame['columns'] = ('Token_no', 'NumberPlate', 'ParkingNo', 'Incoming', 'Outgoing', 'Hrs', 'Rate', 'Button')

        # format our column
        # my_frame.column("#0", width=0)
        my_frame.column("Token_no", anchor=CENTER, width=60)
        my_frame.column("NumberPlate", anchor=CENTER, width=120)
        my_frame.column("ParkingNo", anchor=CENTER, width=60)
        my_frame.column("Incoming", anchor=CENTER, width=120)
        my_frame.column("Outgoing", anchor=CENTER, width=120)
        my_frame.column("Hrs", anchor=CENTER, width=60)
        my_frame.column("Rate", anchor=CENTER, width=60)
        my_frame.column("Button", anchor=CENTER, width=100)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Goudy old Style", 13,"bold"))
        my_frame['show'] = 'headings'
        # Create Headings
        # my_frame.heading("#0", text="",anchor=CENTER)
        my_frame.heading("Token_no", text="N_id", anchor=CENTER)
        my_frame.heading("NumberPlate", text="NumberPlate", anchor=CENTER)
        my_frame.heading("ParkingNo", text="Pk_no", anchor=CENTER)
        my_frame.heading("Incoming", text="IncomingTime", anchor=CENTER)
        my_frame.heading("Outgoing", text="OutgoingTime", anchor=CENTER)
        my_frame.heading("Hrs", text="Hrs", anchor=CENTER)
        my_frame.heading("Rate", text="Rate", anchor=CENTER)
        my_frame.heading("Button", text="Total", anchor=CENTER)
        style = ttk.Style()
        style.configure("Treeview", font=("Goudy old Style", 12),rowheight=40)
        style.layout("Treeview",[('Treeview.treearea', {'sticky': 'nswe'})])
        data = p.read_csv('../Record/try.csv')
        print(data.loc[0][0])
        # add data
        data1 = p.read_csv('../Record/count.csv')
        count = 0
        print(data1.loc[0][0])
        for rg in range(len(data)):
            for gr in range(len(data)):
                print(data.loc[rg][gr], data.loc[rg][gr + 1], data.loc[rg][gr + 2], data.loc[rg][gr + 3],
                      data.loc[rg][gr + 4], data.loc[rg][gr + 5], data.loc[rg][gr + 6], data.loc[rg][gr + 7])
                my_frame.insert(parent='', index='end', iid=count, text='', values=(
                data.loc[rg][gr], data.loc[rg][gr + 1], data.loc[rg][gr + 2], data.loc[rg][gr + 3],
                data.loc[rg][gr + 4], data.loc[rg][gr + 5], data.loc[rg][gr + 6], data.loc[rg][gr + 7]))
                my_frame.insert(parent='',index='end',text='',values=("\n"))
                count = count + 1
                finalco = count
                break
        print(finalco)
        with open('../Record/count.csv', 'w') as fi:
            fi.writelines('Count\n')
            fi.writelines(f'{finalco}')
            fi.close()
        # incoming
        # Frame_out =Frame(Frame_tbl,bg="white",highlightcolor="#EA7676",
        #                             highlightbackground="#EA7676")
        # Frame_out.place(x=705,y=0,width=445,height=500)
        # Frame_title = Frame(Frame_out, bg="#CF2F2F")
        # Frame_title.place(x=0, y=0, width=445, height=500)
        # title = Label(Frame_title, text="Parked Vechiles", font=("Goudy old Style", 20, "bold"), fg="white",
        #               bg="#CF2F2F")
        # title.place(x=150, y=15)
        # Frame_table1 = Frame(Frame_out, bg="white", bd=0)
        # Frame_table1.pack()
        # Frame_table1.place(x=0, y=70, width=445, height=500)
        # frame_sc1 = Scrollbar(Frame_table1)
        # frame_sc1.pack(side=RIGHT, fill=Y)
        # frame_sc = Scrollbar(Frame_table, orient='horizontal')
        # frame_sc.pack(side=BOTTOM, fill=X)
        # my_frame1 = ttk.Treeview(Frame_table1, yscrollcommand=frame_sc1.set)
        # my_frame1.pack()
        # frame_sc1.config(command=my_frame1.yview)
        # # frame_sc1.config(command=my_frame1.xview)
        # my_frame1['columns'] = ('Token_no', 'NumberPlate', 'ParkingNo', 'Incoming')
        #
        # # format our column
        # # my_frame.column("#0", width=0)
        # my_frame1.column("Token_no", anchor=CENTER, width=60)
        # my_frame1.column("NumberPlate", anchor=CENTER, width=120)
        # my_frame1.column("ParkingNo", anchor=CENTER, width=60)
        # my_frame1.column("Incoming", anchor=CENTER, width=120)
        # style = ttk.Style()
        # style.configure("Treeview.Heading", font=("Goudy old Style", 13, "bold"))
        # my_frame1['show'] = 'headings'
        #
        # # Create Headings
        # # my_frame.heading("#0", text="",anchor=CENTER)
        # my_frame1.heading("Token_no", text="N_id", anchor=CENTER)
        # my_frame1.heading("NumberPlate", text="NumberPlate", anchor=CENTER)
        # my_frame1.heading("ParkingNo", text="Pk_no", anchor=CENTER)
        # my_frame1.heading("Incoming", text="IncomingTime", anchor=CENTER)
        # style = ttk.Style()
        # style.configure("Treeview", font=("Goudy old Style", 12), bd=0)
        # style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        # data = p.read_csv('../Record/allincomingrecord.csv')
        # print(data.loc[0][0])
        # # add data
        # data1 = p.read_csv('../Record/count.csv')
        # count = 0
        # print(data1.loc[0][0])
        # for rg in range(len(data)):
        #     for gr in range(len(data)):
        #         print(data.loc[rg][gr], data.loc[rg][gr + 1], data.loc[rg][gr + 2], data.loc[rg][gr + 3])
        #         my_frame1.insert(parent='', index='end', iid=count, text='', values=(
        #             data.loc[rg][gr], data.loc[rg][gr + 1], data.loc[rg][gr + 2], data.loc[rg][gr + 3]))
        #         my_frame1.insert(parent='', index='end', text='', values=("\n"))
        #         count = count + 1
        #         finalco = count
        #         break
        # print(finalco)
        # with open('../Record/count.csv', 'w') as fi:
        #     fi.writelines('Count\n')
        #     fi.writelines(f'{finalco}')
        #     fi.close()

    def close_window(self):
        self.root.destroy()

    def back(self):
        self.root.destroy()
        from MainPage import MainPage
        cs = p.read_csv("../Record/login.csv")
        usr = cs['Username'][0]
        MainPage(Tk(),usr)
#
# m=Tk()
# ShowDetails(m)
# m.mainloop()