#varsayımları
#sürekli değişken olmalı
#normallik olmalı
#doğrusallık olmalı
#H0 hipotezi ilişki yok hipotezidir.(p büyükse 0.05 den ise gerçekleşir)
#H1 hiotezi ilişki var hipotezidir(p küçükse 0.05 den )
import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
import seaborn as sns
veri=pd.read_excel(".\dondurmasıcaklık.xlsx")
print(veri)
#normalliği test edelim
norm=pg.normality(veri)
print(norm)#H0 hipotezi reddedilemez
#Doğrusallığı kontrol edelim
sns.lmplot(data=veri,x="Sıcaklık",y="DondurmaSatış",ci=None)
#x bağımsız ye bağımlı değişken olmalı
plt.show()
#doğrusallık mevcut
korelasyon=pg.corr(x=veri["Sıcaklık"],y=veri["DondurmaSatış"],method="pearson")
print(korelasyon)#r korelasyon katsayısıdır.
