# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:10:48 2022

@author: furka
"""

import pandas as pd 

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

#yaşın  katını almak istiyorum
#yeni sütun açacak ve age in 2katını yazacak
dataFrame1["list_comp"] = [ each*2 for each in dataFrame1.AGE]

#apply() ile aynıişlemin yapılışı

def multiply(age):
    return age*2

dataFrame1["apply_metodu"] = dataFrame1.AGE.apply(multiply)