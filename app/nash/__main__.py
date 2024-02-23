from calc.payoff_generation import PayoffGen
from controller.choices import Choices
from icecream import ic
import numpy as np

PLAYERS : int = 4
STRATEGY: int = 10

payoff_gen: PayoffGen = PayoffGen(PLAYERS, STRATEGY)
payoff_gen.payoff_range(-1, 1)


historic: list[np.ndarray] = []

choices: Choices = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)

for _ in range(5000):
    matrix = payoff_gen.gen_random_payoff_matrix()
    
    P1 = choices.algorithms.get_maxsum(matrix[0], 0)
    P2 = choices.algorithms.get_maxsum(matrix[2], 1)
    P3 = choices.algorithms.randomize(STRATEGY)
    P4 = choices.algorithms.randomize(STRATEGY)
    
    historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))


historic: np.ndarray = np.array(historic)

import matplotlib.pyplot as plt
import seaborn as sns
x: np.ndarray = np.arange(historic.shape[0])
fig, ax = plt.subplots(1, 1)
for n in range(historic.shape[1]):
    sns.lineplot(x=x, y=np.cumsum(historic[:, n]))

plt.show()