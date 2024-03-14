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

    behaviors: list[list[np.ndarray]] = [
            init_simulation(behavior0),
            init_simulation(behavior1),
            init_simulation(behavior2),
            init_simulation(behavior3),
            init_simulation(behavior4)
        ]
    # |--------------------------------------------------------------|
    
    # RidgeLine Graph
    from graph.analysis.ridgeline import RidgeLine
    rigde_line: RidgeLine = RidgeLine(behaviors)
    rigde_line.show()
    
    # Distribution Graph
    from graph.analysis.dist import Dist
    dist: Dist = Dist(behaviors)
    dist.plot_payoff_dist()
    dist.plot_cumsum_dist()
    dist.plot_boxplot_cumsum_dist()
    dist.show()
    
    # Trajectory Graph
    from graph.analysis.trajectory import Trajectory
    trajectory: Trajectory = Trajectory(behaviors)
    trajectory.show()