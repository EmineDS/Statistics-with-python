import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from scipy import stats
import pingouin as pg
data=pd.read_csv(R".\Advertising.csv")
print(data)
sns.pairplot(data,y_vars="Sales",x_vars=["TV","Radio","Newspaper"],kind="reg")
#bu yapıyla her bir değişken için değerleirn doğrusallığını gözlemlemleyebiliriz.
#burada gazete dışındaki diğer değerlerin doğrusal olabildiğini söyleyebiliriz.
plt.show()
#Bir de model üzerinden bakalım
#önce bağımlı değişken ve bağımsız değişkenleri ayıralım
x=data[["TV","Radio","Newspaper"]]#bağımsız değişkenler
y=data[["Sales"]]#bağımlı değişken
sabit=sm.add_constant(x)#sabit değer baımsız değişkenler üzerinden kurulur
model=sm.OLS(y,sabit).fit()#burada da ols içine önce bağımlı değişken sonra sabit değer gönderilir
print(model.summary())
#gazetenin p değerinin aynı grafikte bize anlattığı gibi linear anlamı bulunmadığını bize söyler. çünkü p değerimiz 0.05 ten büyüktür
#resid parametresi modelin hatalarını getirir.
print(np.mean(model.resid))#hataların beklenen değeri genelde 0 a yakındır burada olduğu gibi.
sns.distplot(model.resid,kde=True)
#hataların normal dağılım gösterip göstermediğine bakarız.
plt.show()
normallik=stats.shapiro(model.resid)#hatlara normallik testi yaptığımızda da
#p değerinin 0.05 ten küçük olduğunu görürüz
#yani dağılım normaldir.
print(normallik)
#Ancak genelde normallik testi için
#en azından görselleştirmek için qqplot yapısı en çok kullanılandır
sm.qqplot(model.resid,line="s")
plt.show()


