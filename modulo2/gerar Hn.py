# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:36:56 2018

@author: rafae
"""
from __future__ import division
import numpy as np

def gerMatriz(matriz, n):
    for i in range(n):
        for j in range(n):
                matriz[i][j] = 1 / (i + j - 1 + 2)

n = 2 #Valor do Hn
matriz = np.zeros(shape=(n,n))

gerMatriz(matriz, n)

print(matriz)