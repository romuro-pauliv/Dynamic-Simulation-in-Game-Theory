# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/graph/analysis/dist.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot    as plt
import seaborn              as sns
import numpy                as np
# |--------------------------------------------------------------------------------------------------------------------|

class Dist(object):
    def __init__(self, data: list[np.ndarray]) -> None:
        """
        Initialize the Dist instance.
        Args:
            data (np.ndarray): Full data from binary files
        """
        self.data: np.ndarray = data

        self._trans_payoff_concat()
        self._trans_result_cumsum()
        
    def _trans_payoff_concat(self) -> None:
        self.payoff_data_concatenate: np.ndarray = np.concatenate(self.data)
    
    def _trans_result_cumsum(self) -> None:
        self.end_dist: list[np.ndarray] = []
        for i in self.data:
            self.end_dist.append(np.cumsum(i, axis=0)[-1, :])
        self.end_dist: np.ndarray = np.array(self.end_dist)
    
    def payoff_dist(self) -> None:
        sns.set_theme("paper", "darkgrid", "pastel")
        for i in range(self.payoff_data_concatenate.shape[1]):
            sns.kdeplot(self.payoff_data_concatenate[:, i], fill=True)
        
        plt.show()
        plt.clf()
        
    def end_cumsum_dist(self) -> None:
        sns.set_theme("paper", "darkgrid", "pastel")
        for i in range(self.end_dist.shape[1]):
            sns.kdeplot(self.end_dist[:, i], fill=True)
        
        plt.show()
        plt.clf()