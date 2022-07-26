# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 12:16:16 2022

@author: furka
"""

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1["NAME"]) #name in alt öğelerini verir
print(dataFrame1["AGE"])

#pandas kullanarak alma
print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6] #dataframe e yeni feautrue column ekledik

print(dataFrame1.loc[:,"AGE"]) #Tüm satırları ve istediğmiz sütunu aldık
print(dataFrame1.loc[:3,"AGE"]) #numpy aksine buradaki :3 değerinde 3 dahil

print(dataFrame1.loc[:3,"NAME":"MAAS"]) #3.satıra kadar ve name'den maas'e kadar olanları yazdır
print(dataFrame1.loc[:3,["NAME","MAAS"]]) #name ve maas yazdır
print(dataFrame1.loc[::-1,:]) #tersten hepsini yazdır 
print(dataFrame1.iloc[:,2]) #iloc index numarasına göre yazdırır burda MAAS ekrana yazar
#numpy ile olan ile aynı