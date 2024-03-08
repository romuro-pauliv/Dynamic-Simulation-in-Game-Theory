# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog             import genlog
from config.config_files    import configfiles
from simulation.nash        import init_simulation

import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|
genlog.define_verbose(int(configfiles.dot_ini['simulation']['simulate:info']['verbose']))

if __name__ == "__main__":    
    # Simulation Execution |-----------------------------------------|
    from simulation.nash import *
    behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    behavior_1: list[np.ndarray] = init_simulation(simulate_1)
    behavior_2: list[np.ndarray] = init_simulation(simulate_2)
    behavior_3: list[np.ndarray] = init_simulation(simulate_3)
    behavior_4: list[np.ndarray] = init_simulation(simulate_4)
    behavior_5: list[np.ndarray] = init_simulation(simulate_5)
    behavior_6: list[np.ndarray] = init_simulation(simulate_6)
    behavior_7: list[np.ndarray] = init_simulation(simulate_7)
    # |--------------------------------------------------------------|
    
    # # Distribution Graph
    # from graph.analysis.dist import Dist
    # dist: Dist = Dist([behavior_0, behavior_1])
    # dist.plot_payoff_dist()
    # dist.plot_cumsum_dist()
    # dist.plot_boxplot_cumsum_dist()
    # dist.show()
    
    from graph.analysis.ridgeline import RidgeLine
    rigde_line: RidgeLine = RidgeLine(
        [behavior_0, behavior_1, behavior_2, behavior_3, behavior_4, behavior_5, behavior_6, behavior_7]
    )
    rigde_line.show()
    