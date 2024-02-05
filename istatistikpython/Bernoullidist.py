from scipy import stats
#yazi tura durumu için bernoulli dağılımı
p=0.5
dagilim=stats.bernoulli(p)
turaolasilik=dagilim.pmf(k=0)# k dediğimiz aslında x rassal değişkenidir
yaziolasilik=dagilim.pmf(k=1)
print("yazi gelme olasiliği {}, tura gelme olasiliği {}".format(yaziolasilik,turaolasilik))
print(dagilim.expect())#beklenen değer
print(dagilim.var())#varyans değeri
#desteden papaz seçme durumu için bernoulli dağılımı
p=4/52#52 karttan dördü papazdır
dagilim=stats.bernoulli(p)
gelolasilik=dagilim.pmf(k=1)
gelmeolasilik=dagilim.pmf(k=0)
print("papaz gelme olasiliği {}, papaz gelmeme olasiliği {}".format(gelolasilik,gelmeolasilik))
print(dagilim.expect())
print((dagilim.var()))