import numpy as np

if __name__ == "__main__":
    vec = np.array(range(21))
    for i in range(9, 16):
        vec[i] = vec[i] * (-1)
    print(vec)
