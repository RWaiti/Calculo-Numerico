from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return (x - 1.44)**5


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


a = 1
b = 1.5
num = 10000
erro = 10**-6
graf = []
 
aux = bissecao(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print ("Raiz: ", aux)