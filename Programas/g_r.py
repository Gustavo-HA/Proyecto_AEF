import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

## Función g(r) gráfica única
def g(rho):
    r = np.array([])
    g = np.array([])
    with open(f"C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}//gr.dat") as gr:
        for line in gr:
            datos = line.split()
            r = np.append(r,float(datos[0]))
            g = np.append(g,float(datos[1]))

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.grid(linestyle='--', linewidth=0.7)
    plt.plot(r,g,c='b', label = r'$\rho = $ '+rho)
    plt.ylim((0,max(g)+1))
    plt.xlim((0,max(r)))
    plt.xlabel(r'$ r $',fontsize = 15)
    plt.ylabel(r'$ g(r) $', fontsize = 15)
    plt.legend(loc = 'upper right', bbox_to_anchor=(0.9, 0.9), fontsize = 12)
    plt.gcf().set_size_inches(5, 5)
    plt.tight_layout()
    plt.savefig(f"C://Users//pc//Desktop//Proyecto_AFE//Resultados//g(r)_({rho}).png", dpi = 800)
    plt.clf()
    
## Saca gráficas

os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')
lista = os.listdir()

for rho in lista:
    os.chdir(f'C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}')
    g(rho)