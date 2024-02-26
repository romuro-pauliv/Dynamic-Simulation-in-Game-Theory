# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/config/config_files.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog import genlog

from pathlib import Path, PosixPath
import configparser
import os
# |--------------------------------------------------------------------------------------------------------------------|


class ConfigFiles(object):
    """
    Read and distribute the .ini files in py instance.
    """
    def __init__(self) -> None:
        """
        Initialize the ConfigFiles instance.
        """
        self.config_path    : PosixPath = Path("nash/config")
        self.ini_ext        : str       = "ini"

        self._get_ini_files_path()
        self._read_ini_files()
        
    def _get_ini_files_path(self) -> None:
        """
        Get the .ini filespath
        """
        self.ini_filepath: list[str] = []
        [self.ini_filepath.append(fp) if self.ini_ext in fp else None for fp in os.listdir(self.config_path)]
    
    def _read_ini_files(self) -> None:
        """
        Read the .ini files
        """
        self.ini: dict[str, configparser.ConfigParser] = {}
        for ini_filepath in self.ini_filepath:
            name: str = ini_filepath.split(".")[0]
            
            config: configparser.ConfigParser = configparser.ConfigParser()
            config.read(Path(self.config_path, ini_filepath))
            self.ini[name] = config
            genlog.report(True, f"read {ini_filepath}")
    
    @property
    def dot_ini(self) -> dict[str, configparser.ConfigParser]:
        return self.ini


configfiles: ConfigFiles = ConfigFiles()