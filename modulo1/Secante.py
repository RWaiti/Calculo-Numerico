<<<<<<< HEAD:modulo1/Secante.py
from __future__ import division
import matplotlib.pyplot as plt
import math

def f(x):
    return (x - 1.44)**5

def secante(a, b, erro, num, graf):    
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        xn = b - ((fb * (b - a)) / (fb - fa))
        
        graf.append(xn)
        
        if abs(f(xn)) < erro:
            return xn
        else:
            a = b
            b = xn
            

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")

#fig = plt.figure()
# = fig.add_subplot(111);
a = 1
b = 2
num = 1000000
erro = 10**-6
graf = []

aux = secante(a, b, erro, num, graf)
               
plt.plot(graf)
#ax.set_title("comportamento do método da secante")
plt.show
print("Raiz: ", aux)
=======
from __future__ import division
import matplotlib.pyplot as plt
from math import cos

def f(x):
    return sin(x)*sin((x**2)/pi)
    
    
def secante(a, b, erro, num, graf):    
    for i in range(num):
        fa = f(a)
        fb = f(b)
        
        xn = b - ((fb * (b - a)) / (fb - fa))
        
        graf.append(xn)
        
        if abs(f(xn)) < erro:
            return xn
        else:
            a = b
            b = xn

    print("NÚMERO MÁXIMO DE ITERAÇÕES!")


a = 3
b = 3.2
num = 100
erro = 0.000001
graf = []
 
aux = secante(a, b, erro, num, graf)
               
plt.plot(graf)
plt.show
print("Raiz: ", aux, " fi: ", f(aux))
>>>>>>> 5d833f2a27f851445fcc1876de5a89590d2d65e4:Secante.py
