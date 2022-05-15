import numpy as np

if __name__ == "__main__":
    id = np.array([123456789, 987654321, 322951293, 207830126])
    height = np.array([170, 183, 163, 172])
    indices = np.lexsort((id, height))
    print(indices)
    for i in indices:
        print(id[i], height[i])
