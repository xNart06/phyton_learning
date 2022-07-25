# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 00:00:53 2022

@author: furka
"""

import numpy as np

#listeden array e geçmek için array içine liste yazmak yeterli
liste = [1,2,3,4]

array = np.array(liste)

#arrayden listeye geçmek
liste2 = list(array)
print(type(liste))
print(type(array))
print(type(liste2))