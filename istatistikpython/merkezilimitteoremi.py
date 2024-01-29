import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random
#MERKEZİ LİMİT TEOREMİ
yas=np.random.uniform(low=18,high=75,size=40000)
#1000 kere kırk örnemklem ortalamaları alınıp listeye atıldı
orneklem=[np.mean(random.choices(yas,k=40)) for _ in range(1000)]
#çekilen orneklemin ortalamalarının dağılımı
print(orneklem)
sns.histplot(orneklem)
plt.show()
