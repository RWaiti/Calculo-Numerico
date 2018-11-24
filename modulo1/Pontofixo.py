
from __future__ import division
import matplotlib.pyplot as plt
from math import cos, pi, pow, sin, sqrt
from numpy import exp


def f(x):
    return sin(x) + x**2 - 4.90929828


def g(x):
    return sqrt(4.90929828 - sin(x))


def ponto_fixo(x, erro, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        
        if abs(fxn) < erro:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = -1
erro = 0.000001
num = 5000
graf = []

aux = ponto_fixo(x, erro, num, graf)

plt.plot(graf)
plt.show

print("Raiz: ",aux," fi",f(aux))
