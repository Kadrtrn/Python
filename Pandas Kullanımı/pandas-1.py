import pandas as pd 

numbers=[20,30,40,50]

letters=["a","b","c","d",20]

scalar=5
#pandas serisi oluşturma
pandas_series = pd.Series(numbers)
pandas_series=pd.Series(letters)
pandas_series=pd.Series(scalar)

#veridiğimiz değeri istediğimiz indexe veya istediğimiz key bilgisine aktarmak
#İkinci kısım index değerleri
pandas_series=pd.Series(5,[0,1,2,3,4])
pandas_series=pd.Series(numbers,["a","b","c","d"])

dic={'a':10,'b':20,'c':30,'d':40}

pandas_series=pd.Series(dic)

import numpy as np
random_numbers=np.random.randint(10,100,6)

pandas_series=pd.Series(random_numbers)

pandas_series=pd.Series([20,30,40,50],['a','b','c','d'])

result=pandas_series[0]
result=pandas_series['a']
result=pandas_series[['a','c']]

#listenin kaç boyutlu olduğunu öğrenme
result=pandas_series.ndim
#veri tipini öğrenme
result=pandas_series.dtype
#listenin kaça kaçlık olduğunu öğrenmek 
result=pandas_series.shape

#liste değerlerini toplamak 
result=pandas_series.sum()
result=pandas_series.max()
result=pandas_series.min()

result=pandas_series +pandas_series
result=pandas_series + 50

result=np.sqrt(pandas_series)

result=pandas_series >=50

result= pandas_series %2 == 0

#şartları saglayan sayıları-indexleri yazdırmak


#print(pandas_series[result])
#veya
#print(pandas_series[pandas_series %3==0])





#print(pandas_series)
#print(result)



opel2018=pd.Series([20,30,40,50],['astra','corsa','mokka','insignia'])
opel2019=pd.Series([40,30,20,10],['astra','corsa','grandland','insignia'])

total=opel2018+ opel2019
print(total)
print(total['astra'])














#adfdsfasdf