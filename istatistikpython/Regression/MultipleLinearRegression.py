import pandas as pd
import statsmodels.api as sm
veri=pd.read_excel(R".\tavukveri.xlsx")
print(veri)
x=veri[["Gelir","TavukFiyat","SıgırFiyat"]]#bağımsız değişkenler
y=veri[["TavukTüketim"]]#bağımlı değişken
sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
print(model.summary())
#sabit değer ayrıca ortalama miktardır.
