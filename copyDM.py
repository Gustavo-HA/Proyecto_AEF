import os

rho = os.listdir(r'C:\Users\pc\Desktop\Proyecto AFE\rho_v')

for i in rho:
    os.system(f'copy DM_3.f rho_v\{i}\DM.f')
    print(f'{i}')
