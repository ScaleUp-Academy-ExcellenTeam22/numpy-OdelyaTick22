import numpy as np

if __name__ == "__main__":
    arr = np.random.rand(4, 4)
    print(arr)
    new_arr = arr
    new_arr[[0, 3], :] = arr[[3, 0], :]
    print(new_arr)
