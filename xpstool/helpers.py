import datetime
import matplotlib

import numpy as np
import pandas as pd

# Default minimal info for every region 
info_fields = (
    "File Name", # Original data file name as was recorded in the experiment
    "Spectrum Name", # Spectrum name as written in Sciemta software
    "Region Name", # Single region name (different from previous if spectrum is multi regional)
    "Pass Energy", # Value of pass energy of the analyser
    "Number of Sweeps",
    "Energy Scale", # Kinetic or Binding
    "Step Time", # Dwell time of the measurement
    "Date", 
    "Time"         
) 

class Scan:
    """Contains and handles a single recorded region together with all information
    about the scan and experimental conditions provided in data file
    """
    
    def __init__(self, energy, counts, energy_shift=0, binding_energy_flag=True, 
                 fermi_flag=False, info=None):   
        """Creates the class using two variables (of type list or similar etc.).
        The first goes for energy (X) axis, the second - for counts (Y) axis. The values 
        on energy axis are shifted by the specified constant 'energy_shift', which
        is defined by the experiment (e.g. Fermi-level, instrument work function etc.)
        The boolean 'binding_energy_flag' defines which energy representation is used
        (binding (True) or kinetic (False)). Fermi_flag should be True if the spectrum
        represents the Fermi level measurement. Experimental conditions can be passed
        as 'info' dictionary {"name": value} and stored in the instance. 
        """
        # Correct for the shift if not 0
        if energy_shift != 0:
            for i in range(len(energy)):
                energy[i] -= energy_shift
        
        # The main attribute of the class is pandas dataframe with the possibility 
        self.Data = pd.DataFrame(data={'energy': energy, 'counts': counts}, dtype=float)
        self.Info = info
        self.BindingEnergyFlag = binding_energy_flag
        
    def addColumn(self, column_label, array):
        """Adds one column to the data object assigning it the name 'column_label'
        """
        self.Data[column_label] = array
        
    def removeColumn(self, column_label):
        """Removes one of the columns of the data object
        """
        self.Data = self.Data.drop(column_label, 1) 
           
def parseScientaFileInfo(lines):
    """Parses the Scienta file and returnes 'info' dictionary
    """
    pass

def parseSpecFileInfo(lines):
    """Parses the SPEC.xy file and returns 'info' dictionary
    """
    info = {}    
    return info