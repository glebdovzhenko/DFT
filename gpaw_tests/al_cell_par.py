import numpy as np
from ase.build import bulk
from gpaw import GPAW, PW

a0 = 4.04
al = bulk('Al', 'fcc', a=a0)
cell0 = al.cell

for ecut in range(1100, 1501, 50):
    print('E-cut at %.01f eV' % ecut)
    al.calc = GPAW(mode=PW(ecut),
                   xc='PBE',
                   kpts=(8, 8, 8),
                   basis='dzp',
                   txt=f'Al-{ecut}.txt')
    for eps in np.linspace(-0.02, 0.02, 5):
        al.cell = (1 + eps) * cell0
        al.get_potential_energy()

# al.calc.set(mode=PW(400))
# for k in range(4, 17):
#     print('K-points: %.d' % k)
#     al.calc.set(kpts=(k, k, k),
#                 txt=f'Al-{k:02}.txt')
#     for eps in np.linspace(-0.02, 0.02, 5):
#         al.cell = (1 + eps) * cell0
#         al.get_potential_energy()