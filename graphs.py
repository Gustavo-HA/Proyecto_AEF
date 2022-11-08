import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

r = np.array([])
g = np.array([])

with open("C:/Users/pc/Desktop/PROYECTO AFE/gr.dat") as gr:
    for line in gr:
        datos = line.split()
        r = np.append(r,float(datos[0]))
        g = np.append(g,float(datos[1]))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(r,g, label = r'$g(r)$', c= 'k')
plt.xlabel(r'Distancia radial r',fontsize = 15)
plt.ylabel(r'Probabilidad', fontsize = 15)
plt.title(r'\textbf{Función de distribución radial}', fontsize = 15)
plt.legend()
plt.show()


