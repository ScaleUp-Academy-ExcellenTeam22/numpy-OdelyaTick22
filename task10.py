import numpy as np
if __name__ == "__main__":
    arr = np.array([[4, 6], [2, 1]])
    print("Original array:")
    print(arr)
    print("Sort along the first axis: ")
    first = np.sort(arr, axis=0)
    print(first)
    print("Sort along the last axis: ")
    last = np.sort(first, axis=1)
    print(last)
