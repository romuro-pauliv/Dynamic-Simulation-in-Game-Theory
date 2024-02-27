# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/controller/choices.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np

from typing import Callable
# | -------------------------------------------------------------------------------------------------------------------|

class Algorithms(object):
    """
    Algorithms to find the 'best' choice
    """
    def __init__(self, choice_index: np.ndarray) -> None:
        """
        Initialize the Algorithms Instance.
        Args:
            choice_index (np.ndarray): The choice index array
        """
        self.choice_index: np.ndarray = choice_index
        self.n_players   : int        = len(self.choice_index)
                    
    def get_maxsum(self, player_payoff_matrix: np.ndarray, player_index: int) -> int:
        """
        Get the choice based on the sum of payoffs
        Args:
            player_payoff_matrix (np.ndarray): Player payoff matrix
            player_index (int): The index of the player

        With C and R as possibles choices and index[0] and index[1] to strategy S and T
        >>> C = np.array([[2, 4], [4, 4]])    
        >>> R = np.array([[4, 5], [1, 3]])
        
        >>> C_maxsum = np.array(C[0].sum(), C[1].sum())
        >>> R_maxsum = ...
        
        >>> choice = np.argmax([C_maxsum, R_maxsum])
        
        Returns:
            int: the choice that the algorithm Chose
        """
        maxsum: Callable[[np.ndarray, np.ndarray], np.float64] = lambda pp, ind: np.sum(pp[ind])
        
        payoff_sum: list[np.float64] = []
        for ind in self.choice_index[player_index]:
            payoff_sum.append(maxsum(player_payoff_matrix, ind))
        
        return np.argmax(np.array(payoff_sum))
    
    def get_less_negative(self, player_payoff_matrix: np.ndarray, player_index: int) -> int:
        """
        Based the choice in the strategy with the lowest negative return
        Args:
            player_payoff_matrix (np.ndarray): Player payoff matrix
            player_index (int): The index of the player

        Returns:
            int: The choice that the algorithm chose.
        """
        payoff_sum_negative: list[np.float64] = []
        
        for ind in self.choice_index[player_index]:
            choice: np.ndarray = player_payoff_matrix[ind]
            payoff_sum_negative.append(np.sum(choice[choice < 0]))
            
        return np.argmax(np.array(payoff_sum_negative))
    
    def randomize(self, qnt_strategy: int) -> int:
        """
        Random strategy
        Args:
            qnt_strategy (int): Strategy options

        Returns:
            int: The choice that the algorithm chose
        """
        return np.random.choice(range(qnt_strategy))

class Choices(object):
    def __init__(self, choice_index: np.ndarray, possibilities: list[tuple[int]]) -> None:
        """
        Initialize the Choices instance.
        Args:
            choice_index (np.ndarray): The choice index array
        """
        self.possibilites   : list[tuple[int]]  = possibilities
        self.choice_index   : np.ndarray        = choice_index
        self.algorithms     : Algorithms        = Algorithms(self.choice_index)
        self.n_players      : int               = len(self.choice_index)
    
    def get_payoffs(self, matrix: np.ndarray, choice: tuple[int]) -> np.ndarray:
        """
        Get the results based on payoffs matrix
        Args:
            matrix (np.ndarray): Payoff matrix
            choice (tuple[int]): The group choice

        Returns:
            np.ndarray: payoffs
        """
        master_index: int = self.possibilites.index(choice)
        
        payoff: list[np.float64] = []
        for n, _ in enumerate(choice):
            payoff.append(matrix[n][master_index])
        
        return np.array(payoff)