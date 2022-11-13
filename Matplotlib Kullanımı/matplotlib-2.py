import matplotlib.pyplot as plt
import numpy as np

"""
x=[1,2,3,4]
y=[1,4,9,16]

#Grafiği oluşturur
#renk ve kalınlık gibi özellikler verilebilir 
#plt.plot(x,y,color='red',linewidth='5')
#daha farklı kullanım şelilleri için websitesine bak
#sıralama markerk çizgi tipi ve renk şeklinde olmalı hepsini vermek zorunlu değil
plt.plot(x,y,'o--g')
# x ve ye aralığını belirlememek
#ÖNCE X ARALIGI SONRA Y ARALIGI VERİLİR
plt.axis([0,6,0,20])

#ism vermek 

plt.title('Grafik Başlığı')
plt.xlabel('X label')
plt.ylabel('Y label')
"""

"""
x=np.linspace(0,2,100)


plt.plot(x,x,label='linear',color='red')
plt.plot(x,x**2,label='quadratic',color='yellow')
plt.plot(x,x**3,label='cubic',color='green')


plt.title('Simple plot')
"""


"""
#birden fazla grafik yapmak
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2)

axs[0].plot(x,x,'red')
axs[0].set_title('lineer')
axs[1].plot(x,x**2,color='green')
axs[1].set_title('quadratic')

#başlıkların sayılarlarla biribirine girmesini engellemek
plt.tight_layout()
"""
"""
#2 satır 2 sutün şeklinde grafikleri dizmek 
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2)


axs[0,0].plot(x,x,color='red')
axs[0,1].plot(x,x**2,color='red')
axs[1,0].plot(x,x**3,color='red')
axs[1,1].plot(x,x**4,color='red')
fig.suptitle('Grafik Başlığı')
""""


plt.show()

















































#aasassa