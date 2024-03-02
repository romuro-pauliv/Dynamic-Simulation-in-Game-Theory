# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/controller/choices.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np

from controller.algorithms import Single, Group
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
        
        self.single_class: Single = Single(self.choice_index)
        self.group_class : Group  = Group(self.choice_index)
    
    @property
    def single(self) -> Single:
        return self.single_class
    
    @property
    def group(self) -> Group:
        return self.group_class

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