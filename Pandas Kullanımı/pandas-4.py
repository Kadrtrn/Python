import pandas as pd 

#csv dosyasını okumak
#df=pd.read_csv('sample.csv')

#df=pd.read_json('sample.json')

#!!!!!excel okumak için xlrd kütüphanesi kurulması gerekiyor 

df=pd.read_excel("sample.xlsx")

#Bu kısmı kendim ekledim index sayılarını kendim verebilmek için
data=pd.DataFrame(df,index=(1,2,3))
print(data)