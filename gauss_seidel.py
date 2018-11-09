import numpy as np
import time
from matplotlib import pyplot

inicio= time.time()
m = 3
n = 3
matriz = np.matrix([[1,0,-1,0.2],
                    [-0.5,1,-0.25,-1.425],
                    [1,-0.5,1,2]], dtype = 'double')
x=np.ones((m))

vetor = np.zeros((n))    
comp=np.zeros((m))
erro=[]
graf=([])
fig = pyplot.figure(1)


for r in range(0,m):
    for c in range(0,n):
        matriz[r,c]= 1 /( (r+1) + (c+1) -1)
        


tol=0.001
itera=10000000
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
        graf[0:r]=x[0:r]
        
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
        #graf_erro[0:r]=erro[0:r]
        #pyplot.plot(graf_erro[0:r],k)
    print("iteraçoes:",k)
    if all(i<=tol for i in erro) == True:
        break   
print(graf[0:])        

#pyplot.plot(graf_erro[0:r])
#pyplot.show()
fim= time.time()
print(fim - inicio)
