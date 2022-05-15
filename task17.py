import numpy as np


def med(matrix: np.array) -> float:
    return np.median(matrix)


if __name__ == "__main__":
    print("Original array:")
    mat = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
    print(mat)
    print("Median of said array:")
    print(med(mat))
