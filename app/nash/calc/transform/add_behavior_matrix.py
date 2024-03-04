# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                          app/calc/transform/add_behavior_matrix.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|


class AddBehavior(object):
    def __init__(self) -> None:
        """
        Initialize the AddBehavior instance.
        """
        self.stack_behavior_data: dict[str, list[np.ndarray]] = {}
        self.concat_stack_behavior_data: list[np.ndarray] = []
        self.n: int = 0
        
    def add(self, data: list[np.ndarray]) -> None:
        """
        Data in format [POH[IxST]][1xP]. See nash/calc/transform/to_player_matrix.py
        Args:
            data (list[np.ndarray]): Data in [POH[IxST]][1xP]
        """
        self.stack_behavior_data[self.n] = data
        self.n_players: int = data[0].shape[1]
        self.n += 1
        
    def concat(self) -> list[np.ndarray]:
        """
        Concatenates the behaviors in one object.
        Returns:
            list[np.ndarray]: The behaviors concatenates
        """
        for p in range(self.n_players):
            dt: list[np.ndarray] = []
            for n in range(self.n):
                dt.append(self.stack_behavior_data[n][p])
            self.concat_stack_behavior_data.append(np.concatenate(dt))
        
        return self.concat_stack_behavior_data