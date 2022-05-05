from ase import Atoms
from gpaw import GPAW
from ase.optimize import QuasiNewton
from ase.eos import EquationOfState
from ase.units import kJ
from ase.spacegroup import Spacegroup
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    a = 4.01  # AA
    al3ti = Atoms(
        symbols=['Al', 'Al', 'Al', 'Ti'],
        scaled_positions=[(0.0, 0.5, 0.5), (0.5, 0.0, 0.5), (0.5, 0.5, 0.0), (0.0, 0.0, 0.0)],
        cell=[a, a, a],
        pbc=True,
        info={
            'spacegroup': Spacegroup(221)
        }
    )

    # atomic position optimization
    # calc_PBE = GPAW(xc='PBE')
    # al3ti.set_calculator(calc_PBE)
    # relax = QuasiNewton(al3ti)
    # relax.run(fmax=0.001)
    #
    # print("RESULTS")
    # print(al3ti.get_cell())
    # print(al3ti.get_positions())

    # cell size optimization
    calc = GPAW(mode='pw', kpts=(12, 12, 12))
    al3ti.set_calculator(calc)

    v, e = [], []
    for x in np.linspace(0.9, 1.1, 5):
        al3ti.set_cell(x * np.array([a, a, a]))
        al3ti.set_scaled_positions([(0.0, 0.5, 0.5), (0.5, 0.0, 0.5), (0.5, 0.5, 0.0), (0.0, 0.0, 0.0)])

        v.append(al3ti.get_volume())
        e.append(al3ti.get_potential_energy())

    eos = EquationOfState(v, e, eos='birch')
    v0, e0, B = eos.fit()
    eos.plot('eos_Al3Ti.pdf')

    print('B =', B / kJ * 1.0e24, 'GPa')
    print('a =', v0 ** (1/3), 'AA')
