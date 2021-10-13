#bu bir python yorum satırıdır
""" 
Python dizi yorumu
""" 
print("Selam")
##
x = 5
y = "naber" 
print(x)
print(y)
##
x,y,z = "elma","armut","muz" 
print(x,y,z)
##
x=y=z= "merhaba"
print(z)
##
x = "harika"
print("lan " + x)
##
x = "python "
y = "başldım"
z = x+y
print(z)
##
x = 5
y = 3
print(x+y)
##
# Eğer bir x değişkenini fonkisyon dışında tanımlarsak o değişken tüm koda etki eder
# fakat fonksiyon içinde değer verirsek sadece o fonksiyon içinde kullanılır

                   # Veri türü
x = "5"
print(type(x)) #type verinin türünü öğrenmek için kullanılır
y = str("selam dünya")
print(y)

## string=str // integer=int // float=float // 
#Metin	str
#Sayı	int, float, complex
#Dize (Seri)	list, tuple, range
#Haritalama	dict
#Atama	set, frozenset
#Mantıksal	bool
#İkili	bytes, bytearray, memoryview 

x = 1#int
y = 1.2#float
z = 3j#complex
t = 34e3
print(type(t))
    ## Sayısal Türleri Birbirine Çevirme ##
x = 1
a = float(x)
print(a)

y = 2.8
b = int(y)
print(b) 
   ## Python ile rastgele sayı oluşturma ##
# Python'da rastgele sayı elde edebilmek için random modülünün uygulamaya dahil edilmesi (import) gereklidir.
import random
print(random.randrange(1,10))
####
