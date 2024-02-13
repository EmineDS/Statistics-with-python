import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
veri=pd.read_excel(".\gübretohum.xlsx")
gubrea=veri[veri["Gübre"]=="a"]["Verim"]
gubreb=veri[veri["Gübre"]=="b"]["Verim"]
gubrec=veri[veri["Gübre"]=="c"]["Verim"]
gubre=[gubrea,gubreb,gubrec]
tohumx=veri[veri["Tohum"]=="x"]["Verim"]
tohumy=veri[veri["Tohum"]=="y"]["Verim"]
tohumz=veri[veri["Tohum"]=="z"]["Verim"]
tohumw=veri[veri["Tohum"]=="w"]["Verim"]

#HOMOJENLİK TESTİ YAPILIR
homojenlik=stats.levene(gubrea,gubreb,gubrec)
print(homojenlik)
homojenlik=stats.levene(tohumw,tohumz,tohumx)
print(homojenlik)
#varyanslar homojendir.
model="Verim~ C(Gübre)+C(Tohum)+C(Gübre):C(Tohum)"
test=ols(model,data=veri).fit()
anova=sm.stats.anova_lm(test,type=2)
print(anova)#PRF DEĞERİNE BAKILIR VE H0 HİPOTEZİNİ REDDEDEMEYİZ.