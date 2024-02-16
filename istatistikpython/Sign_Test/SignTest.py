#non parametrik testlerde median üzerinden yorum yapılır
import pandas as pd
from scipy import stats
from statsmodels.stats.descriptivestats import sign_test
#elimizdeki notların medianının 30 dan farklı olup olmadığına bakacağız
veri=pd.read_excel(".\örneknot.xlsx")
print(veri)
#öncelikle veri setimiz yeterince büyük değil ve merkezi limit teromeini sağlamıyo
#normal dağılım testi yapalım
norm=stats.shapiro(veri["Not"])
print(norm)#p eğeri 0.05 ten küçük çıktı yani H0 hipotezi reddedilir.yani dağılım normal değil.
# tek örneklem t testinin non parametrik karşılığı olan işaret testini yapacağız.
test=sign_test(veri.Not,mu0=30)
print(test)
#p değeri 0.05 ten küçük çıktığından H0 hipotezi reddedilir. çıktığından not medianı 30 dan farklıdır.
print((veri.Not.median()))