import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
data=pd.read_excel(".\otokorelasyon.xlsx")
print(data)
y=data["Y"]
x=data[["X1","X2","X3"]]
sabit=sm.add_constant(x)
model=sm.OLS(y,sabit).fit()
print(model.summary())

error=model.resid
sm.graphics.tsa.plot_acf(error)
plt.show()
lm=smd.acorr_breusch_godfrey(model,nlags=2)
print(lm[1])#p değeri 0.05 ten büyük otokorelasyonsorunu yoktur ancak ya var olsaydı?
#o zaman farklı bir yol kullanacaktık
model2=sm.OLS(y,sabit).fit(cov_type="HAC",cov_kwds={"maxlags":3})
print(model2.summary())
#görüldüğü gibi paremetrelein standart hataları değişmiş durumda.
#otokorelasyon durumu yani dubin watson değeri değişmese de otoorelasyonun modele
#olumsuz etkisi bu yöntemle engellenebilir.

