import pandas as pd
from scipy import stats
veri=pd.read_excel("C:\\Users\edisa\Desktop\calisandegisim.xlsx")
print(veri)
#bir grup öğrenciye sınav yapılıyor
# dersten önce ve sonra olmaz üzere iki şekilde sınav yapılıp başarı puanları şinceleniyor
once=veri["ÖNCE"]
sonra=veri["SONRA"]
print(once)
print(sonra)
#normal dağılımı test et
#bağımlı örneklemde normallik testi yapıyorsak iki örneklemin verilerini birbirinden çıkarıyoruz.
#bu farkı normal dağılım testine gönderiyoruz
fark=once-sonra
print(fark)
normallik=stats.shapiro(fark)#p değeri 0.05 ten büyük olduğu için H0 nromallik hipotezi reddedilemez
print(normallik)
#VARYANSLARIN HOMOJENLİĞİ TESTİ
varyans=stats.bartlett(once,sonra)
print(varyans)
#p değeri 0.05 değeirnden büyük olduğu için varyansların homojenliği kabul edilir
test=stats.ttest_rel(once,sonra)
print(test)
#gelişirdiğimiz bir motor yağının yakıt tüketi konusunda bir fark yaratacağının düşünüyoruz
ver=pd.DataFrame()
veri["once"]=[8.003467,5.8575,6.16466,7.6557,7.494,7.027,7.119,6.646,6.824,8.860]
veri["sonra"]=[5.311,8.03,8.283,6.939,8.473,8.004,6.401,5.2,7.271,7.115]
fark=veri["once"]-veri["sonra"]
normallik=stats.shapiro(fark)
print(normallik)
homojen=stats.bartlett(veri["once"],veri["sonra"])
print(homojen)
test=stats.ttest_rel(veri["once"],veri["sonra"])
print(test)