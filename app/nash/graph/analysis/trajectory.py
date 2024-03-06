# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/graph/analysis/trajectory.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot    as plt
import numpy                as np

from matplotlib.axes    import Axes
from matplotlib.figure  import Figure

from calc.transform.add_behavior_matrix import AddBehavior
from calc.transform.to_player_matrix    import ST2P_matrix
from config.config_files                import configfiles
# |--------------------------------------------------------------------------------------------------------------------|


class Trajectory(object):
    def __init__(self, behaviors: list[list[np.ndarray]]) -> None:
        """
        Initialize the Trajectory Instance.
        Args:
            behaviors (list[list[np.ndarray]]): Simulation data list
        """
        self.n_players      : int = int(configfiles.ini['simulation']['simulate:matrix']['players'])
        
        self.data_concat     : list[np.ndarray] = self._concat(behaviors)
        self.data_sort_concat: list[np.ndarray] = self._concat_sort(behaviors)
        
    def _concat(self, behaviors: list[list[np.ndarray]]) -> list[np.ndarray]:
        """
        Concatenates the data behaviors using "AddBehavior" class
        """
        add_behavior: AddBehavior = AddBehavior(self.n_players)
        for b in behaviors:
            add_behavior.add(ST2P_matrix(b))
        return add_behavior.concat()

    def _concat_sort(self, behaviors: list[list[np.ndarray]]) -> list[np.ndarray]:
        """
        Concatenates the data behaviors using "AddBehavior" class
        """
        add_behavior: AddBehavior = AddBehavior(self.n_players)
        for b in behaviors:
            add_behavior.add(np.sort(ST2P_matrix(b), axis=1))
        return add_behavior.concat()
    
    def define_colors_agents(self, colors_list: list[str]) -> None:
        """
        Defines a color for each player
        Args:
            colors_list (list[str]): Color list (length must be equal to the number of players)
        """
        self.colors_list: list[str] = colors_list
    
    @staticmethod
    def graph_func(ax: Axes, player: np.ndarray, sort_player: np.ndarray, color: str) -> None:
        """
        Creates the graph for each player in Axes [ax]
        Args:
            ax (Axes): plt axes to plot data
            player (np.ndarray): Player array
            sort_player (np.ndarray): Player sorted array
            color (str): Color to player
        """
        player      : np.ndarray = np.cumsum(player, axis=0)
        sort_player : np.ndarray = np.cumsum(sort_player, axis=0)
        
        mean_player     : np.ndarray = np.mean(player, axis=1)
        mean_sort_player: np.ndarray = np.mean(sort_player, axis=1)
        
        ax.plot(mean_player, alpha=0.5, color=color, linewidth=0.5)
        ax.plot(mean_sort_player, alpha=0.2, color=color, linewidth=0.5, linestyle="dashed")
    
    def show(self) -> None:
        """
        Execute the player trajectory graph
        """
        graph: tuple[Figure, Axes] = plt.subplots()
        
        for player, sort_player, c in zip(self.data_concat, self.data_sort_concat, self.colors_list):
            self.graph_func(graph[1], player, sort_player, c)
        
        graph[1].set_ylabel("Cumulative payoff")
        graph[1].set_xlabel("iterations")
        graph[1].grid(True, "both", "both")
        
        plt.show()
        plt.clf()