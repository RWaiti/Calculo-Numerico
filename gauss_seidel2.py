# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 01:20:50 2018

@author: filipe
"""

import numpy
m=int(input('Valor de m:'))
n=int(input('Valor de n:'))
matriz = numpy.zeros((m,n))
x=numpy.zeros((m))

vetor = numpy.zeros((n))
comp = numpy.zeros((m))
erro=[]

matriz = numpy.matrix([[1,0,-1,0.2],
                    [-0.5,1,-0.25,-1.425],
                    [1,-0.5,1,2]], dtype = "float")
vetor = numpy.array([0.2,-1.425,2])


#print ('Método de Gauss-Seidel')
#print ('Introduce la matriz de coeficientes y el vector solución')
#for r in range(0,m):
    #for c in range(0,n):
     #   matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
   # vetor[(r)]=float(input('b['+str(r+1)+']: '))
#print ("Método de Gauss-Seidel")

tol = 10**-2
intera = int(300)
k=0
while k<intera:
    suma=0
    k=k+1
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            if (c != r):
                suma=suma+matriz[r,c]*x[c]               
        x[r]=(vetor[r]-suma)/matriz[r,r]
        
    del erro[:]
    for r in range(0,m):
        suma=0
        for c in range(0,n):
            suma=suma+matriz[r,c]*x[c]
        comp[r] = suma
        dif = abs(comp[r]-vetor[r])
        erro.append(dif)
        print(erro[r])
    print(k)
    if all(i>=tol for i in erro) == True:
        break

        


    #Comprobación