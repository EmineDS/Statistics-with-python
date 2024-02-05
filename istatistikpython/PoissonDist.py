#nadir olan olaylarla ilgili yapılan dağılım olduğunu öğrenmiştik.
#ortalama değer yapısı lambdaya ihtiyacımız oldupunu biliyorduk.
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
ort=10
dagilim=stats.poisson(ort)
print(dagilim)
p0=dagilim.pmf(k=0)
print(p0*100)#yüzde kaç ihtimal olduğunu merak ettiğimiz için 100 ile çarptık.
#x markasının y serisiyle ilgili satış olasılık modallemesi
#bu televizyondan 1 yılda 1825 tane satıldı
#bir günde bu tv den 9 adet satma olasılığımız kaçtır(p(x=9))
gunort=1825/365
dagilim=stats.poisson(gunort)
p=dagilim.pmf(k=9)#olmama olasılığı olsaydı 1 den çıkarırdık ya da k yı 0 seçerdik
print(p*100)
#x ülkesine çatı malzemesi satılıyor,ülkede 1 yılda ortalama 2 fırtına çıkıyor
#yılda 1,3,5 fırtına olma olasılığı nedir
ort=2
dagilim=stats.poisson(ort)
p1=dagilim.pmf(k=1)
p3=dagilim.pmf(k=3)
p5=dagilim.pmf(k=5)
print(p1*100,p3*100,p5*100)
#marmara bölgesinde 1 yılda ortalama 6 deprem oluyor
#önümüzdeki bir yılda en fazla ve en az üç deprem olma olasılığı nedir=
ort=6
dagilim=stats.poisson(ort)
p3az=dagilim.cdf(x=3)*100
p3faz=(1-dagilim.cdf(x=3))*100
print(p3az,p3faz)
