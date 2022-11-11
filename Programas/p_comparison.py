import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

lista = ['0.1','0.55','0.9','1.0']

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.grid(linestyle='--', linewidth=0.7)
plt.title(r'\textbf{Comparación de g(r)}', fontsize = 15)
plt.ylim((0,5))
plt.xlim((0,3.1))
plt.xlabel(r'$ r $',fontsize = 15)
plt.ylabel(r'$ g(r) $', fontsize = 15)

def g(rho):
    r = np.array([])
    g = np.array([])
    with open(f"C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}//gr.dat") as gr:
        for line in gr:
            datos = line.split()
            r = np.append(r,float(datos[0]))
            g = np.append(g,float(datos[1]))
    plt.plot(r,g, label = r'$\rho = $ '+rho)

for rho in lista:
    g(rho)

plt.gcf().set_size_inches(5, 5)
plt.tight_layout()
plt.legend()
plt.savefig(f"C://Users//pc//Desktop//Proyecto_AFE//Resultados//p_comparison.png", dpi = 800)




