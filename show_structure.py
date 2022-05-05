from ase.spacegroup import crystal
import ase.io as io

if __name__ == '__main__':
    a = 4.01  # AA
    al3ti = crystal(('Al', 'Ti'),
                    basis=[(0.0, 0.5, 0.5), (0.0, 0.0, 0.0)],
                    spacegroup=221,
                    cellpar=[a, a, a, 90, 90, 90])

    al3ti_doped = crystal(('Al', 'Ag', 'Ti'),
                          basis=[(0.0, 0.5, 0.5), (0.0, 0.5, 0.5), (0.0, 0.0, 0.0)],
                          occupancies=[0.893, 0.107, 1.0],
                          spacegroup=221,
                          cellpar=[a, a, a, 90, 90, 90])

    # generating .png with the structure
    for name, structure in zip(('al3ti.pov', 'al3ti_doped.pov'), (al3ti, al3ti_doped)):
        renderer = io.write(name, structure,
                            rotation='90y',
                            radii=0.4,
                            povray_settings=dict(transparent=False,
                                                 camera_type='perspective',
                                                 canvas_width=320,
                                                 bondlinewidth=0.07))

        renderer.render()
