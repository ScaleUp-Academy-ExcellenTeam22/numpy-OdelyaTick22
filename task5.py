import numpy as np


def adding_vector(matrix: np.array, vec: np.array) -> None:
    """
    function for adding vector to matrix.
    :param matrix: N-dimensional array.
    :param vec: 1 dimension array.
    :return: None.
    """
    matrix += vec


if __name__ == "__main__":
    my_matrix = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])
    my_vec = np.array([1, 1, 1])
    adding_vector(my_matrix, my_vec)
    print(my_matrix)
