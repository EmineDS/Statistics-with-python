import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#sed yapısı bize her program çalıştığında sabit veri seti üretmemizi sağlar
#np.random.seed(0)
#normal(ortalama,standat sapma,büyüklük veri sayısı)
veri=np.random.normal(35,2,40000)
#veriz ile standartlaştırma yaptık z score formülünü uygladık
veriz=(veri-np.mean(veri))/np.std(veri)
#ya da tek fonk yapısıyla formül kullanmadan veriz 2 deki scipyden alınan stats fonk zscore parametresiyle yapabiliriz
veriz2=stats.zscore(veri)
sns.displot(veriz,kde=True)
plt.title("veri dağılım garfiği",fontsize=15,loc="right",c="red")
plt.xlabel("veriler",fontsize=15,c="red")
plt.ylabel("frekans",fontsize=15,c="red")
plt.xlim(-3,3) #x düzlemindeki sınırları belirledik
#plt.axvline dikey çizgi çizdirir ve ekstra çizgi çizdirip ne olduğunu etiketle belirtmek istiyorssak plt.legend() kullanılır.
plt.axvline(x=veriz.mean(),linestyle="--",linewidth=2.5,label="ortalama",c="red")
#standart sapmaları çziyoruz iki farklı yazım kullandım np li ve np siz
plt.axvline(x=veriz.mean()-veriz.std(),linestyle="--",linewidth=2.5,label="ortalama+-1 std",c="black")
plt.axvline(x=np.mean(veriz)+np.std(veriz),linestyle="--",linewidth=2.5,c="black")
plt.axvline(x=veriz.mean()-2*veriz.std(),linestyle="--",linewidth=2.5,label="ortalama+-2 std",c="blue")
plt.axvline(x=np.mean(veriz)+2*np.std(veriz),linestyle="--",linewidth=2.5,c="blue")
plt.legend()
plt.show()

