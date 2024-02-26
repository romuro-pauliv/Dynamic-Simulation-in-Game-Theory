# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/graph/read_all_bin.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from resources.generate_bin import GenBin, PATH_

import numpy as np
import os
# |--------------------------------------------------------------------------------------------------------------------|


class ReadAllBin(GenBin):
    """
    Read all binary files to plot graphs
    """
    def __init__(self) -> None:
        """
        Initialize the ReadAllBin instance.
        """        
        super().__init__()
        self.read()
        
    def _get_bin_filenames(self) -> None:
        """
        Get all binary filenames
        """
        self.bin_filenames: list[str] = os.listdir(PATH_)
    
    def read(self) -> None:
        """
        Read all .bin files
        """
        self._get_bin_filenames()
        self.bin_data: list[np.ndarray] = []
        for i in self.bin_filenames:
            self.bin_data.append(self.load(i))
    
    @property
    def data(self) -> list[np.ndarray]:
        return self.bin_data