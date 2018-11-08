# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:38:50 2018

@author: filipe
"""

import numpy as np

def d(x,y,n):
    f = [0.0] * n
    for i in range(n):
        f[i] = [0.0]*n
    f[:,0] = y;
    d = np.zeros(n)
    for i in range(1,n):
        for j in range(i,n):        
            f[j][i] = ((f[j][i-1] - f[j-1][i-1])/(x[j] - x[j-1]))
            #f([j][i]) = 
    
    print(f)
    p = np.array([f[0,0]], dtype="double")  
    paux = np.array([-x[0],1], dtype="double")  
    p.resize(2)
    for i in range(n):
        p = p + (f[i,i]*paux)  
        paux = np.polymul(paux,[-x[i],i])  
        p.resize(i)
    
    print(p)
    
        
    #return p



x = [-1,0,2]
y = [4,1,-1]
vet1 = map(float,x)
vet2 = map(float,y) 
n = 3
d(vet1,vet2,n)

        
        
      