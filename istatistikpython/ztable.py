from scipy.stats import norm
#norm(loc=ortalama,scale=standat sapma).cdf(hangi değerden küçük olasılık istiyoruz) eğer büyük olma olasılığını istiyorsak değeri 1 den çıkarıcaz
olasilik=norm(loc=5.3,scale=1).cdf(4.5) #4.5 ten küçük olma olasılığı
olasilik2=1-norm(loc=5.3,scale=1).cdf(4.5) #4.5 ten büyük olma olasılığı
print(olasilik)
print(olasilik2)
#4.5 ile 6.5 aralığında olma olasılığı
ustsinir=norm(loc=5.3,scale=1).cdf(6.5) #6.5 ten küçük olma olasılığı
altsinir=norm(loc=5.3,scale=1).cdf(4.5) #4.5 ten küçük olma olasılığı
olasilik3=ustsinir-altsinir
print(olasilik3)
#a)kamu bankası personel alımı için yapılan test sonuçlarında ortalama 60 standat sapma 12 dir
#a.1)seçilen adayın 60-70 arasında puan almış olam olasılığı kaçtır?
ustsinir=norm(loc=60,scale=12).cdf(70)
altsinir=norm(loc=60,scale=12).cdf(60)
olasilik4=ustsinir-altsinir
print(olasilik4)
#a.2) tesadüfen seçilecek bir adayın 45-60 arasında puan almış olam olasılığı?
ustsinir=norm(loc=60,scale=12).cdf(60)
altsinir=norm(loc=60,scale=12).cdf(45)
olasilik5=ustsinir-altsinir
print(olasilik5)
#a.3)seçilen adayın 45 den az puan alma olasılığı nedir?
olasilik6=norm(loc=60,scale=12).cdf(45)
print(olasilik6)
#b)imal edilen ampüllerin ortalama ömrü 800 saat standart sapması 40 saattir.
#b.1)bir ampülün 778 saatten daha fazla ömre sahip olma olasılığı nedir?
olasilik7=1-norm(loc=800,scale=40).cdf(778)
print(olasilik7)
#b.2)bir ampülün 834 saatten daha az ömre sahip olma olasılığı nedir?
olasilik8=norm(loc=800,scale=40).cdf(834)
print(olasilik8)
#b.3)ampülün ömrünün 778 ile 834 saatleri arasında olma olasılığı nedir?
ustsinir=norm(loc=800,scale=40).cdf(834) #olasilik8 de yazilabilirdi
altsinir=norm(loc=800,scale=40).cdf(778)#olasilik7+1 de yazılabilirdi
olasilik9=ustsinir-altsinir
print(olasilik9)
#c)bir imalathanede üretilen millerin çaplarının ortalaması 3.0005 inç ve satndart sapmaları 0.001 dir.
#üretilen miller eğer 3.000+-0.002 inçaralığının dışında iseler hatalı kabul edilmektedirler.
#hatalı ürün miktasını bulunuz.
ustsinir=norm(loc=3.0005,scale=0.001).cdf(3.000+0.002)
altsinir=norm(loc=3.0005,scale=0.001).cdf(3.000-0.002)
olasilik10=1-(ustsinir-altsinir)#birden çıkardım çünkü hatalı ampüllerin bu alanın dışında olduğunu söylemiş hatalı ampülleri bulmak istiyoruz.
print(olasilik10)