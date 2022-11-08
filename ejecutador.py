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
    plt.plot(r,g, label = r'$\rho = $ '+rho)
    plt.xlabel(r'Distancia radial r',fontsize = 15)
    plt.ylabel(r'Probabilidad', fontsize = 15)
    plt.title(r'\textbf{Función de distribución radial}', fontsize = 15)
    plt.legend()
    plt.savefig(f"C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}//g(r)_({rho}).png", dpi = 800)
    plt.clf()

## Ejecuta los códigos y saca gráficas

os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')
lista = os.listdir()

for rho in lista:
    os.chdir(f'C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}')
    os.system(f'gfortran DM_({rho}).f')
    os.system('a.exe')
    g(rho)
