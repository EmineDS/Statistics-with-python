from scipy import stats
import numpy as np
#bi farbrikada ürütelin ürünün ortalama ağırlığı 500 gram varyansı 100 gramdır
#seçilen bir ürünün ağırlığının 518 gramdan az olma olasılığı nedir
#bunun için birikimli dağılım fonk. kullanmalıyız.
ortalama=500
varyans=100
dagilim=stats.norm(ortalama,np.sqrt(varyans))#ortalama ve standart sapma yazılır
olasilik=dagilim.cdf(x=518)
print(olasilik)

#Bir üretim işinde a isimli bir ürün üretiliyor ve günlük talep miktarı ortalama 100 adettir.
#varyans ise 3000 dir. elimizde 3500 adet stok vardır. elimizdeki stoğun
#1ayda bitme olasılığı nedir(p (x>=3500))
urunsayi=100*30 #aylık ortalama talep
varyans=3000*30 #aylık varyans
dagilim=stats.norm(urunsayi,np.sqrt(varyans))
olasilik=1-dagilim.cdf(x=3500)
print(olasilik*100)
#a ülkesindeki orman yangınları inceleniyor. inceleme sonunda yıllık ortalama 4300 dönüm yanıyot
#varyans değeri 562.500 dür.herhnagi bir yılda p(2500< x <4200)?
#once 2500 den az ola olasılığını sonra 4200 den az olma olsaılığını bulup
#birbirinden çıkarmalıyız
urunort=4300
standartsapma=np.sqrt(562500)
dagilim=stats.norm(urunort,standartsapma)
olasilik1=dagilim.cdf(x=2500)
olasilik2=dagilim.cdf(x=4200)
print(olasilik2-olasilik1)
#3000 fazla dönüm yanma olasılığı
#burada 1-cdf kullanmka yerine sf kullanacağız. tamamen aynı şey
olasilik=dagilim.sf(x=3000)
print(olasilik)
#ürettiğiniz bir ürünün ortalama ömrü 58 aydır. varyansı ise 100 aydır.
#ürünleri arıza garantisi 3 yıl tanınır. 1 yılda 1 milyon
#ürün üretiliyorsa 3 yıl içinde kaçı granatiye gelir.
ortalama=58
standarsapma=np.sqrt(100)
dagilim=stats.norm(ortalama,standarsapma)
olasilik=dagilim.cdf(x=36)#3 yıl 36 aydır
print(olasilik*100)#bür ürünün 36 ayda arızalanma olasılığı
print(olasilik*1000000)#yılda garantiye 13900 ürün gelme olasılığı vardır.
#bir restoraanın teslimat süresi ortalama 30 dk dır.varyans değeri ise 25 dakikadır.
#p(20<x<40)?
ortalama=30
ss=np.sqrt(25)
dagilim=stats.norm(ortalama,ss)
olasilik1=dagilim.cdf(x=20)
olasilik2=dagilim.cdf(x=40)
print(olasilik2-olasilik1)