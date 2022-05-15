import numpy as np

if __name__ == "__main__":
    first = np.array([[10], [20], [30]])
    second = np.array([[40], [50], [60]])
    new_array = np.dstack((first, second))
    print(new_array)
