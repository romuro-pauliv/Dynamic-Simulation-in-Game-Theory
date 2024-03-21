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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0 if np.random.random() <= 0.25 else 2], 2, np.argmax)
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[3], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[4], 4, np.argmax)
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[5], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[6], 6, np.argmax)
        
        LC     : int = choices.algorithms.single.sum_payoffs(matrix[7], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[8], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[9], 9, np.argmax)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 3], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 4], 4, np.argmax)
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[5], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[6], 6, np.argmax)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[7], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[8], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[9], 9, np.argmax)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 3], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 4], 4, np.argmax)
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[5], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[0 if np.random.random() <= 0.5 else 6], 6, np.argmax)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[7], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[8], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[9], 9, np.argmax)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[5], 0, np.argmin)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 3], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[5 if np.random.random() <= 0.5 else 4], 4, np.argmax)
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[0], 5, np.argmin)
        
        if np.random.choice([0, 1]) == 0:
            USSR: int = choices.algorithms.single.sum_payoffs(matrix[0 if np.random.random() <= 0.5 else 6], 6, np.argmax)
        else:
            USSR: int = choices.algorithms.single.sum_payoffs(matrix[5], 6, np.argmin)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[7], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[8], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[9], 9, np.argmax)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([3, 4])], 0, np.argmin)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        
        if np.random.choice([0, 1]) == 0:
            UK     : int = choices.algorithms.single.sum_payoffs(matrix[0], 3, np.argmin)
            FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[0], 4, np.argmin)
        else:
            UK     : int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([3, 4])], 3, np.argmax)
            FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([3, 4])], 4, np.argmax)
        
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[0], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 6])], 6, np.argmax)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[7], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[8], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[9], 9, np.argmax)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)


def behavior5() -> None:
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([3, 4, 9])], 0, np.argmin)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[9], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[9], 4, np.argmax)
        
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[0], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 6])], 6, np.argmax)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[0], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[0], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[0], 9, np.argmin)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[10], 10, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)


def behavior6() -> None:
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
        GERMANY: int = choices.algorithms.single.sum_payoffs(matrix[4], 0, np.argmin)
        AUSTRIA: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmax)
        CZECHO : int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmax)
        
        UK     : int = choices.algorithms.single.sum_payoffs(matrix[4], 3, np.argmax)
        FRENCH : int = choices.algorithms.single.sum_payoffs(matrix[0], 4, np.argmin)
        
        POLAND : int = choices.algorithms.single.sum_payoffs(matrix[0], 5, np.argmax)
        USSR   : int = choices.algorithms.single.sum_payoffs(matrix[np.random.choice([0, 6])], 6, np.argmax)

        LC     : int = choices.algorithms.single.sum_payoffs(matrix[0], 7, np.argmax)
        DENMARK: int = choices.algorithms.single.sum_payoffs(matrix[0], 8, np.argmax)
        NORWAY : int = choices.algorithms.single.sum_payoffs(matrix[0], 9, np.argmin)
        ITALY  : int = choices.algorithms.single.sum_payoffs(matrix[4], 10, np.argmin)
        
        historic.append(choices.get_payoffs(matrix, 
            (GERMANY, AUSTRIA, CZECHO, UK, FRENCH, POLAND, USSR, LC, DENMARK, NORWAY, ITALY)))
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
