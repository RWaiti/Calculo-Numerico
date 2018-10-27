# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np


def fatL(a):
    u = np.copy(a)
    n = np.shape(u)[0]
    l = np.eye(n)
    for j in range(n-1):
        for i in range(j+1,n):
            l[i,j] = u[i,j]/u[j,j]
            for k in range(j+1,n):
                u[i,k] = u[i,k] - l[i,j]*u[j,k]
            u[i,j] = 0
    return l
def fatU(a):
    u = np.copy(a)
    n = np.shape(u)[0]
    l = np.eye(n)
    for j in range(n-1):
        for i in range(j+1,n):
            l[i,j] = u[i,j]/u[j,j]
            for k in range(j+1,n):
                u[i,k] = u[i,k] - l[i,j]*u[j,k]
            u[i,j] = 0
    return u

E = np.array([[1,0,-1,0.2],
              [-0.5,1,-0.25,-1.425],
              [1,-1.5,1,2]], dtype = 'double')

    
print(E)
U = fatU(E)
L = fatL(E)
print("Matriz L: \n",L)
print("Matriz U: \n", U) 
    