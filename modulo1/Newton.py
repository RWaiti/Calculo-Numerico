<<<<<<< HEAD:modulo1/Newton.py
from __future__ import division
import matplotlib.pyplot as plt
import math

def f(x):
    return (x - 1.44)**5

def df(x): 
    return 5*(x-1.44)**4

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


fig = plt.figure()
ax = fig.add_subplot(111);
x = 1
num = 100000
erro = 10**-6
graf = []


 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show
ax.set_title("comportamento do método de newton")
print("Raiz: ", aux)

=======
from __future__ import division
import matplotlib.pyplot as plt
from math import sin, log, pi, cos


def f(x):
    return sin(x)*sin((x**2)/pi)


def df(x):
    return (cos(x)*sin((x**2)/pi)) + (2*cos((x**2)/pi)*sin(x)) / pi


def newton(x, erro, num, graf):
    for i in range(num):
        fx = f(x)
        graf.append(x)
        
        if abs(fx) < erro:
            return x
        else:
            x = x - (fx / df(x))        
    
    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

   
x = 2.5
num = 10000
erro = 0.000001
graf = []
 
aux = newton(x, erro, num, graf)
               
plt.plot(graf)
plt.show

print("Raiz: ", aux, " fi: ", f(aux))
>>>>>>> 5d833f2a27f851445fcc1876de5a89590d2d65e4:Newton.py
        