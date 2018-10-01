from __future__ import division
import matplotlib.pyplot as plt
from math import sin, log, pi, cos


def f(x):
    return sin(x)*sin((x**2)/pi)


def df(x):
    return (cos(x)*sin((x**2)/pi)) + (2*cos((x**2)/pi)*sin(x)) / pi


def newton(x, erro, num, graf):
    for i in range(num):
        fx = f(x)
        graf.append(x)
        
        if abs(fx) < erro:
            return x
        else:
            x = x - (fx / df(x))        
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

   
x = 2.5
num = 10000
erro = 0.000001
graf = []
 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show

print("Raiz: ", aux, " fi: ", f(aux))
        