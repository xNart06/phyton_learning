# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:49:17 2022

@author: furka
"""

import numpy as np
#farklı arrayleri birleştirme
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

#verticl dikey birleştirme

array3 = np.vstack((array1,array2))

#horizontal yatay birleştirme

array4 = np.hstack((array1,array2))

print(array3)
print(array4)