# ___STRING DEĞİŞKENLER__

a = "merhaba"
b = 'merhaba_2'
print(a+' '+b)

c = """ Burada 
    birkaç
     satırlık
    yazılar 
    yazılabilir """
print(c)# 3'lü tırank ile birkaç satırlık yazı yazılıyor

# ______String Aynı Zamanda Bir Harf Dizisidir_____

a = "Hello World"
print(a[1]) #2.harfi ekrana yazdırdı
print(a[4]) #5.harfi ekrana yazdırdı

b = "Farklı bi olay"
print(b[2:7]) #2'den 7'ye kadar olan dizi elemanlarını aldık

c = "Çok farklı bi olay"
print(c[-5:-2]) # Burada karakter uzunluğu toplam 18. 18-5=13.karakter ile 18-2=16.karakter arasını yazdırır

# __STRING İFADENİN UZUNLUĞUNU BULMAK
u = "Ali topu tuttu"
print(len(u))#len = length

#______String Yardımcı Fonksiyonları (Metotları)
a = "   Bu boşlukları temizler   "
a.strip()

b = "HArfleri KüÇültür"
b.lower()

c = "harfleri büyütür"
c.upper()

d = "istediğin harfleri değiştirir"
d.replace("e","a")

e = "Dizeye dönüştürür"
e.split(" ")

#_BİR DEĞERİN OLUP OLMADIĞINI GÖSTERMEK

yazi = "Akdeniz Bölgesinde dağlar denize paraleldir"
x = "paralel" in yazi
print(x)#içinde paralel var//IN//=true 
y = "paralel" not in yazi
print(y)#içinde paralel yok//NOT IN//=false

#_İki string ifadeyi birleştirme
yas = 36
metin = "Benima adım Ali yaşım {}"
print(metin.format(yas))
#_____
adet = 3
urun = 567
fiyat = 49.95
siparis = "Ben {} parça {} numaralı üründen {} TL karşılığında alacağım."
print(siparis.format(adet, urun, fiyat))
## print(metin.format.(içreik_1, içerik_2, içerik3))
adet = 3
urun = 567
fiyat = 49.95
siparis = "Ben {0} parça {1} numaralı üründen {2} TL karşılığında alacağım."
print(siparis.format(adet, urun, fiyat))
#Ya da her parantez içine o değerin index numarasını yazıp da alabiliriz

#____Python ' sorunu
x = 'Ankara\'nın'#2 tane ' olduğu için bunalrı birbirinden ayırmak için "\"kullanırız
print(x)
