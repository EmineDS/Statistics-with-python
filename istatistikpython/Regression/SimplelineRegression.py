#bağımlı değişkenimiz bir aet olduğu için basit regresyon denir
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
pd.set_option('display.max_rows', None)
veri=sns.load_dataset("tips")
sns.regplot(x=veri["total_bill"],y=veri["tip"],ci=None)
sabit=sm.add_constant(veri["total_bill"])#sabit bağımsız değişkenden etkilenir
bagımlıdeg=veri["tip"]
plt.show()
model=sm.OLS(bagımlıdeg,sabit).fit()
print(model.summary())
#sabit değer için de iki var sayım vardır H0 ve H1 hipotezi H0 hipotezi sabit değer 0 a aşittir der
#yani varlığının bir önemi yoktur ve bir şey değiştirmez der
#H1 ise sabit değer 0 dan farklı ve anlamlıdır der.
#tablodaki p değeri 0.05 ten küçüse(95 güvenle çalıştığımızdan)h0 hipotezi reddedilir ve sabit anlamlıdır.
print(model.params)#sabit değeri ve x in katsayısını verir(regresyon denklemi için)
#genelde modelin parametrelerin tümü anlalıysa modelin kendisi de anlamlıdır.
#sonrasında modelanlamlılığı için f statistic in olasılık değerine bakarız . 0.05 ten küçükse model anlamlıdır.
#matrikstede gösterilen ve değişkenler arasındaki ilişki anlamlılık düzeyini
#gösteren R2 nin hesaplanma formülü
#genel kareler toplamı (GKT)= regresyon kareler toplamı (RKT)+HATA KARELER TOPLAMI (HKT)
#R2 DEĞERİ ASLINDA RKT/GKT dir ancak RKT bulıunması zor bir değer olduğundan ilk denkelemde yerine koyma metoduyla
#R2 denkelmeini 1-(HKT/GKT) yaparız
GKT=model.ess+model.ssr
HKT=model.ssr
print(1-(HKT/GKT))
#R2 adjustment değerine ise bağımsız değişken bir den fazlaysa bakılır çünkü birden fazla bağımsız değişken
#R2 güvenilirliğini azaltır.
