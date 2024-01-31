import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
#gçstermek istediğim şey serbestlik derecesi arttıkça t dağılımı normal yakınsar
np.random.seed(0)
#rvs(loc=ortalama,df=serbestlik derecesi,size=büyüklük,veri sayısı)
veri1t=stats.t.rvs(loc=0,df=1,size=15)# standartlaştırmak için ortalamayı 0 sapmayı 1 aldık
veri2t=stats.t.rvs(loc=0,df=2,size=15)
veri3t=stats.t.rvs(loc=0,df=5,size=15)
veri4t=stats.t.rvs(loc=0,df=20,size=15)
plt.xlim(-5,5)
sns.distplot(veri1t,hist=False,color="red")# distplotu kullandığımız zaman kde parametresini girmek zorunda değiliz
sns.distplot(veri2t,hist=False,color="blue")
sns.distplot(veri3t,hist=False,color="green")
sns.distplot(veri4t,hist=False,color="black")
#normale en yakın dağılım df derecesi en yüksek(20) olan siyah ile çizilen dağılımdır.
plt.show()