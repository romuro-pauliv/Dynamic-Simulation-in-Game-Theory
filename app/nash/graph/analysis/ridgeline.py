# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                    app/grpah/analysis/ridgeline.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from calc.transform.add_behavior_matrix import AddBehavior
from calc.transform.to_player_matrix    import ST2P_matrix
from config.config_files                import configfiles

import pandas   as pd
import numpy    as np

from joypy import joyplot
import matplotlib.pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure
# |--------------------------------------------------------------------------------------------------------------------|


class RidgeLine(object):
    def __init__(self, behaviors: list[list[np.ndarray]]) -> None:
        """
        Initialize the Ridgeline instance.
        Args:
            behaviors (list[list[np.ndarray]]): List of behaviors
        """
        self.n_simulations  : int = len(behaviors)
        self.n_players      : int = int(configfiles.dot_ini['simulation']['simulate:matrix']['players'])
        self.data           : list[np.ndarray] = self._concat(behaviors)
        self.spliter_indexes: list[int] = self._get_spliter_indexes()

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
    
    def _get_spliter_indexes(self) -> list[int]:
        """
        Generates the indexes spliter to each behavior
        Returns:
            list[int]: Indexes spliter
        """
        spliter: int = int(self.data[0].shape[0]/self.n_simulations)
        spliter_indexes: list[int] = []
        for i in range(self.n_simulations):
            spliter_indexes.append(spliter-1) if i == 0 else spliter_indexes.append(spliter_indexes[-1] + spliter)
        return spliter_indexes
    
    def _concat(self, behaviors: list[list[np.ndarray]]) -> list[np.ndarray]:
        """
        Concatenates the behaviors
        """
        add_behavior: AddBehavior = AddBehavior(self.n_players)
        for b in behaviors:
            add_behavior.add(ST2P_matrix(b))
        
        data: list[np.ndarray] = add_behavior.concat()
        for n, _ in enumerate(data):
            data[n] = np.cumsum(data[n], axis=0)
        return data
    
    def _dataframe_structure(self) -> pd.DataFrame:
        """
        Creates a pandas dataframe structure to apply in joyplot
        Returns:
            pd.DataFrame: Dataframe structure
        """
        player_behaviors: dict[str, list[np.float64]] = {"group": []}
        for n, p in enumerate(self.data):
            result_list: list[np.float64] = []
            
            for h, idx in enumerate(self.spliter_indexes):
                d: np.ndarray = p[idx,:]
                for numbers in d:
                    result_list.append(numbers)
                    player_behaviors["group"].append(f"B{h}") if n == 0 else None

            player_behaviors[f"P{n}"] = result_list
            
        return pd.DataFrame(player_behaviors)
        
    def show(self) -> None:
        data: pd.DataFrame = self._dataframe_structure()
        graph: tuple[Figure, Axes] = joyplot(
            data, by="group",
            fade=True, color=self.color_list, fill=True, linecolor="white"
        )
        plt.show()
        plt.clf()