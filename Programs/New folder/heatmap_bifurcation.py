#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:03:30 2020

@author: kripa
"""
import rigidSimBifurcation
import numpy as np
import matplotlib.pyplot as plt

mat=np.zeros([20,50])

for i in range(20):
    g=(i+1)*0.03
    a,c,p,d=rigidSimBifurcation.f(1.15,g,1500)
    x,y=np.histogram(d,bins=0,range=(0,14),density=True)
    mat[i,:]=x
    
plt.imshow(mat.T)