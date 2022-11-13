import numpy as np 
#10 dan 100 e 3 artış miktralı array oluşturma 100 dahil değil 
result = np.arange(10,100,3)
#sadece 0 lardan oluşan array 
result=np.zeros(10)
#1lerden oluşan bir dizi
result=np.ones(10)
#başlangıç ve bitiş degerini eşit aralıklarla bölüp dizi oluşturma
result=np.linspace(0,100,5)

result = np.random.randint(0,10)
#rastgele üretilcek sayıların sayını seçme
result =np.random.randint(0,10,3)

#0 ile bir arasında belirtilen kadar sayı üretme
result = np.random.rand(5)
# eksi sayılarıda dahil etmek 
result =np.random.randn(5)

np_array=np.random.randint(0,50,9)
np_multi=np_array.reshape(3,3)
#Satırların toplamı
#print(np_multi.sum(axis=1))
#Sütunların toplamı
#print(np_multi.sum(axis=0))

rnd_numbers=np.random.randint(1,100,10)
#print(rnd_numbers)

result=rnd_numbers.max()
result=rnd_numbers.min()
result=rnd_numbers.mean()

#Dizi içerisindeki en büyük ve en küçük sayıların index numaralarını almak

result=rnd_numbers.argmax()
result=rnd_numbers.argmin()

#print(result)


#Bir şey denediğim bir kod
sample=np.random.randint(10,100,9).reshape(3,3)
print(sample)

maks=sample.max()
print(maks)
maks_index=sample.argmax()
print(maks_index)
sample_mean=sample.mean()
print(sample_mean)










