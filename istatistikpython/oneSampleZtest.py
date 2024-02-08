from statsmodels.stats.weightstats import ztest

veri=[95,70,120,65,130,38,116,90,60]
#elimizdeki veri setinin ortalamasının 80 den büyük olma ihtimali var mı
alfa=0.05
#burada alternative 80 den büyk değerleri istediğimiz için larger oldu eşit olan değeri isteseydik
#çiftkuyruk yapısı olacağından tewo sided i yazardırk
#z test iki değer gönderir ilki tablodaki z değeri ikincisi de bizim istediğimiz
#p değer.
zhesap,p=ztest(veri,value=80,alternative="larger")#"smaller , two sided
print(zhesap,p)

if p<alfa:
    print("H0 reddedilir")
else:
    print("H0 reddedilemez")

#genelde z testi yerine z testi kullanılır
#çünkü z testinde popülasyon standart sapma ve
#ortalaması bilinmelidir
#ancak gerçek hayatta biz örneklemlerle çalışırız
#popülasyonlarla değil.