import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats as ss
import matplotlib.pyplot as plt



veri=pd.read_excel(".\calisanperform.xlsx")
print(veri)
#veriye göre mevki ve çalışma süresi performansı etkiliyor mu ona bakacağız
#iki bağımsız girdi olduğu için iki yönlü anova kullanacağız.
#iki yönlü anova arka planda doğrusal bir model yapısı çalıştırır
model=ols("Performans~C(Mevki)+C(Süre)+C(Mevki):C(Süre)",data=veri).fit()
#***********önemli
hatalar=model.resid
#doğrusal modellemede varsayımları bu formülle doğrudan bir değişkene atarız
#çünkü modellemede varsayımlara hata olarakkabul eedilir.
normallik=stats.shapiro(hatalar)
print(normallik)
#p değeri 0.05 ten büyük çıktığı için H0 hipotezi reddedilemiyor yani dağılım normalliğe uygun
#ancak genelde bunun grafiği çizdirilir
fig=sm.qqplot(hatalar,line="s")
plt.show()
print(model.summary()) #prob f kısmına bakınc 0.05 ten küçük olduğu için bu modle anlamlıdır.

anova=sm.stats.anova_lm(model,type=2)#type ta ger bir grupta değişkenler gruplarının kendi içinde sayıları eşitse
#2 yi eşit değilse 3 ü kullanıyoruz
print(anova)
#posthoc testine bakalım
#mevki içindeki gruplara posthoc testini yapalım
etkimevki=ss.multicomp.pairwise_tukeyhsd(endog=veri["Performans"],groups=veri["Mevki"])
print(etkimevki)

grup1=veri.groupby("Mevki")["Performans"].mean()
print(grup1)#performans oranlarına baktık
etkimevkisüre=ss.multicomp.pairwise_tukeyhsd(endog=veri["Performans"],groups=veri["Mevki"]+veri["Süre"])
print(etkimevkisüre)
grup1=veri.groupby(["Mevki","Süre"]).mean()
print(grup1)