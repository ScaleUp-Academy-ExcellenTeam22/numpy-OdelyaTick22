import numpy as np

if __name__ == "__main__":
    matrix = np.zeros((10, 10))
    matrix[0] = 1
    matrix[9] = 1
    for i in range(10):
        matrix[i][0] = 1
        matrix[i][9] = 1
    print(matrix)
