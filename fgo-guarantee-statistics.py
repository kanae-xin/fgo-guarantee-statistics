# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 14:21:11 2022

@author: kanx
"""
import matplotlib.pyplot as plt
import numpy as np
import random

limit = 220  # 井
pickUp = 0  # up平均概率
count = 0  # 总抽数
num = np.zeros([limit+1])
for i in range(1000000): #模拟100w人抽卡
    for j in range(1,limit+1):
        index = random.random()
        if(index<0.008): #抽到up
            num[j] = num[j] + 1
            break
        if(j==limit and index>=0.008):  #吃井
            num[limit] = num[limit] + 1
    count += j

pickUp =  1000000 / count
median = np.where(num==np.median(num))
print("平均: ",1/pickUp)
print("中位数: ",median[0])
plt.plot(num[1:])
plt.show()