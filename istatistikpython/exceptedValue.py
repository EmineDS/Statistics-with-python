from scipy import stats
import scipy.integrate
#zar için beklenen değeri bulalım
x=[1,2,3,4,5,6]#olasılık değerleri
p=[1/6,1/6,1/6,1/6,1/6,1/6]#olasılıkları
#kesikli bir olasılıkta beklenen değeri bulmak için rv_discrete kullanırız
beklenendeg=stats.rv_discrete(values=([x],[p])).expect()
print(beklenendeg)
#sürekli continuous değişken için beklenen değeri bulmak için integral alma kullanılır
def f(x):
    return (3/7)*x**3
#scipy.integrate.quad tek dereceli integral almak için kullanılan fonksiyon(fonksiyon,integralin üst sınırı,integralin alt sınırı)
beklenendeg=scipy.integrate.quad(f,1,2)
print(beklenendeg)#ilk yazdırılan değer beklenen değerdir
