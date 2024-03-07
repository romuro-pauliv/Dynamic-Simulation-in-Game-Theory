# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/graph/analysis/dist.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot    as plt
import seaborn              as sns
import numpy                as np
import pandas               as pd

from calc.transform.add_behavior_matrix import AddBehavior
from config.config_files                import configfiles
# |--------------------------------------------------------------------------------------------------------------------|

class Dist(object):
    def __init__(self, behaviors: list[list[np.ndarray]]) -> None:
        """
        Initialize the Dist instance.
        Args:
            data (np.ndarray): Full data from binary files
        """
        self.data: np.ndarray = self._concat(behaviors)

        self._get_labels()
        self._simulation_info()
        
        self._trans_payoff_concat()
        self._trans_result_cumsum()

        sns.set_theme("paper", "darkgrid", "pastel")
    
    def _concat(self, behaviors: list[list[np.ndarray]]) -> list[np.ndarray]:
        """
        Concatenates the behaviors data
        """
        add_behavior: AddBehavior = AddBehavior(int(configfiles.dot_ini['simulation']['simulate:samples']['times']))
        for b in behaviors:
            add_behavior.add(b)
        return add_behavior.concat()
    
    def _simulation_info(self) -> None:
        PLAYERS     : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
        STRATEGY    : int   = int(configfiles.dot_ini['simulation']['simulate:matrix']['strategy'])
        ITERATIONS  : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['iterations'])
        TIMES       : int   = int(configfiles.dot_ini['simulation']['simulate:samples']['times'])
        MIN_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['min'])
        MAX_RANGE   : float = float(configfiles.dot_ini['simulation']['simulate:payoff_range']['max'])
        
        self.simu_info: str = f"P:[{PLAYERS}] S:[{STRATEGY}] R:({MIN_RANGE}, {MAX_RANGE}), ITER:[{ITERATIONS}*{TIMES}]"
    
    def define_colors_agents(self, color_list: list[str]) -> None:
        self.color_list: list[str] = color_list
    
    def _get_labels(self) -> None:
        """
        Get labels (algorithms names) from .ini file
        """
        self.labels: list[str] = configfiles.dot_ini['simulation']['simulate:info']['algorithms_names'].split(",")
    
    def _trans_payoff_concat(self) -> None:
        """
        Concatenates the payoffs
        """
        self.payoff_data_concatenate: np.ndarray = np.concatenate(self.data)
    
    def _trans_result_cumsum(self) -> None:
        """
        Cumulates the array and get the last acumulate payoff
        """
        self.end_dist: list[np.ndarray] = []
        for i in self.data:
            self.end_dist.append(np.cumsum(i, axis=0)[-1, :])
        self.end_dist: np.ndarray = np.array(self.end_dist)
    
    def plot_payoff_dist(self) -> None:
        """
        Payoff distributions
        """
        fig, ax = plt.subplots()
        for c, i in zip(self.color_list, range(self.payoff_data_concatenate.shape[1])):
            sns.kdeplot(self.payoff_data_concatenate[:, i], fill=True, label=self.labels[i], ax=ax, color=c)
        ax.legend()
        ax.set_xlabel("payoffs")
        ax.set_title(f"Payoffs Distribution {self.simu_info}")
        
    def plot_cumsum_dist(self) -> None:
        """
        Cumulative payoff distribution
        """
        fig, ax = plt.subplots()
        for c, i in zip(self.color_list, range(self.end_dist.shape[1])):
            sns.kdeplot(self.end_dist[:, i], fill=True, label=self.labels[i], ax=ax, color=c)
        ax.legend()
        ax.set_xlabel("cumulative payoff")
        ax.set_title(f"Comparing Cumulative Payoffs {self.simu_info}")
    
    def plot_boxplot_cumsum_dist(self) -> None:
        """
        Boxplot of cumulative payoff distribution
        """
        fig, ax  = plt.subplots()
        data: pd.DataFrame = pd.DataFrame(self.end_dist, columns=self.labels)
        sns.boxplot(data=data, fill=True, palette=self.color_list) 
        ax.set_ylabel("cumulative payoff")
        ax.set_title(f"Comparing Cumulative Payoffs {self.simu_info}")
    
    def show(self) -> None:
        plt.show()
        plt.clf()