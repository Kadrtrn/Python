import pandas as pd 

from numpy.random import randn 

df=pd.DataFrame(randn(3,3),index=['A','B','C'], columns=(['Column1','Column2','Column3']))

#kolon seçme 
result=df['Column1']
#Tipii ögrenelim (pandas serisi)
result=type(df['Column1'])
#Çoklu kolon seçme
result=df[['Column1','Column2']]
#Satır seçme (pandas serisi olarak döner)
result=df.loc['A']
#iloc 0 dan saymaya başlar yazdıgımız indexteki satırı getirir
result=df.iloc[2]
result=type(df.loc['A'])
#loc kullanımı 
#-----loc['row  bilgisi','column bilgisi']
#-----loc['row bilgisi']
#-----loc[':','column bilgisi']
result=df.loc[:,'Column1']
result=df.loc[:,['Column1','Column2']]
#Belli bir aralıktaki kolonları seçmek yazılan kolonlar dahil
result=df.loc[:,'Column1':'Column3']
result=df.loc[:,:'Column3']
#Satırlarda da aralık belirtilebilir
result=df.loc['A':'C',:'Column3']
#Belli bir satırın belli bir sutündaki degerini almak 
result=df.loc['A','Column2']
result=df.loc['B','Column3']
#Birden fazla satır ve sutun yazabiliriz
result=df.loc[['A','B'],['Column1','Column2']]

#Yeni kolon eklemek
#df['Column4']=pd.Series(randn(3),['A','B','C'])

#Bu satırı kendim denedim böyle olacak mı diye 
dictt={'A':10,'B':40,'C':50}
df['Columns4']=pd.Series(dictt)

df['Column5']=df['Column1'] +df['Column3']

#Kolon silme axis 1 için y kordinatı yani yukardan aşagıya x kordinatı için 0 verilmeli
#Bu değişiklik gerçek veri seti içinde yapılmıyor bunu kullanabilmek için farklı bir değişkene atanıp kullanılabilir

df.drop('Column5',axis=1)
df_2=df.drop('Column5',axis=1)
print(df_2)
#Eger inplace true verirsek gerçek veri seti üzerinde de değişiklik yapılacak default değeri false

df.drop('Column5',axis=1,inplace=True)
 







result=df







print(result)




















