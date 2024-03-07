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
    from simulation.nash import simulate_0, simulate_1
    behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    behavior_1: list[np.ndarray] = init_simulation(simulate_1)
    # |--------------------------------------------------------------|

    # Trajectory Graph
    from graph.analysis.trajectory import Trajectory
    trajectory: Trajectory = Trajectory([behavior_0, behavior_1])
    trajectory.show()
    
    # Distribution Graph
    from graph.analysis.dist import Dist
    dist: Dist = Dist([behavior_0, behavior_1])
    dist.plot_payoff_dist()
    dist.plot_cumsum_dist()
    dist.plot_boxplot_cumsum_dist()
    dist.show()