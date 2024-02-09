import pandas as pd
from scipy import stats
#ÖRNEKLER
#ÖRNEK1*********************************************
veri=pd.read_excel("C:\\Users\edisa\Desktop\sigarazaman.xlsx")
print(veri)
icen=veri[veri["sigara"]=="Evet"]
icmeyen=veri[veri["sigara"]=="Hayır"]
#ÖNCELİKLE NORMALLİK TESTİ YAPILMALI
#norrmallik testinde p değerleri 0.05 ten büyükse H0 kabul edilir yani
#dağılımların normal dağılım gösterdiği tespit edilir
normicen=stats.shapiro(icen["zaman"])
normicmeyen=stats.shapiro(icmeyen["zaman"])
print(normicen)
print(normicmeyen)
#varyans homojenliği testi yapılır
#varyans homojenlik testinde p değeri 0.05 ten büyükse
#H0 hipetzi kabul edilir. H0 hipotezinde varyanslar homojen
#varsayımı kabuledilir.
homojen=stats.bartlett(icen["zaman"],icmeyen["zaman"])
print(homojen)
#T testi yapalım
#p değeri 0.05 ten büyükse H0 hipotezi kabul edilir
#H0 hipotezi örneklemlerin ortalamaları arasında bir fark yokturu kabul eder
#yani sigara içen ile içmeyen aarasında nefes süreleri ölçüldüğünde istatiksel
#bir fark yokturu kabul eder(bizim oluşturduğumuz verilere göre)
test=stats.ttest_ind(icen["zaman"],icmeyen["zaman"],alternative="two-sided")
#bir farklılıktan bahsettiğimiz eşit ve ya değil dediğimşz için two sided
print(test)
#ÖRNEK2*********************************************
veri=pd.read_excel("C:\\Users\edisa\Desktop\gruptutum.xlsx")
eski=veri[veri["Grup"]=="Eski"]
yeni=veri[veri["Grup"]=="Yeni"]
normeski=stats.shapiro(eski["Tutum"])
normyeni=stats.shapiro(yeni["Tutum"])
print(normeski)
print(normyeni)
homojen=stats.bartlett(eski["Tutum"],yeni["Tutum"])
print(homojen)
test=stats.ttest_ind(eski["Tutum"],yeni["Tutum"],alternative="two-sided")
print(test)
#p değeri büyük çıktı ama eğer küçük çıksaydı eski ve yeni tutumalrı arasında istatiatiksel fark vardır diyebilirdik
 #varyanslar homojen olmasaydı homojenlik testinde p dğeri 0.05 ten KÜÇÜK çıksaydı ne yapacaktık?
test=stats.ttest_ind(eski["Tutum"],yeni["Tutum"],alternative="two-sided",equal_var=False)
#tek yapmamız gereken default olarak True olan
#equal_varparametresini false çevirlmek (WELCH'IN T TESTİ)
