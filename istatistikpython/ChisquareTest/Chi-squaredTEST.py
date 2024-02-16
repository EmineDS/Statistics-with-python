import pandas as pd
from scipy import stats
veri=pd.read_excel(".\kilofrekans.xlsx")
print(veri)
frekans=pd.value_counts(veri["Kilo"])
print(frekans)
kikare,p=stats.chisquare(frekans)
print(kikare,p)