import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#burada  bir yazı tura olayının nasıl yüzde elli ihtimale yakınsadığı kanıtlanmıştır.
liste=[]
for i in np.arange(0,30):
    denemesayisi=i+1
    #randint(başlangı. değeri,bitiş değeri dahil olmayan,sayı miktarı)
    yt=np.random.randint(0,2,size=denemesayisi)#para atma olasılığı
    yolasilik=np.mean(yt)
    liste.append(yolasilik)
    print("deneme sayısı{}-----ortalama{}".format(denemesayisi,yolasilik))
sns.lineplot(data=liste,linewidth=2)
plt.xlabel("deneme sayisi")
plt.ylabel("ortalama")
plt.ylim(0,1)
plt.axhline(0.5,color="red",linestyle="--",linewidth=1.)
plt.show()
#burada görmemiz gerken deneme sayısı arttıkça beklenen olasılık değerine yakınsama durumu gerçekleşir.
