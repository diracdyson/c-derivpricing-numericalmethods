


from matplotlib.cbook import print_cycles
import numpy as np 
import os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io
import pandas as pd

from google.colab import files
uploaded = files.upload()

df1 = pd.read_csv(io.BytesIO(uploaded['credits.csv']))
df2 = pd.read_csv(io.BytesIO(uploaded['4-14.csv']))
df3 = pd.read_csv(io.BytesIO(uploaded['4-20.csv']))
df4 = pd.read_csv(io.BytesIO(uploaded['4-29.csv']))
df5 = pd.read_csv(io.BytesIO(uploaded['5-06.csv']))
#
maturities=[0,1/48,2/48,3/48,4/48]
filenames=[df1,df2,df3,df4,df5]
prices=[]
deltakk=1
deltat =1
f=[]
for i in range(10,20):
    f.append(i%5)
print(f)
maturities=[0,1/48,2/48,3/48]
for e, f in enumerate(filenames):
    frame=(f)
    strikes=frame.Strike.iloc[0:20]
    prices.append(frame.Midpoint.iloc[0:20])
for i in range(1,99):
    partialkk=prices[i-1]+2*prices[i]-prices[i+1]/deltat
    partialk=prices[i+1]-prices[i-1]
    particular=prices[i+1]+prices[i:20]/deltakk
    
prices=np.array(prices)
prices=np.reshape(prices,(-1,1))
strikes=np.array(strikes)
print(len(prices))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
T, X= np.meshgrid(maturities,strikes)
ax.plot_surface(T,X,prices,cmap='YlGnBu_r')
