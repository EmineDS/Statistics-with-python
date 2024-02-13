#VARSAYIMLARIMIZ
#göslemlerin bağımsız olması
#her bağımlı değişkenin sürekli olması
#normal dağılım göstermesi(gösterme de sorun yok)
#varyans homojenliği
#kovaryans matris eşitliği
import pingouin as pg
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
veri=pd.read_excel(".\ürüntutum.xlsx")
print(veri)
#varyans homojenliğini test edelim
homojenlik=pg.homoscedasticity(veri,dv="ErkekTutum",group="Ürün",center="mean")#levene testi uuygular
print(homojenlik)
homojenlik=pg.homoscedasticity(veri,dv="KadınTutum",group="Ürün",center="mean")#levene testi uuygular
print(homojenlik)
#varyanslar homojendir
#kovaryans matrisi eşitliğine bakalım
varcov=pg.box_m(veri,dvs=["ErkekTutum","KadınTutum"],group="Ürün")
print(varcov)
#p değeri 0.05 ten H0 kabul edilir. yani kovaryans matrisi eşittir
model=MANOVA.from_formula("ErkekTutum+KadınTutum~Ürün",data=veri)
#direkt model print edilirse obje ifadesi döndürülür
print(model.mv_test())#genelde wilks' lambda testine bakılır . pr>f değerine bakılır.
#p değeri 0.05 ten büyük çıktığı için ürün kategorisindeki bağımsız değişkenin bağımlı değişkenler üzerine
#bir etkisi yoktur diyebilir. ürünlerin cinsiyet talebi üzzerine istatistiksel bir anlamlılık yok

#ANLAMLI ÇIKSAYDI BİR FARKLILIK İFADE EDECEKTİ. O ZAMAMN NE YAPACAKTIK?
#ürünler arasındaki anlamlılığa baktık
posthoc1=pg.pairwise_tukey(data=veri,dv="ErkekTutum",between="Ürün")
posthoc2=pg.pairwise_tukey(data=veri,dv="KadınTutum",between="Ürün")
print(posthoc1)
print(posthoc2)
