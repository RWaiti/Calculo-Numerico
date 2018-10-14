<<<<<<< HEAD:modulo1/FalsaPosição.py
from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return math.cos(x) + 1
def bissecao(a, b, erro, num, graf):
    for i in range(num):
        fa = f(a)
        fb = f(b)
        xn = ((a * fb) - (b * fa)) / (b - a)
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


a = 2
b = 4
num = 10000
erro = 2.87**-3
graf = []
 
aux = bissecao(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print ("Raiz: ", aux)
=======
from __future__ import division
import matplotlib.pyplot as plt


def f(x):
    return sin(x)*sin((x**2)/pi)    

def falsaposicao(a, b, erro, num, graf):
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        xn = ((a * fb) - (b * fa)) / (fb - fa)
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
num = 10000
erro = 0.000001
graf = []
 
aux = falsaposicao(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print ("Raiz: ", aux," fi",f(aux))
>>>>>>> 5d833f2a27f851445fcc1876de5a89590d2d65e4:FalsaPosição.py
