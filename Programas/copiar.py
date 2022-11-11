## Copia y modifica el código original ajustandolo a los valores de densidad deseados

import os    
import numpy as np

valores = os.listdir(r'C:\Users\pc\Desktop\Proyecto_AFE\rho_v')
for rho in valores:
  lineas=[]
  with open("C://Users//pc//Desktop//Proyecto_AFE//DM_corregido.f") as codigo:
    for line in codigo:
      new_line = line
      check = line.split()
      if len(check)!=0:
        if check[0] == 'rho':
          check[2] = rho
          new_line = "\t" "\t" "\t" "\t"+check[0]+f" {check[1]}"+f" {check[2]}"+"\n"
      lineas = np.append(lineas,new_line)
  f = open("C://Users//pc//Desktop//Proyecto_AFE//rho_v//"+rho+f"//DM_({rho}).f","w")
  f.writelines(lineas)
  f.close()