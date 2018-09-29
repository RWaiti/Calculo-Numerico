from __future__ import division
import matplotlib.pyplot as plt

def f(x):
    return (x**3) - (9*x) + 5

def df(x):
    return (3*(x**2)) - 9

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


x = 0.75
num = 100
erro = 0.01
graf = []
 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show

print("Raiz: ", aux)
        