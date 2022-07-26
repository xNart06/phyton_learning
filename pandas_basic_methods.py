# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:17:46 2022

@author: furka
"""

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1.columns) #Name Age Maas gibi başlangıç objelerinin ismini verir

print(dataFrame1.info()) #dataFrame içeriği hakkında bilgi verir

print(dataFrame1.dtypes) #her column elemanının data tipini gösterir

print(dataFrame1.describe()) #numeric feature gösterir column için/ özet raporu
#count : içeriğindeki eleman sayıs
#mean : içerikteki verilerin ortalaması
#min : içeriğindeki en küçük değer
#max : içeriğindeki en büyük değer
#std : içeriğindeki standart sapma değeri
#%'ler : içeriğindeki taoplam kayıtların %x'inin ortalama değeri