#varsayımları
#1)gözlemlerin bağımsız olması
#2)bağımlı değişkenin sürekli olması
#3)normal dağılıma sahip olmalı ama yine de
#unutmayalım ki anova testi normalliğe karşı çok dirençlidir
#Küresellik(sphericity)varyans homojenliğini küresellik varyansıyla kontrol ediyoruz
#küresellik varsayımı için meuchly'nin küresellik testi uygulanır.
#ORNEK:ELİMİZDE KİŞİLERİN TESTLER SONRASI KANDEĞERLERİ MEVCUT BUNŞAR ARASINDA
#ANLAMLI BİR İLİŞKİ OLUP OLMADIĞINA BAKTIK
import pandas as pd
import pingouin as pg
veri=pd.read_excel(".\\testSonuclari.xlsx")
veri2=pd.melt(veri,id_vars="Örneklem",value_vars=["TÖ","TS1","TS2","TS3"])
veri2.columns=["Örneklem","Testler","Puanlar"]
print(veri2)#H0 hipotezi reddedilemez
#normallik varsayımı test edilir
normallik=pg.normality(data=veri2,dv="Puanlar",group="Testler",method="shapiro")
print(normallik)
#küresellik testi
homojenlik=pg.sphericity(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler")
print(homojenlik)#h0 hipotezi reddedilemez
#eğer küresellik geçerli değilse greenhouse testi uygulanmalı
anova=pg.rm_anova(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler")
print(anova) #h0 hipotezi reddedilir yani gruplar arasında istatistiki olarak bir fark var
#post hoc ile aralarındaki ilişkiyi detaylı analiz edelim
posthoc=pg.pairwise_ttests(data=veri2,dv="Puanlar",subject="Örneklem",within="Testler",padjust="bonf")
print(posthoc)#pcorr lara bakılır.
grup=veri2.groupby("Testler")
print(grup.describe())#ortalamalarına bakıyoruz