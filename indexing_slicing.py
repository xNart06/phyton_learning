# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:25:36 2022

@author: furka
"""

import numpy as np
#-1 son elemanı alır
#TEK BOYUTLU DİZİ İÇİN
array = np.array([1,2,3,4,5,6,7])

print(array[0:3]) #0<=x<3 index arasını print eder

#array i ters yazdırma
reverse_array = array[::-1]
print(reverse_array)

#2 BOYUTLU DİZİ İÇİN
array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array1[1,1])

print(array1[:,1]) #satırların hepsini al, 1 index numaralı sırayı al

print(array1[1,1:4])
print(array1[-1,:])#son satırı alır
print(array1[:,-1])#son sütunu alır