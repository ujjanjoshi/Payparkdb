import pandas as p

datainc=p.read_csv("../Record/copy.csv")
dataout=p.read_csv("../Record/try.csv")
# print(datainc)
# print(dataout)
lst=[]
for i in range(len(datainc)):
    for j in range(len(dataout)):
        if(datainc.loc[i]["NumberPlate"]==dataout.loc[j]["NumberPlate"]):
            lst.append(datainc.loc[i]["N_id"]-1)

print(lst)
updated=datainc.drop(lst)
print(updated)

