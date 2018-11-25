# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:38:11 2018

@author: filipe
"""
import numpy as np

def f(x):
    return np.exp(-x**2)

def fl(x):
    return 2 * np.exp(-x**2)*-x

x = 1.5
h = 1e-2
#progressiva de ordem 1
derivada = fl(x)
print("Derivada de: ",x, " e: ", derivada)
print("\n")
dp1 = (f(x+h) - f(x))/h
erroabs1 = np.abs(fl(x)-dp1)
errorelat1 = np.abs(erroabs1 / dp1)
errotruc = (f(x+h) - f(x)) / h - dp1
print("Diferenças progressivas: ", dp1)
print("Erro absoluto: ", erroabs1)
print("Erro relativo: ", errorelat1)
print("Erro de trucamento: ", errotruc)
print("\n")
#regressiva de ordem 1
dr1 = (f(x) - f(x-h))/h
erroabs2 = np.abs(fl(x)-dr1)
errorelat2 = np.abs(erroabs1 / dr1)
print("Diferenças regressivas: ", dr1)
print("Erro absoluto: ", erroabs2)
print("Erro relativo: ", errorelat2)
print("\n")
#central de ordem 2
dc2 = (f(x+h) - f(x-h))/(2*h)
erroabs3 = np.abs(fl(x)-dc2)
errorelat3 = np.abs(erroabs3 / dc2)
print("Diferenças centrais: ", dc2)
print("Erro absoluto: ", erroabs3)
print("Erro relativo: ", errorelat3)
print("\n")
#progressiva de ordem 2
dp2 = (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)
erroabs4 = np.abs(fl(x)-dp2)
errorelat4 = np.abs(erroabs3 / dp2)
print("Diferenças progressivas usando lagrange:", dp2)
print("Erro absoluto: ", erroabs4)
print("Erro relativo: ", errorelat4)
print("\n")
#regressiva de ordem 2
dr2 = (f(x-2*h) - 4*f(x-h) + 3*f(x)) / (2*h)
erroabs5 = np.abs(fl(x)-dr2)
errorelat5 = np.abs(erroabs3 / dr2)
print("Diferenças regressivas usando lagrange: ", dr2)
print("Erro absoluto: ", erroabs5)
print("Erro relativo: ", errorelat5)
print("\n")
#central de ordem 4
dc4 = (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)
erroabs6 = np.abs(fl(x)-dc4)
errorelat6 = np.abs(erroabs3 / dc4)
print("Diferenças centrais usando lagrange: ", dc4)
print("Erro absoluto: ", erroabs6)
print("Erro relativo: ", errorelat6)
print("\n")
