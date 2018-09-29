from __future__ import division
import matplotlib.pyplot as plt

def f(x):
    return cos(x) + 1

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


a = 2
b = 4
num = 100
erro = 10**-6
graf = []
 
aux = secante(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print("Raiz: ", aux)