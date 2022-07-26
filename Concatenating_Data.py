# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 18:56:04 2022

@author: furka
"""

import pandas as pd 

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

dataFrame1.drop(["NAME"],axis=1,inplace=True) #tamamen yok etmek için inplace = True kullanıyoruz
# axis=0 satır drop etme axis=1 sütun drop eder

#2 data birleştirme
data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
data_concat = pd.concat([data1,data2],axis=0)

#horizontal
maas = dataFrame1.MAAS
age = dataFrame1.AGE
data_h_concat = pd.concat([maas,age],axis=1)

#drop ve concat gördük