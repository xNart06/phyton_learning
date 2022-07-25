# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:24:29 2022

@author: furka
"""

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
#ayrı olan bu diziyi birleştirip bir bütün yapcaz
#bu çok fazla kullanılacak

a = array.ravel() #düz hale gelmiş array
print(a)
array2 = a.reshape(3,3) #eski haline çevirme
print(array2)

#transpozunu alma yani 1 4 7  2 5 8  3 6 9 olarak yazdırma
arrayT = array2.T
print(arrayT)
print(arrayT.shape)

array5 = np.array([[1,2],[3,4],[5,6]])
array5.resize((2,3))
print(array5)
#reshape de yapılan işlemi başka bir değişkene eşitlemek gerekir
#resize ise direk değişken üstünden arrayi değiştirir