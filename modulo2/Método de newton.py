# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:38:50 2018

@author: filipe
"""

import numpy as np

def d(x,y,n):
    f = np.zeros((n,n));
    f[:,0] = y;
    d = np.zeros(n+1)
    for i in range(1,n):
        for j in range(i,n):        
            f[j][i] = ((f[j][i-1] - f[j-1][i-1])/(x[j] - x[j-1]))
            #f([j][i]) = 
    
    print(f)
       # if(i == 1):
        #    d[i] = f[i]
         #   p = p + d[i]*(x+1)
        #if(i > 1):
         #   p = p + f[i]
        
    #return p


x = np.matrix([-1,0,2])
y = np.matrix([4,1,-1])
n = 3
d(x,y,n)

        
        
      