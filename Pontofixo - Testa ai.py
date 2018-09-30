from __future__ import division
import matplotlib.pyplot as plt


def f(x):
    return (x**3) - 3*(x**2)*(2**(-x)) + (3*x*4**(-x)) - (8**(-x))


def g(x):
    return ((-x**3) + (3*(x**2))*(2**(-x)) + (8**(-x))) / (3 * (4**(-x))) 


def ponto_fixo(x, erro, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        
        if abs(fxn) < erro:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 0.5
erro = 0.000001
num = 5000
graf = []

aux = ponto_fixo(x, erro, num, graf)

plt.plot(graf)
plt.show

print("Raiz: ",aux)