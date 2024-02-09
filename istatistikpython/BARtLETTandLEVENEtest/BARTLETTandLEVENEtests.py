import pandas as pd
from scipy import stats
veri=pd.read_excel("C:\\Users\edisa\Desktop\cinsiyetharcama.xlsx")#klosördeki dosya yolu değiştirilmeli
print(veri)
erkek=veri[veri["Cinsiyet"]=="Erkek"]
kadin=veri[veri["Cinsiyet"]=="Kadın"]
#şimdi de her iki dağılım için normallik testi yapılmalıdır
p1=stats.shapiro(erkek["Harcamalar"])
p2=stats.shapiro(kadin["Harcamalar"])
print(p1)
print(p2)
#her iki değer de 0.05 ten büyük olduğundan H0 hipotezi reddedilemez. H0 hipotezi de normal dağılımı savunur.
h1=stats.levene(erkek["Harcamalar"],kadin["Harcamalar"],center="mean")
#burada center paramtersi zorunlu parametre değildir. ancak levene testi default olarak medianı baz alır
#bunun nedeni de levene testinin normal olmayan dağılımlarda kullanıldığıdır.
#ancak center parametresiyle ortalamayı baz almasını sağladık
print(h1)
#p değerimiz 0.05 ten büyük olduğundan H0 reddedilemez yani varyanslarlar %95 güvenle homojendir
h2=stats.bartlett(erkek["Harcamalar"],kadin["Harcamalar"])
print(h2)
#aynı şekilde h2 de 0.05 ten büyük olduundan H0 reddedilemez H0 varyansın homojenliğini savunur.
#ARTIK BU YAPI T TESTİNE HAZIR DİYEBİLİRİZ :)