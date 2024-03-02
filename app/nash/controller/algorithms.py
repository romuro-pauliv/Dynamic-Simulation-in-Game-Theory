# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/controller/algorithm.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np

from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|


class Single(object):
    def __init__(self, choice_index: np.ndarray) -> None:
        """
        Initialize the Single instance.
        Args:
            choice_index (np.ndarray): The choice indexes
        """
        self.choice_index: np.ndarray = choice_index
    
    def sum_payoffs(self, POM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        payoff_sum: list[np.float64] = []
        for ind in self.choice_index[player_index]:
            payoff_sum.append(np.sum(POM[ind]))
        
        return decision(np.array(payoff_sum))
    
    def sum_negative_payoffs(self, POM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        payoff_sum_negative: list[np.float64] = []
        for ind in self.choice_index[player_index]:
            choice: np.ndarray = POM[ind]
            payoff_sum_negative.append(np.sum(choice[choice < 0]))
            
        return decision(np.array(payoff_sum_negative))

    def randomize(self, strategies_num: int) -> int:
        return np.random.choice(range(strategies_num))


class Group(object):
    def __init__(self, choice_index: np.ndarray) -> None:
        """
        Initialize the Group instance.
        Args:
            choice_index (np.ndarray): The choice indexes
        """
        self.choice_index: np.ndarray = choice_index

        self.sum_PO_cache           : dict[Callable[[np.ndarray], int], int] = {}
        self.sum_negative_PO_cache  : dict[Callable[[np.ndarray], int], int] = {}
    
    def clear_cache(self) -> None:
        self.sum_PO_cache           : dict[Callable[[np.ndarray], int], int] = {}
        self.sum_negative_PO_cache  : dict[Callable[[np.ndarray], int], int] = {}
    
    def sum_payoffs(self, APOM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        payoff_sum: list[np.float64] = []
        for n in range(APOM.shape[1]):
            situation_array: np.ndarray = APOM[:, n]
            payoff_sum.append(np.sum(situation_array))
        
        choice_index: int = decision(payoff_sum)
        return np.where(self.choice_index[player_index] == choice_index)[0][0]

    def sum_negative_payoffs(self, APOM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        payoff_negative_sum: list[np.float64] = []
        for n in range(APOM.shape[1]):
            situation_array: np.ndarray = APOM[:, n]
            payoff_negative_sum.append(np.sum(situation_array[situation_array < 0]))
        
        choice_index: int = decision(payoff_negative_sum)
        return np.where(self.choice_index[player_index] == choice_index)[0][0]