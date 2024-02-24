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
        print(
            f"{Fore.CYAN}[{datetime.now()}]{rst} [{state_color}{str(state).upper()}{rst}] [{comment}]"
        )


genlog: Genlog = Genlog()