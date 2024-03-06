# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from resources.generate_data_dir    import GenDataDir
from resources.read_all_bin         import ReadAllBin
from core.multiprocessing           import CoreChunk

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
    # from simulation.nash  import simulate_0    
    
    # behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    
    # from graph.analysis.dist import Dist
    # dist: Dist = Dist(behavior_0)
    # dist.plot_payoff_dist()
    # dist.plot_cumsum_dist()
    # dist.plot_boxplot_cumsum_dist()
    # dist.show()
    
    from simulation.nash import simulate_0, simulate_1, simulate_2, simulate_3

    behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    behavior_1: list[np.ndarray] = init_simulation(simulate_1)
    behavior_2: list[np.ndarray] = init_simulation(simulate_2)
    behavior_3: list[np.ndarray] = init_simulation(simulate_3)

    from graph.analysis.trajectory import Trajectory
    trajectory: Trajectory = Trajectory([behavior_0, behavior_1, behavior_2, behavior_3])
    trajectory.define_colors_agents(["red", "blue", "blue", "blue"])
    trajectory.show()
    
    
    # # GRAPH 1 |-------------------------------------------------------|
    # player_0: np.ndarray = behavior_0[0]
    
    # player_0_cumsum: np.ndarray = np.cumsum(player_0, axis=0)
    
    # mean: np.ndarray = np.mean(player_0_cumsum, axis=1)
    # std : np.ndarray = np.std(player_0_cumsum, axis=1)
    
    # x: np.ndarray = np.array([])
    # y: np.ndarray = np.array([])
    
    # for i in range(player_0_cumsum.shape[1]):
    #     y = np.append(y, player_0_cumsum[:, i])
    #     x = np.append(x, range(player_0_cumsum.shape[0]))
    
    # import matplotlib.pyplot as plt
    # from matplotlib.axes import Axes
    # from matplotlib.figure import Figure
    
    # graph1: tuple[Figure, Axes] = plt.subplots()
    # graph1[1].scatter(x, y, color="blue", s=0.1)
    
    
    # graph2: tuple[Figure, Axes] = plt.subplots()
    # graph2[1].hist2d(x, y, bins=(100, 100))
    # graph2[1].plot(mean, color="cyan", alpha=0.4)
    # graph2[1].plot(mean+2*std, color="cyan", alpha=0.2)
    # graph2[1].plot(mean-2*std, color="cyan", alpha=0.2)
    
    # plt.show()
    # |-------------------------------------------------------------------|
    