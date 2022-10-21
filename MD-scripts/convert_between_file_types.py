from subprocess import list2cmdline
import numpy as np
import ase.io

"""requires ase package to be installed. If using unbuntu use: 
sudo apt update 
sudo apt install ase
If using Mac, use:
    brew install ase"""

atoms = ase.io.read("graphene_single_layer_test_time_9-9.xyz",format="xyz")
ase.io.write("graphene_single_layer_test_time_9-9_real_charge.data",atoms,format="lammps-data",units="real",atom_style="charge")
