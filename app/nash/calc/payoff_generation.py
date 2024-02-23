# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/calc/payoff_generation.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np

from itertools import product
# |--------------------------------------------------------------------------------------------------------------------|


class PayoffGen(object):
    def __init__(self, players: np.int16, strategy: np.int16) -> None:
        """
        Initialize the PayoffGen instance.
        Args:
            players (np.int16): Players qnt.
            strategy (np.int16): Strategy qnt.
        """
        self.players    : np.int16 = players
        self.strategy   : np.int16 = strategy
        
        self.possibilities: list[tuple[int]]    = [comb for comb in product(range(self.strategy), repeat=players)]
        self.poss_len     : int                 = len(self.possibilities)
        
        self.calc_choices_index()
        
    def calc_choices_index(self) -> None:
        """
        Defines the strategy index for each strategy. The data is in self.choices_index. 
        """
        self.choices_index: dict[int, np.ndarray] = {}
        
        for h in range(self.players):
                self.choices_index[h] = np.array([
                np.array([n for n, strategy_option in enumerate(self.possibilities) if strategy_option[h] == i])
                for i in range(self.strategy)
                ])

    @property
    def choice_index_data(self) -> dict[int, np.ndarray]:
        return self.choices_index
    
    def payoff_range(self, min_: np.float64 = -1, max_: np.float64 = 1) -> None:
        """
        Defines a random payoff range
        """
        self.po_min: np.float64 = min_
        self.po_max: np.float64 = max_
    
    def gen_random_payoff(self) -> np.ndarray:
        """
        Generates a random payoff to one player 
        Returns:
            np.ndarray: Random payoff [use possibilities as an index]
        """
        return np.random.uniform(self.po_min, self.po_max, self.poss_len)
    
    def gen_random_payoff_matrix(self) -> dict[int, np.ndarray]:
        """
        Generates a random payoff to all players
        Returns:
            dict[int, np.ndarray]: [player index: payoffs]
        """
        payoff_matrix: list[np.ndarray] = [self.gen_random_payoff() for _ in range(self.players)]
        return np.array(payoff_matrix)