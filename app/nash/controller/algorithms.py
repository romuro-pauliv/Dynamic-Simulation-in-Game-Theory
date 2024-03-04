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
        """
        sums the payoffs of the player matrix and uses the "decision" function to find the strategy based on the sum.
        Args:
            POM (np.ndarray): player PayOff Matrix [POM]
            player_index (int): Player index
            decision (Callable[[np.ndarray], int]): Function that receives the payoff sum [np.argmin, np.argmax, ...]

        Returns:
            int: The player decision
        """
        payoff_sum: list[np.float64] = []
        for ind in self.choice_index[player_index]:
            payoff_sum.append(np.sum(POM[ind]))
        
        return decision(np.array(payoff_sum))
    
    def sum_negative_payoffs(self, POM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        """
        Sums the negative payoffs of the player matrix and uses the "decision" function to find the strategy based on
        the sum.
        Args:
            POM (np.ndarray): player PayOff Matrix [POM]
            player_index (int): Player index
            decision (Callable[[np.ndarray], int]): Function that receives the negative payoff sum
                                                    [np.argmin, np.argmax, ...]

        Returns:
            int: The player decision
        """
        payoff_sum_negative: list[np.float64] = []
        for ind in self.choice_index[player_index]:
            choice: np.ndarray = POM[ind]
            payoff_sum_negative.append(np.sum(choice[choice < 0]))
            
        return decision(np.array(payoff_sum_negative))

    def randomize(self, strategies_num: int) -> int:
        """
        Random player strategy
        Args:
            strategies_num (int): Quantity of strategies

        Returns:
            int: The player decision
        """
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
        """
        Clears all caches. Required to use in each iteration
        """
        self.sum_PO_cache           : dict[Callable[[np.ndarray], int], int] = {}
        self.sum_negative_PO_cache  : dict[Callable[[np.ndarray], int], int] = {}
    
    def sum_payoffs(self, APOM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        """
        Sums the payoffs of the all player and uses the "decision" function to find the strategy based on the sum.
        Args:
            APOM (np.ndarray): All PayOffs Matrix [APOM]
            player_index (int): Player index
            decision (Callable[[np.ndarray], int]): Function that receives the payoffs sum [np.argmin, np.argmax, ...]

        Returns:
            int: The player decision
        """
        try:
            choice_index: int = self.sum_PO_cache[decision]
            return np.where(self.choice_index[player_index] == choice_index)[0][0]
        except Exception:    
            payoff_sum: list[np.float64] = []
            for n in range(APOM.shape[1]):
                situation_array: np.ndarray = APOM[:, n]
                payoff_sum.append(np.sum(situation_array))
        
            choice_index: int = decision(payoff_sum)
            self.sum_PO_cache[decision] = choice_index          # Add cache
            return np.where(self.choice_index[player_index] == choice_index)[0][0]

    def sum_negative_payoffs(self, APOM: np.ndarray, player_index: int, decision: Callable[[np.ndarray], int]) -> int:
        """
        Sums the negative payoffs of the all player and uses the "decision" function to find the strategy based on the 
        sum.
        Args:
            APOM (np.ndarray): All PayOffs Matrix [APOM]
            player_index (int): Player index
            decision (Callable[[np.ndarray], int]): Function that receives the payoffs sum [np.argmin, np.argmax, ...]

        Returns:
            int: The player decision
        """
        try:
            choice_index: int = self.sum_negative_PO_cache[decision]
            return np.where(self.choice_index[player_index] == choice_index)[0][0]
        except Exception:
            payoff_negative_sum: list[np.float64] = []
            for n in range(APOM.shape[1]):
                situation_array: np.ndarray = APOM[:, n]
                payoff_negative_sum.append(np.sum(situation_array[situation_array < 0]))
        
            choice_index: int = decision(payoff_negative_sum)
            self.sum_negative_PO_cache[decision] = choice_index # Add cache
            return np.where(self.choice_index[player_index] == choice_index)[0][0]