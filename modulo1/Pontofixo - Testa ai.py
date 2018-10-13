from __future__ import division
import matplotlib.pyplot as plt
import math


def f(x):
    return x**3 - 3* x**2 * (2**-x) + 3 * x * (4**-x) - 8**-x


def g(x):
    return (1 / math.e**(x-2)**2) + 1

def h(x):
    return math.sqrt(8.003 / x)

def fi(x):
    return 1 + (math.e**(x**2 - 4*x * 4) / math.e**(x**2 - 4*x * 4))

def ponto_fixo(x, erro, num, graf):
    for i in range(num):
        fxn = f(x)
        graf.append(x)
        
        if abs(fxn) < erro:
            return x
        else:
            x = fi(x)

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

fig = plt.figure()
ax = fig.add_subplot(111);
x = 1
erro = 10**-6
num = 5000
graf = []

aux = ponto_fixo(x, erro, num, graf)

plt.plot(graf)
ax.set_title("comportamento do método da ponto fixo")
plt.show

print("Raiz: ",aux)