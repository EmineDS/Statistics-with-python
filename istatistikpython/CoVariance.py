#Kovaryans nedir?
#Iki değişkenin birlikte ne kadar değiştiklerinin ölçüsüdür.
import numpy as np
x=[45,37,42,35,39]
y=[38,31,26,28,33]
veri=np.array([x,y])
varcov=np.cov(veri,bias=True)#bias true ise popülasyon false ise örneklem üzerinden işlem yapar
print(varcov)
print(np.var(x))
print(np.var(y))