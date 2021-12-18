import csv
import pandas as p
import numpy as np
import datetime
import time
def record():
    cs = p.read_csv("../Record/allincomingflag.csv")
    flag = cs['flag'][0]
    incoming = p.read_csv("../Record/IncomingTime.csv")
    data = p.read_csv("../Record/record.csv")
    inc = incoming['IncomingTime']
    print(inc)
    id = data.loc[0]["N_id"]
    inc_id = incoming["N_id"]
    count = 0
    lst = []
    with open('../Record/allincomingrecord.csv', 'r+') as f:
        headerlist = ["N_id", "NumberPlate", "ParkingNumber", "IncomingTime"]
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        dw.writeheader()
        with open('../Record/allflag.csv', 'w') as fi:
            fi.writelines('flag\n')
            fi.writelines('1')
            fi.close()
        for i in range(len(data)):
            id = data.loc[i]["N_id"]
            for j in inc_id:
                if id == j:
                    lst.append([id, data.loc[count]["NumberPlate"], data.loc[count]["ParkingNumber"],incoming.loc[count]["IncomingTime"]])
                    f.writelines(f'\n{id},{data.loc[count]["NumberPlate"]},{data.loc[count]["ParkingNumber"]},{incoming.loc[count]["IncomingTime"]}')
                    count = 0
                    break
                count = count + 1
        print(lst)
