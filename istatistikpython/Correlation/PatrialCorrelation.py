import pandas as pd
import pingouin as pg
veri=pd.read_excel(".\kiloyaş.xlsx")
print(veri)
kor=pg.pairwise_corr(veri)
print(kor)
kısmikor=pg.partial_corr(data=veri,x="Öğün",y="Kilo",covar="Yaş")#bağımsız değişken x bağımlı değişken y dir.
#hangi değişkenin etkisini ortadan kaldırmak istiyorsak covar'a onu yazıyoruz
print(kısmikor)
#burada görebiliriz ki öğün ve kilo arasındaki ilişkinin büyük bir kısmı hatta anlamlı kabul etmemizi sağlayan etki
#yaş parametresinden geliyormuş.