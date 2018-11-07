from __future__ import division


def lagrange(xn, yn, x):
    retorno = 0
    
    for i in range(len(xn)):
        aux2 = 1
        
        for j in range(len(yn)):
            if i != j:
                aux2 = aux2 * ((x - xn[j])/(xn[i] - xn[j]))
                
        aux2 = aux2 * yn[i]
        retorno = retorno + aux2
    
    return retorno


xn = [-1, 0, 2]
yn = [4, 1 , -1]
x = 1

aux = lagrange(xn, yn, x)

print ('resultado: ',aux)