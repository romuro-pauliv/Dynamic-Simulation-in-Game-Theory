# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/__main__.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from simulation.nash import init_simulation

import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|

colors: list[str] = ["red", "blue", "blue", "blue", "green"]

if __name__ == "__main__":
    # Simulation Execution |-----------------------------------------|
    from simulation.nash import simulate_0, simulate_1, simulate_2, simulate_3
    behavior_0: list[np.ndarray] = init_simulation(simulate_0)
    behavior_1: list[np.ndarray] = init_simulation(simulate_1)
    behavior_2: list[np.ndarray] = init_simulation(simulate_2)
    behavior_3: list[np.ndarray] = init_simulation(simulate_3)
    # |--------------------------------------------------------------|

    # Trajectory Graph
    from graph.analysis.trajectory import Trajectory
    trajectory: Trajectory = Trajectory([behavior_0, behavior_1, behavior_2, behavior_3])
    trajectory.define_colors_agents(colors)
    trajectory.show()
    
    # Distribution Graph
    from graph.analysis.dist import Dist
    dist: Dist = Dist([behavior_0, behavior_1, behavior_2, behavior_3])
    dist.define_colors_agents(colors)
    dist.plot_payoff_dist()
    dist.plot_cumsum_dist()
    dist.plot_boxplot_cumsum_dist()
    dist.show()
    