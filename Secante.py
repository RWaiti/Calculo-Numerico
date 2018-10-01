from __future__ import division
import matplotlib.pyplot as plt
from math import cos

def f(x):
    return sin(x)*sin((x**2)/pi)
    
    
def secante(a, b, erro, num, graf):    
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        xn = b - ((fb * (b - a)) / (fb - fa))
        
        graf.append(xn)
        
        if abs(f(xn)) < erro:
            return xn
        else:
            a = b
            b = xn

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


a = 3
b = 3.2
num = 100
erro = 0.000001
graf = []
 
aux = secante(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print("Raiz: ", aux, " fi: ", f(aux))