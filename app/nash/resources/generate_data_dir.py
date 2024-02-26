# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                 app/resources/generate_data_dir.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import os
import shutil
from pathlib import Path, PosixPath

from log.genlog import genlog
# |--------------------------------------------------------------------------------------------------------------------|

class GenDataDir(object):
    """
    Generate the 'data' directory.
    """
    def __init__(self) -> None:
        """
        Initialize the GenDataDir
        """
        self.root_path  : PosixPath = Path("nash")
        self.data_dir   : PosixPath = Path("data")
        self.path_      : PosixPath = Path(self.root_path, self.data_dir)
        
        self.exist_or_not: bool = False
        
    def _scan_dir(self) -> None:
        """
        Verify if the directory 'data' exists in root_path. 
        """
        if str(self.data_dir) in os.listdir(self.root_path):
            self.exist_or_not: bool = True
        else:
            self.exist_or_not: bool = False
    
    def create(self) -> None:
        """
        Creates the data directory
        """
        self._scan_dir()
        if self.exist_or_not == False:
            os.mkdir(self.path_)
            genlog.report(True, f"[mkdir] created {self.path_}")
        else:
            genlog.report(False, f"[mkdir] {self.path_} already exists")
        
    def delete(self) -> None:
        """
        Deletes the data directory
        """
        self._scan_dir()
        if self.exist_or_not == True:
            shutil.rmtree(Path(self.root_path, self.data_dir))
            genlog.report(True, f"[rmtree] deleted {self.path_}")
        else:
            genlog.report(False, f"[rmtree] {self.path_} not exists")


generate_data_dir: GenDataDir = GenDataDir()