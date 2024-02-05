from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#olasılık yoğunluk fonksiyonu
#stats.norm.pdf(x=nokta,loc=dağılım ortalaması,scale=standart sapma)
olasilik=stats.norm.pdf(x=11,loc=15,scale=3)#11 değerine denk gelen fonksiyon değerini verir f(11)
print(olasilik)
#ancak 11 değerinden küçük değerleri bulmak istiyorsak
#eksi sonsuz ile 11 sınırlarına fonksiyonun integrali alınmalıdır.
olasilik2=stats.norm.cdf(x=11,loc=15,scale=3)
print(olasilik2) #11 den öncekilerin tamamının olasılığını verir z score ve z table ile yaptıklarımızı verir.
#para atma olasılığı üzerinden baktığımızda
x=[0,1,2,3]
p=[1/8,3/8,3/8,1/8]
cum=[]
#kumulatif dağılım fonkç birbirinin üzerine eklenerek ilerler.
for i in range(0,len(p)):
    if len(cum)==0:
        cum.append(p[0])
    else:
        cum.append(p[i]+cum[i-1])
print(cum)
plt.plot(x,cum,drawstyle="steps")
plt.show()

#sürekli değişken için kümülatif dağılım
x=np.random.randn(10000)
pdf=stats.norm.pdf(x)#zscore alan hesabı
cdf=stats.norm.cdf(x)#kümaltif dğılım hesabı
sns.lineplot(x=x,y=pdf)
sns.lineplot(x=x,y=cdf)
plt.show()