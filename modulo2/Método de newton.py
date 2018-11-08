# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:38:50 2018

@author: filipe
"""

import numpy as np

def d(x,y,n):
    f = np.zeros((n,n), dtype = "double");
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
    p = p + f[1,1]*paux  
    paux = np.polymul(paux,[-x[1],1])  
    p.resize(3)  
    p = p + f[2,2]*paux  
    paux = np.polymul(paux,[-x[2],1])  
    p.resize(4)  
    p = p + f[3,3]*paux
    print(p)
        
    #return p



x = [-1,0,2]
y = [4,1,-1]
n = 3
d(x,y,n)

        
        
      