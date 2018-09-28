from __future__ import division
import matplotlib.pyplot as plt


def f(x):
    return (x**3) - (9 * x) + 5


def g(x):
    return ((x**3) + 5) / 9


def ponto_fixo(x, error, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        if abs(fxn) < error:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 0.75
error = 1e-2
num = 50
graf = []

aux = ponto_fixo(x, error, num, graf)
plt.plot(graf)
plt.show

print(aux)