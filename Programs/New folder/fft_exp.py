#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:28:22 2020

@author: k
ripa
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,21)
y=np.sin(5*x)
freq=21*np.fft.fftfreq(21)
yk=np.fft.fft(y)
plt.plot(freq,np.abs(yk),'-o')