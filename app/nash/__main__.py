from calc.payoff_generation import PayoffGen
from controller.choices import Choices
from resources.generate_bin import GenBin
import numpy as np
from uuid import uuid4

def simulate() -> None:
    PLAYERS     : int = 4
    STRATEGY    : int = 2
    ITERATIONS  : int = 100000
    MIN_RANGE   : float = -1
    MAX_RANGE   : float = 1
    ID_         : str   = str(uuid4())
    
    payoff_gen  : PayoffGen = PayoffGen(PLAYERS, STRATEGY)
    choices     : Choices   = Choices(payoff_gen.choice_index_data, payoff_gen.possibilities)
    payoff_gen.payoff_range(MIN_RANGE, MAX_RANGE)
    historic: list[np.ndarray] = []
    for _ in range(ITERATIONS):
        matrix = payoff_gen.gen_random_payoff_matrix()
        # Algorithms to each player |------------------------------------|
        P1 = choices.algorithms.get_maxsum(matrix[0], 0)
        P2 = choices.algorithms.get_maxsum(matrix[1], 1)
        P3 = choices.algorithms.get_maxsum(matrix[2], 2)
        P4 = choices.algorithms.get_maxsum(matrix[3], 3)
        historic.append(choices.get_payoffs(matrix, (P1, P2, P3, P4)))
        # |--------------------------------------------------------------|
        
    historic: np.ndarray = np.array(historic)
    GenBin.save(ID_, historic)



if __name__ == "__main__":    
    from core.multiprocessing import CoreChunk

    core_chunk: CoreChunk = CoreChunk(1, 20)
    core_chunk.define_function(simulate)
    core_chunk.run()