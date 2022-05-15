import numpy as np

if __name__ == "__main__":
    arr = np.ones((3, 1, 4))
    print(np.squeeze(arr).shape)
