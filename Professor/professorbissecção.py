import numpy as np
import matplotlib.pyplot as plt

a=0.1
b=3
num_iter = 100
erro = 1e-6
#definir uma função de teste
def f(x):
    return x**7-113

#função dropwave
def f_1(x):
    return -(1-np.cos(12*np.sqrt(x**2)))/(0.5*np.sqrt(x**2)+2)
#Iniciar os valores dentro da função bissecção
a0 = a
b0 = b
x = 1e5*np.ones((1,num_iter))
graf = np.ones_like(x)
#atualização do ponto x
for i in range(num_iter):
    
    if (b0-a0)<erro:
        break
    else:
        x[0,i] = (a0+b0)/2
        f0 = f(a)
        f1 = f(b)
        fmed = f(x[0,i])
        
        if np.sign(f1)*np.sign(fmed)<0:
            a0 = x[0,i]
            if (b0-a0)<erro:
                break
        if np.sign(f0)*np.sign(fmed)<0:
            b0 = x[0,i]
            if (b0-a0)<erro:
                break
    print(a0,b0)
    graf[0,i] = f(x[0,i])

#fazer o gráfico dos x
fig=plt.figure(1)
plt.plot(x[0,0:i])
plt.show()
