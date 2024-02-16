from scipy import stats
import pandas as pd
veri=[25,26,25,20,18,29,30,32,17,23,34,27,26,30,33,32,21,21,20,11,16,14,15,18,19]
#önceki verilere göre bir snraki sınavın ortalamaısnın 28 olma ihtimali nedir
#burada 28 olması H0 dır ve ana kitleyi oluşturur.
alfa=0.05 #%95 güven aralığında çalışıcaz
#popmean bizim seçtiğimiz değerdir ayrıca two sided da bir değer seçtiğimiz için çift kyruk yapısında
#çalışacağımızı ifade eder.
thesap,p=stats.ttest_1samp(veri,popmean=28,alternative="two-sided")
#stats ın 1 samp t testi ikiparametre döndürür ilki hesaplanan t değeri ikincisi ise olasılık alanı olan p
print(thesap,p)
if p<alfa: #yani p değerimiz alfa alanı içinde kalacak kadar küçükse
    print("H0 reddedilir")#çünkü hipotezimizden sapma olmuştur
else:
    print("H0 reddedilemez")#eğer p değeri ana kitle içine düşseydi bu bize ortalamnın 28 olabileceğini
    #gösterirdi ki bu da H0 ı rededilemez yaniimkan dahilinde yapardı
    #unutmamaız gereken şeyi tekrar hatırlatmak gerekirse bir H1 i hiçbir zaman reddedemeyiz
    #çünkü %100 güven aralığı diye bir şey yoktur.

#Günlük hatalı üretim ortalam 20dir.ve bu güvenli bir alandır.
#ancak müşterilerin hata raporlarınıincelediğimizde bunun 20 olduğu
#veya olmadığı konusunda endişeye düşüyoruz.aşağıdaki veride
#günlük hata sayısı verilmiştir.
#bu hata oranın ortalama 20 olum olmadığını est edelim.
#H0 ana kitlenin ortalama 20 yi ifade ettiğini bliyoruz
veri=[25,26,25,20,18,29,30,32,17,23,34,27,26,30,33,32,21,21,20,11,16,14,15,18,19]
thesap,p=stats.ttest_1samp(veri,popmean=20,alternative="two-sided")
print(thesap,p)
if p<alfa: #yani p değerimiz alfa alanı içinde kalacak kadar küçükse
    print("H0 reddedilir")#çünkü hipotezimizden sapma olmuştur
    #ortalama 20 hata ifadesi doğru değil
else:
    print("H0 reddedilemez")
