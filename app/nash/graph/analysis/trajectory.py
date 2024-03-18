# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/graph/analysis/trajectory.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from calc.transform.to_player_matrix    import ST2P_matrix
from calc.transform.add_behavior_matrix import AddBehavior
from config.config_files import configfiles

import numpy                as np
import matplotlib.pyplot    as plt
from matplotlib.gridspec    import GridSpec
from scipy.stats            import gaussian_kde


from matplotlib.axes    import Axes
from matplotlib.figure  import Figure
# |--------------------------------------------------------------------------------------------------------------------|


class Trajectory(object):
    def __init__(self, behaviors: list[np.ndarray]) -> None:
        """
        Initialize the Trajectory instance.
        Args:
            behaviors (list[np.ndarray]): The behaviors data
        """
        self.data: list[np.ndarray] = self._concat(behaviors)
        
        self.x: np.ndarray = self._get_x(self.data)

        self._simulation_info(len(behaviors))
        self.define_colors_agents()
        
    def define_colors_agents(self) -> None:
        """
        Defines a color for each player
        Args:
            colors_list (list[str]): Color list (length must be equal to the number of players)
        """
        color_list  : list[str] = configfiles.dot_ini['simulation']['simulate:info']['colors'].split(",")
        color_hex   : bool      = bool(int(configfiles.dot_ini['simulation']['simulate:info']['color_hex']))
        if color_hex == True:
            color_list: list[str] = [f"#{c}" for c in color_list]
        self.color_list: list[str] = color_list
    
    def _simulation_info(self, len_behaviors: int) -> None:
        PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
        STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
        ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations']) * len_behaviors
        TIMES       : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['times'])
        MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
        MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
        
        self.simu_info: str = f"P:[{PLAYERS}] S:[{STRATEGY}] R:({MIN_RANGE}, {MAX_RANGE}), ITER:[{ITERATIONS}*{TIMES}]"
    
    def _concat(self, behaviors: list[np.ndarray]) -> list[np.ndarray]:
        """
        Concatenates the behaviors and applies the cumulative sum in each columns
        """
        add_behavior: AddBehavior = AddBehavior(int(configfiles.dot_ini['simulation']["simulate:matrix"]['players']))
        for b in behaviors:
            add_behavior.add(ST2P_matrix(b))
        
        data: list[np.ndarray] = add_behavior.concat()
        for n, d in enumerate(data):
            data[n] = np.cumsum(d, axis=0)
        return data
    
    def _get_x(self, data: list[np.ndarray]) -> np.ndarray:
        """
        Get x data to hist2d plot
        """
        x_seg: np.ndarray = np.arange(0, data[0].shape[0])
        x: np.ndarray = np.array([])
        for _ in range(data[0].shape[1]):
            x: np.ndarray = np.append(x, x_seg)
        return x
    
    def _get_y(self, player_data: np.ndarray) -> np.ndarray:
        """
        Get y data for the player
        """
        y: np.ndarray = np.array([])
        for n in range(player_data.shape[1]):
            y: np.ndarray = np.append(y, player_data[:,n])
        return y
    
    def _get_mean_and_std(self, player_data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """
        Get Mean and Standart Deviation from the player data
        """
        return np.mean(player_data, axis=1), np.std(player_data, axis=1)
    
    def _define_figs(self) -> tuple[Axes, Axes, Figure]:
        """
        Define fig and configure the fig with GridSpec
        Returns:
            tuple[Axes, Axes]: _description_
        """
        fig: Figure = plt.figure()
        gs: GridSpec = GridSpec(4, 4)
        
        ax_dens2d: Axes = fig.add_subplot(gs[0:4,0:3])
        ax_hist_y: Axes = fig.add_subplot(gs[0:4,3])
        return ax_dens2d, ax_hist_y, fig
    
    def _assemble_hist2d(self, ax: Axes, y: np.ndarray, mean: np.ndarray, std: np.ndarray, n: int) -> None:
        ax.plot(self.x, y, alpha=0.2, color=self.color_list[n], linewidth=0.2)
        #ax.plot(mean, color="red", linewidth=0.5)
        #ax.plot(mean+2*std, color="red", linestyle="dashed", linewidth=0.5)
        #ax.plot(mean-2*std, color="red", linestyle="dashed", linewidth=0.5)
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Cumulative Payoffs")
        ax.set_title(f"Player {n} | {self.simu_info}")
        
    def _assemble_hist_y(self, ax: Axes, player_data: np.ndarray, y: np.ndarray, n: int) -> None:
        density: gaussian_kde = gaussian_kde(player_data[-1, :])
        density.covariance_factor = lambda : .25
        density._compute_covariance()
        kde_x: np.ndarray = np.arange(min(y), max(y))
        ax.plot(density(kde_x), kde_x, color=self.color_list[n], linewidth=1)
        ax.fill_between(density(kde_x), kde_x, interpolate=True, color=self.color_list[n], alpha=0.1)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
    
    def plot_player(self, player_data: np.ndarray, n: int) -> None:
        """
        Creates the graph with player data
        """
        ax_dens2d, ax_hist_y, fig = self._define_figs()
        
        y: np.ndarray = self._get_y(player_data)
        mean, std = self._get_mean_and_std(player_data)
        
        self._assemble_hist2d(ax_dens2d, y, mean, std, n)
        self._assemble_hist_y(ax_hist_y, player_data, y, n)
        
    def show(self) -> None:
        """
        Show the trajectory graphs
        """
        for n, player_data in enumerate(self.data):
            self.plot_player(player_data, n)
        plt.show()
        plt.clf()