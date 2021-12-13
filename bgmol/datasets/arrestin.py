import os
import numpy as np
from bgmol.datasets.base import DataSet
from bgmol.api import system_by_name
from bgmol.tpl.hdf5 import HDF5TrajectoryFile, load_hdf5
import pickle
import mdtraj

__all__ = ["ArrestinActive", "ArrestinInactive"]


class ArrestinActive(DataSet):
    """ArrestinActive at 310 K.
    1 ms Langevin dynamics with 1/ps friction coefficient and 2fs time step,
    output spaced in 10 ps intervals.
    """
    #url = "http://ftp.mi.fu-berlin.de/pub/cmb-data/bgmol/datasets/ala2/Ala2Implicit300.tgz"
    #md5 = "ce9d6f6aa214f3eb773d52255aeaeacb"
    #num_frames = 99999
    #size = 49692000 # in bytes
    selection = "all"
    openmm_version = "7.4.1"
    date = "2021/8/15"

    loc = '/oak/stanford/groups/rondror/projects/ensemble-generators/arrestin/openmm-arrestin/'
    top = loc+'arr2-active_start_centered.pdb'
    trj = loc+'arr2-active_output_aligned_final.xtc'
    log = loc+'arr2-active_log.txt'

    def __init__(self, root=os.getcwd()):
        super(ArrestinActive, self).__init__(root=root)
        self._system = system_by_name("ArrestinActive")
        self._temperature = 310
        self._xyz = mdtraj.load_xtc(self.trj, self.top).xyz

    def read(self):
        self._energies = np.loadtxt(self.log, delimiter=',')[:,1]
       

class ArrestinInactive(DataSet):
    """ArrestinInactive at 310 K.
    1 ms Langevin dynamics with 1/ps friction coefficient and 2fs time step,
    output spaced in 10 ps intervals.
    """
    #url = "http://ftp.mi.fu-berlin.de/pub/cmb-data/bgmol/datasets/ala2/Ala2Implicit1000.tgz"
    #md5 = "9a90965254dac7440976d0d62687caed"
    #num_frames = 100000
    #size = 51071715 # in bytes
    selection = "all"
    openmm_version = "7.4.1"
    date = "2021/08/15"

    loc = '/oak/stanford/groups/rondror/projects/ensemble-generators/arrestin/openmm-arrestin/'
    top = loc+'arr2-inactive_start_centered.pdb'
    trj = loc+'arr2-inactive_output_aligned_final.xtc'
    log = loc+'arr2-inactive_log.txt'

    def __init__(self, root=os.getcwd()):
        super(ArrestinInactive, self).__init__(root=root)
        self._system = system_by_name("ArrestinInactive")
        self._temperature = 310
        self._xyz = mdtraj.load_xtc(self.trj, self.top).xyz

    def read(self):
        self._energies = np.loadtxt(self.log, delimiter=',')[:,1]


