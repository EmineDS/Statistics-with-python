import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
data=pd.read_csv(".\Advertising.csv")
print(data)
x=data[["TV","Radio"]]
y=data["Sales"]
sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
print(model.summary())
hata=model.resid
#hataların sabit varyansı hipotez testlerinde H0 sabit varyansdır
# H1  hipotezi farklı varyans vardırı savunur. bizim amacamız H0 ı görmektir
whitetest=smd.het_white(hata,model.model.exog)
print(whitetest[3])
#değer 0.05 ten küçük bir değer çıktığından H0 hipotezi reddedilir ve
#sabit varyans varsayımı desteklenemz
#bu teste alternatif olarak Pagan varyans testi de kullanılabilir.
BPtest=smd.het_breuschpagan(hata,model.model.exog)
print(BPtest[3])
#Burada da 0.05 ten büyük bir değer çıktı bu def da H0 hipotezi reddedilemiyor oluyor
#ynai ikisi de varyans testi olmasına rağmen sonuçlar farklı çıktı
#buradahatalar normal dağılım gösteriyorsa pagan testi kullanılır.
#ancak hatalar normal dağılım göstermiyorsa bile
#merkezi limit teoreminden yeterince öreklem sayısı varsa white testi kullanılmalıdır.
