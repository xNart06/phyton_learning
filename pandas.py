# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:54:21 2022

@author: furka
"""

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary) #dictionary'yi excel gibi gösterir DataFrame
 
head = dataFrame1.head() #DataFrame içindeki baştan 5 satırı ver demek head()
#dataları dışardan import edeceğiz, içeriğini hızlıca görmek için bunu kullanırız

tail = dataFrame1.tail() #Sondan 5 satırı verir

#parantez içine girilecek sayı adedinde veri görebiliriz
dataFrame2 = pd.DataFrame(dictionary)
head2 = dataFrame2.head(2)