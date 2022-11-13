import numpy as np

#Numpy array

np_array= np.array([1,2,3,4,5,6,7,8,9])

#Matris oluşturma
np_multi =np_array.reshape(3,3)

print(np_multi)

#Boyut öğrenme

print(np_array.ndim)
print(np_multi.ndim)

#Kaça kaç matris olduğunu bulma
print(np_array.shape)
print(np_multi.shape)