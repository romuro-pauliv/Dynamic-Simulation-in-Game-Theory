import numpy as np
import matplotlib.pyplot as plt
import random
from icecream import ic

from calc.payoff_generation import PayoffGen

payoff_gen: PayoffGen = PayoffGen(10, 2)
payoff_gen.payoff_range(-1, 1)
ic(payoff_gen.gen_random_payoff_matrix())