from scipy import stats
n=6
#bir zar üzerinden düşünüyoruz
dagilim=stats.randint(1,n+1)
olasilik=dagilim.pmf(k=5)#5 değerinin gelme olasılığı
print(olasilik)
print(dagilim.expect())#beklenen değer
print(dagilim.var())#varyans
olasilikkucuk3=dagilim.cdf(x=3)#değerin 3 ve 3 den küçük olma olasılığı
print(olasilikkucuk3)