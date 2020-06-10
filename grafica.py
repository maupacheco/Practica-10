#Importando las bibiotecas
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

#Datos de entrada
x = linspace(0, 5, 20)  #Generando 10 puntos entre 0 y 5


fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, sin(x), marker="o", color="r", linestyle='None')

ax.grid(True)
ax.set_xlabel('X') #Etiqueta del eje x
ax.set_ylabel('Y') #Etiqueta del eje y
ax.grid(True)
ax.legend(["y = x**2"])

plt.title('Puntos')
plt.show()

fig.savefig("gráfica.png") #Guardando la gráfica