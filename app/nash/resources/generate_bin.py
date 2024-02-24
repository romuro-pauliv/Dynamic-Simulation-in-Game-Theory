# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/resources/generate_bin.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import pickle
from pathlib import Path, PosixPath

from log.genlog import genlog

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|

PATH_: PosixPath = Path("nash")

class GenBin(object):
    @staticmethod
    def save(name: str, obj: Any) -> None:
        """
        Save a object
        """
        with open(Path(PATH_, f"{name}.bin"), "wb") as f:
            pickle.dump(obj, f)
        genlog.report(True, f"saved [{name}.bin]")
    
    @staticmethod
    def load(name: str) -> Any:
        """
        Load a object
        """
        with open(Path(PATH_, f"{name}.bin"), "rb") as f:
            file: Any = pickle.load(f)
        return file