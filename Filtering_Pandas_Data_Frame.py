# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 13:30:18 2022

@author: furka
"""

import pandas as pd 

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)
#Data içindeki bilgileri filtrelemek için kullanılır
#filtering'de boolen ifadeler kullanılır
filtre1 = dataFrame1.MAAS > 200 #maası 200 den büyükleri olanları yazar

filtrelenmis_data = dataFrame1[filtre1]
print(filtrelenmis_data) #True değerleri ekrana basmak için kullancaz

#yasi 20 den küçük ve maası 200 den fazla olanlar
filtre2 = dataFrame1.AGE < 20 
dataFrame1[filtre1 & filtre2]

print(dataFrame1[dataFrame1.AGE>60]) #farklı bi filtreleme metodu