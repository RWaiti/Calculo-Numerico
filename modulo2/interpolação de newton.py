# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 01:57:32 2018

@author: filipe
"""

print ("------- Interpolação de Newton -------")
n = int(input("Insira o grau do polinomio: "))+1

f = [0.0] * n
for i in range(n):
    f[i] = [0.0] * n

vet = [0.0] * n

for i in range(n):
    x = float(input("insira o valor de x: "))
    y = float(input("insira o valor de f(x): "))
    vet[i]=x
    f[i][0]=y
#print (vector)    
#2print (matriz)

p = float(input("Insira o ponto a ser calculado: "))


for i in range(1,n):
    for j in range(i,n):
        f[j][i] = ( (f[j][i-1]-f[j-1][i-1]) / (vet[j]-vet[j-i]))
        

print ("------------------------------")
print ("------------------------------")
for i in range(n):
    print (f[i])
print ("------------------------------")
print ("------------------------------")

aprx = 0
mult = 1.0
for i in range(n):
    print ("d",i+1,"=",f[i][i])
    mult = f[i][i];
    for j in range(1,i+1):
        mult *= (p - vet[j-1])
    aprx += mult

print ("------------------------------")
print ("------------------------------")
print ("O valor aproximado de p(",p,") e: ", aprx)