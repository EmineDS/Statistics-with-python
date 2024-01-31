import numpy as np
from scipy import stats
#Soru1: bir fabrikadan rassal olarak seçilen 100 ürünün ortalama ağırlığı 1040 g dır.
# Standart sapması 25 gr olarak bulunmuşşur.
# Bu fabrikada üretilen tüm ürünlerin 95 güven aralığında ağırlığı kaçtır?
n=100
xort=1040
xstandart=25
guven=0.95
#norm.interval(confidence=guven aralığı, loc=ortalama,scale=standatsapma/kök n )
aralik=stats.norm.interval(confidence=guven, loc=xort,scale=xstandart/np.sqrt(n))#aslında scale kısmına standart hatayı yazıyoruz
print(aralik)
#Soru2:85 ev sahibi ile yapılan bir ankette,
#ev bakımına aylık oalrak 67 dolar (standart sapma=14 dolar) harcadıkları tespit edilmiştir.
# Tüm ev sahiplerinin aylık ev bakım harcamaları için %95 güven aralığı oluşturunuz.
n=85
xort=67
xstandart=14
guven=0.95
aralik=stats.norm.interval(confidence=0.95,loc=xort,scale=xstandart/np.sqrt(n))
print(aralik)
#Soru3:piyasaya yeni sürülen bir ürünün uzunluğunun standart sapması 2 cmdir.
#rastgele seçilen 16 ürünün ort uzunluğu 4 cm olarak hesaplanmıştır.
#%95 güvenle anakütle ortalamasını tahmin ediniz.
# (normalde n sayısının 30 dan küçük olğu için t tablosuna bakılacağı düşünülebilir ancak standart sapması verildiği için buna gerek yoktur örneklem sayısına standart sapma verilmesiği durumda bakılır)
n=16
xort=4
xstandart=2
guven=0.95
aralik=stats.norm.interval(confidence=0.95,loc=4,scale=2/np.sqrt(n))
print(aralik)
#Soru4:Bir fabrikada üretilen margarin paketlerinin ağırlığının varyansı 100 gr dır.
#rastgele seçilen 25 pakedin ağırlığının ortalaması 120 gr dı.
#anakütle ortalamasının 90 ve 99 güvenle tahmin ediniz
n=25
xort=120
xstandart=np.sqrt(100)
onem1=0.9
onem2=0.99
aralik=stats.norm.interval(confidence=onem1,loc=xort,scale=xstandart/np.sqrt(n))
aralik2=stats.norm.interval(confidence=onem2,loc=xort,scale=xstandart/np.sqrt(n))
print(aralik)
print(aralik2)
#Soru5:Bir firmanın ürünlerinin 100 tanesi rassal örneklem olarak seçilmiştir.
#ortalama ağırlık 385 gr ve standart sapması 12 gr olarak hesaplanmıştır.
#üretilen ürünlerin ortalama ağırlığını 95 güven düzeyinde belirleyin.
n=100
xstandart=12
xort=385
guven=0.95
aralik=stats.norm.interval(confidence=guven,loc=xort,scale=xstandart/np.sqrt(n))
print(aralik)