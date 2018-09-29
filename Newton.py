from __future__ import division
import matplotlib.pyplot as plt
import math

def f(x):
    return cos(x) + 1

def df(x): 
    return (-1) * sin(x)

def newton(x, erro, num, graf):
    cont = 0
    
    for i in range(num):
        fx = f(x)
        graf.append(x)
        
        if abs(fx) < erro:
            return x
        else:
            x = x - (fx / df(x))
            
        cont += 1        
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 1
num = 100
erro = 10**-6
graf = []
 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show

print("Raiz: ", aux)
        