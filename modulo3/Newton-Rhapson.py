# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:32:20 2018

@author: filipe
"""


from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x, y, z, p):
    return x + y * p + z * math.pow(p,2)


def df(x):
    return 

def p(x):
   return (1/(0.00428/((1/0.00428)+(1/0.0018)+(1/0.01156))))

def newton(x, erro, num, graf):
    for i in range(num):
        fx = f(x)
        graf.append(x)
        
        if abs(fx) < erro:
            return x
        else:
            x = x - (fx / df(x))        
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

   
p1 = (1/0.00428/((1/0.00428)+(1/0.0018)+(1/0.01156)))
l = 627
m = 9.13
n = 0.00214
pl = f(l,m,n,p1)
print(pl)
print(p1)
num = 10000
erro = 0.000001
graf = []
 
#aux = newton(x, erro, num, graf)
               
#plt.plot(graf)
#plt.show

#print("Raiz: ", aux, " fi: ", f(aux))

        