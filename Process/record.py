import csv
import pandas as p
import numpy as np
import datetime
from tkinter import *
from removeincoming import removeincming
import qr
from showqr import QrShow
def record():
    inc = p.read_csv("../Record/IncomingTime.csv")
    out = p.read_csv("../Record/OutgoingTime.csv")
    rc = p.read_csv("../Record/record.csv")
    with open('../Record/try.csv', 'r+') as f:
        headerlist = ["N_id", "NumberPlate", "ParkingNumber", "IncomingTime", "OutGoingTime", "Hrs", "Rate",
                      "Total"]
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        dw.writeheader()
        with open('../Record/allflag.csv', 'w') as fi:
            fi.writelines('flag\n')
            fi.writelines('1')
            fi.close()
        for i in range(len(rc)):
            for j in range(len(inc)):
                if rc.loc[i]["N_id"] == inc.loc[j]['N_id']:
                    # # print(rc.loc[i]["N_id"])
                    # print(i,j)
                    for k in range(len(out)):
                        if inc.loc[j]["N_id"] == out.loc[k]["N_id"]:
                            rate = 15
                            d0 = datetime.datetime.strptime(inc.loc[j]["IncomingTime"], "%H:%M:%S")
                            d1 = datetime.datetime.strptime(out.loc[k]["OutgoingTime"], "%H:%M:%S")
                            diff = (d1 - d0)
                            print(diff)
                            hrs = round(diff.seconds / 3600)
                            total = hrs * rate
                            if hrs == 0:
                                total = hrs + rate
                            print(out.loc[k]["N_id"], rc.loc[i]["NumberPlate"], rc.loc[i]["ParkingNumber"],
                                  inc.loc[j]["IncomingTime"], out.loc[k]["OutgoingTime"], hrs, rate, total)
                            f.writelines(
                                f'\n{out.loc[k]["N_id"]},{rc.loc[i]["NumberPlate"]},{rc.loc[i]["ParkingNumber"]},{inc.loc[j]["IncomingTime"]},{out.loc[k]["OutgoingTime"]},{hrs},{rate},{total}')
    removeincming()
    qr
    QrShow(Tk())

