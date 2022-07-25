# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:45:25 2022

@author: furka
"""
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array.shape)

#kaça kaçlık bir matris olduğunu yazdı x.shape
a = array.reshape(3,5)

#reshape ise matrise bölme
print(a)
print("matris boyutu - shape: ",a.shape)

#array içindeki değerlerin data type ını görme
print("data type:", a.dtype.name)
print("size: ",a.size)
print("type:", type(a))

#reshape kullanmadan numpy ile 2 veya 3 boyutlu matris yapma
array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print("matris boyutu",array1.shape)
print(" ")

#sıfırlardan oluşan matris zeros/bellekte yer ayırmak için kullanılır
#daha sonrasında bu alana değer atanabilir
        #print("ZEROS():",np.zeros((5,3)))
zeros = np.zeros((5,3))
zeros[0,0] = 5
print("zeros();",zeros)

#ones tıpkı zeros gibi yer açar fakat 0 yerine 1 kullanılır
print(" ")
ones = np.ones((2,3))
print("ones();",ones)

#1 veya 0 yerine rastgele değerlerde yer açması için empty()
#bu konsola yazınca düzgün çalıştı
print(" ")
empty = np.empty((3,2))
print(empty)

#ilk değerden son değere kadar girilen artış miktarına göre yazdırma
print(" ")
arange = np.arange(10,40,3)
print("arange(): ",arange)

#linspace() arange gibi fakat araya son girilen değer adedinde sayı yazar
print(" ")
linspace = np.linspace(10,13,9)
print("linspace(); ",linspace)
