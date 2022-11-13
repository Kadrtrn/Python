import pandas as pd 
import numpy as np 

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])

#İndexleri yeniden veriyoruz boş olan kısımlar NaN dönecek
df=df.reindex(['a','b','c','d','e','f','g','h'])
result=df

#İşimize yaramayacak bir sutunu bu şekilde silebiliriz
result=df.drop('column1',axis=1)
#Sutunları çoklu silmek
result=df.drop(['column1','column2'],axis=1)
#Satır silmek 
result=df.drop('a',axis=0)
result=df.drop(['a','b','h'],axis=0)

#NaN olan yerleri true döndürmek
result=df.isnull()

#NaN olmayanları True döndürmek
result=df.notnull()
#NaN değerleri saydırma
result=df.isnull().sum()
result=df['column1'].isnull().sum()

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4']=newColumn

#column1 de NaN olan değerleri getirmek
result=df[df['column1'].isnull()]
result=df[df['column1'].isnull()]['column1']

#NaN olmayanları getirme
result=df[df['column1'].notnull()]

#Bir satırda null değer varsa o satırı tamamen silmek

result=df.dropna()#axis değeri default olarak 0
#Bir sutunda null varsa o sutunu tamamen silmek
result=df.dropna(axis=1)

result=df.dropna(how='any')# satırda her hangibir null varsa o satırı tamamen siler
#Satır tamamen null ise o satırı getirmez
result=df.dropna(how='all')

#Özel olarak sutün belirtmek 
#sadece column1 ve column2 nin aynı satırlarında null degeri olan satırları getirmez
result=df.dropna(subset=['column1','column2'],how='all')
#column1 veya column2 nin herhangi bir satırında null varsa o satırı tamamen siler 
result=df.dropna(subset=['column1','column2'],how='any')
#satırda en az 2 değer varsa o satırı silme
#axis=1 verilerek sutun içinde uygulanabilir
result=df.dropna(thresh=2)

#Boş yerleri doldurmak

result=df.fillna(value='no input')
result=df.fillna(value=1)
print(df)


#Bu satırı kendim yazdım 
result=df['column1'].fillna(value=(df['column1'].mean()))

print(result)

























