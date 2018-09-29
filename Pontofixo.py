from __future__ import division
import matplotlib.pyplot as plt


def f(x):
    return cos(x) + 1


def g(x):
    return  x - 3 * x * cos(x)

def ponto_fixo(x, error, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        
        if abs(fxn) < error:
            return x
        else:
            x = g(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 1
error = 10**-6
num = 1000000
graf = []

aux = ponto_fixo(x, error, num, graf)

plt.plot(graf)
plt.show

print("Raiz: ",aux)