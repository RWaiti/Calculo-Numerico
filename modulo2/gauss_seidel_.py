# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 12:58:34 2018

@author: filipe
"""

import numpy as np

def beta(A):
    b = np.zeros(3)
    b[0] = (A[0,2] + A[0,3]) / A[0,0]
    b[1] = (b[0]*A[1,0] + A[1,3]) / A[1,1]
    b[2] = (b[0] * A[2,0] + A[2,1] * b[1]) / A[2,2]
    bmaior = abs(b[0])
    for i in range(3):
        if(abs(b[i]) > abs(bmaior)):
            bmaior = b[i]
        
    if(bmaior < 0):
        return 1

    else:
        return 0

def maior(A):
    
    numaior = A[0,0]
    for i in range(3):
        if(abs(A[i:]) > abs(numaior)):
            numaior = A[i:]
    
    return numaior

def x0(A):
    x = np.zeros(3)
    x[0] = A[0,3] / A[0,0]
    x[1] = A[1,3] / A[1,1]
    x[2] = A[2,3] / A[2,2]
    return x


def seidel(A, k):
    x = np.zeros(3)
    x[0] = (1/A[0,0]) * (A[0,3] - A[0,1] * k[1] - A[0,2] * k[2])
    x[1] = (1/A[1,1]) * (A[1,3] - A[1,0] * x[0] - A[1,2] * k[2])
    x[2] = (1/A[2,2]) * (A[2,3] - A[2,0] * x[0] - A[2,1] * x[1])


sist = np.array([[10,2,1,7],
                 [1,5,1,-8],
                 [2,3,10,6]], dtype = 'double')

precisao = 5e-2
verif = beta(sist)
k = np.zeros(3)
x = np.zeros(3)
interac = 300
k = x0(sist)

if(verif == 1):
    for i in range(interac):
        x = seidel(sist, k)
        kmaior = maior(k)
        xmaior = maior(x)
        k = x
        dr = abs(xmaior - kmaior) / abs(xmaior)
        if(dr < precisao):
            i == interac
            break

print(dr)



    