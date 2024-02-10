#bir websitesinin görünümünün satışları arttırıp arttrılmayacağı kontrol ediliyor
#buun için websitesinin tasarımını değiştirip bir grup insana önceki halini
#bir grup insana sonraki hali gösteriliyor
#ve alışveriş yapılıp yapılmamasını çıkarıyorlar
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
veri=pd.read_excel("C:\\Users\edisa\Desktop\ornekAB.xlsx")
#print(veri.head())
tablo=pd.crosstab(veri["Grup"],veri["Sayfa"])
#burada çapraz tablo oluşturduk ilk column dikey ikinci kolumn yatay değerleri yerleştirir.
#ve bunarın çapraz değerlerini vererek yeni bir tablo oluşturuz
#print(tablo)
#İKİ GRUBUN DA SAYISININ AYNI OLMASI İÇİN 50000 ER ÖRNEKLEM ALDIK
kontrol=veri[veri["Grup"]=="Kontrol"].sample(n=5000,random_state=42)
deneysel=veri[veri["Grup"]=="Deneysel"].sample(n=5000,random_state=42)
#print(kontrol.count(),deneysel.count())

veriyeni=pd.concat([kontrol,deneysel],axis=0)#verilerle yeni bir tablo oluşturduk
veriyeni.reset_index(drop=True,inplace=True)#indexlerini sıfırladık
#print(veriyeni)
gruplama=veriyeni.groupby("Grup")["Satış"]
print(gruplama.mean())#satış ortalamalarını aldık
#satış ortalamana bakarak yorum yapıp eskisinin ortalaması daha yüksek olduğu için eskisi daha iyi
#diyebilsek de yine de bunu test etmemiz gerekir
#deneysel ve kontrole göre satış değerlerini ayırdık
kontrol2=veriyeni[veriyeni["Grup"]=="Kontrol"]["Satış"]
deneysel2=veriyeni[veriyeni["Grup"]=="Deneysel"]["Satış"]
Basari=[kontrol2.sum(),deneysel2.sum()]
gozlem=[kontrol2.count(),deneysel2.count()]
test,p=proportions_ztest(Basari,gozlem,alternative="two-sided")
print(test,p)
#p değeri 0.05 ten büyük çıktığı için aralarında %95 güvenle istatistiksel bir fark yoktur denir