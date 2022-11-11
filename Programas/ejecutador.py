import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

## Ejecuta los códigos 

os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')
lista = os.listdir()

for rho in lista:
    os.chdir(f'C://Users//pc//Desktop//Proyecto_AFE//rho_v//{rho}')
    os.system(f'gfortran DM_({rho}).f')
    os.system('a.exe')