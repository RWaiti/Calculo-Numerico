from __future__ import division
import matplotlib.pyplot as plt
import math

def f(x):
    return 10 + (x - 2)**2 - 10 * math.cos(2 * 3.1415926 * x)
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


a = 1
b = 2.2
num = 1000000
erro = 10**-6
graf = []
 
aux = secante(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print("Raiz: ", aux)