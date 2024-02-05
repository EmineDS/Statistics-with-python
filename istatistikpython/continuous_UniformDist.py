from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
#bir otobüs 15 dakikada bir kalkıyor
a=0
b=15
dagilim=stats.uniform(a,b)
olasilik=dagilim.expect()
print(olasilik)
#bir kişinin bu durakta otobusu 12.5 dakikadan az bekleme olasılığı nedir?
olasilik=dagilim.cdf(x=12.5)
print(olasilik)
#bir ürünün tamir süresi 1.5 saat ile 4 saat arasında değişir.zamandan bahsettiği için
#sürekli uniform dağılımdır.
#tamir süresinin 2 den fazla olma olasılığı nedir
a=1.5
b=4
dagilim=stats.uniform(a,b)
print(dagilim)
olasilik=1-dagilim.cdf(x=2)
print(olasilik)