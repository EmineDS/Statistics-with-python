import pandas as pd
import pingouin as pg
veri=pd.read_excel(".\cinsiyetsüre.xlsx")
#kadın ve erkeklerin sürelerinin medianları arasında far var mı diye bakıyoruz
print(veri)
#elimizdeki data sayısı düşük merkezi limi teoremi dışında kalıyor
#normalliğini test edelim
normallik=pg.normality(veri,dv="Süre",group="Cinsiyet")
print(normallik)
#kadın için normallik var erkek için yok kadın true olarak döndü.
#NONPARAMETRİK TEST UYGULAYACAĞIZ.
kadın=veri[veri["Cinsiyet"]=="Kadın"].Süre
erkek=veri[veri["Cinsiyet"]=="Erkek"].Süre
test=pg.mwu(x=kadın,y=erkek,alternative="two-sided")
print(test)
#medianlar farklı