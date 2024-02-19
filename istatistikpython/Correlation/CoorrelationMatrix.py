import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
veri=pd.read_excel(".\CORRMATRIS.xlsx")
print(veri)
kormat=veri.corr()
print(kormat)
sns.heatmap(kormat,annot=True,cmap=plt.cm.Blues)
plt.show()
p1=pg.pairwise_corr(veri)
print(p1)#buarada p ve r değerleri göreceksiniz.
#p değerleri0.05 ten küçü r değeriyle ilişkinin gücüne bakılır.
p2=pg.rcorr(veri,stars=False)
print(p2)#kçşegen üst kısmı p alt kısmı r değerlerini gösterir