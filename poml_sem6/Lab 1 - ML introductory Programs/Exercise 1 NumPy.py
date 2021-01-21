 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

import math as mt


#Array Creation
b= np.array([0,4,6])
b.size
b.dtype.name
type(b)

#2D Array
c=np.array([(1,2,3), (4,5,6)])
c.shape


a1=np.arange(0,10,2)
a1=np.arange(0,10,0.2)
a1

a2=np.linspace(0,10,2)

a=np.arange(15).reshape(3,5)
a.shape
a.ndim
a.dtype.name


a3=np.random.rand(2,3)
a3=a3*10+1
a3

a3=np.floor(a3*10)+1  
a3

import array as ar
a4=ar.array('i');
k=0
for i in a3:
    for j in i:
        a4.insert(k,mt.floor(j*10)+1)
        k=k+1
a5=np.reshape(a4,(2,3))
a5

a3.min()
a3.sum()
a3.sum(axis=1) # Row Sum
a3.sum(axis=0) # Col Sum

a3
a3[:,:] # All Rows and Cols
a3[:,1] # All Rows and 1st Col
a3[0,:] # 0th Row and All Cols
a3[0,0:2] # 0th Row and 0 to 1st col
a3[:,:-1] # Leaving last col
a3[:-1,:] # Leaving last Row



d=np.zeros((2,3))
d=np.ones((2,3))



x=np.linspace(0,10,5)
y= x **2

plt.figure()
plt.plot(x,y,'r') # r red line
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('This be the quadratic function')
plt.show()

