# Python program to create a table

from tkinter import *


class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
                #
                if j==4:
                    button=Button(self.e,text="Edit",bg="blue",fg="white",padx=30,pady=3)
                    button.grid(row=i,column=j,sticky="nsew",padx=1,pady=1)
                    self.e.grid_columnconfigure(j,weight=1)
# take the data
lst = [(1, 'Raj', 'Mumbai', 19,''),
       (2, 'Aaryan', 'Pune', 18,''),
       (3, 'Vaishnavi', 'Mumbai', 20,''),
       (4, 'Rachna', 'Mumbai', 21,''),
       (5, 'Shubham', 'Delhi', 21,'')]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
print(total_rows)
print(range(total_columns))
# create root window
root = Tk()
t = Table(root)
root.mainloop()
