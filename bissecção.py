# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:49:28 2018

@author: filip
"""
import numpy as np
import matplotlib.pyplot as plt

a = 0.1
b = 2
interacoes = 100
precisao = 1e-6

def f(x):

    return x**5 + 22* x**3 - 8 * x**2 - 18 * x


a0 = a
b0 = b

x = 1e5*np.ones((1,interacoes))
graf = np.ones_like(x)

for i in range(interacoes):
    if(b0 - a0) < precisao:
        break
    else:
        x[0,i] = (a0 + b0)/2
        f0 = f(a)
        f1 = f(b)
        fmedio = f(x[0,i])

        if np.sign(f1)*np.sign(fmedio) < 0:
            a0 = x[0,i]
            if(b0 - a0) < precisao:
                break
            
        if np.sign(f0)*np.sign(fmedio) < 0:
            if(b0 - a0) < precisao:
                break
        print(a0,b0)
        graf[0,i] = f(x[0,i])

        fig = plt.figure(1)
        plt.plot(x[0,0:i])
        plt.show()

