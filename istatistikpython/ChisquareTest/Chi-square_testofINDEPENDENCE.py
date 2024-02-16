import pandas as pd
from scipy import stats
#********************************2x2 FREKANS TABLOSU İÇİN ********************************************
veri=pd.read_excel(".\cinsiyetel.xlsx")
print(veri)
tablo=pd.crosstab(index=veri["Cinsiyet"],columns=veri["El"])
print(tablo)
test,p,sd,bekledeg=stats.chi2_contingency(tablo)
print(bekledeg)#beklenen değer hangi testi uygulayacağımızı bulmam için çok önemli
#en küçük beklenen değer 5 ile 25 arasında olduğu için yatesin düzeltmesi kullanılır.
#ancak pearsonun testine de varsayımını sağlıyormuş gibi bakalım.
test,p,sd,bekledeg=stats.chi2_contingency(tablo,correction=False)
#burada tamamen aynı test sadece correction parametresi gönderdik. pearsonun testi için correction parametresi
#false olarak yazılır. yatesin testi için ise bu parametreye True değerini
#gireceğiz
print(test,p)#elimdeki veri setinin p değerinin 0.05 ten büyük çıkması
#h0 hipotezini reddederiz.
#sonucunda el ve cinsiyet arasında bir ilişki yoktur.
#ANCAK UNUTMAYALIM BU PEARSON TESTİNİN SONUCU BİZİM YATES TESTİNİ KULLANMAMIZ GEREKİYORDU.
test,p,sd,bekledeg=stats.chi2_contingency(tablo,correction=True)
print(test,p)#p değeri farklı ıksa da 0.05 ten büyük olduğu gerçeği
#değişmedi yani H0 hipotezimizi hala reddedemiyoruz.
#iki frekans tablosu arasında bir ilişki yoktur.
#PEKİ YA EN KÜÇÜK BEKLENEN DEĞER 5 TEN KÜÇÜK OLSAYDI;
#fisher'in ki kare testini uygulayalım
test=stats.fisher_exact(tablo)
print(test)
#*****************************************************************************************************
#********************************RxC FREKANS TABLOSU İÇİN ********************************************
veri=pd.read_excel(".\cinsiyetmarka.xlsx")
tablo=pd.crosstab(index=veri.Cinsiyet,columns=veri.Marka)
print(tablo)
#amacımız cinsiyet ve marka arasında bir ilişki var mıdır yok mudur buna bakmak
test,p,sd,beklenen=stats.chi2_contingency(tablo)
print(beklenen)
kucuk=[]
toplam=[]
for i in beklenen:
    for x in i:
        toplam.append(x)
        if x<5:
            kucuk.append(x)
print(len(kucuk)/len(toplam))#%87 nin beşten küçük beklenen frekansa sahip olduğunu bulduk
#yani fisher testini kullanmamız gerekecek.
#ancak yine de peorsan'un testini de görelim
test,p,sd,bekledeg=stats.chi2_contingency(tablo,correction=False)
print(test,p)
#peorsan testine göre marka ve cinsiyet arasında bir bağıntı yoktur.
#FİSHER TESTİNİN PYTHONDA BİR FONKSİYONU YOK R DİLİNDEN YARARLANILIYOR.
#ANCAK GENELDE BU KADAR KÜÇÜK VERİLERE İHTİYACINIZ OLMAYACAĞI İÇİN FİSHER TESTİNİ KULLANMAZSINIZ.