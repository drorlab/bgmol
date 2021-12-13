import os
import tempfile
import numpy as np
from simtk.openmm import app
import mdtraj as md
from ..systems.base import OpenMMToolsTestSystem, OpenMMSystem
from torchvision.datasets.utils import download_url
import pickle


__all__ = ["ArrestinActive", "ArrestinInactive"]


class ArrestinActive(OpenMMSystem):
    """
    """
    def __init__(self,  root=tempfile.gettempdir(), download=True):
        super(ArrestinActive, self).__init__()
        
        inputdir = "/oak/stanford/groups/rondror/projects/ensemble-generators/arrestin/openmm-arrestin/"
        pdbname = inputdir+"arr2-active_start_centered.pdb"
        picklename = inputdir+'arr2-active_system.pkl'

        with open(picklename, 'rb') as f:
            system = pickle.load(f)
            self._system = system

        ff = app.ForceField("amber99sbildn.xml", "amber96_obc.xml")

        pdb = app.PDBFile(pdbname)

        self._positions = pdb.getPositions(asNumpy=True)
        self._topology = pdb.getTopology()
        self.z_matrix = None
        self.rigid_block = None


class ArrestinInactive(OpenMMSystem):
    """
    """
    def __init__(self,  root=tempfile.gettempdir(), download=True):
        super(ArrestinInactive, self).__init__()

        inputdir = "/oak/stanford/groups/rondror/projects/ensemble-generators/arrestin/openmm-arrestin/"
        pdbname = inputdir+"arr2-inactive_start_centered.pdb"
        picklename = inputdir+'arr2-inactive_system.pkl'

        with open(picklename, 'rb') as f:
            system = pickle.load(f)
            self._system = system

        ff = app.ForceField("amber99sbildn.xml", "amber96_obc.xml")

        pdb = app.PDBFile(pdbname)

        self._positions = pdb.getPositions(asNumpy=True)
        self._topology = pdb.getTopology()
        self.z_matrix = None
        self.rigid_block = None


