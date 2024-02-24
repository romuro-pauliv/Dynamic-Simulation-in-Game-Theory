from calc.payoff_generation import PayoffGen
from controller.choices import Choices
from icecream import ic
import numpy as np

PLAYERS : int = 10
STRATEGY: int = 5

payoff_gen: PayoffGen = PayoffGen(PLAYERS, STRATEGY)
payoff_gen.payoff_range(-10, 10)

historic: list[np.ndarray] = []

choices: Choices = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)

for _ in range(100):
    matrix = payoff_gen.gen_random_payoff_matrix()
    
    P1 = choices.algorithms.get_maxsum(matrix[0], 0)
    P2 = choices.algorithms.get_maxsum(matrix[1], 1)
    P3 = choices.algorithms.get_maxsum(matrix[2], 2)
    P4 = choices.algorithms.get_maxsum(matrix[3], 3)
    P5 = choices.algorithms.get_maxsum(matrix[4], 4)
    P6 = choices.algorithms.get_maxsum(matrix[5], 5)
    P7 = choices.algorithms.get_maxsum(matrix[6], 6)
    P8 = choices.algorithms.get_maxsum(matrix[7], 7)
    P9 = choices.algorithms.get_maxsum(matrix[8], 8)
    P10 = choices.algorithms.get_maxsum(matrix[9], 9)
    
    historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10)))


historic: np.ndarray = np.array(historic)

import matplotlib.pyplot as plt
import seaborn as sns
x: np.ndarray = np.arange(historic.shape[0])
fig, ax = plt.subplots(1, 1)
for n in range(historic.shape[1]):
    sns.lineplot(x=x, y=np.cumsum(historic[:, n]))

plt.show()