# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                  app/log/genlog.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from datetime import datetime
from colorama import Fore, Style
from typing import Union
# |--------------------------------------------------------------------------------------------------------------------|


class Genlog(object):
    """
    Generate the logs in the terminal
    """
    def __init__(self) -> None:
        self.verbose: bool = True
    
    def define_verbose(self, verbose: int) -> None:
        self.verbose: bool = bool(verbose)
        
    def report(self, state: Union[str, bool], comment: str) -> None:
        """
        Report the logs
        Args:
            state (Union[str, bool]): True or False or "debug"
            comment (str): The log report
        """
        state_color: str = Fore.GREEN if state == True else Fore.RED if isinstance(state, bool) else Fore.YELLOW
        state: str = "SUCCESS" if state == True else "FAILED" if isinstance(state, bool) else state
        rst: str = Style.RESET_ALL
        
        if self.verbose == True:
            print(f"{Fore.CYAN}[{datetime.now()}]{rst} [{state_color}{str(state).upper()}{rst}] [{comment}]")


genlog: Genlog = Genlog()