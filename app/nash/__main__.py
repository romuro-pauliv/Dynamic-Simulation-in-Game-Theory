# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from resources.generate_data_dir    import GenDataDir
from resources.read_all_bin         import ReadAllBin
from core.multiprocessing           import CoreChunk

from icecream import ic
import numpy as np
from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|

def init_simulation(simulation: Callable[[None], None]) -> list[np.ndarray]:
    """
    Initialize the simulation in multiprocessing. 
    Args:
        simulation (Callable[[None], None]): The simulation function

    Such PO = PayOff
    such i = iterations
    
    There is PORL = [PO[player_0], PO[player_1], ..., PO[player_n]] -> matrix PORL[1xplayers]
    Then: POH = [PORL[i=0], PORL[i=1], ..., PORL[i=iterations]] = -> matrix POH[IterationsxPlayers] -> POH[IxP]
    
    This function will return a list of history (POH) with a Simulation Times (ST) size.
    Returns:
        list[np.ndarray]: [POH[IxP]][1xST]
    """
    generate_data_dir: GenDataDir = GenDataDir()
    generate_data_dir.delete(), generate_data_dir.create()
    
    core_chunk: CoreChunk = CoreChunk()
    core_chunk.define_function(simulation)
    core_chunk.run()

    read_all_bin: ReadAllBin = ReadAllBin()
    return read_all_bin.bin_data

if __name__ == "__main__":
    from simulation.nash  import simulate_0    
    
    behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    
    from graph.analysis.dist import Dist
    dist: Dist = Dist(behavior_0)
    dist.plot_payoff_dist()
    dist.plot_cumsum_dist()
    dist.plot_boxplot_cumsum_dist()
    dist.show()