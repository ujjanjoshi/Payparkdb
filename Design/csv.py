import csv
import numpy as np

import pandas as pd

inp=pd.read_csv("1.csv")
output=pd.read_csv("two.csv")
lst=[]
b=(inp[~inp['Number'].isin(output['Number'])])
print(b.values)
for i in range(len(b)):
    lst.append(b.values[i])
    print(lst[i])

file = open('1.csv', 'w+', newline='')

# writing the data into the file
with file:
    header = ['Number']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    write = csv.writer(file)
    write.writerows(lst)
