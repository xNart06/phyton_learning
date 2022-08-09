# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:00:13 2022

@author: furka
"""

import pandas as pd 

#iris.csv dosyasını dataframe içine atcaz
df = pd.read_csv("iris.csv")

print(df.columns) #data columns adlarını yazıyor ekrana

print(df.Species.unique()) 
#dataFrame içindeki kaç farklı tür varsa onu yazdırır unique()

print(df.info()) #dataframe içeriği hakkında bilgi veriyor

print(df.describe()) #dataframe içeriği hakkında bilgi veriyor

#dataframe içindeki bir bilgiyi ayrı bi dataframe içine almak
setosa = df[df.Species == "Iris-setosa"] #Iris-setosa nın bilgileri setosa dataframe ine atıldı
versicolor = df[df.Species == "Iris-versicolor"]

#dataları ayırdık ve şimdi elimizde anlammlı veriler oldu, burdan inceleme yapılıyor
print(setosa.describe())
print(versicolor.describe())

#%%
import matplotlib.pyplot as plt
#ıd işme yaramayacak o yüzden drop ediyoruz
df1 = df.drop(["Id"],axis=1) #columns slmek için axis=1 yapmayı unutma

#plt göstermek için kullancaz
# df1.plot()
# plt.show()

setosa = df[df.Species == "Iris-setosa"] 
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label= "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label= "versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label= "virginica")
#x ve y eksenine yazı yazdık
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")

plt.legend() #label değerini yazmak için bunu koda ekliyoruz
plt.show()
#scatter
plt.scatter(setosa.PetalLengthCm, setosa.PetalLengthCm, color="red") #nokta şeklinde gösterim
plt.show()
#histogram
plt.hist(setosa.PetalLengthCm)
plt.show()
#Detayları w3school da mevcut
