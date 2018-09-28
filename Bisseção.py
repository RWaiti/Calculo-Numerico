from __future__ import division
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 9*x + 5


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


a = 0.5
b = 1
num = 100
erro = 0.01
graf = []
 
aux = bissecao(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print ("Raiz: ", aux)