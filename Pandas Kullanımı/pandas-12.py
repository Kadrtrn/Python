import pandas as pd 
import numpy as np


data={
      'Column1':[1,2,3,4,5],
      'Column2':[10,20,13,20,25],
      'Column3':['abc','bcaa','ade','cb','dea']
      }


df=pd.DataFrame(data)

result=df
#Herhangi bir kolonDAKİ her bilgiyi sadece bir kere  almak 
result=df['Column2'].unique()
#Yukarda dönenlerin sayısını almak
result=df['Column2'].nunique()
#İlgili sutun içerisinde her bir elemanın kaç kere tekrarlardıgını bulmak
result=df['Column2'].value_counts()
#Column1 deki elemanların hepsini ikiyle çarpmak
result=df['Column1']*2


#Fonksiyonları uygulayan apply fonksiyonu


def kareal(x):
    return x*x

#Kareal fonksiyonunu her bir eleman için uygulayacak
result=df['Column1'].apply(kareal)

kareal2=lambda x:x*x
result=df['Column1'].apply(kareal2)
#Şu şekilde de yapılabilir
result=df['Column1'].apply(lambda x:x*x)

#Karekter sayılarını bulmak 
#Column3deki elemanların karakter sayılarını döndürür
result=df['Column3'].apply(len)



#Sutun bilgilerini almak
result=df.columns
result=len(df.columns)
#İndex bilgilerini almak
result=df.index
result=len(df.index)

#Detaylı bilgi verir
result=df.info

#DataFrame kolon 2 ye göre sıralanır   küçükten büyüğe
result=df.sort_values('Column2')
#Alfabetik sıralanır 
result=df.sort_values('Column3')
#ascending false verirsek tersi şekilde sıralar
#Büyükten küçüğe sıralar
result=df.sort_values('Column2',ascending=False)
#Alfabeye göre tersten sıralar 
result=df.sort_values('Column3',ascending=False)


print(result)



data={
      'Ay':['Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan'],
      'Kategori':['Elektronik','Elektronik','Elektronik','Kitap','Kitap','Kitap','Giyim','Giyim','Giyim'],
      'Gelir':[20,30,15,14,32,42,12,36,52]
      }
data=pd.DataFrame(data)


print(data)

#Yukardaki DataFrame'i yeniden düzenlemek
print(data.pivot_table(index='Ay',columns='Kategori',values='Gelir'))







































