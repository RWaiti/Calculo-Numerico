# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:11:55 2018

@author: filip
"""

import numpy as np



E = np.array([[3,2,4,1],
              [1,1,2,2],
              [4,3,-2,3]], dtype = 'double')

print(E)
print("\n")

aux = np.copy(E[1,:])
E[1,:] = np.copy(E[0,:])
E[0,:] = np.copy(aux)
print(E)
print("\n")

E[1,:] = E[1,:] - (E[1,0] / E[0,0] * E[0,:])
E[2,:] = E[2,:] - (E[2,0] / E[0,0] * E[0,:])
print(E)
print("\n")

E[2,:] = E[2,:] - (E[2,1] / E[1,1]) * E[1,:]
print(E)
print("\n")

x = np.zeros(3)
x[2] = E[2,3] / E[2,2];
x[1] = (E[1,3] - E[1,2] * x[2]) / E[1,1];
x[0] = (E[0,3] - E[0,2] * x[2] - E[0,1] * x[1]) / E[0,0];
print(x)
print("\n")