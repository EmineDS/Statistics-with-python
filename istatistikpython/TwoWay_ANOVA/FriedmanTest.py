import pandas as pd
import pingouin as pg
from scikit_posthocs import posthoc_conover_friedman
import numpy as np
veri=pd.read_excel(".\hastaçoktest.xlsx")
print(veri)
veri2=pd.melt(veri,id_vars=["Hastalar"],value_vars=["TÖ","TS","TS2","TS3"])
veri2.columns=["Hastalar","Testler","Değerler"]
print(veri2)
normallik=pg.normality(veri2,dv="Değerler",group="Testler")
print(normallik)
#ikisi normal dağılım gösteriyor sadece.
#küreselliğe de bakabilirdik ama zaten normallik varsayımını karşılamadığı için
#çok da bakmamıza gerek yok.
#non parametrik test için friedman testini kullanalım
test=pg.friedman(veri2,dv="Değerler",within="Testler",subject="Hastalar")
print(test)#teste göre aralarında fark yoktur.
#Eğer fark olsaydı ne olacaktı? post hoc testi kullanacaktım
df=np.array([veri.TÖ,veri.TS,veri.TS2,veri.TS3])
posthoc=posthoc_conover_friedman(df,p_adjust="bonf")
print(posthoc)