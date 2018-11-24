# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:38:11 2018

@author: filipe
"""
import numpy as np

def f(x):
    return np.exp(-x)

def fl(x):
    return 2*np.cos(2*x) - 2*x

x = 1.5
h = 1e-2
#progressiva de ordem 1
dp1 = (f(x+h) - f(x))/h
erroabs1 = np.abs(fl(x)-dp1)
errorelat1 = np.abs(erroabs1 / dp1)
errotruc = (f(x+h) - f(x)) / h - dp1
print("Diferenças progressivas: ", dp1)
print("Erro absoluto: ", erroabs1)
print("Erro relativo: ", errorelat1)
print("Erro de trucamento: ", errotruc)
#regressiva de ordem 1
dr1 = (f(x) - f(x-h))/h
erroabs2 = np.abs(fl(x)-dr1)
errorelat2 = np.abs(erroabs1 / dr1)
print("Diferenças regressivas: ", dr1)
print("Erro absoluto: ", erroabs2)
print("Erro relativo: ", errorelat2)
#central de ordem 2
dc2 = (f(x+h) - f(x-h))/(2*h)
erroabs3 = np.abs(fl(x)-dc2)
errorelat3 = np.abs(erroabs3 / dc2)
print("Diferenças centrais: ", dc2)
print("Erro absoluto: ", erroabs3)
print("Erro relativo: ", errorelat3)
#progressiva de ordem 2
dp2 = (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)
#print("Progressiva de segunda ordem:", dp2)
#regressiva de ordem 2
dr2 = (f(x-2*h) - 4*f(x-h) + 3*f(x)) / (2*h)
#print("Regressiva de segunda ordem: ", dr2)
#central de ordem 4
dc4 = (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)
#print("Central de quarta ordem: ", dc4)
