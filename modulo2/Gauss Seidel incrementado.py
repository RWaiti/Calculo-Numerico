import numpy as np
import time
from matplotlib import pyplot

inicio= time.time()

def gerMatriz(matriz, n):
    for i in range(n):
        for j in range(n):
                matriz[i][j] = 1 / (i + j - 1 + 2)

m = n = 3 #Valor do Hn
matriz = np.zeros(shape=(n,n))
matriz = np.matrix([[1,0,-1,],
                    [-0.5,1,-0.25],
                    [1,-0.5,1]], dtype = 'double')

#gerMatriz(matriz, n)

print(matriz)

x=np.ones((m))

vetor = np.zeros((n))
vetor = np.array([0.2,-1.425,2])    
comp=np.zeros((m))
erro=[]
graf_erro=[]
fig = pyplot.figure(1)


for r in range(0,m):
    for c in range(0,n):
        matriz[r,c]= 1 /( (r+1) + (c+1) -1)
        


tol=0.001
itera=300
k=0

while k< itera :
    soma=0
    k=k+1
    for r in range(0,m):
        soma=0
        for c in range(0,n):
            if (c != r):
                soma=soma+matriz[r,c]*x[c]               
        x[r]=(vetor[r]-soma)/matriz[r,r]
        
        print("x["+str(r)+"]: "+str(x[r ]))
    
    del erro[:]    

    #Comprovação
    
    for r in range(0,m):
        soma=0
        for c in range(0,n):
             soma=soma+matriz[r,c]*x[c]
        comp[r]=soma
        dif=abs(comp[r]-vetor[r]) 
        erro.append(dif)
        print("erro em x[",r,"]=",erro[r])
        #graf_erro[0:r]= list.append(erro([r]))
        graf_erro.append(erro[r])
        pyplot.plot(graf_erro)
    print("iteraçoes:",k)
    if all(i<=tol for i in erro) == True:
        break         

pyplot.plot(graf_erro[0:r])
pyplot.show()
fim= time.time()
print(fim - inicio)