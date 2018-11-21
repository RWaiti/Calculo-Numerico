# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:38:11 2018

@author: filipe
"""
import numpy as np

def f(x):
    return ((5*x**2 + 3*x -9)/(x**2 + 5))

x = 5
h = 0.01
#progressiva de ordem 1
dp1 = (f(x+h) - f(x))/h
print("Progressiva de primeira ordem: ", dp1)
#regressiva de ordem 1
dr1 = (f(x) - f(x-h))/h
print("Regressiva de primeira ordem: ", dr1)
#central de ordem 2
dc2 = (f(x+h) - f(x-h))/(2*h)
print("Central de segunda ordem: ", dc2)
#progressiva de ordem 2
dp2 = (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)
print("Progressiva de segunda ordem:", dp2)
#regressiva de ordem 2
dr2 = (f(x-2*h) - 4*f(x-h) + 3*f(x)) / (2*h)
print("Regressiva de segunda ordem: ", dr2)
#central de ordem 4
dc4 = (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)
print("Central de quarta ordem: ", dc4)
