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