# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:33:06 2019

@author: Cristian
"""
import numpy as np

def derivada_gradiente(x,y,teta):
    m,n = x.shape
    h = np.matmul(x,teta)
    for i in range(m):
        cost = (h-y) * x[m,m]
    return cost    
