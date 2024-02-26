# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/resources/generate_bin.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pickle
from pathlib import Path, PosixPath

from config.config_files import configfiles

from log.genlog import genlog

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|

root_path: str = configfiles.dot_ini['bindata']['bindata:path']['root']
dir_path : str = configfiles.dot_ini['bindata']['bindata:path']['dir']
bin_ext  : str = configfiles.dot_ini['bindata']['bindata:ext']['ext']

PATH_: PosixPath = Path(root_path, dir_path)

class GenBin(object):
    @staticmethod
    def save(name: str, obj: Any) -> None:
        """
        Save a object
        """
        with open(Path(PATH_, f"{name}{bin_ext}"), "wb") as f:
            pickle.dump(obj, f)
            f.close()
        genlog.report(True, f"saved [{name}{bin_ext}]")
    
    @staticmethod
    def load(name: str) -> Any:
        """
        Load a object
        """
        with open(Path(PATH_, name), "rb") as f:
            file: Any = pickle.load(f)
        genlog.report("LOAD", f"{Path(PATH_, name)}")
        return file