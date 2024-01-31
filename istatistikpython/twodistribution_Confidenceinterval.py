import numpy as np
from scipy import stats
#iki farklı örneklem için ortalama tahmini kurallarının tek örneklemden farkı yoktur.
#Soru1:Bir fabrikada Ave B ürünlerinin ağırlıklarının varyansları sırasıyla 164 gr ve 216gr dır.
#a türünden 28 adet b türünden 30 adte örneklem alınmıştır
#a türünün ortalama ağırlığı 32 gr b türünün ortalama ağırlığı 26 gr çıkmıştır
#a ve b  türünün ortalama ağırlıklarının farkı % 95 güven aralığında kaçtır?
na=28
nb=30
vara=164
varb=216
orta=32
ortb=26
guven=0.95
#stats.norm.interval(confidence=guven aralığı,loc=ortalamalar farkı,scale=kök(varyansların örneklem sayılarına bölünüp toplanması))
aralik=stats.norm.interval(confidence=guven,loc=(orta-ortb),scale=np.sqrt((vara/na)+(varb/nb)))
print(aralik)
#Soru2:ingilizce ve franszca eğitim alan iki öğrenci grubundan sırasıyla 30 ve 40 ogr seçiliyor.
#ing gurubu ögrlerinin dil öğrenme süresi 182 gün fransıza grubu öğrencilerinin 176 gündür.
#aynı gruplar için varyanslar sırasıyla 196 gün ve 144 gündür.
#iki farklı dil kurusunun öğrenme süreleri arasındaki fark 95 güven aralığında kaçtır?
ni=30
nf=40
orti=182
ortf=176
vi=196
vf=144
guven=0.95
aralik=stats.norm.interval(confidence=guven,loc=orti-ortf,scale=np.sqrt((vi/ni)+(vf/nf)))
print(aralik)
#Soru3:2 farklı hasta grubu arasında 8 ve 10 bireylerden oluşan örneklemler çekildi
#bu iki gruubun virüse reaksiyon verme süreleri sırasıyla 3 ve 2.7 dir.
#birleştirilmiş varyans 0.05 olarak alındığına göre
#hasta gruplarının raksiyon sürresi farkları %95 güven aralığında kaçtır?
###### örneklemler 30 dan küçük olduğu için t tablosu kullanılacak serbestlik derecesi n1+n2-2 dir.
###### ortak bir varyans (birleştirilmiş varyans kullanılır)
##### scale=kök((1/na+1/nb)*birleştirilmiş varyans)
na=8
nb=10
birvar=0.05
orta=3
ortb=2.7
guven=0.95
aralik=stats.t.interval(confidence=guven,df=na+nb-2,loc=orta-ortb,scale=np.sqrt(((1/na+1/nb)*birvar)))
print(aralik)


