import matplotlib.pyplot as plt
import numpy as np

from ase.eos import EquationOfState
from ase.io import read


def fit(filename):
    configs = read(filename + '@:')
    volumes = [a.get_volume() for a in configs]
    energies = [a.get_potential_energy() for a in configs]
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    return (4 * v0)**(1 / 3.0)


if __name__ == '__main__':
    cutoffs = range(200, 1501, 50)
    a = [fit(f'Al-{ecut}.txt') for ecut in cutoffs]
    plt.figure(figsize=(6, 4))
    plt.plot(cutoffs, a, 'o-')
    plt.plot(cutoffs, [np.mean(a)] * len(cutoffs), '--')
    plt.axis(ymin=4.03, ymax=4.05)
    plt.xlabel('Plane-wave cutoff energy [eV]')
    plt.ylabel('lattice constant [Ang]')

    kpoints = range(4, 17)
    plt.figure(figsize=(6, 4))
    a = [fit(f'Al-{k:02}.txt') for k in kpoints]
    plt.plot(kpoints, a, '-')
    plt.xlabel('number of k-points')
    plt.ylabel('lattice constant [Ang]')

    plt.show()
