import pandas as pd
import pingouin as pg
#elimizde bir test öncesi ve test sonrası dataların listeti mevcut
#test öncesi ve sonrası arasında anlamlı bir fark olum olmadığına bakalım.
veri=pd.read_excel(".\hastatest.xlsx")
#data sayısı azolduğu için norn parametrik test uygulayacağız
print(veri)
fark=veri.TÖ-veri.TS
test=pg.normality(fark)
print(test)#p değeri 0.05 ten küçük olduğundan normal değil
test=pg.wilcoxon(veri.TÖ,veri.TS)
print(test)
#p değeri 0.05 ten büyük çıktığı için test öncesi ve test sonrası durumlarda anlamlı bir fark yoktur.