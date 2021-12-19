import csv
import pandas as p
import cv2
import easyocr as easyocr
import datetime
from record import record
def con():
    img = cv2.imread("../img/outplate.jpg")
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    read = result[0][-2]
    read = ''.join(e for e in read if e.isalnum())
    print(read)
    stat = read[0:]
    print(result[0][-2])
    cs = p.read_csv("../Record/flagOutgoing.csv")
    flag = cs['flag'][0]
    if flag == 0:
        header()
        with open('../Record/flagOutgoing.csv', 'w') as fi:
            fi.writelines('flag\n')
            fi.writelines('1')
            fi.close()
    save(stat)


def header():
    with open('../Record/OutgoingTime.csv', 'r+') as f:
        headerlist = ["N_id", "OutgoingTime"]
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        dw.writeheader()
        f.close()
def save(img):
        cs=p.read_csv("../Record/record.csv")
        numbrplt=cs["NumberPlate"]
        no=cs["N_id"]
        print(cs)
        print(numbrplt)
        count=0
        print(img[0:2])
        id=0
        for r in numbrplt:
            count=count+1
            print(r)
            if(img[0:2]==r[0:2]):
                df=p.read_csv("../Record/record.csv")
                id=df.loc[count-1]["N_id"]
                print(df.loc[count-1]["N_id"])
                with open('../Record/OutgoingTime.csv', 'r+') as f:
                    mydataList = f.readlines()
                    namelist = []
                    print(mydataList)
                    for line in mydataList:
                        entry = line.split(',')
                        namelist.append(entry[0])
                    if id not in namelist:
                        now = datetime.datetime.now()
                        dtString = now.strftime('%H:%M:%S')
                        f.writelines(f'\n{id},{dtString}')
                        print(mydataList)
        # record()

