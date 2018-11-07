# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:09:29 2018

@author: Dhiego L. de Araújo

Implementação do Polinômio interpolador de Lagrange
"""

import numpy
from matplotlib import pyplot

x = [2, 2.75, 4, 5, 7, 19]
y = [1/2, 4/11, 1/4, 1/5, 1/7, 1/19]

n = len(x)


# determinar o coeficiente de Lagrange
def L(num, xi, x):
    prod = 1
    for xj in x:
        if xi != xj:
            prod *= (num-xj)/(xi-xj)
    return prod


# interpolar no ponto x = 3
zeta = 3
L_n = [L(zeta, xi, x) for xi in x]

Lagrange = sum(yi*j for yi, j in zip(y, L_n))

# função para determinar o valor do polinômio de Lagrange
def P(z, x, y):
    return sum(yi*L(z, xi, x) for xi, yi in zip(x, y))

teste = P(3, x, y)

t = numpy.linspace(0.1, 5.1, num=50)
y_p = P(t, x, y)

fig = pyplot.figure(1)

pyplot.plot(t, 1/t, 'ro')
pyplot.plot(t, y_p, 'b-')

pyplot.show()
