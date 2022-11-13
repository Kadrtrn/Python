import numpy as np 

#Bazılarını yazmadım kolay diye unutma

numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])

#1. indexdekilerin 2.index elemanını getirir
result=numbers2[:,2]

result=numbers2[2,2]

result=numbers2[:,0:2]
print(result)