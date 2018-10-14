<<<<<<< HEAD:modulo1/Bisseção.py
from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return (x - 1)*math.e**(x-2)**2 - 1

def bissecao(a, b, erro, num, graf):
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        xn = (a + b)/2
        fxn = f(xn)
        fxnabs = abs(fxn)
        graf.append(xn)
            
        if fxn < 0:
            if fb < 0:
                b = xn
                if fxnabs < erro:
                    return xn
            else:
                a = xn
                if fxnabs < erro:
                    return xn
        else:
            if fb > 0:
                b = xn
                if fxnabs < erro:
                    return xn
            else:
                a = xn
                if fxnabs < erro:
                    return xn
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

fig = plt.figure()
ax = fig.add_subplot(111);
a = 0
b = 3
num = 10000
erro = 10**-6
graf = []
 
aux = bissecao(a, b, erro, num, graf)
               
plt.plot(graf)
ax.set_title("comportamento do método da bissecção")
plt.show
print ("Raiz: ", aux)
=======
from __future__ import division
import matplotlib.pyplot as plt
from math import cos,sin,pi
from numpy import exp


def f(x):
    return sin(x)*sin((x**2)/pi)


def bissecao(a, b, erro, num, graf):
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        if (fa * fb) < erro:
            xn = (a + b)/2
            fxn = f(xn)
            fxnabs = abs(fxn)
            graf.append(xn)
            
            if fxn < 0:
                if fb < 0:
                    b = xn
                    if fxnabs < erro:
                        return xn
                else:
                    a = xn
                    if fxnabs < erro:
                        return xn
            else:
                if fb > 0:
                    b = xn
                    if fxnabs < erro:
                        return xn
                else:
                    a = xn
                    if fxnabs < erro:
                        return xn
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


a = 3
b = 4
num = 100
erro = 0.000001
graf = []
 
aux = bissecao(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print ("Raiz: ", aux, " fi: ",f(aux))
>>>>>>> 5d833f2a27f851445fcc1876de5a89590d2d65e4:Bisseção.py
