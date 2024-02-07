import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(10)#ürettiğimiz rassal sayıların hep aynı olması için
veri=stats.norm.rvs(loc=38,size=500)
print(veri)
#arık elimizde normal dağılıma uygun bir veri seti var
#pekibunun normal dağılıma uygun olduğunu nasıl belirleyebiliriz.
#normal dağılım için skewness ve kurtosis -1,5 ve +1,5 aralığında olmalıdır.
#bazı kaynaklarda bu değerlerin normal dağılım için +1 -1 aralığında olması gerektiği savunulur.
print(stats.kurtosis(veri))
print(stats.skew(veri))
#grafiklere bakark normal dağılım mı değil mi görebilirz
#distplot bir histogram yapısıdır.
#sns.distplot(veri)
#stats.probplot(veri seti, dist="hangi dağılıma uygun olup olmadığına bakılmak isteniyorsa",plot=plt(zorunlu))
stats.probplot(veri,dist="norm",plot=plt)
#değerlerimiz çizgi üzerinde ne kadar düzgün ilerliyorsa veri seti o kadar normal dağılıma uygundur
#çizgi üzerinde olmayanlar da aykırı değerlerdir.
plt.show()
#hipotez testlerine bakacak olursak H0 normal dağılım olduğunu H1 normal dağılım olmadığını ifade eder.
#örneklemin normal olup olmadığına bakmak için çeşitli normallik sınamaları vardır.
#Kolmogorov-Smirnov testi (tek örneklem sınaması)
ks=stats.kstest(veri,cdf="norm")#şu an standart normal dağılımı test ediyor
print(ks)
#ancak normal dağılım olsa da bizim dağılımımız standart değil ve ort 0 olmadığı
#için biz bunu zaten biliyouz.
ks=stats.kstest(veri,cdf="norm",args=(veri.mean(),veri.std()))#burada ise
#arg için verimizin ortalama ve standart sapmasını girdik ki standart notmal dağılıma değil
#bizim verilerimizle normal dağılıma uygun olup olmadığına baksın
print(ks)
print(f"{ks.pvalue:5f}")#p value yi çağırdık ve burada sadece vizrgülden sonra
#beş adet rakamı göstermesini sağladık
#SONUÇ OLARAK P DEĞERİ ALFADAN BÜYÜK OLDUĞU İÇİN H0 REDDEDİLEMEZ VE H0 NORMAL DAĞILIMI İFADE EDİYORDU
#YANİ DAĞILIMIMIZ NORMAL DAĞILIM.
#Shapiro-Wilk sınaması(DAHA FAZLA KULLANILIR)
#yien aynı şekilde h0 normal dağılım h1 normal dağılım değil anlamına gelir
#yani p değerimiz 0.5 ten büyük çıkarsa dağılımın normal dağılım olduğunu söyleyebiliriz
sw=stats.shapiro(veri)
print(sw)
print(sw.pvalue)#değerimiz 0.509 alfa da 0.05 olduğunda ve p değeri alfadan büyük olduğundan
#dağılım %95 güvenle normal dağılımdır.