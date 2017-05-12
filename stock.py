# -*- coding: utf-8 -*-
"""
Created on Tue May  9 01:01:58 2017

@author: Pavlo Lyalyutskyy
"""

import matplotlib.pyplot as plt
from random import randint
import numpy as np

#initialize the array
price = []
time = []

#time of stock over time
t = 0

#create the starting point
price.append(0)
time.append(t)

#pick a random int between 0 and 1
rand = randint(0,1)

#change to the appropriate step
if rand == 0:
    rand = -1
else:
    rand = 1

#drift velocity
def vel(time):
    if time > 20 and time < 100:
        return 0.5
    else: 
        return -0.3
    
    
#potential
def potential(time):
    return 0.01*(50 - price[time-1])

#perform walk
while t<2000:
    rand = randint(0,1)
    if rand == 0:
        rand = -1
    else:
        rand = 1
    t=t+1
    time.append(t)
    price.append(price[t-1]+rand+potential(t))
    
#plot results as well as regression line    
plt.plot(time, price)
linetool = np.polyfit(time, price, 1)
line = np.poly1d(linetool)
plt.plot(line(time))
plt.show()



