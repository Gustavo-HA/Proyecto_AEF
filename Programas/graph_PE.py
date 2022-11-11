import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special
from math import *
import os

os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')
lista = os.listdir()
pressure = []
energy = []
p = np.array(lista)
p = p.astype(float)


for rho in lista:
    r = []
    gr = []
    with open(f"C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}//gr.dat") as grdata:
        for line in grdata:
            data = line.split()
            r = np.append(r,float(data[0]))
            gr = np.append(gr,float(data[1]))
    u = ((1/r)**(12)-2*(1/r)**(6)) #Adimensional, potencial/epsilon = u / profundidad de pozo de potencial
    u_r = 12*((1/r)**(7)-(1/r)**(13))
    E_f = u*gr*(r**2)
    P_f = u_r*r*gr
    I_e = integrate.simpson(E_f,r)
    I_p = integrate.simpson(P_f,r)
    # Energía normalizada E' = E / KTN
    E_normalizada = 3/2 + (2*pi*I_e*float(rho))
    energy = np.append(energy, E_normalizada)
    # Presión normalizada P' = P/pKT
    P_normalizada = 1 - (2/3)*pi*float(rho)*I_p
    pressure = np.append(pressure,P_normalizada)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.grid(linestyle='--', linewidth=0.7)
plt.plot(p,energy, label = r'$E = E(\rho)$',c = '#FFD1DC')
plt.plot(p,pressure, label = r'$P = P(\rho)$',c = '#d29bfd')
plt.xlabel(r'$\rho$',fontsize = 15)
plt.xlim((min(p),max(p)))
plt.title(r'\textbf{Energía, presión vs densidad}', fontsize = 15)
plt.legend(loc = 'upper right', bbox_to_anchor=(0.9, 0.9), fontsize = 12)
plt.gcf().set_size_inches(5, 5)
plt.tight_layout()
plt.savefig(f"C://Users//pc//Desktop//Proyecto_AFE//Resultados//graph_PE.png", dpi = 800)
