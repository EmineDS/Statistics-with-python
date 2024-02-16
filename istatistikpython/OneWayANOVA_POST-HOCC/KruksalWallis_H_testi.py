import pandas as pd
import pingouin as pg
from scikit_posthocs import posthoc_conover
veri=pd.read_excel(".\yöntemgözlem.xlsx")
print(veri)
veri2=pd.melt(veri,value_vars=["A Yöntem","B Yöntem","C Yöntem"])
veri2.columns=["Yöntem","Değer"]
print(veri2)
normallik=pg.normality(veri2,dv="Değer",group="Yöntem")
print(normallik)#üçü de false dönmüşH0 hipotezi reddedilir normal dağılım göstermiyorlar
#adet sayısı da az olduğun merkei limit teoremi de uygulanamaz
test=pg.kruskal(veri2,dv="Değer",between="Yöntem")
print(test)#değer 0.05 ten küçük olduğundan yöntemlerin medianları farklı
#aralarında nalamlılık farknı daha iyi analiz etmek için post hoc testine bakalım.
#conover testini uygulayacağız
posthoc=posthoc_conover(veri2,val_col="Değer",group_col="Yöntem",p_adjust="bonf")
print(posthoc)#A ile C arasında anlamlı bir fark vardır.