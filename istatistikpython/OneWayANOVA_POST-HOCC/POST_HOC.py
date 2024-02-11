#tukey testi kullanıcaktır(veryanslar eşit olduğu için)
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pingouin as pg
import scikit_posthocs as sp
veri=pd.read_excel(".\egitim_tv.xlsx")
print(veri)
#öncelikle verilerin normal dağılım gösterip göstermedğini kontrol etmeliyiz
g1=veri[veri["Eğitim"]=="İlkokul"]
g2=veri[veri["Eğitim"]=="Lise"]
g3=veri[veri["Eğitim"]=="Üniversite"]
g4=veri[veri["Eğitim"]=="Yükseklisans"]
#BU VERİ SETİNİN VARYANS VE NORMALLİK TESTLERİNİ ONE WAY ANOVA KISMINDA KONTROL ETTİK
testanova=stats.f_oneway(g1["Tvizleme"],g2["Tvizleme"],g3["Tvizleme"],g4["Tvizleme"])
print(testanova) #ANOVA TESTİ BİZE MİN İKİ GRUP ARASINDA FARK OLDUĞUNU GÖSTERDİ
#ANCAK HANGİ GRUPLAR ARASINDA FARK OLDUĞUNU GÖSTEREMEDİ POST HOC TESTİNİ BU YÜZDEN YAPIYORUZ.
#pairwise_turkeyhsd(tüm sayısal değerler(sürekli değişken değişken),tüm girdi değerleri,alpha=anlamlılık)
posthoc=pairwise_tukeyhsd(veri["Tvizleme"],veri["Eğitim"],alpha=0.05)
print(posthoc)#burada gelen matrixte tru döndürülen çitlerin arasında anlamlı bir fark olduğunu gösterir
#yani yükske lisans ile üniversite ve yüksek lisans ile ilk okul arasında anlamlı bir fark var
print(g4["Tvizleme"].mean(),g3["Tvizleme"].mean())
print(g4["Tvizleme"].mean(),g1["Tvizleme"].mean())
#aralarında anlamlı fark olaraın hangisinin fazla hangisinin az izlediğine ortalamalarına bakarak karar verdik
#baktığımızda yüksek lisan öğrencisi hem ilkokul hem de üniversite öğrencisinden daha az tv izliyor %95 oranla.
#**************************************************************************
#peki ya varyanslar homojen olmasaydı
#WELCH'IN ANOVA TESTİNİ uygulayacaktık
#dv=sürekli değişken
#between=gruplaar
#buarada başta dataya tüm data frame i gönderdiğimiz için diğer
#parametrelere sadece kolum adını yolladık
test=pg.welch_anova(data=veri,dv="Tvizleme",between="Eğitim")
print(test)
#evet burada H0 hipotezini yine reddettik yani anlamlı farklar var dedik.
#fakat yine detay alamadık bunun için başka bir post hoc testi kullanacağız(TAMHANE TESTİ)
tamhane=sp.posthoc_tamhane(veri,val_col="Tvizleme",group_col="Eğitim")
print(tamhane)
#tamhane matrisinde true false gibi bir değer yazmak yerine bize çapraz tablo döndürüyor.
#buarada değerlerin 0.05ten küçük olduğu kesişimlerdeki
# değerlerin arasında nalamlı bir farklılık var deriz