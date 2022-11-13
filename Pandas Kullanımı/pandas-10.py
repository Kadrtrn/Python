import pandas as pd

data=pd.read_csv('nba.csv')
#!!!!!!!!!!!!!!!Normal STRİNG FONKSİYONLARI BURADA DA KULLANILIYOR UNUTMA!!!!!!!!
data.dropna(inplace=True)
#String Fonksiyonları 
#Name kolonundaki bütün harfleri büyük yapmak 
#data['Name']=data['Name'].str.upper()

#bütün harfleri küçük yapmak 
#data['Name']=data['Name'].str.lower()

#A karakterlerinin Name kolonunda hangi indexte oldugunu index adlı yeni kolona yazar a karakteri yoksa -1 yazar
#data['İndex']=data['Name'].str.find('a')

#Name kolonu içinde jordan yazanları bulmak 
#True False olarak döner 
#data=data.Name.str.contains('Jordan')
#Name içinde Jordan olan kayıtları getirmek
#data=data[data.Name.str.contains('Jordan')]
#Team sutunundaki boşlukları çizgi ile değiştirdik 
#data=data.Team.str.replace(' ','-')

#Name kolonunu Fisrtname ve Lastname olarak ikiye ayırmak ama sadece bir ismi ve soyismi olanlar için 
data[['FirstName','Lastname']]=data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)
print(data.head(10))