# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             app/simulation/nash.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from calc.payoff_generation import PayoffGen
from controller.choices     import Choices
from resources.generate_bin import GenBin
from config.config_files    import configfiles

from datetime               import datetime
from uuid                   import uuid4
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|


"""
    Saves the simulation history in .bin file.
    
    The strucuture of .bin file:
    Where PORL (PayOff Result Line) = array([PO_p0, PO_p1, ..., PO_pn])
    POH = array(PORL[i=0], PORL[i=1], ..., PORL[i=iterations])
    
    Then:
    PORL[1xPlayers] -> POH[IterationsxPlayers] where the matrix data is the payoffs.
"""

def behavior0() -> None:
    PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
    STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
    ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
    MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
    MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
    ID_         : str   = str(uuid4())

    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()

        # Algorithms to each player |------------------------------------|
        P0: int = choices.algorithms.single.sum_payoffs(matrix[2], 0, np.argmax)
        P1: int = choices.algorithms.single.sum_payoffs(matrix[2], 1, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[3], 2, np.argmin)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[2], 3, np.argmin)
        
        historic.append(choices.get_payoffs(matrix, (P0, P1, P2, P3)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)

def behavior1() -> None:
    PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
    STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
    ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
    MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
    MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
    ID_         : str   = str(uuid4())

    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()

        # Algorithms to each player |------------------------------------|
        P0: int = choices.algorithms.single.sum_payoffs(matrix[2], 0, np.argmax)
        P1: int = choices.algorithms.single.sum_payoffs(matrix[2], 1, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[3], 2, np.argmin)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[2], 3, np.argmin)
        
        historic.append(choices.get_payoffs(matrix, (P0, P1, P2, P3)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)


def behavior2() -> None:
    PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
    STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
    ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
    MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
    MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
    ID_         : str   = str(uuid4())

    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()

        # Algorithms to each player |------------------------------------|
        P0: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        P1: int = choices.algorithms.single.sum_payoffs(matrix[1], 1, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 1])], 2, np.argmax)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[3], 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P0, P1, P2, P3)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)


def behavior3() -> None:
    PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
    STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
    ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
    MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
    MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
    ID_         : str   = str(uuid4())

    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()

        # Algorithms to each player |------------------------------------|
        P0: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        P1: int = choices.algorithms.single.sum_payoffs(matrix[1], 1, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 1])], 2, np.argmax)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[3], 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P0, P1, P2, P3)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)


def behavior4() -> None:
    PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
    STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
    ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
    MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
    MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
    ID_         : str   = str(uuid4())

    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()

        # Algorithms to each player |------------------------------------|
        P0: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        P1: int = choices.algorithms.single.sum_payoffs(matrix[1], 1, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 1])], 2, np.argmax)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[3], 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P0, P1, P2, P3)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)

# | Imports |----------------------------------------------------------------------------------------------------------|
from typing                         import Callable
from resources.generate_data_dir    import GenDataDir
from core.multiprocessing           import CoreChunk
from resources.read_all_bin         import ReadAllBin
from colorama                       import Fore, Style
# |--------------------------------------------------------------------------------------------------------------------|

def init_simulation(simulation: Callable[[None], None]) -> list[np.ndarray]:
    """
    Initialize the simulation in multiprocessing. 
    Args:
        simulation (Callable[[None], None]): The simulation function

    Such PO = PayOff
    such i = iterations
    
    There is PORL = [PO[player_0], PO[player_1], ..., PO[player_n]] -> matrix PORL[1xplayers]
    Then: POH = [PORL[i=0], PORL[i=1], ..., PORL[i=iterations]] = -> matrix POH[IterationsxPlayers] -> POH[IxP]
    
    This function will return a list of history (POH) with a Simulation Times (ST) size.
    Returns:
        list[np.ndarray]: [POH[IxP]][1xST]
    """
    generate_data_dir: GenDataDir = GenDataDir()
    generate_data_dir.delete(), generate_data_dir.create()
    
    core_chunk: CoreChunk = CoreChunk()
    core_chunk.define_function(simulation)
    print(f"Exec: {Fore.CYAN}{simulation.__name__}{Style.RESET_ALL}")
    core_chunk.run()

    read_all_bin: ReadAllBin = ReadAllBin()
    return read_all_bin.bin_data
