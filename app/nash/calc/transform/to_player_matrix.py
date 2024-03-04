# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                             app/calc/transform/to_player_matrix.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
# |--------------------------------------------------------------------------------------------------------------------|


def ST2P_matrix(data: list[np.ndarray]) -> list[np.ndarray]:
    """
    Transform [POH[IxP]][1xST] to [POH[IxST]][1xP] 
    Args:
        data (list[np.ndarray]): From .bin files type [POH[IxP]][1xST]

    Returns:
        list[np.ndarray]: [POH[IxST]][1xP]
    """
    data_trans: list[np.ndarray] = []
    for i in range(data[0].shape[1]):
        data_trans.append(np.column_stack([arr[:, i] for arr in data]))
    return data_trans        