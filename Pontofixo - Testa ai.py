from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return (x - 1.44)**5


def g(x):
    return math.sqrt(1.44**5 / x**3)


def ponto_fixo(x, erro, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        
        if abs(fxn) < erro:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 1.3
erro = 10**-6
num = 5000
graf = []

aux = ponto_fixo(x, erro, num, graf)

plt.plot(graf)
plt.show

print("Raiz: ",aux)