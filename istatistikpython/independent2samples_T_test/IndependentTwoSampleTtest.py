from scipy import stats
import pandas as pd
#bu okulda öğrencilerin sınav sonuçları karşılatırılmak isteniyor
#aynı öğrenciler olmadığı için bağımlı t test yerine bağımsız t test yapılır
#bu arkadaşlardan 9 ar örneklem alınır.
#H0 ana kitlehipotezi a okuluyla b okulu sınav ortalamaları arasında bir fark oladığını savunur
#H1 ise Ma =! Mb yi savunur
Aokul=[280,287,280,275,279,278,289,284,288]
Bokul=[281,274,270,273,276,273,281,282,284]
alfa=0.05
#burada iki örneklem arasındaki ilişkiyi test etmek istediğimiz için popmean yazmadık
thesap,p=stats.ttest_ind(Aokul,Bokul,alternative="two-sided")
print(thesap,p)

if p<alfa:
    print("H0 reddedilir")
else:
    print("H0 reddedilemez")