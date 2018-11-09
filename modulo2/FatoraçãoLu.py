# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np
from matplotlib import pyplot

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

def Ly(A, B):
    y = np.zeros(3)
    y[0] = B[0]
    y[1] = B[1] - (y[0] * A[1,0])
    y[2] = B[2] - y[1] - (y[0] * A[2,0])
    return y

def Ux(A, B):
    x = np.zeros(3)
    x[2] = B[2] / A[2,2]
    x[1] = (B[1] - (x[2] * A[1,2])) / A[1,1]
    x[0] = (B[0] - (x[2] * A[0,2]) - (x[1] * A[0,1])) / A[0,0]
    return x

E = np.array([[1,0,-1],
              [-0.5,1,-0.25],
              [1,-0.5,1]], dtype = 'double')
    
F = np.matrix([[1,0,-2],
              [-0.5,1,-0.25],
              [1,-0.5,1]], dtype = 'double')

A = np.array([[3,2,4],
              [1,1,2],
              [4,3,2]], dtype = 'double') 
    
x = np.array([0.2,-1.425,2])

#print(E)
U = fatU(F)
L = fatL(F)
print("Matriz L: \n",L)
print("Matriz U: \n", U)
a = Ly(L, x)
print("\n\ny: ",a)
b = Ux(U, a)
print("\nx: ", b)
erro=[]
graf_erro=[]
fig = pyplot.figure(1)

for i in range(3):
    erro.append(x)
    graf_erro.append(erro[i])
    pyplot.plot(graf_erro)
    
pyplot.plot(graf_erro[0:i])
pyplot.show()
    