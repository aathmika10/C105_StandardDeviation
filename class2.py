import csv
with open('class2.csv',newline='')as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)

newData=[]
for i in range(len(data)):
    number=data[i][1]
    newData.append(float(number))
n=len(newData)
total=0
for x in newData:
    total+=x
mean=total/n
print("mean is "+ str(mean))

import pandas as pd
import plotly_express as px

df=pd.read_csv('class2.csv')
figure =px.scatter(df,x="Student Number", y= "Marks")
figure.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= n
    )
])

figure.show()