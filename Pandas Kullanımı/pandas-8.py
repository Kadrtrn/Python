import pandas as pd 

personeller={
    'Çalışan':['Ahmet Yılmaz','Can Ertük','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertük','Mustafa Can'],
    'Departman':['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş':[30,25,45,50,23,34,42],
    'Semt':['Kadiköy','Tuzla','Maltepe','Tuzla','Kadiköy','Tuzla','Maltepe'],
    'Maaş':[5000,3000,4000,3500,2750,6500,4500]
    }

df=pd.DataFrame(personeller)

result=df
#Maaşların toplamı
result=df['Maaş'].sum()
#Departmanları gruplandırarak bize döndürür
result=df.groupby('Departman').groups
#Hem departman hem de semtleri gruplandırma
result=df.groupby(['Departman','Semt']).groups

#Setmlere göre gruplandırmayı yazdırma
#for name,group in df.groupby('Semt'):
 #   print(name)
  #  print(group)


#Yapılan gruplandırma içerisinden isteğimiz grubu almak 
#Semtler grubundan kadiköy olanları seçmek
result=df.groupby('Semt').get_group('Kadiköy')

#Yaş ve maaşların toplamını döndürecek
result=df.groupby('Departman').sum()
#Muhasebedekilerin maaş bilgilerini görmek
result=df.groupby('Departman').get_group('Muhasebe')['Maaş']

#ortalama bulmak 

result=df.groupby('Departman').mean()

result=df.groupby('Departman').get_group('Bilgi İşlem').mean()

#Kendi denedigim bir kod bilgi işlemdekilerin sayısını verdi 
result=len(df.groupby('Departman').get_group('Bilgi İşlem'))

result=df.groupby('Departman')['Maaş'].mean()

#Semtlere göre çalışan sayısını alalım 
result=df.groupby('Semt')['Çalışan'].count()

#Departmana göre maximum yaş bilgisi almak 
result=df.groupby('Departman')['Yaş'].max()
result=df.groupby('Departman')['Yaş'].min()

#Muhasebe bölümündeki max maaşı yazdırmak 
result=df.groupby('Departman')['Yaş'].max()['Muhasebe']

import numpy as np 

#agg fonksiyonu içerisinde işlmeler yapılabilir
result=df.groupby('Departman').agg(np.mean)

result=df.groupby('Departman').agg([np.sum,np.mean,np.max,np.min])

#Hesaplamaların sadece muhasebe için kulllanılması 
result=df.groupby('Departman')['Maaş'].agg([np.sum,np.mean,np.max,np.min]).loc['Muhasebe']
print(result)