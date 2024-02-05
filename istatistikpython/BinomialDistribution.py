from scipy import stats
#paranın bir defa atlınca yazı gelme olasılığı
p=0.5#olasılık değeri
n=1#deneme sayısı
x=1
dagilim=stats.binom(n,p)
yazi=dagilim.pmf(k=x)
print(yazi)
#paranın yedi defa atlınca 3 kere yazı gelme olasılığı
p=0.5#olasılık değeri
n=7
x=3
dagilim=stats.binom(n,p)
yazi=dagilim.pmf(k=x)
print(yazi)
#bir fabrikada üreilen her 100 üründen biri kusurludur. (p=0.1).
#bu olay göz önüne alındığında müsteriye satılan 10 ürünün tamamının kusursuz olma olasılığı
#veya en faz ikisinin kusurlu olma olasılığı
p=0.1
n=10
kusursuz=stats.binom(n,p)
cikis=kusursuz.pmf(k=0)#kusur durumunun gerçekleşmemesini istediğimiz için k y 0 yazdık 0 tane kusur durumu gerçekleşti
print(cikis)
#en az ve ya en fazla gibikavramlarda noktasal bir x değeri olmaz onun yerine x<2
kusur1=kusursuz.pmf(k=1)
kusur2=kusursuz.pmf(k=2)
print(kusur2+kusur1+cikis)
#ya da
kusurqum=kusursuz.cdf(x=2)
print(kusurqum)# buarada eğer aralık söz konusuysa yani 0 1 ve 2 olasılıklarının birikimini istediğinden
#olasılık kütle fonk. yerine kümülatif yoğunluk fonk kullandık.
#aynı sonucu aldık.
#bir mağazada haftalık olarak ürün iadesi süreci için olasılık modelleme yapılmak istenmektedir.
#haftalık ortalama her 100 satışın 10 tanesi iade ediliyor.(p=0.1).
#50 satışta 5 iade gelme olasılığı , 15 den az iade gelme olasılığı, 10 dan fazla iade gelme olasılığı
p=0.1
n=50
dagilim=stats.binom(n,p)
besiade=dagilim.pmf(k=5)
print(besiade)
onbesdenaz=dagilim.cdf(x=15)
print(onbesdenaz)
ondanfazla=1-dagilim.cdf(x=10)
print(ondanfazla)
