from __future__ import division
import matplotlib.pyplot as plt
import math

def f(x):
    return 10 + (x - 2)**2 - 10 * math.cos(2 * 3.1415926 * x)
def df(x): 
    return 2 * 3.1415926 * x + 20 * (3.1415926)**2 * math.sin(2 * 3.1415926 * x) - 4 * 3.1415926

def newton(x, erro, num, graf):
    cont = 0
    
    for i in range(num):
        fx = f(x)
        graf.append(x)
        
        if abs(fx) < erro:
            return x
        else:
            x = x - (fx / df(x))
            
        cont += 1        
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


x = 1.3
num = 100000
erro = 10**-6
graf = []
 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show

print("Raiz: ", aux)
        