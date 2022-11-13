import pandas as pd 
import numpy as np

data=np.arange(10,85).reshape(15,5)
df=pd.DataFrame(data,columns=['Column1','Column2','Column3','Column4','Column5'])
result=df

#Kolon isimlerini almak
result=df.columns
#İlk 5 kaydı çagırma
result=df.head()
#ilk 10 satırı almka 
result=df.head(10)
#satırları sonran almak içinde tail kullanılır 
result=df.tail()
result=df.tail(10)
#Belirli bir kolonun baştan belirli bir kısmını almak
result=df['Column1'].head(5)
#Aynısı su şekilde de yapılabilir 
result=df.Column1.head()
#Aşagıdaki gibi bir şeyde var unutma
result=df.Column1

result=df[['Column1','Column2']].head()
#Berlirli bir aralıktaki satırları seçmek
result=df[5:15][['Column1','Column2']]


#Filtreleme işlemleri 
#

#50den büyükler için true yazar
result=df >50
#sadece 50 den büyük kayıtları göstermek için
result=df[df>50]

result=df[df %2==0]

#İstediğimiz bir kolon üzerinden filtreleme yapmak 
result=df['Column1']>50
#Column1 in 50 den büyük oldugu kayıtlerı getirir diger kolonlar dahil 
result=df[df['Column1']>50]
#Yukardaki işlemde istedigimiz kolonları belirterek onları getirtebiliriz
result=df[df['Column1']>50][['Column1','Column2']]


result=df[(df['Column1']>50) & (df['Column2']<=70)]
#İki şarttan herhangi birini sağlayan kolonlar yazdırılacak
result=df[(df['Column1'] >50) | (df['Column2']<=20)][['Column1','Column2']]


#Koşul yazarken farklı bir yöntemimiz de var 
result=df.query('Column1 >=50 & Column1 %2==0').Column1


print(result)