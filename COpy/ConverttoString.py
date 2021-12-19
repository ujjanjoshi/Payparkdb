import csv
import pandas as p
import cv2
import easyocr as easyocr
from IncomingTime import incomingTime
from IncomingTime import incomingheader

def con():
    img = cv2.imread("../img/plate.jpg")
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    read=result[0][-2]
    read = ''.join(e for e in read if e.isalnum())
    print(read)
    stat = read[0:]
    cs = p.read_csv("../Record/flag.csv")
    flag = cs['flag'][0]

    if flag == 0:
        header()
        with open('../Record/flag.csv', 'w') as fi:
            fi.writelines('flag\n')
            fi.writelines('1')
            fi.close()
    save(stat)


def header():
    with open('../Record/record.csv', 'r+') as f:
        headerlist = ["N_id", "NumberPlate","ParkingNumber"]
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerlist)
        dw.writeheader()
        f.close()


def save(img):
        with open('../Record/record.csv', 'r+') as f:
            id = p.read_csv("../Record/record.csv")
            count = len(id)
            count=count+1
            print(count)
            mydataList = f.readlines()
            namelist = []
            print(mydataList)
            for line in mydataList:

                entry = line.split(',')
                namelist.append(entry[0])
            if img not in namelist:

                f.writelines(f'\n{count},{img},P{count}')
                print(mydataList)
            incomingheader()
            incomingTime(count)

