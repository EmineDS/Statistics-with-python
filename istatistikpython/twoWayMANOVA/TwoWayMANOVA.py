#birden fazla bağımı değişken iki bağımsız değişken
import pandas as pd
from statsmodels.multivariate.manova import MANOVA
import pingouin as pg
#elimizde mevki ve departmanları verilen çalışanların mevki ve departmanlarının
#performans ve sahiplenme üzerine istatistiksel olarak anlamlı bir etkisi var mı?
veri=pd.read_excel(".\departmandata.xlsx")
print(veri)
manova=MANOVA.from_formula("Performans+Sahiplenme~Mevki+Departman+Mevki:Departman",data=veri)
print(manova.mv_test())
#ikisinin de etkisi yok
#ama etkisi var olsaydı hangisi üzerinde varlık etki varsa postoc yapısı kullanmalıyız
posthoc1=pg.pairwise_tukey(data=veri,dv="Performans",between="Mevki")
posthoc2=pg.pairwise_tukey(data=veri,dv="Performans",between="Departman")
posthoc3=pg.pairwise_tukey(data=veri,dv="Sahiplenme",between="Mevki")
posthoc4=pg.pairwise_tukey(data=veri,dv="Sahiplenme",between="Departman")
print(posthoc1)
print(posthoc2)
print(posthoc3)
print(posthoc4)