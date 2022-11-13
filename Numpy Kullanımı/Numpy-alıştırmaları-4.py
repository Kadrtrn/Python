import numpy as np 

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

#aynı indexdeki elemanları toplamak
result=numbers1 + numbers2
#her indexe 10 ekleme 
#çıkarmada yapılabilir
result =numbers1 +10
#çarpma
result =numbers1*numbers2
# bölme 
result=numbers1/numbers2
#sayı ile de bölünüp çarpılabilir

#her indexdeki elemanların sin ve cosünü almak

result=np.sin(numbers1)
result=np.cos(numbers1)
#her indexin karekökünü almak
result=np.sqrt(numbers1)
#logaritma almak 
result=np.log(numbers1)

mnumbers1=numbers1.reshape(2,3)
mnumbers2=numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)
#2.matrisi 1.nin hemen sonuna eklemek 
result=np.vstack((mnumbers1,mnumbers2))
#2.matrisi 1. matrisin sağ tarafıan dogru eklemek 
result=np.hstack((mnumbers1,mnumbers2))

#50 den büyük sayıları arar ve boolen döner
result=numbers1>=50

result=numbers1 %2 == 0

#resulttan true dönen indexleri yazırmak
print(numbers1[result])

print(result)




















##sasas