import matplotlib.pyplot as plt
import numpy as np 

x=np.linspace(-10,9,20)
y=x**3
z=x**2


"""
figure=plt.figure()

#sayfanın yüzde 10 sagında asagıdan yüzde 10 yukarsa yüzde 80 yüksekliğinde yüzde 80 genişliğinde
axes_cube=figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel('X axis')
axes_cube.set_ylabel('Y axis')
axes_cube.set_title('Cube')


axes_square=figure.add_axes([0.15,0.6,0.25,0.3])
axes_square.plot(x,y,'red')
axes_square.set_xlabel('X axis')
axes_square.set_ylabel('Y axis')
axes_square.set_title('Square')
"""

"""
figure=plt.figure()

axes=figure.add_axes([0,0,1,1])

axes.plot(x,z,label='Square')
axes.plot(x,y,label='Cube')
#default ve 2 sol üst  1 sağ üst 3 sol alt 4 sağ alt  
axes.legend(loc=2)
"""

#nrows ve ncols yazmak gerekli değil direkt sayılar yazılabilir
#figsize gösterilcek x ve y değerlerini belirler
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))

axes[0].plot(x,y)
axes[0].set_title('Cube')
axes[1].plot(x,z)
axes[1].set_title('Square')



plt.tight_layout()

#Figurü kaydetmek pdf şeklinde de kaydedilebilir 
fig.savefig('figure1.png')
 
plt.show()
































