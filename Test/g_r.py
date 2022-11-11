import numpy as np
import matplotlib.pyplot as plt

r = []
g = []

with open("gr.dat") as coord:
    for linea in coord:
        datos = linea.split()
        r = np.append(r,float(datos[0]))
        g = np.append(g,float(datos[1]))

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.grid(linestyle='--', linewidth=0.7)
plt.plot(r,g,c='b', label = r'$\rho = $ 0.9')
plt.ylim((0,max(g)+1))
plt.xlim((0,max(r)))
plt.xlabel(r'$ r $',fontsize = 15)
plt.ylabel(r'$ g(r) $', fontsize = 15)
plt.legend(loc = 'upper right', bbox_to_anchor=(0.9, 0.9), fontsize = 12)
plt.gcf().set_size_inches(5, 5)
plt.tight_layout()
plt.savefig('g.png')
