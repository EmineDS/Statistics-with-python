from scipy import stats
#aynı sample üzerinden değişiklikten önce ve değişiklşikten sonra değerleri verilmiştir
#gerçekten istatistiksek bir fark olum olmadığını kontrol edeceğiz
#H0 fark yok hipotezidir ve p değerimizn 0.05 değerinden büyük olduğu durumlarda reddedileemz gerçek olur
#h1 ise fark var hipotezidir eğer p değeri 0.05 ten küçük olursa H0 hipotezi rededilir ve H1
#değerlendirmeye alınır
once=[280,287,280,275,279,278,289,284,288]
sonra=[281,274,270,273,276,273,281,282,284]
test=stats.ttest_rel(once,sonra,alternative="two-sided")
print(test)