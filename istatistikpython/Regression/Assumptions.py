import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from scipy import stats
import statsmodels.stats.diagnostic as smd
import pingouin as pg
data=pd.read_csv(R".\Advertising.csv")
print(data)
#*******************************************************************
#DEĞERLERİN DOĞRUSALLIK VARSAYIMINI TEST EDELİM
#*******************************************************************
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
#*******************************************************************
#HATALARIN NORMALLİK VARSAYIMINI TEST EDELİM
#*******************************************************************
#resid parametresi modelin hatalarını getirir.
print(np.mean(model.resid))#hataların beklenen değeri genelde 0 a yakındır burada olduğu gibi.
sns.distplot(model.resid,kde=True)
plt.show()
normallik=stats.shapiro(model.resid)#hatlara normallik testi yaptığımızda da
#p değerinin 0.05 ten küçük olduğunu görürüz
#yani dağılım normal dağılım değildir. normallik varsayımını H0 hipotezi destekler.
print(normallik)
#Ancak genelde normallik testi için en azından görselleştirmek için qqplot yapısı en çok kullanılandır
sm.qqplot(model.resid,line="s")
plt.show()
#aynı zamanda modelin matrixindeki prob(JB) değeri de bize hataların normalliğini verir
#*******************************************************************
#HATALARIN OTOKORELASYON VARSAYIMINI TEST EDELİM
#*******************************************************************
hata=model.resid
sm.graphics.tsa.plot_acf(hata)
plt.show()
#burada ilki hariç tüm noktalar içerdeki mavi alan içerisinde(güven aralığında)
#kalıyorsa otokorelasyon sorunumuz yoktur.
#Matrixteki Durbin watson testine otokorelasyon için bakılır ve durbin-Watson değeri
#1.5 ve 2.5 arasında ise otokorelasyon bakımından bir sorun yoktur denir.
#peki ya sorun olsaydı ve değer 1.5 ile 2.5 arasında olmasaydı?
#o zaman ek testler uygulanır.
lm=smd.acorr_breusch_godfrey(model,nlags=2)
print(lm)#ikinci değere bakılır ki bu p değeridir. p değeri 0.05 ten büyük
#olduğundan H0 reddedilemez.
#H0 otokorelasyon yoktur H1 otokorelasyon vardır der.
