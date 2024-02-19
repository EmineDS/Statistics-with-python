import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
import seaborn as sns
veri=pd.read_excel(".\\ap_sperman.xlsx")
print(veri)
#normallik varsayımını kontrol edelim
#normallik testi yapalım
normallik=pg.normality(veri)
print(normallik)#A normalken B değil
#normal olsaydı doğrusallığı kontrol edecektik
#doğrusalllık varsayımını kontrol edelim
sns.lmplot(x="A",y="B",data=veri)
#burası aynı zamanda bize güven aralığı da veriyor. değerler güven aralığının dışında kaldıysa
#veriler o kadar da doğrusal değil.
plt.show()
#spearmen ın korelasyon testini yapmamız lazım ama pearson a da bir bakalım.
pkor=pg.corr(veri["A"],veri["B"],method="pearson")
skor=pg.corr(veri["A"],veri["B"],method="spearman")
print(pkor)
print(skor)
#korelasyon testind r değerlerine bakılır. negatif korelasyon var