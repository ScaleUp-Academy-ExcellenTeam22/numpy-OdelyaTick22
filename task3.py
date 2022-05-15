from typing import Tuple
import numpy as np


def num_of_rows_and_columns(matrix: np.array) -> Tuple:
    """
    function that return number of rows and columns of matrix.
    :param matrix: N-dimensional array.
    :return: The size's tuple.
    """
    return matrix.shape


if __name__ == "__main__":
    print(num_of_rows_and_columns(np.array([[1, 2, 3], [4, 5, 6]])))
