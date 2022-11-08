import os
import numpy as np

os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')

nd = np.arange(0.1,1,0.05)
nd = np.round(nd,2)

for i in nd:
    os.system(f'md {i}')
    os.chdir(f'C://Users//pc//Desktop//Proyecto_AFE//rho_v//{i}')
    os.system('type nul > .gitignore')
    os.chdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')