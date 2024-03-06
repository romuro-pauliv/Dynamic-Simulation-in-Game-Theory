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


def simulate_0() -> None:
    """
    Saves the simulation history in .bin file.
    
    The strucuture of .bin file:
    Where PORL (PayOff Result Line) = array([PO_p0, PO_p1, ..., PO_pn])
    POH = array(PORL[i=0], PORL[i=1], ..., PORL[i=iterations])
    
    Then:
    PORL[1xPlayers] -> POH[IterationsxPlayers] where the matrix data is the payoffs.
    """
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
        P1: int = choices.algorithms.group.sum_negative_payoffs(matrix, 0, np.argmax)
        P2: int = choices.algorithms.group.sum_negative_payoffs(matrix, 1, np.argmax)
        P3: int = choices.algorithms.group.sum_negative_payoffs(matrix, 2, np.argmax)
        P4: int = choices.algorithms.group.sum_negative_payoffs(matrix, 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)

def simulate_1() -> None:
    """
    Saves the simulation history in .bin file.
    
    The strucuture of .bin file:
    Where PORL (PayOff Result Line) = array([PO_p0, PO_p1, ..., PO_pn])
    POH = array(PORL[i=0], PORL[i=1], ..., PORL[i=iterations])
    
    Then:
    PORL[1xPlayers] -> POH[IterationsxPlayers] where the matrix data is the payoffs.
    """
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
        P1: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        P2: int = choices.algorithms.group.sum_negative_payoffs(matrix, 1, np.argmax)
        P3: int = choices.algorithms.group.sum_negative_payoffs(matrix, 2, np.argmax)
        P4: int = choices.algorithms.group.sum_negative_payoffs(matrix, 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)

def simulate_2() -> None:
    """
    Saves the simulation history in .bin file.
    
    The strucuture of .bin file:
    Where PORL (PayOff Result Line) = array([PO_p0, PO_p1, ..., PO_pn])
    POH = array(PORL[i=0], PORL[i=1], ..., PORL[i=iterations])
    
    Then:
    PORL[1xPlayers] -> POH[IterationsxPlayers] where the matrix data is the payoffs.
    """
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
        P1: int = choices.algorithms.single.sum_payoffs(matrix[0], 0, np.argmax)
        P2: int = choices.algorithms.single.sum_payoffs(matrix[0], 1, np.argmin)
        P3: int = choices.algorithms.single.sum_payoffs(matrix[0], 2, np.argmin)
        P4: int = choices.algorithms.single.sum_payoffs(matrix[0], 3, np.argmin)
        
        historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)

def simulate_3() -> None:
    """
    Saves the simulation history in .bin file.
    
    The strucuture of .bin file:
    Where PORL (PayOff Result Line) = array([PO_p0, PO_p1, ..., PO_pn])
    POH = array(PORL[i=0], PORL[i=1], ..., PORL[i=iterations])
    
    Then:
    PORL[1xPlayers] -> POH[IterationsxPlayers] where the matrix data is the payoffs.
    """
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
        P1: int = choices.algorithms.group.sum_negative_payoffs(matrix, 0, np.argmax)
        P2: int = choices.algorithms.group.sum_negative_payoffs(matrix, 1, np.argmax)
        P3: int = choices.algorithms.group.sum_negative_payoffs(matrix, 2, np.argmax)
        P4: int = choices.algorithms.group.sum_negative_payoffs(matrix, 3, np.argmax)
        
        historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))
        # |--------------------------------------------------------------|

        choices.algorithms.group.clear_cache()
    
    historic: np.ndarray = np.array(historic)
    GenBin.save(f"{datetime.now()}_{ID_}", historic)