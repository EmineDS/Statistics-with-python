from scipy import stats
import pandas as pd
grupA=[1,2,3,6]
grupB=[1,3,5,7]
grupC=[2,4,6,8]
fdeger,Pdeger=stats.f_oneway(grupC,grupB,grupA)
print(fdeger,Pdeger) #DEĞER 0.05 TEN BÜYÜK ÇIKTIĞI İÇİN PRTALAMALAR ARASINDA FARK VAR
#h0 hipotei ortalamalar eşit hipotezi reddedilir.
#ÖRNEK**************************************************************
veri=pd.read_excel("C:\\Users\edisa\Desktop\egitim_tv.xlsx")
print(veri)
#öncelikle verilerin normal dağılım gösterip göstermedğini kontrol etmeliyiz
g1=veri[veri["Eğitim"]=="İlkokul"]
g2=veri[veri["Eğitim"]=="Lise"]
g3=veri[veri["Eğitim"]=="Üniversite"]
g4=veri[veri["Eğitim"]=="Yükseklisans"]
normallik=stats.shapiro(g1["Tvizleme"])
print(normallik)
normallik=stats.shapiro(g2["Tvizleme"])
print(normallik)
normallik=stats.shapiro(g3["Tvizleme"])
print(normallik)
normallik=stats.shapiro(g4["Tvizleme"])
print(normallik)
#tüm veriler normal dağılıma uygun
#şimdi varyanshomojenliğini test edelim
homojenlik=stats.bartlett(g1["Tvizleme"],g2["Tvizleme"],g3["Tvizleme"],g4["Tvizleme"])
print(homojenlik)
#bartlett testinin sonucu da 0.05 ten büyük çıktığı için %95 güvenle
#varyanslar homojendir deriz
#ANOVA TESTİ YAPALIM
testanova=stats.f_oneway(g1["Tvizleme"],g2["Tvizleme"],g3["Tvizleme"],g4["Tvizleme"])
print(testanova)
#test sonucunda p değerimiz 0.05 ten küçük çıktığı için
#H0 hipotezi reddedilir
#gruplar arasında en az iki tanesinin ortalaması farklıdır.
#yani eğitim düzeyine göre televizyon izleme süreleri farklılık gösterir deriz.