# Author: Stijn van den Berg
# Date: 11/09/2020


# init
import pandas as pd
import matplotlib.pyplot as plt
# Reading 
x = pd.read_csv('C:\Seminars\CS_Assignment\istherecorrelation.csv',sep=';')
x1 = pd.DataFrame(x,columns=['NL Beer Consumption [x1000 hectoliter]'])
print(x)

plt.rcParams["figure.dpi"] = 300
fig = x.plot(kind='line',x='Year',y='NL Beer consumption [x1000 hectoliter]')
plt.savefig('fig.png')
plt.show()

