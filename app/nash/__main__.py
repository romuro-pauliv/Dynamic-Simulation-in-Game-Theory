from calc.payoff_generation import PayoffGen
from controller.choices import Choices
from resources.generate_bin import GenBin
import numpy as np
from icecream import ic

PLAYERS     : int = 2
STRATEGY    : int = 2
ITERATIONS  : int = 10

MIN_RANGE   : float = -1.0
MAX_RANGE   : float = 1

payoff_gen: PayoffGen = PayoffGen(PLAYERS, STRATEGY)
payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
choices: Choices = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)


historic: list[np.ndarray] = []

for _ in range(ITERATIONS):
    matrix = payoff_gen.gen_random_payoff_matrix()
    
    P1 = choices.algorithms.get_maxsum(matrix[0], 0)
    P2 = choices.algorithms.get_maxsum(matrix[1], 1)
    
    historic.append(choices.get_payoffs(matrix, (P1, P2)))

historic: np.ndarray = np.array(historic)