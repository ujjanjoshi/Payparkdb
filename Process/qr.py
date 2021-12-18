import pyqrcode
import pandas as p

data= p.read_csv("../Record/try.csv")
length=len(data)-1
print(length)
s=f"Number_id = {data.loc[length]['N_id']}\nNumber Plate = {data.loc[length]['NumberPlate']}\nIncoming Time = {data.loc[length]['IncomingTime']}\nOutgoing Time = {data.loc[length]['OutGoingTime']}\nHours = {data.loc[length]['Hrs']}\nRate = {data.loc[length]['Rate']}\nTotal = {data.loc[length]['Total']}"
url = pyqrcode.create(s)
url.png("Qr.png",scale=6)




