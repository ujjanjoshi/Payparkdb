import pandas as p
import csv
def removeincming():
        inp = p.read_csv("../Record/allincomingrecord.csv")
        output = p.read_csv("../Record/try.csv")
        lst = []
        b = (inp[~inp['N_id'].isin(output['N_id'])])
        print(b.values)
        for i in range(len(b)):
            lst.append(b.values[i])
            print(lst[i])

        file = open('../Record/allincomingrecord.csv', 'w+', newline='')

        # writing the data into the file
        with file:
            header = ['N_id','NumberPlate','ParkingNumber','IncomingTime']
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            write = csv.writer(file)
            write.writerows(lst)
removeincming()