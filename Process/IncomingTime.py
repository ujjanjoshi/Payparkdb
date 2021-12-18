import csv
import pandas as p
import datetime
from totalincoming import record
def incomingheader():
    with open('../Record/IncomingTime.csv', 'r+') as f:
        headerlist = ["N_id", "IncomingTime"]
        cs = p.read_csv("../Record/flagIncoming.csv")
        flag = cs['flag'][0]
        if flag == 0:
            dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
            dw.writeheader()
            with open('../Record/flagIncoming.csv', 'w') as fi:
                fi.writelines('flag\n')
                fi.writelines('1')
                fi.close()


def incomingTime(N_id):
        with open('../Record/IncomingTime.csv', 'r+') as f:
            mydataList = f.readlines()
            namelist = []
            print(mydataList)
            for line in mydataList:
                entry = line.split(',')
                namelist.append(entry[0])
            if N_id not in namelist:
                now = datetime.datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{N_id},{dtString}')
                print(mydataList)
        record()