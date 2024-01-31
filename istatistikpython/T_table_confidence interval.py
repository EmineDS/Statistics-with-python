import numpy as np
from scipy import stats
#örneklem sayısı 30dan küçük ve ya 30 a eşitse
# aynı zamanda standart sapma verilmemişse normla dağılım değil t dağılım kullanılarak interval bulunur.
#t dağılımda farklı olarsak orneklem sayısı-1 dediğimiz serbestlik derecesi(df) vardır.
#popülasyon standart sapması olmadığından örneklem standart sapması kullanılır.
n=30
xort=140
xsapma=25
guven=0.95
sderecesi=n-1
#stats.t.interval(confidence=guven aralığı,loc=orneklem ortalaması,df=serbestlik derecesi,scale=orneklem standart sapma/kök orneklem sayısı)
aralik=stats.t.interval(confidence=guven,loc=xort,df=sderecesi,scale=xsapma/np.sqrt(n))
print(aralik)
#Soru:Rassal olarak seçilen 20 bilgisayarın tamir maliyetleri kaydedilmiştir.
#seçilen 20 örneklemin maliyet ort 216.53 dolar olarak hesaplanmıştır.
#bu örneklemin standart sapması 15.86 dolardır.
#tüm bilgisayarların ortalama maliyet oranlarını 95 güven aralığında tespit ediniz.
n=20
xort=216.53
xsapma=15.86
sderecesi=n-1
guven=0.95
aralik=stats.t.interval(confidence=guven,df=sderecesi,loc=xort,scale=xsapma/np.sqrt(n))
print(aralik)