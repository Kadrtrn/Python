import pandas as pd 


#Ufak bir gösterim
#s1=pd.Series([3,2,0,1])
#s2=pd.Series([0,3,7,2])
#data=dict(apples= s1,orange =s2)
#df=pd.DataFrame(data)
#print(df)


#df=pd.DataFrame()
#df=pd.DataFrame([1,2,3,4])
#df=pd.DataFrame([['Ahmet',50],['Ali',60],['Yağmur',70],['Çınar',80]])




#data=[['Ahmet',50],['Ali',60],['Yağmur',70]]
#Sutün isimleri eklemek index numaralarınıda değiştirebiliriz 0 dan değilde 1 den başlatabiliriz
#dtype ile data tipinide girebiliriz aşagıda float yapalım 
#df=pd.DataFrame(data,columns=['Name','Grade'],index=[1,2,3],dtype=float)


#Yukardaki dataframe i sözlük yapısı ile oluşturalım 
#dictt={'Name':['Ahmet','Ali','Yağmur','Çınar'],
#       'Grade':[50,60,70,80]
 #      }
#Eğer istersek index bilgilerini hala değiştirebiliriz yukardaki gibi 
#df=pd.DataFrame(dictt)

#Sözlük içindeki her bit satırın dataframede de bir satıra karşılık gelecek şekilde yazılması yukarıdakinin aynısı dönecek

dictt=[
       {'Name':'Ahmet','Grade':50},
       {'Name':'Ali','Grade':60},
       {'Name':'Yağmur','Grade':70},
       {'Name':'Çınar','Grade':80},
       
       ]
df=pd.DataFrame(dictt,index=[222,234,123,423])
print(df)


























