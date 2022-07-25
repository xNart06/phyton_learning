# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:37:12 2022

@author: furka
"""

#numpy basic operations

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**b)
#numpy ile olanlar
print(np.sin(a))
print(a<2)
print("")
#element wise prodcut (karşılıklı çarpım)
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6]])
print(x*y)
print("")
#0 ile 1 arası random sayılar
a = np.random.random((5,5))
print(a)
print("")
print("toplam", a.sum())
print("en büyük sayı", a.max())
print("en küçük sayı", a.min())
#sütun toplama
print("sütun toplama",a.sum(axis=0))
print("satır toplama",a.sum(axis=0))
print("")
print("karekökü ",np.sqrt(a)) 
print("karesi ",np.square(a))
#dikkat a+a ile np.add(a,a) aynı şeydir