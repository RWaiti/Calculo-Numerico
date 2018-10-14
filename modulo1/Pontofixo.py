<<<<<<< HEAD:modulo1/Pontofixo.py
from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return (x - 1.44)**5


def g(x):
    return  x - 3 * math.cos(x + 1)

def ponto_fixo(x, error, num, graf):
    for i in range(1,num):
        fxn = f(x)
        graf.append(x)
        
        if abs(x - (x-1)) < error:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 1
error = 10**-6
num = 100000
graf = []

aux = ponto_fixo(x, error, num, graf)

plt.plot(graf)
plt.show

print("Raiz: ",aux)
=======
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
>>>>>>> 5d833f2a27f851445fcc1876de5a89590d2d65e4:Pontofixo.py
