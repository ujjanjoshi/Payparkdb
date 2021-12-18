import csv
import pandas as p
import numpy as np
import datetime
from tkinter import *
from removeincoming import removeincming
import qr
from showqr import QrShow
def record():
    cs = p.read_csv("../Record/allflag.csv")
    flag = cs['flag'][0]
    incoming = p.read_csv("../Record/IncomingTime.csv")
    outgoing = p.read_csv("../Record/OutgoingTime.csv")
    data = p.read_csv("../Record/record.csv")
    # print(incoming)
    # print(outgoing)
    # print(data)
    inc = incoming['IncomingTime']
    print(inc)
    out = outgoing['OutgoingTime']
    print(out)
    id = data.loc[0]["N_id"]
    # print(id)
    inc_id = incoming["N_id"]
    out_id = outgoing["N_id"]
    count = 0
    lst = []
    with open('../Record/try.csv', 'r+') as f:
        headerlist = ["N_id", "NumberPlate", "ParkingNumber", "IncomingTime","OutGoingTime","Hrs","Rate","Total"]
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        dw.writeheader()
        with open('../Record/allflag.csv', 'w') as fi:
            fi.writelines('flag\n')
            fi.writelines('1')
            fi.close()
        for i in range(len(data)):
            id = data.loc[i]["N_id"]
            # f.writelines(id)
            for j in inc_id:
                if id == j:
                    # print(id, data.loc[count]["NumberPlate"], data.loc[count]["ParkingNumber"],
                    #       incoming.loc[count]["IncomingTime"])
                    lst.append([id, data.loc[count]["NumberPlate"], data.loc[count]["ParkingNumber"],
                          incoming.loc[count]["IncomingTime"]])
                    # f.writelines(
                    #     f'\n{id},{data.loc[count]["NumberPlate"]},{data.loc[count]["ParkingNumber"]},{incoming.loc[count]["IncomingTime"]}')
                    count = 0
                    break
                count = count + 1
        print(lst)
        lstoutgoing = []
        count1 = 0
        for i in range(len(outgoing)):
            lstoutgoing.append([outgoing.loc[i]["N_id"],outgoing.loc[i]["OutgoingTime"]])
        for a in lst:
            for b in lstoutgoing:
                # print(b)
                if(a[0]==b[0]):
                  for e in range(a[0]):
                      count3=e
                  lst[count3] = [a[0], a[1], a[2], a[3], b[1]]
                  break


        print(lst[2][4])
        for rg in range(len(lst)):
            # print(rg)
            for id in range(len(lst)):
                rate=15
                d0=datetime.datetime.strptime(lst[rg][id + 3],"%H:%M:%S")
                d1=datetime.datetime.strptime(lst[rg][id + 4],"%H:%M:%S")
                diff=(d1-d0)
                print(diff)
                hrs = round(diff.seconds/3600)
                total = hrs*rate
                if hrs==0:
                    total=hrs+rate
                print(round(diff.seconds/3600))
                print(lst[rg][id],lst[rg][id+1],lst[rg][id+2],lst[rg][id+3],lst[rg][id+4])
                f.writelines(f'\n{lst[rg][id]},{lst[rg][id+1]},{lst[rg][id+2]},{lst[rg][id+3]},{lst[rg][id+4]},{hrs},{rate},{total}')
                break
    removeincming()
    qr
    QrShow(Tk())

