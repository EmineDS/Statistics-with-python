#A ve B olmak üzere iki değişkenli gruptan oluşur.
#genelde tutumları karşılaştırabilmek için kullanılan testlerdir.
#oran test yapısıdır.
#H0 ana kitle hipotezi oranlar arasında fark yoktur hipotezidir. yani tutum değişmemiştir olarak döner
#H1 hipotezi fark var hipotezidir p değeri 0.05 alanı içine düzmeli yani 0.05 ten küçük olmalıdır
#n1 ve n2 >30 olmalıdır
#SORU:KADIN VE ERKEĞİN İNTERNETTE bir habere tıklama oranının CİNSİYETLE ALAKASI OLUP OLMADIĞINA BAKILIYOR
#VE erkeklerin daha fazla tıkladığı öne sürülüyor
from statsmodels.stats.proportion import proportions_ztest
import numpy as np
basari=np.array([45,40])
gozlem=np.array([50,50])
test=proportions_ztest(basari,gozlem,alternative="larger")
print(test)#ikinci değer p değeri ve 0.05 ten büyük çıktığı için H0 reddedilemez
#erkekler kadınlardan daha fazla tıklamaz